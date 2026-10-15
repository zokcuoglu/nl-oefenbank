"""Mailer job for NL Oefenbank (runs in GitHub Actions, see .github/workflows/mailer.yml).

Modes
  hourly : "kabul edildin" mail to newly approved accounts + send queued announcements
  weekly : weekly summary to every approved account (children: also to the linked parent)

Secrets (GitHub > Settings > Secrets and variables > Actions)
  FIREBASE_SERVICE_ACCOUNT : JSON key of a Firebase service account (reads/writes Firestore)
  GMAIL_USER               : sending address, e.g. nloefenbank@gmail.com
  GMAIL_APP_PASSWORD       : Gmail app password of that address

--dry-run prints the mails instead of sending them and writes nothing to Firestore.
"""
import argparse
import datetime as dt
import json
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path
from zoneinfo import ZoneInfo

SITE = "https://zokcuoglu.github.io/nl-oefenbank/"
ROOT = Path(__file__).resolve().parent.parent
FOOTER = f"\n\n--\nNL Oefenbank · {SITE}\nHaftalık özeti istemiyorsan sitede Profil sayfasından kapatabilirsin."


# ---------- helpers ----------

def module_titles():
    """Exercise id -> readable title, from the same catalog the website uses."""
    cat = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))
    return {m["id"]: m["title"] for m in cat["modules"]}


def is_approved(u):
    return u.get("role") == "admin" or u.get("status") == "approved"


def first_name(u):
    return (u.get("name") or "").split(" ")[0] or "Merhaba"


def iso(t):
    return t.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------- mail sending ----------

class GmailSender:
    """Sends plain-text mail through Gmail SMTP with an app password."""

    def __init__(self, user, password):
        self.user, self.password = user, password

    def send(self, to, subject, body, bcc=None):
        msg = EmailMessage()
        msg["From"] = f"NL Oefenbank <{self.user}>"
        msg["To"] = to
        msg["Subject"] = subject
        msg.set_content(body)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
            s.login(self.user, self.password)
            s.send_message(msg, to_addrs=[to] + list(bcc or []))


class PrintSender:
    """Dry run: show what would be sent."""

    def __init__(self):
        self.sent = []

    def send(self, to, subject, body, bcc=None):
        self.sent.append((to, subject, body, list(bcc or [])))
        print(f"--- MAIL to={to} bcc={len(bcc or [])} subject={subject!r}\n{body}\n")


# ---------- jobs ----------

def run_hourly(db, sender, now, dry_run=False):
    """Welcome mail for newly approved accounts, then queued announcements."""
    users = [(d.id, d.to_dict()) for d in db.collection("users").stream()]

    for uid, u in users:
        if is_approved(u) and u.get("email") and not u.get("welcome_sent_at"):
            body = (f"Merhaba {first_name(u)},\n\n"
                    f"NL Oefenbank hesabın onaylandı. Artık siteye girip alıştırmalara başlayabilirsin:\n{SITE}\n\n"
                    "Her pazar o haftanın kısa bir özetini e-postayla alacaksın." + FOOTER)
            sender.send(u["email"], "NL Oefenbank: hesabın onaylandı", body)
            if not dry_run:
                db.collection("users").document(uid).update({"welcome_sent_at": iso(now)})

    recipients = sorted({u["email"] for _, u in users if is_approved(u) and u.get("email")})
    for a in db.collection("announcements").stream():
        n = a.to_dict()
        if n.get("sent_at") or not recipients:
            continue
        # One mail, everyone in BCC so addresses stay private
        sender.send(sender_address(sender), f"NL Oefenbank: {n.get('subject', '')}", n.get("body", "") + FOOTER, bcc=recipients)
        if not dry_run:
            db.collection("announcements").document(a.id).update({"sent_at": iso(now), "recipients": len(recipients)})


def sender_address(sender):
    return getattr(sender, "user", None) or os.environ.get("GMAIL_USER", "nloefenbank@gmail.com")


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
    today = now.astimezone(ZoneInfo("Europe/Amsterdam")).date()
    cutoff = iso(now - dt.timedelta(days=7))
    users = {d.id: d.to_dict() for d in db.collection("users").stream()}

    for uid, u in users.items():
        if not is_approved(u) or not u.get("email"):
            continue
        att = [d.to_dict() for d in where_gte(db.collection("users").document(uid).collection("attempts"), "finished_at", cutoff).stream()]
        summary = weekly_text(u, att, titles, today)
        name = u.get("name") or "Öğrenci"

        if u.get("email_weekly", True):
            sender.send(u["email"], "NL Oefenbank: haftalık özetin",
                        f"Merhaba {first_name(u)},\n\n{summary}\n\nDevam etmek için: {SITE}" + FOOTER)

        # Children: the linked parent gets a copy (once, even if they share an e-mail address)
        parent = users.get(u.get("parent_uid") or "")
        if u.get("type") == "child" and parent and parent.get("email") and parent["email"] != u["email"]:
            sender.send(parent["email"], f"NL Oefenbank: {name} için haftalık özet",
                        f"Merhaba {first_name(parent)},\n\n{name} bu hafta:\n\n{summary}" + FOOTER)


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
    ap.add_argument("--mode", choices=["hourly", "weekly"], required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    import firebase_admin
    from firebase_admin import credentials, firestore

    cred = credentials.Certificate(json.loads(os.environ["FIREBASE_SERVICE_ACCOUNT"]))
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    if args.dry_run:
        sender = PrintSender()
    else:
        sender = GmailSender(os.environ["GMAIL_USER"], os.environ["GMAIL_APP_PASSWORD"])

    now = dt.datetime.now(dt.timezone.utc)
    (run_hourly if args.mode == "hourly" else run_weekly)(db, sender, now, dry_run=args.dry_run)
    print(f"done: mode={args.mode} dry_run={args.dry_run}")


if __name__ == "__main__":
    main()
