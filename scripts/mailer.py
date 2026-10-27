"""Mailer job for NL Oefenbank (runs in GitHub Actions, see .github/workflows/mailer.yml).

The workflow runs this every hour (--mode hourly). Each run:
  1. "hesabın onaylandı" mail to newly approved accounts + queued announcements
  2. the news mail, when the admin schedule says so (default: Monday 08:00, Amsterdam time);
     logged in nieuws_sent/{date}
  3. the weekly summary, when the schedule says so (default: Sunday 18:00); logged in mail_log/weekly-{date}
The schedule lives in Firestore settings/mail and is edited on the admin page.
Manual runs can force one job: --mode news or --mode weekly (ignores the schedule).
--mode test sends a preview of the next news mail, a sample weekly summary and a sample welcome mail to one
address (TEST_TO, default: the sending address). It writes nothing, so the real schedule is not affected.

Secrets (GitHub > Settings > Secrets and variables > Actions)
  FIREBASE_SERVICE_ACCOUNT : JSON key of a Firebase service account (reads/writes Firestore)
  GMAIL_USER               : sending address, e.g. nloefenbank@gmail.com
  GMAIL_APP_PASSWORD       : Gmail app password of that address

--dry-run prints the mails instead of sending them and writes nothing to Firestore.
All mails go out as plain text + an HTML version in the site's colours.
"""
import argparse
import datetime as dt
import html
import json
import os
import re
import smtplib
from collections import Counter
from email.message import EmailMessage
from email.utils import formatdate, make_msgid
from pathlib import Path
from zoneinfo import ZoneInfo

SITE = "https://zokcuoglu.github.io/nl-oefenbank/"
ROOT = Path(__file__).resolve().parent.parent
AMS = ZoneInfo("Europe/Amsterdam")
NOTE_WEEKLY = "Haftalık özeti istemiyorsan sitede Profil sayfasından kapatabilirsin."
NOTE_NEWS_MAIL = "Haftalık haberi istemiyorsan sitede Profil sayfasından kapatabilirsin."
NOTE_NEWS = "Bu duyuru NL Oefenbank üyelerine gönderildi."

# Site colours (light theme) for the HTML template; inline styles because mail clients drop <style>
C = {"ground": "#F2F4F7", "surface": "#FFFFFF", "line": "#D3DAE3", "ink": "#142033", "muted": "#566377",
     "accent": "#C8551B", "blue": "#1F4E8C", "blue_soft": "#DCE6F4",
     "a0": "#0E7C7B", "a1": "#2E7D4F", "a2": "#1F6FB0", "b1": "#B07A10", "b2": "#B8462F", "c1": "#7A3E9D"}
FONT = "'Segoe UI',Arial,Helvetica,sans-serif"


# ---------- helpers ----------

def module_titles():
    """Exercise id -> readable title, from the same catalog the website uses."""
    cat = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))
    titles = {m["id"]: m["title"] for m in cat["modules"]}
    titles.setdefault("nieuws", "Nieuws in niveaus (quiz)")
    return titles


def is_approved(u):
    return u.get("role") == "admin" or u.get("status") == "approved"


def first_name(u):
    return (u.get("name") or "").split(" ")[0] or "Merhaba"


def iso(t):
    return t.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def esc(t):
    return html.escape(str(t or ""), quote=True)


def rich(t):
    """Escape, but keep <strong> from our own content files."""
    return re.sub(r"&lt;(/?)strong&gt;", r"<\1strong>", esc(t))


def text_to_html(text):
    """Plain text (paragraphs separated by blank lines) -> simple HTML, links made clickable."""
    out = []
    for p in re.split(r"\n\s*\n", (text or "").strip()):
        p = esc(p).replace("\n", "<br>")
        p = re.sub(r"(https?://[^\s<]+)", r'<a href="\1" style="color:%s">\1</a>' % C["blue"], p)
        out.append(f'<p style="margin:0 0 14px;line-height:1.6">{p}</p>')
    return "".join(out)


def html_wrap(title, inner, note=""):
    """Branded e-mail layout: header bar, white card, footer with site link."""
    return f"""<!doctype html><html><body style="margin:0;padding:0;background:{C['ground']}">
<div style="max-width:640px;margin:0 auto;padding:24px 16px;font-family:{FONT};color:{C['ink']};font-size:16px">
  <div style="font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:{C['muted']}">Hollandaca çalışma</div>
  <div style="font-size:22px;font-weight:700;margin:2px 0 16px">NL Oefenbank</div>
  <div style="background:{C['surface']};border:1px solid {C['line']};border-radius:12px;padding:24px">
    <h1 style="font-size:21px;margin:0 0 16px;line-height:1.3">{esc(title)}</h1>
    {inner}
  </div>
  <p style="font-size:13px;color:{C['muted']};margin:16px 4px 0;line-height:1.5">
    <a href="{SITE}" style="color:{C['accent']};font-weight:600">NL Oefenbank'a git</a><br>{esc(note)}<br><a href="{SITE}profile.html" style="color:{C['muted']};text-decoration:underline">E-posta ayarları / abonelikten çık</a></p>
</div></body></html>"""


def button(url, label):
    return (f'<p style="margin:18px 0"><a href="{esc(url)}" style="background:{C["accent"]};color:#fff;text-decoration:none;'
            f'padding:11px 20px;border-radius:8px;font-weight:600;display:inline-block">{esc(label)}</a></p>')


# ---------- mail sending ----------

class GmailSender:
    """Sends text + HTML mail through Gmail SMTP with an app password."""

    def __init__(self, user, password):
        self.user, self.password = user, password
        self.smtp = None

    def _conn(self):
        # Log in once and reuse the connection: sending one mail per person means many mails per run
        if self.smtp is None:
            self.smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            self.smtp.login(self.user, self.password)
        return self.smtp

    def send(self, to, subject, body, bcc=None, html_body=None):
        msg = EmailMessage()
        msg["From"] = f"NL Oefenbank <{self.user}>"
        msg["To"] = to
        msg["Subject"] = subject
        msg["Date"] = formatdate(localtime=True)
        msg["Message-ID"] = make_msgid(domain="nloefenbank")
        # Gmail shows an "Unsubscribe" link for this; it leads to the profile page where mails can be turned off
        msg["List-Unsubscribe"] = f"<{SITE}profile.html>, <mailto:{self.user}?subject=unsubscribe>"
        msg.set_content(body)
        if html_body:
            msg.add_alternative(html_body, subtype="html")
        self._conn().send_message(msg, to_addrs=[to] + list(bcc or []))


class PrintSender:
    """Dry run: show what would be sent (text part only, HTML length)."""

    def __init__(self):
        self.sent = []

    def send(self, to, subject, body, bcc=None, html_body=None):
        self.sent.append({"to": to, "subject": subject, "body": body, "bcc": list(bcc or []), "html": html_body or ""})
        print(f"--- MAIL to={to} bcc={len(bcc or [])} subject={subject!r} html={len(html_body or '')} chars\n{body}\n")


def sender_address(sender):
    return getattr(sender, "user", None) or os.environ.get("GMAIL_USER", "nloefenbank@gmail.com")


def send_simple(sender, to, subject, title, text, note, bcc=None, link=None, link_label=None):
    """One helper for welcome/weekly/announcement mails: same text in plain and HTML form."""
    inner = text_to_html(text) + (button(link, link_label) if link else "")
    plain = text + (f"\n\n{link_label}: {link}" if link else "") + f"\n\n--\nNL Oefenbank · {SITE}\n{note}\nAbonelikten çık: {SITE}profile.html"
    sender.send(to, subject, plain, bcc=bcc, html_body=html_wrap(title, inner, note))


# ---------- hourly: welcome + announcements ----------

def run_hourly(db, sender, now, dry_run=False):
    users = [(d.id, d.to_dict()) for d in db.collection("users").stream()]

    for uid, u in users:
        if is_approved(u) and u.get("email") and not u.get("welcome_sent_at"):
            text = (f"Merhaba {first_name(u)},\n\nNL Oefenbank hesabın onaylandı. Artık siteye girip alıştırmalara başlayabilirsin.\n\n"
                    "Haftada bir, o haftanın kısa bir özetini e-postayla alacaksın.")
            send_simple(sender, u["email"], "NL Oefenbank: hesabın onaylandı", "Hesabın onaylandı", text, NOTE_WEEKLY,
                        link=SITE, link_label="Siteye git")
            if not dry_run:
                db.collection("users").document(uid).update({"welcome_sent_at": iso(now)})

    approved = [u for _, u in users if is_approved(u) and u.get("email")]
    by_email = {u["email"]: u for u in approved}
    for a in db.collection("announcements").stream():
        n = a.to_dict()
        if n.get("sent_at"):
            continue
        # Audience: all (default), adult or child accounts; children's parents follow their child's audience
        aud = n.get("audience") or "all"
        rec = sorted({u["email"] for u in approved if aud == "all" or u.get("type") == aud or (aud == "adult" and u.get("role") == "admin")})
        if not rec:
            continue
        # One mail per person, addressed to them (a To: own-address + BCC mail looks like bulk mail / spam)
        for email in rec:
            send_simple(sender, email, f"NL Oefenbank: {n.get('subject', '')}", n.get("subject", ""),
                        f"Merhaba {first_name(by_email[email])},\n\n{n.get('body', '')}", NOTE_NEWS)
        if not dry_run:
            db.collection("announcements").document(a.id).update({"sent_at": iso(now), "recipients": len(rec)})


# ---------- schedule (settings/mail, edited on the admin page) ----------

# weekday: 1 = Monday ... 7 = Sunday (ISO), hour: 0-23 Amsterdam time
DEFAULT_SCHEDULE = {"news": {"enabled": True, "weekday": 1, "hour": 8},
                    "weekly": {"enabled": True, "weekday": 7, "hour": 18}}


def load_schedule(db):
    """Admin settings merged over the defaults, so a missing or half-filled doc still works."""
    snap = db.collection("settings").document("mail").get()
    saved = (snap.to_dict() or {}) if snap.exists else {}
    out = {}
    for job, d in DEFAULT_SCHEDULE.items():
        out[job] = {**d, **{k: v for k, v in (saved.get(job) or {}).items() if k in d}}
    return out


CATCH_UP = dt.timedelta(hours=48)


def last_slot(job_cfg, now):
    """Most recent scheduled moment (chosen weekday and hour, Amsterdam time) that is not in the future."""
    local = now.astimezone(AMS)
    days_back = (local.isoweekday() - int(job_cfg["weekday"])) % 7
    slot = (local - dt.timedelta(days=days_back)).replace(hour=int(job_cfg["hour"]), minute=0, second=0, microsecond=0)
    return slot - dt.timedelta(days=7) if slot > local else slot


def is_due(job_cfg, now, sent_dates):
    """Due when the last scheduled moment has passed, nothing was sent since then, and it was at most 48 hours ago.
    GitHub's hourly schedule sometimes skips hours, so a later run still catches up; the 48-hour limit stops an
    old, missed slot (e.g. right after changing the schedule) from sending at an odd moment."""
    if not job_cfg.get("enabled"):
        return False
    slot = last_slot(job_cfg, now)
    return now - slot <= CATCH_UP and not any(d >= slot.date().isoformat() for d in sent_dates)


# ---------- news item ----------

def load_news():
    return json.loads((ROOT / "data" / "nieuws.json").read_text(encoding="utf-8"))["items"]


def toets_for(item):
    """The mixed test that opens together with this item (tests cover 1-3, 1-4, ...), or None."""
    data = json.loads((ROOT / "data" / "nieuws.json").read_text(encoding="utf-8"))
    return next((t for t in data.get("toetsen", []) if t.get("tot") == item.get("nr")), None)


def pick_news(items, sent_log):
    """Next item: the first one never sent (file order); after a full round, the one sent longest ago."""
    last = {}
    for s in sent_log:
        last[s["item_id"]] = max(last.get(s["item_id"], ""), s.get("date", ""))
    fresh = [i for i in items if i["id"] not in last]
    if fresh:
        return fresh[0]
    return min(items, key=lambda i: last.get(i["id"], ""))


def pipe_rows(raw, n):
    rows = []
    for line in (raw or "").split("\n"):
        if line.strip():
            c = [x.strip() for x in line.split("|")]
            rows.append(c + [""] * (n - len(c)))
    return rows


def news_html(item, date_str, greeting=""):
    """News mail: video, the story at A1-C1, idioms, words, grammar; the quiz is on the site."""
    url = f"{SITE}nieuws/?id={item['id']}"
    video = ""
    if item.get("video_url"):
        sep = "&" if "?" in item["video_url"] else "?"
        vurl = item["video_url"] + (f"{sep}t={item['video_start']}s" if item.get("video_start") else "")
        thumb = f'<a href="{esc(vurl)}"><img src="{esc(item.get("afbeelding_url", ""))}" alt="video" style="width:100%;border-radius:8px;display:block"></a>' if item.get("afbeelding_url") else ""
        part = ""
        if item.get("video_end"):
            mm = lambda x: f"{x // 60}:{x % 60:02d}"
            part = f'<p style="color:{C["muted"]};font-size:14px;margin:0 0 8px">Bu haber videonun {mm(item.get("video_start", 0))}–{mm(item["video_end"])} arasındaki kısmı.</p>'
        video = thumb + button(vurl, f"▶ Videoyu izle ({item.get('bron') or 'YouTube'})") + part

    def levelbox(l):
        paras = "".join(f'<p style="margin:0 0 10px;line-height:1.65">{rich(p).replace(chr(10), "<br>")}</p>' for p in re.split(r"\n\s*\n", item.get(l) or "") if p.strip())
        gloss = f'<div style="font-size:13px;color:{C["muted"]};border-top:1px dashed {C["line"]};padding-top:6px;margin-top:6px">{rich(item["gloss"][l])}</div>' if (item.get("gloss") or {}).get(l) else ""
        return (f'<div style="border-left:4px solid {C[l]};padding:2px 0 2px 14px;margin:16px 0">'
                f'<div style="font-weight:700;color:{C[l]};font-size:13px;margin-bottom:6px">{l.upper()}</div>{paras}{gloss}</div>')

    idioms = ""
    if item.get("uitdrukkingen"):
        rows = "".join(f'<p style="margin:0 0 12px"><b>{esc(u.get("nl"))}</b>'
                       + (f' <span style="font-size:12px;font-weight:700;color:{C.get(str(u.get("niveau", "")).lower(), C["muted"])}">{esc(u.get("niveau"))}</span>' if u.get("niveau") else "")
                       + f' — {esc(u.get("tr"))}<br>'
                       f'<span style="color:{C["muted"]};font-size:14px">{esc(u.get("uitleg", ""))}</span>'
                       + (f'<br><i style="font-size:14px">{esc(u.get("voorbeeld"))}</i>' if u.get("voorbeeld") else "") + "</p>"
                       for u in item["uitdrukkingen"])
        idioms = f'<h2 style="font-size:17px;margin:24px 0 8px">Günlük deyimler</h2>{rows}'

    vocab = ""
    vr = pipe_rows(item.get("woordenschat"), 6)  # woord | soort | betekenis | voorbeeld | turks | niveau
    if vr:
        td = f'style="border-bottom:1px solid {C["line"]};padding:6px 8px;vertical-align:top;font-size:14px"'
        vocab = (f'<h2 style="font-size:17px;margin:24px 0 8px">Woordenschat</h2><table style="border-collapse:collapse;width:100%">'
                 + "".join(f"<tr><td {td}><b>{esc(c[0])}</b></td><td {td}>{esc(c[2])}</td><td {td}><b>{esc(c[4])}</b></td></tr>" for c in vr) + "</table>")

    grammar = ""
    if item.get("grammatica"):
        g = []
        for t in item["grammatica"].split("\n"):
            t = t.strip()
            if not t:
                continue
            if re.match(r"^\d+\)", t):
                g.append(f'<p style="font-weight:700;color:{C["blue"]};margin:14px 0 6px">{esc(t)}</p>')
            elif t.startswith("•"):
                g.append(f'<div style="background:{C["blue_soft"]};border-radius:6px;padding:6px 10px;margin:4px 0;font-size:14px">{esc(t[1:].strip())}</div>')
            else:
                g.append(f'<p style="margin:4px 0">{esc(t)}</p>')
        grammar = f'<h2 style="font-size:17px;margin:24px 0 8px">Grammatica</h2>{"".join(g)}'

    n_q = len(item.get("toets") or [])
    quiz = (f'<h2 style="font-size:17px;margin:24px 0 8px">Quiz</h2>'
            f'<p style="line-height:1.6">Sitede {n_q} soruluk bir quiz seni bekliyor: içerik, kelimeler, deyimler ve gramer. '
            f'Sonuçların kaydedilir; her 3 haberden sonra karma bir sınav açılır.</p>') if n_q else ""

    nr = f"#{item['nr']} " if item.get("nr") else ""
    toets = toets_for(item)
    if toets:
        turl = f"{SITE}nieuws/?toets={toets['id']}"
        quiz += (f'<div style="border:2px dashed {C["line"]};border-radius:10px;padding:12px 14px;margin:16px 0">'
                 f'<b>Yeni karma sınav açıldı: {esc(toets["titel"])}</b><br>'
                 f'<span style="color:{C["muted"]};font-size:14px">20 soru; bu ana kadarki bütün haberlerden.</span>'
                 + button(turl, "Sınava başla") + '</div>')
    inner = ((f'<p style="line-height:1.6">{esc(greeting)}</p>' if greeting else "")
             + f'<p style="color:{C["muted"]};margin:-8px 0 12px">{esc(date_str)} · {esc(item.get("bron", ""))} · video {esc(item.get("niveau_video", ""))} · metin A0 → C1</p>'
             + video + "".join(levelbox(l) for l in ["a0", "a1", "a2", "b1", "b2", "c1"]) + idioms + vocab + grammar + quiz
             + button(url, "Sitede aç: quiz"))
    plain = ((f"{greeting}\n\n" if greeting else "") + f"{nr}{item['titel']} ({date_str})\n\nVideo: {item.get('video_url', '')}\n\n"
             + "\n\n".join(f"[{l.upper()}]\n{re.sub(r'<[^>]+>', '', item.get(l) or '')}" for l in ["a0", "a1", "a2", "b1", "b2", "c1"])
             + f"\n\nQuiz: {url}"
             + (f"\nYeni karma sınav: {toets['titel']} – {SITE}nieuws/?toets={toets['id']}" if toets else "")
             + f"\n\n--\nNL Oefenbank · {SITE}\n{NOTE_NEWS_MAIL}\nAbonelikten çık: {SITE}profile.html")
    return plain, html_wrap(f"{nr}{item['titel']}", inner, NOTE_NEWS_MAIL)


def wants_news(u):
    """Profile checkbox, on by default for adults (like the weekly summary); email_daily is its old name."""
    return bool(u.get("email_news", u.get("email_daily", True)))


def run_news(db, sender, now, dry_run=False, force=False):
    today = now.astimezone(AMS).date().isoformat()
    log_col = db.collection("nieuws_sent")
    sent = [d.to_dict() for d in log_col.stream()]
    if not force and any(s.get("date") == today for s in sent):
        print(f"news: already sent for {today}")
        return
    items = load_news()
    todays = next((x for x in sent if x.get("date") == today), None)
    # Manual re-run on the same day: send today's item again, not the next one
    item = next((i for i in items if todays and i["id"] == todays.get("item_id")), None) or pick_news(items, sent)
    users = [d.to_dict() for d in db.collection("users").stream()]
    subs = {u["email"]: u for u in users if is_approved(u) and u.get("email") and u.get("type") != "child" and wants_news(u)}
    rec = sorted(subs)
    if not rec:
        print("news: no subscribers")
        return
    date_str = now.astimezone(AMS).strftime("%d-%m-%Y")
    # One mail per person, addressed to them and starting with their name
    for email in rec:
        plain, html_body = news_html(item, date_str, greeting=f"Merhaba {first_name(subs[email])},")
        sender.send(email, f"🇳🇱 Nieuws #{item.get('nr', '')}: {item['titel']}", plain, html_body=html_body)
    print(f"news: #{item.get('nr')} {item['titel']} -> {len(rec)} recipients")
    if not dry_run:
        log_col.document(today).set({"date": today, "item_id": item["id"], "titel": item["titel"], "sent_at": iso(now), "recipients": len(rec)})


# ---------- weekly summary ----------

def weekly_text(u, attempts, titles, today):
    """Plain-text summary of the last 7 days for one account."""
    lines = []
    by_mod = {}
    for a in attempts:
        m = a.get("module") or "lezen"
        s = by_mod.setdefault(m, {"n": 0, "ok": 0, "tot": 0})
        s["n"] += 1
        s["ok"] += a.get("score", 0) or 0
        s["tot"] += a.get("total", 0) or 0
    if by_mod:
        n = sum(s["n"] for s in by_mod.values())
        lines.append(f"Bu hafta {n} tur çözüldü:")
        for m, s in sorted(by_mod.items(), key=lambda kv: -kv[1]["n"]):
            if s["tot"]:
                pct = round(100 * s["ok"] / s["tot"])
                lines.append(f"  • {titles.get(m, m)}: {s['n']} tur, %{pct} doğru")
            else:
                # Modules without an automatic score (Spreken: the AI scores it) show only the count
                lines.append(f"  • {titles.get(m, m)}: {s['n']} tur")
        # Multiplication tables (Slimspel): the sums that went wrong most often this week,
        # so a parent sees what to practise. qid is the sum itself, e.g. "7×8".
        wrong = Counter(an.get("qid") for a in attempts if a.get("module") == "slimspel-tafels"
                        for an in (a.get("answers") or []) if not an.get("correct") and an.get("qid"))
        if wrong:
            top = ", ".join(f"{q} ({k} kez)" for q, k in wrong.most_common(5))
            lines.append(f"\nTafels'te en çok yanlış yapılanlar: {top}")
    else:
        lines.append("Bu hafta hiç tur çözülmedi. Kısa bir Hızlı 10 bile fark yaratır.")

    exams = []
    for m, d in (u.get("exams") or {}).items():
        if not d:
            continue
        try:
            left = (dt.date.fromisoformat(d) - today).days
        except ValueError:
            continue
        if left >= 0:
            exams.append(f"  • {titles.get(m, m)}: {left} gün ({d})")
    if exams:
        lines.append("\nSınavlara kalan süre:")
        lines.extend(exams)
    return "\n".join(lines)


def run_weekly(db, sender, now, dry_run=False, force=False):
    titles = module_titles()
    today = now.astimezone(AMS).date()
    log_ref = db.collection("mail_log").document(f"weekly-{today.isoformat()}")
    if not force and log_ref.get().exists:
        print(f"weekly: already sent for {today}")
        return
    count = 0
    cutoff = iso(now - dt.timedelta(days=7))
    users = {d.id: d.to_dict() for d in db.collection("users").stream()}

    for uid, u in users.items():
        if not is_approved(u) or not u.get("email"):
            continue
        att = [d.to_dict() for d in where_gte(db.collection("users").document(uid).collection("attempts"), "finished_at", cutoff).stream()]
        summary = weekly_text(u, att, titles, today)
        name = u.get("name") or "Öğrenci"

        if u.get("email_weekly", True):
            send_simple(sender, u["email"], "NL Oefenbank: haftalık özetin", "Haftalık özetin",
                        f"Merhaba {first_name(u)},\n\n{summary}", NOTE_WEEKLY, link=SITE, link_label="Çalışmaya devam et")
            count += 1

        # Children: the linked parent gets a copy (once, even if they share an e-mail address)
        parent = users.get(u.get("parent_uid") or "")
        if u.get("type") == "child" and parent and parent.get("email") and parent["email"] != u["email"]:
            send_simple(sender, parent["email"], f"NL Oefenbank: {name} için haftalık özet", f"{name} için haftalık özet",
                        f"Merhaba {first_name(parent)},\n\n{name} bu hafta:\n\n{summary}", NOTE_WEEKLY)
            count += 1

    if not dry_run:
        log_ref.set({"job": "weekly", "date": today.isoformat(), "sent_at": iso(now), "mails": count})


def where_gte(col, field, value):
    """Firestore 'field >= value' that works on old and new firebase-admin versions."""
    try:
        from google.cloud.firestore_v1.base_query import FieldFilter
        return col.where(filter=FieldFilter(field, ">=", value))
    except ImportError:
        return col.where(field, ">=", value)


# ---------- test: preview mails to one address ----------

def run_test(db, sender, now, to):
    """Send the mails people would get, to one address only. Nothing is written to Firestore."""
    sent = [d.to_dict() for d in db.collection("nieuws_sent").stream()]
    item = pick_news(load_news(), sent)
    plain, html_body = news_html(item, now.astimezone(AMS).strftime("%d-%m-%Y"), greeting="Merhaba Test,")
    sender.send(to, f"[TEST] 🇳🇱 Nieuws #{item.get('nr', '')}: {item['titel']}", plain, html_body=html_body)

    # Weekly summary: the first admin's real numbers of the last 7 days, as an example
    users = [(d.id, d.to_dict()) for d in db.collection("users").stream()]
    uid, u = next(((i, x) for i, x in users if x.get("role") == "admin"), (None, {"name": "Test"}))
    att = []
    if uid:
        cutoff = iso(now - dt.timedelta(days=7))
        att = [d.to_dict() for d in where_gte(db.collection("users").document(uid).collection("attempts"), "finished_at", cutoff).stream()]
    summary = weekly_text(u, att, module_titles(), now.astimezone(AMS).date())
    send_simple(sender, to, "[TEST] NL Oefenbank: haftalık özetin", "Haftalık özetin",
                f"Merhaba {first_name(u)},\n\n{summary}", NOTE_WEEKLY, link=SITE, link_label="Çalışmaya devam et")

    text = (f"Merhaba {first_name(u)},\n\nNL Oefenbank hesabın onaylandı. Artık siteye girip alıştırmalara başlayabilirsin.\n\n"
            "Haftada bir, o haftanın kısa bir özetini e-postayla alacaksın.")
    send_simple(sender, to, "[TEST] NL Oefenbank: hesabın onaylandı", "Hesabın onaylandı", text, NOTE_WEEKLY, link=SITE, link_label="Siteye git")
    print(f"test: 3 preview mails sent (next news item: #{item.get('nr')} {item['id']})")


# ---------- entry point ----------

# ---------- yearly: children move up one groep in the summer ----------

GROEP_MAX = 8  # groep 8 is the last year of primary school: stays 8


def run_groep_up(db, sender, now, dry_run=False, force=False):
    """Once a year, in August (summer holiday everywhere), every child account goes up one groep:
    groep5 -> groep6. Groep 8 stays. A log document (mail_log/groep-{year}) makes sure it runs once a year,
    and each account remembers the year (groep_up_year) so it can never move up twice.
    Only in August, so a deploy in another month never moves anyone by accident.
    force (manual run): ignore the month and the log; use it with --dry-run to see what would change."""
    local = now.astimezone(AMS)
    year = local.year
    log_ref = db.collection("mail_log").document(f"groep-{year}")
    if not force:
        if local.month != 8:
            return
        if log_ref.get().exists:
            return
    changes = []
    for d in db.collection("users").stream():
        u = d.to_dict()
        g = u.get("groep") or ""
        if u.get("type") != "child" or not re.fullmatch(r"groep[1-8]", g) or u.get("groep_up_year") == year:
            continue
        n = int(g[5:])
        if n >= GROEP_MAX:
            continue
        new = f"groep{n + 1}"
        changes.append((u.get("name") or u.get("email") or d.id, g, new))
        print(f"groep-up: {changes[-1][0]}: {g} -> {new}{' (dry run)' if dry_run else ''}")
        if not dry_run:
            d.reference.update({"groep": new, "groep_up_year": year})

    # Tell the admins what changed
    admins = [u for u in (x.to_dict() for x in db.collection("users").stream()) if u.get("role") == "admin" and u.get("email")]
    if changes:
        lines = "\n".join(f"  • {name}: Groep {old[5:]} → Groep {new[5:]}" for name, old, new in changes)
        text = (f"Yeni okul yılı: {len(changes)} öğrenci hesabının grubu bir artırıldı.\n\n{lines}\n\n"
                "Bir hata varsa çocuğun profil sayfasından düzeltilebilir.")
    else:
        text = "Yeni okul yılı: grubu artırılacak öğrenci hesabı bulunmadı (grup seçilmemiş ya da Groep 8)."
    for a in admins:
        send_simple(sender, a["email"], "NL Oefenbank: öğrenciler bir üst gruba geçti", "Yeni okul yılı", text,
                    "Bu bilgi e-postası sadece adminlere gönderilir.")
    if not dry_run and not force:
        log_ref.set({"job": "groep-up", "year": year, "ran_at": iso(now), "changes": len(changes)})


def run_scheduled(db, sender, now, dry_run=False):
    """The hourly job: always the quick checks, plus news/weekly when the schedule says so."""
    run_hourly(db, sender, now, dry_run=dry_run)
    sched = load_schedule(db)
    print(f"schedule: {sched} | now {now.astimezone(AMS):%a %H:%M} Amsterdam")
    news_dates = [d.to_dict().get("date", "") for d in db.collection("nieuws_sent").stream()]
    weekly_dates = [x.get("date", "") for x in (d.to_dict() for d in db.collection("mail_log").stream()) if x.get("job") == "weekly"]
    if is_due(sched["news"], now, news_dates):
        run_news(db, sender, now, dry_run=dry_run)
    if is_due(sched["weekly"], now, weekly_dates):
        run_weekly(db, sender, now, dry_run=dry_run)
    run_groep_up(db, sender, now, dry_run=dry_run)  # does nothing outside August


def env_or_stop(names):
    """Missing secrets: explain in the Actions log and stop without failing the run
    (a red run every hour only floods the inbox with failure mails)."""
    missing = [n for n in names if not os.environ.get(n, "").strip()]
    if missing:
        print(f"::warning::Mailer skipped: GitHub secret(s) missing or empty: {', '.join(missing)}. "
              "Add them under Settings > Secrets and variables > Actions.")
        raise SystemExit(0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["hourly", "news", "weekly", "test", "groep"], required=True,
                    help="hourly = scheduled run; news/weekly = send that job now, ignoring the schedule; test = previews to one address; "
                         "groep = move children up one groep now (use with --dry-run to only see what would change)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.mode == "test":
        args.dry_run = False  # a test always sends, but only to the test address
    env_or_stop(["FIREBASE_SERVICE_ACCOUNT"] + ([] if args.dry_run else ["GMAIL_USER", "GMAIL_APP_PASSWORD"]))
    try:
        info = json.loads(os.environ["FIREBASE_SERVICE_ACCOUNT"])
    except json.JSONDecodeError as e:
        print(f"::error::FIREBASE_SERVICE_ACCOUNT is not valid JSON ({e.msg}). Paste the whole key file content into the secret.")
        raise SystemExit(1)

    import firebase_admin
    from firebase_admin import credentials, firestore

    firebase_admin.initialize_app(credentials.Certificate(info))
    db = firestore.client()

    sender = PrintSender() if args.dry_run else GmailSender(os.environ["GMAIL_USER"].strip(), os.environ["GMAIL_APP_PASSWORD"].replace(" ", ""))
    now = dt.datetime.now(dt.timezone.utc)
    if args.mode == "hourly":
        run_scheduled(db, sender, now, dry_run=args.dry_run)
    elif args.mode == "test":
        run_test(db, sender, now, os.environ.get("TEST_TO", "").strip() or os.environ["GMAIL_USER"].strip())
    elif args.mode == "news":
        run_news(db, sender, now, dry_run=args.dry_run, force=True)
    elif args.mode == "groep":
        run_groep_up(db, sender, now, dry_run=args.dry_run, force=True)
    else:
        run_weekly(db, sender, now, dry_run=args.dry_run, force=True)
    print(f"done: mode={args.mode} dry_run={args.dry_run}")


if __name__ == "__main__":
    main()
