"""Mailer job for NL Oefenbank (runs in GitHub Actions, see .github/workflows/mailer.yml).

Modes
  hourly : "hesabın onaylandı" mail to newly approved accounts + queued announcements
  daily  : today's news item ("Lezen en kijken in niveaus") to subscribers; logged in nieuws_sent/{date}
  weekly : weekly summary to every approved account (children: also to the linked parent)

Secrets (GitHub > Settings > Secrets and variables > Actions)
  FIREBASE_SERVICE_ACCOUNT : JSON key of a Firebase service account (reads/writes Firestore)
  GMAIL_USER               : sending address, e.g. nloefenbank@gmail.com
  GMAIL_APP_PASSWORD       : Gmail app password of that address
  NEWS_EXTRA_RECIPIENTS    : optional, comma separated addresses that get the daily news without a site account

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
from email.message import EmailMessage
from pathlib import Path
from zoneinfo import ZoneInfo

SITE = "https://zokcuoglu.github.io/nl-oefenbank/"
ROOT = Path(__file__).resolve().parent.parent
AMS = ZoneInfo("Europe/Amsterdam")
NOTE_WEEKLY = "Haftalık özeti istemiyorsan sitede Profil sayfasından kapatabilirsin."
NOTE_DAILY = "Günlük haberi istemiyorsan sitede Profil sayfasından kapatabilirsin."
NOTE_NEWS = "Bu duyuru NL Oefenbank üyelerine gönderildi."

# Site colours (light theme) for the HTML template; inline styles because mail clients drop <style>
C = {"ground": "#F2F4F7", "surface": "#FFFFFF", "line": "#D3DAE3", "ink": "#142033", "muted": "#566377",
     "accent": "#C8551B", "blue": "#1F4E8C", "blue_soft": "#DCE6F4",
     "a1": "#2E7D4F", "a2": "#1F6FB0", "b1": "#B07A10", "b2": "#B8462F", "c1": "#7A3E9D"}
FONT = "'Segoe UI',Arial,Helvetica,sans-serif"


# ---------- helpers ----------

def module_titles():
    """Exercise id -> readable title, from the same catalog the website uses."""
    cat = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))
    titles = {m["id"]: m["title"] for m in cat["modules"]}
    titles.setdefault("nieuws", "Dagelijks Nieuws (quiz)")
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
    <a href="{SITE}" style="color:{C['accent']};font-weight:600">NL Oefenbank'a git</a><br>{esc(note)}</p>
</div></body></html>"""


def button(url, label):
    return (f'<p style="margin:18px 0"><a href="{esc(url)}" style="background:{C["accent"]};color:#fff;text-decoration:none;'
            f'padding:11px 20px;border-radius:8px;font-weight:600;display:inline-block">{esc(label)}</a></p>')


# ---------- mail sending ----------

class GmailSender:
    """Sends text + HTML mail through Gmail SMTP with an app password."""

    def __init__(self, user, password):
        self.user, self.password = user, password

    def send(self, to, subject, body, bcc=None, html_body=None):
        msg = EmailMessage()
        msg["From"] = f"NL Oefenbank <{self.user}>"
        msg["To"] = to
        msg["Subject"] = subject
        msg.set_content(body)
        if html_body:
            msg.add_alternative(html_body, subtype="html")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
            s.login(self.user, self.password)
            s.send_message(msg, to_addrs=[to] + list(bcc or []))


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
    plain = text + (f"\n\n{link_label}: {link}" if link else "") + f"\n\n--\nNL Oefenbank · {SITE}\n{note}"
    sender.send(to, subject, plain, bcc=bcc, html_body=html_wrap(title, inner, note))


# ---------- hourly: welcome + announcements ----------

def run_hourly(db, sender, now, dry_run=False):
    users = [(d.id, d.to_dict()) for d in db.collection("users").stream()]

    for uid, u in users:
        if is_approved(u) and u.get("email") and not u.get("welcome_sent_at"):
            text = (f"Merhaba {first_name(u)},\n\nNL Oefenbank hesabın onaylandı. Artık siteye girip alıştırmalara başlayabilirsin.\n\n"
                    "Her pazar o haftanın kısa bir özetini e-postayla alacaksın.")
            send_simple(sender, u["email"], "NL Oefenbank: hesabın onaylandı", "Hesabın onaylandı", text, NOTE_WEEKLY,
                        link=SITE, link_label="Siteye git")
            if not dry_run:
                db.collection("users").document(uid).update({"welcome_sent_at": iso(now)})

    approved = [u for _, u in users if is_approved(u) and u.get("email")]
    for a in db.collection("announcements").stream():
        n = a.to_dict()
        if n.get("sent_at"):
            continue
        # Audience: all (default), adult or child accounts; children's parents follow their child's audience
        aud = n.get("audience") or "all"
        rec = sorted({u["email"] for u in approved if aud == "all" or u.get("type") == aud or (aud == "adult" and u.get("role") == "admin")})
        if not rec:
            continue
        # One mail, everyone in BCC so addresses stay private
        send_simple(sender, sender_address(sender), f"NL Oefenbank: {n.get('subject', '')}", n.get("subject", ""),
                    n.get("body", ""), NOTE_NEWS, bcc=rec)
        if not dry_run:
            db.collection("announcements").document(a.id).update({"sent_at": iso(now), "recipients": len(rec)})


# ---------- daily: news item ----------

def load_news():
    return json.loads((ROOT / "data" / "nieuws.json").read_text(encoding="utf-8"))["items"]


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


def news_html(item, date_str):
    """Daily news mail: video link, the story at A1-C1, idioms, words, grammar, questions; quiz on the site."""
    url = f"{SITE}nieuws/?id={item['id']}"
    video = ""
    if item.get("video_url"):
        sep = "&" if "?" in item["video_url"] else "?"
        vurl = item["video_url"] + (f"{sep}t={item['video_start']}s" if item.get("video_start") else "")
        thumb = f'<a href="{esc(vurl)}"><img src="{esc(item.get("afbeelding_url", ""))}" alt="video" style="width:100%;border-radius:8px;display:block"></a>' if item.get("afbeelding_url") else ""
        video = thumb + button(vurl, f"▶ Videoyu izle ({item.get('bron') or 'YouTube'})")

    def levelbox(l):
        paras = "".join(f'<p style="margin:0 0 10px;line-height:1.65">{rich(p).replace(chr(10), "<br>")}</p>' for p in re.split(r"\n\s*\n", item.get(l) or "") if p.strip())
        gloss = f'<div style="font-size:13px;color:{C["muted"]};border-top:1px dashed {C["line"]};padding-top:6px;margin-top:6px">{rich(item["gloss"][l])}</div>' if (item.get("gloss") or {}).get(l) else ""
        return (f'<div style="border-left:4px solid {C[l]};padding:2px 0 2px 14px;margin:16px 0">'
                f'<div style="font-weight:700;color:{C[l]};font-size:13px;margin-bottom:6px">{l.upper()}</div>{paras}{gloss}</div>')

    idioms = ""
    if item.get("uitdrukkingen"):
        rows = "".join(f'<p style="margin:0 0 12px"><b>{esc(u.get("nl"))}</b> — {esc(u.get("tr"))}<br>'
                       f'<span style="color:{C["muted"]};font-size:14px">{esc(u.get("uitleg", ""))}</span>'
                       + (f'<br><i style="font-size:14px">{esc(u.get("voorbeeld"))}</i>' if u.get("voorbeeld") else "") + "</p>"
                       for u in item["uitdrukkingen"])
        idioms = f'<h2 style="font-size:17px;margin:24px 0 8px">Günlük deyimler</h2>{rows}'

    vocab = ""
    vr = pipe_rows(item.get("woordenschat"), 5)
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

    questions = ""
    if item.get("vragen"):
        questions = (f'<h2 style="font-size:17px;margin:24px 0 8px">Vragen</h2>'
                     f'<p style="line-height:1.6">{esc(item["vragen"]).replace(chr(10), "<br>")}</p>'
                     f'<p style="color:{C["muted"]};font-size:14px">Cevaplar ve quiz sitede, sonuçların kaydedilir.</p>')

    inner = (f'<p style="color:{C["muted"]};margin:-8px 0 12px">{esc(date_str)} · {esc(item.get("bron", ""))} · A1 → C1</p>'
             + video + "".join(levelbox(l) for l in ["a1", "a2", "b1", "b2", "c1"]) + idioms + vocab + grammar + questions
             + button(url, "Sitede aç: cevaplar ve quiz"))
    plain = (f"{item['titel']} ({date_str})\n\nVideo: {item.get('video_url', '')}\n\n"
             + "\n\n".join(f"[{l.upper()}]\n{re.sub(r'<[^>]+>', '', item.get(l) or '')}" for l in ["a1", "a2", "b1", "b2", "c1"])
             + f"\n\nCevaplar ve quiz: {url}\n\n--\nNL Oefenbank · {SITE}\n{NOTE_DAILY}")
    return plain, html_wrap(item["titel"], inner, NOTE_DAILY)


def run_daily(db, sender, now, dry_run=False, extra=()):
    today = now.astimezone(AMS).date().isoformat()
    log_col = db.collection("nieuws_sent")
    sent = [d.to_dict() for d in log_col.stream()]
    if any(s.get("date") == today for s in sent):
        print(f"daily: already sent for {today}")
        return
    item = pick_news(load_news(), sent)
    users = [d.to_dict() for d in db.collection("users").stream()]
    rec = {u["email"] for u in users if is_approved(u) and u.get("email") and u.get("type") != "child" and u.get("email_daily")}
    rec |= {e.strip() for e in extra if e.strip()}
    if not rec:
        print("daily: no subscribers")
        return
    date_str = now.astimezone(AMS).strftime("%d-%m-%Y")
    plain, html_body = news_html(item, date_str)
    sender.send(sender_address(sender), f"🇳🇱 {item['titel']} – {date_str}", plain, bcc=sorted(rec), html_body=html_body)
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
            pct = round(100 * s["ok"] / s["tot"]) if s["tot"] else 0
            lines.append(f"  • {titles.get(m, m)}: {s['n']} tur, %{pct} doğru")
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


def run_weekly(db, sender, now, dry_run=False):
    titles = module_titles()
    today = now.astimezone(AMS).date()
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

        # Children: the linked parent gets a copy (once, even if they share an e-mail address)
        parent = users.get(u.get("parent_uid") or "")
        if u.get("type") == "child" and parent and parent.get("email") and parent["email"] != u["email"]:
            send_simple(sender, parent["email"], f"NL Oefenbank: {name} için haftalık özet", f"{name} için haftalık özet",
                        f"Merhaba {first_name(parent)},\n\n{name} bu hafta:\n\n{summary}", NOTE_WEEKLY)


def where_gte(col, field, value):
    """Firestore 'field >= value' that works on old and new firebase-admin versions."""
    try:
        from google.cloud.firestore_v1.base_query import FieldFilter
        return col.where(filter=FieldFilter(field, ">=", value))
    except ImportError:
        return col.where(field, ">=", value)


# ---------- entry point ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["hourly", "daily", "weekly"], required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    import firebase_admin
    from firebase_admin import credentials, firestore

    cred = credentials.Certificate(json.loads(os.environ["FIREBASE_SERVICE_ACCOUNT"]))
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    sender = PrintSender() if args.dry_run else GmailSender(os.environ["GMAIL_USER"], os.environ["GMAIL_APP_PASSWORD"])
    now = dt.datetime.now(dt.timezone.utc)
    if args.mode == "hourly":
        run_hourly(db, sender, now, dry_run=args.dry_run)
    elif args.mode == "daily":
        run_daily(db, sender, now, dry_run=args.dry_run, extra=os.environ.get("NEWS_EXTRA_RECIPIENTS", "").split(","))
    else:
        run_weekly(db, sender, now, dry_run=args.dry_run)
    print(f"done: mode={args.mode} dry_run={args.dry_run}")


if __name__ == "__main__":
    main()
