"""Daily Lezen mails for adults preparing for the Lezen exam (used by scripts/mailer.py).

Two mails a day until the exam date in the profile (exams.lezen, or the older exam_date):
  morning (lezen_ochtend, default 07:00) : yesterday's wrong answers with the right one, the explanation and the
                                           sentence of the text that gives the answer; a tip of the day; one reading piece
  evening (lezen_aksam,   default 19:00) : today's result, which question types went well, the weakest type over all
                                           rounds with its tip, which text to do next; one reading piece
Who: approved adults with the mail switched on (profile email_lezen, on by default) who did at least one Lezen round,
and whose exam is today or later. Without an exam date: only people who did Lezen in the last 14 days.
A reading piece = one section of one of OUR practice texts (never the official exam texts) with the questions whose
answer is in that section; the answers are at the bottom of the mail, so you can try first.

Everything here is plain data in -> text/HTML out (no Firestore), so it can be tried locally with sample answers:
  python3 scripts/lezen_mail.py   (writes sample mails to /tmp/lezen_ochtend.html and /tmp/lezen_aksam.html)
"""
import datetime as dt
import html as _html
import json
from urllib.parse import quote as _q
import random
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://zokcuoglu.github.io/nl-oefenbank/"
SETS = {   # attempt module -> data file and how a link to one text looks
    "lezen-teksten": {"file": "lezen-teksten.json", "link": "lezen/teksten.html?t=", "name": "Lezen B1"},
    "lezen-a2": {"file": "lezen-a2.json", "link": "lezen/teksten.html?set=a2&t=", "name": "Lezen A2"},
}
OFFICIEEL = "lezen-officieel"   # letters typed in on lezen/officieel.html after an official practice exam
MODULES = tuple(SETS) + (OFFICIEEL,)
WITHOUT_DATE_DAYS = 14
MAX_WRONG = 8
esc = _html.escape

# Tips from the official practice exams 2023 and 2025 (70 questions; see the project table b1_lezen_officieel_sorular.csv)
TIPS = [
    ("Metin türü → amaç sorusu",
     "Resmî örnek sınavlarda 9 amaç sorusunun 9'unda da cevap metin türüne uyuyordu: ikna eden metin → overtuigen / enthousiast maken / "
     "nieuwe … vinden; tanıtan metin → informeren / uitleggen; talimat metni → uitleggen hoe / op de hoogte brengen. "
     "Önce giriş cümlesine (Deze tekst komt van …) ve metnin tonuna bak."),
    ("Kişiye uygulama soruları", "2025'te 35 sorunun 11'i 'Joseph / Marly / Claire …' diye başlıyordu. Önce kişinin durumunu yaz (yaş, saat, ne istiyor), "
     "sonra metinde o duruma uyan kuralı bul. Kendi mantığınla değil, metnin kuralıyla cevapla."),
    ("'Zowel … als …' ve 'én' şıkları", "Cevap iki parçalıysa (hem para hem masraf iadesi; hem coördinator hem diğer buddy'ler) yanlış şıklar "
     "parçalardan sadece birini ya da yanlış eşleşmeyi verir. Metinde iki parçanın da geçtiğini kontrol et."),
    ("Kim karar veriyor?", "'Wie bepaalt …?' sorularında yanlış şıklar rolleri değiştirir (werkgever ↔ OR, buddy ↔ cliënt). "
     "Metinde 'bepaalt / beslist / besluit' fiilinin öznesini bul."),
    ("Eskiden / şimdi", "Metin 'vroeger … tegenwoordig …' diyorsa, eski durum çoğu zaman yanlış şıktır. Soru şimdiki durumu sorar."),
    ("Başka yerden alınmış sayı", "Şıkta metinde geçen bir sayı (50 minuten, € 25,-) olması onu doğru yapmaz. O sayı başka bir kurala ait olabilir. "
     "Sayının geçtiği cümlenin konusuna bak."),
    ("'Alleen' her zaman yanlış değil", "Genelde 'alleen / altijd / nooit' içeren şıklar yanlıştır. Ama metinde bir koşul varsa doğru olabilir "
     "(2025: 'Alleen als het uitje onderdeel is van het lesprogramma' doğru cevaptı)."),
    ("Arama metninde her yere bak", "Son metinde cevap birden fazla bölüme dağılabilir (2025: Visionpas hem 'Aanwezigheid' hem 'Visionpas' "
     "bölümünde). Anahtar kelimeyi metnin geri kalanında da tara."),
    ("Zamanı böl", "110 dakika, 35 soru: soru başına yaklaşık 3 dakika. İlk beş metne toplam 75 dakika, arama metnine 25–30, en sona 5 dakika kontrol."),
    ("Arama metnini baştan okuma", "Önce soruyu oku, ara başlıklarda cevabın yerini bul, sadece o paragrafı oku."),
    ("Boş bırakma", "Puan sadece doğru sayısından hesaplanıyor. Emin değilsen en makul şıkkı işaretle, soruyu not et, sonra geri dön."),
    ("Sözlüğü az kullan", "Van Dale pocketwoordenboek NT2 serbest ama zaman alır. Sadece soruda ya da şıkta geçen ve cevabı değiştiren kelimeye bak."),
    ("Doğru cevap çoğu zaman başka kelimelerle", "Doğru şık metindeki cümleyi başka kelimelerle söyler (beslist de examenleider → "
     "aan de examenleider vragen). Metindeki kelimeyi aynen tekrar eden şık bir tuzak olabilir."),
    ("Görüş soruları", "'Wat vindt … ervan?' / 'Vindt … dat goed?': kişinin metindeki sözlerinin (tırnak içi) özetini seç, yazarın ya da kendi görüşünü değil."),
]


def load_sets():
    """{module: {"data", "q": {"textid:qid": (text, question)}, "text": {id: text}}} for B1 and A2."""
    out = {}
    for m, s in SETS.items():
        data = json.loads((ROOT / "data" / s["file"]).read_text(encoding="utf-8"))
        q = {f"{t['id']}:{v['id']}": (t, v) for t in data["teksten"] for v in t["vragen"]}
        out[m] = {"data": data, "q": q, "text": {t["id"]: t for t in data["teksten"]}, **s}
    return out


def plain_text(md):
    """Markdown-light text of a Lezen text -> plain lines (headings, tables and lists as simple text)."""
    return re.sub(r"\*\*|__", "", md)


def pieces(sets):
    """Reading pieces from our own B1 texts: one '## ' section (plus the intro paragraph for the first one) with the
    questions whose 'bewijs' sentence is in that section. Sections without a question are skipped."""
    out = []
    for t in sets["lezen-teksten"]["data"]["teksten"]:
        parts = re.split(r"\n\s*\n(?=## )", t["tekst"])
        for k, sec in enumerate(parts):
            qs = [v for v in t["vragen"] if v["bewijs"] in sec]
            if not qs or len(sec.split()) > 260:
                continue
            m = re.match(r"## (.+)\n", sec)
            pid = f"{t['id']}#{k}"
            # In the data the right option is mostly the first one (the site shuffles them when it shows a question);
            # a mail shows them in a fixed shuffled order (same order every time for this piece), else the answer would always be A
            rnd = random.Random(pid)
            shown = []
            for v in qs[:2]:
                order = list(range(len(v["opties"])))
                rnd.shuffle(order)
                shown.append({**v, "opties": [v["opties"][i] for i in order], "juist": order.index(v["juist"])})
            out.append({"id": pid, "tekst": t, "kop": m.group(1) if m else "",
                        "body": sec[m.end():].strip() if m else sec.strip(), "vragen": shown})
    return out


def piece_for(all_pieces, day, slot):
    """Same piece for everybody on a day; morning (slot 0) and evening (slot 1) differ; goes round all pieces."""
    return all_pieces[(day.toordinal() * 2 + slot) % len(all_pieces)]


def tip_for(day):
    return TIPS[day.toordinal() % len(TIPS)]


def exam_date(u):
    d = (u.get("exams") or {}).get("lezen") or u.get("exam_date") or ""
    try:
        return dt.date.fromisoformat(d[:10])
    except ValueError:
        return None


_OFF = None
def officieel_rows(a):
    """Wrong answers of an official practice exam: no CvTE question text, only number, text title, type, letters and
    our explanation (data/officieel.json)."""
    global _OFF
    if _OFF is None:
        _OFF = json.loads((ROOT / "data" / "officieel.json").read_text(encoding="utf-8"))
    if a is None:
        return []
    ex = next((e for e in _OFF["examens"] if e["id"] == a.get("test")), None)
    if not ex:
        return []
    out = []
    for x in a.get("answers", []):
        if x.get("correct") or not x.get("chosen"):
            continue                                  # blank = that text was not done yet (one text a day), not a mistake
        n = int(x["qid"].split(":")[1])
        v = ex["vragen"][n - 1]
        t = ex["teksten"][v["tekst"] - 1]
        out.append({"set": {"name": f"Resmî sınav {ex['id']}"}, "tekst": {"titel": t["titel"]},
                    "vraag": {"vraag": f"Vraag {n} · {_OFF['types'][v['soort']]['label']}", "uitleg": v["uitleg"], "bewijs": ""},
                    "gekozen": x.get("chosen") or "", "juist": v["juist"], "link": SITE + "lezen/officieel.html?jaar=" + ex["id"]})
    return out


OFFICIEEL_ORDER = ("2025", "2024", "2023")   # newest official exam first


def next_official(rounds):
    """Next official exam text not done yet: (exam, text) or None when all are done.
    A text counts as done when any of its questions has an answer in a lezen-officieel round."""
    officieel_rows(None)                          # loads data/officieel.json once
    done = {(a.get("test"), int(x["qid"].split(":")[1])) for a in rounds if a.get("module") == OFFICIEEL
            for x in a.get("answers", []) if x.get("chosen")}
    for y in OFFICIEEL_ORDER:
        ex = next((e for e in _OFF["examens"] if e["id"] == y), None)
        for t in (ex["teksten"] if ex else []):
            if not any((y, n) in done for n in range(t["van"], t["tot"] + 1)):
                return ex, t
    return None


def official_block(rounds, M, when):
    """(plain lines, html) suggesting one official exam text for 'when' (bugün / yarın). We only link to the official
    practice site; the CvTE text itself is never in the mail."""
    nx = next_official(rounds)
    link = SITE + "lezen/officieel.html?jaar="
    if not nx:
        line = "Resmî 2023, 2024 ve 2025 sınavlarının bütün metinlerini çözdün. Zorlandığın birini tekrar çözebilirsin."
        return ["", line], _p(esc(line))
    ex, t = nx
    head = f"Resmî sınavdan {when}: {ex['id']} – Tekst {t['nr']}: {t['titel']} (vraag {t['van']}–{t['tot']})"
    how = (f"{_OFF['site']} sitesinde bu metni çöz, sonra sadece bu soruların harflerini Officieel sayfasına gir ve "
           "'Kontrol et'e bas. Yanlışlarını ertesi sabahki mailde açıklamalarıyla görürsün.")
    plain = ["", head, how, f"  Sınav sitesi: {_OFF['site']}", f"  Cevap sayfası: {link}{ex['id']}"]
    html = (f'<div style="border:1px solid {M.C["line"]};border-radius:10px;padding:12px 14px;margin:16px 0">'
            f'<b>Resmî sınavdan {esc(when)}:</b> {esc(ex["id"])} – Tekst {t["nr"]}: <span lang="nl">{esc(t["titel"])}</span> '
            f'<span style="color:{M.C["muted"]}">(vraag {t["van"]}–{t["tot"]})</span><br>{esc(how)}<br>'
            f'<a href="{_OFF["site"]}" style="color:{M.C["blue"]}">Sınav sitesini aç →</a> &nbsp; '
            f'<a href="{link}{ex["id"]}" style="color:{M.C["blue"]}">Cevaplarını gir →</a></div>')
    return plain, html


_SK = None
SK_PER_MAIL = 5
SK_START = dt.date(2026, 11, 24)   # the list starts with its most frequent words from this day on


def exam_words_block(today, slot, M):
    """(plain lines, html): 5 of the B1+ words that come up most in the official exams 2023-2025
    (data/sinav-kelimeleri.json, most frequent first). Every mail (morning = slot 0, evening = 1) takes the next 5."""
    global _SK
    if _SK is None:
        _SK = json.loads((ROOT / "data" / "sinav-kelimeleri.json").read_text(encoding="utf-8"))["woorden"]
    n = len(_SK)
    k = max(0, (today - SK_START).days * 2 + slot - 1)    # evening mail of SK_START = first 5 words
    start = (k * SK_PER_MAIL) % n
    ws = [_SK[(start + i) % n] for i in range(SK_PER_MAIL)]
    page = SITE + "lezen/sinav-kelimeleri.html"
    href = lambda w: SITE + "kelime/?w=" + _q(re.sub(r"^(de|het|een)\s+", "", w["nl"].lower()).strip())
    plain = ["", "SINAVDA EN ÇOK ÇIKAN KELİMELER (2023-2025, B1+)"] + \
            [f"  {w['nl']} – {w['tr']} ({w['y']}/3 yıl, {w['n']} kez)" for w in ws] + [f"  Hepsi: {page}"]
    rows = "".join(f'<tr><td style="padding:3px 10px 3px 0;font-weight:700" lang="nl"><a href="{href(w)}" style="color:{M.C["ink"]};text-decoration:none">{esc(w["nl"])}</a></td>'
                   f'<td style="padding:3px 10px 3px 0">{esc(w["tr"])}</td>'
                   f'<td style="padding:3px 0;color:{M.C["muted"]};font-size:13px;white-space:nowrap">{"●" * w["y"]}{"○" * (3 - w["y"])} {w["n"]}×</td></tr>' for w in ws)
    html = (f'<div style="border:1px solid {M.C["line"]};border-radius:10px;padding:12px 14px;margin:16px 0">'
            f'<b>Sınavda en çok çıkan kelimeler</b> <span style="color:{M.C["muted"]};font-size:13px">(resmî sınavlar 2023–2025, B1+; ●●● = 3 yılın üçünde de)</span>'
            f'<table style="border-collapse:collapse;margin-top:6px">{rows}</table>'
            f'<a href="{page}" style="color:{M.C["blue"]};font-size:14px">Bütün liste ve konular →</a></div>')
    return plain, html


def wrong_answers(attempts, sets):
    """Wrong answers of Lezen rounds, newest round first; one row per question (the last wrong try counts)."""
    rows, seen = [], set()
    for a in sorted(attempts, key=lambda a: a.get("finished_at", ""), reverse=True):
        if a.get("module") == OFFICIEEL:
            rows += [r for r in officieel_rows(a) if r["vraag"]["vraag"] + r["set"]["name"] not in seen]
            seen.update(r["vraag"]["vraag"] + r["set"]["name"] for r in rows)
            continue
        s = sets.get(a.get("module"))
        if not s:
            continue
        for x in a.get("answers", []):
            if x.get("correct") or x["qid"] in seen or x["qid"] not in s["q"]:
                continue
            seen.add(x["qid"])
            t, v = s["q"][x["qid"]]
            chosen = v["opties"][int(x["chosen"])] if str(x.get("chosen", "")).isdigit() else None
            rows.append({"set": s, "tekst": t, "vraag": v, "gekozen": chosen, "juist": v["opties"][v["juist"]],
                         "link": SITE + s["link"] + t["id"]})
    return rows


def pattern_stats(attempts, sets):
    """{pattern number: [correct, total]} over the given rounds (B1 patterns; A2 rounds counted by their own list)."""
    st = defaultdict(lambda: [0, 0])
    for a in attempts:
        if a.get("module") not in sets:
            continue
        for x in a.get("answers", []):
            p = x.get("patroon")
            if p:
                st[(a["module"], p)][1] += 1
                st[(a["module"], p)][0] += bool(x.get("correct"))
    return st


def pattern_name(sets, key):
    module, p = key
    pats = sets[module]["data"]["patronen"]
    return pats[p - 1] if 0 < p <= len(pats) else {"p": f"kalıp {p}", "tr": "", "tip": ""}


def next_text(all_attempts, sets, weakest):
    """Text to do next: a B1 text not done yet with the most questions of the weakest pattern; else any not done; else
    the text with the lowest score."""
    s = sets["lezen-teksten"]
    done = {a.get("test") for a in all_attempts if a.get("module") == "lezen-teksten"}
    todo = [t for t in s["data"]["teksten"] if t["id"] not in done]
    if todo:
        p = weakest[1] if weakest and weakest[0] == "lezen-teksten" else None
        todo.sort(key=lambda t: -sum(v["patroon"] == p for v in t["vragen"]))
        return todo[0], "henüz çözmediğin"
    best = {}
    for a in all_attempts:
        if a.get("module") == "lezen-teksten" and a.get("test") in s["text"] and a.get("total"):
            best[a["test"]] = max(best.get(a["test"], 0), a["score"] / a["total"])
    if best:
        tid = min(best, key=best.get)
        return s["text"][tid], "en düşük puan aldığın"
    return s["data"]["teksten"][0], ""


# ---------- rendering ----------

def _p(t):  # one paragraph
    return f'<p style="margin:0 0 10px;line-height:1.55">{t}</p>'


def piece_html(pc, M):
    """The reading piece: text section, then its questions; answers come at the end of the mail (answers_html)."""
    t = pc["tekst"]
    body = "".join(_p(esc(x).replace("\n", "<br>")) for x in pc["body"].split("\n\n"))
    qs = "".join(
        f'<p style="margin:12px 0 4px;font-weight:700" lang="nl">{k}. {esc(v["vraag"])}</p>'
        + "".join(f'<div style="margin:2px 0 2px 14px" lang="nl">{"ABCD"[i]}. {esc(o)}</div>' for i, o in enumerate(v["opties"]))
        for k, v in enumerate(pc["vragen"], 1))
    return (f'<div style="border:1px solid {M.C["line"]};border-radius:10px;padding:14px 16px;margin:6px 0 4px;background:{M.C["ground"]}">'
            f'<div style="font-size:12px;color:{M.C["muted"]};text-transform:uppercase;letter-spacing:.06em">Okuma parçası · {esc(t["soort"])}</div>'
            f'<div style="font-weight:700;font-size:17px;margin:4px 0 2px" lang="nl">{esc(t["titel"])}</div>'
            + (f'<div style="font-weight:700;color:{M.C["accent"]};margin:6px 0" lang="nl">{esc(pc["kop"])}</div>' if pc["kop"] else "")
            + f'<div lang="nl">{body}</div>{qs}</div>')


def answers_block(pc, M):
    plain = ["", "CEVAPLAR (önce kendin dene)"]
    rows = ""
    for k, v in enumerate(pc["vragen"], 1):
        letter = "ABCD"[v["juist"]]
        plain += [f"{k}. {letter} – {v['opties'][v['juist']]}", f"   {v['uitleg']}"]
        rows += (f'<p style="margin:6px 0"><b>{k}. {letter}</b> – <span lang="nl">{esc(v["opties"][v["juist"]])}</span><br>'
                 f'<span style="color:{M.C["muted"]}">{esc(v["uitleg"])}</span></p>')
    link = SITE + SETS["lezen-teksten"]["link"] + pc["tekst"]["id"]
    plain.append(f"Metnin tamamı: {link}")
    html = (f'<div style="margin-top:22px;padding-top:10px;border-top:2px dashed {M.C["line"]}">'
            f'<div style="font-size:12px;color:{M.C["muted"]};text-transform:uppercase;letter-spacing:.06em">Cevaplar · önce kendin dene</div>'
            f'{rows}<p style="margin:8px 0 0"><a href="{link}" style="color:{M.C["blue"]}">Metnin tamamını sitede aç →</a></p></div>')
    return plain, html


def countdown(today, exam):
    if not exam:
        return ""
    n = (exam - today).days
    return "Sınav bugün. Succes!" if n == 0 else ("Sınav yarın!" if n == 1 else f"Sınava {n} gün kaldı.")


def morning_mail(u, wrong, today, exam, pc, M, rounds=()):
    """(subject, plain, inner html) of the morning mail."""
    name = M.first_name(u)
    cd = countdown(today, exam)
    title, tip = tip_for(today)
    plain = [f"Günaydın {name},", ""] + ([cd, ""] if cd else [])
    inner = _p(f"Günaydın {esc(name)},") + (_p(f"<b>{esc(cd)}</b>") if cd else "")
    if wrong:
        plain.append(f"DÜNKÜ YANLIŞLARIN ({len(wrong)})")
        inner += f'<h3 style="margin:16px 0 6px;font-size:16px">Dünkü yanlışların ({len(wrong)})</h3>'
        for r in wrong[:MAX_WRONG]:
            v = r["vraag"]
            plain += ["", f"{r['tekst']['titel']} ({r['set']['name']})", v["vraag"],
                      f"  Senin cevabın: {r['gekozen'] or '(boş)'}", f"  Doğru cevap: {r['juist']}",
                      f"  Neden: {v['uitleg']}"] + ([f"  Metinde: \"{v['bewijs']}\""] if v["bewijs"] else []) + [f"  {r['link']}"]
            inner += (f'<div style="border-left:4px solid {M.C["accent"]};padding:6px 0 6px 12px;margin:12px 0">'
                      f'<div style="font-size:12px;color:{M.C["muted"]}">{esc(r["tekst"]["titel"])} · {esc(r["set"]["name"])}</div>'
                      f'<div style="font-weight:700;margin:2px 0 6px" lang="nl">{esc(v["vraag"])}</div>'
                      f'<div lang="nl">✗ <s style="color:{M.C["muted"]}">{esc(r["gekozen"] or "(boş)")}</s></div>'
                      f'<div lang="nl" style="color:{M.C["a1"]};font-weight:700">✓ {esc(r["juist"])}</div>'
                      f'<div style="margin-top:6px">{esc(v["uitleg"])}</div>'
                      + (f'<div style="margin-top:4px;color:{M.C["muted"]}" lang="nl">Metinde: “{esc(v["bewijs"])}”</div>' if v["bewijs"] else "")
                      + f'<a href="{r["link"]}" style="color:{M.C["blue"]};font-size:14px">Metni aç →</a></div>')
        if len(wrong) > MAX_WRONG:
            plain.append(f"(+{len(wrong) - MAX_WRONG} yanlış daha; sitede metnin sonuç ekranında görebilirsin)")
            inner += _p(f'<span style="color:{M.C["muted"]}">+{len(wrong) - MAX_WRONG} yanlış daha: sitede metnin sonuç ekranında.</span>')
    else:
        plain.append("Dün yanlışın yok (ya da dün Lezen çözmedin). Bugün bir metin daha çözmeye ne dersin?")
        inner += _p("Dün yanlışın yok (ya da dün Lezen çözmedin). Bugün bir metin daha çözmeye ne dersin?")
    plain += ["", f"GÜNÜN İPUCU: {title}", tip, "", "OKUMA PARÇASI", pc["tekst"]["titel"]]
    inner += (f'<div style="background:{M.C["blue_soft"]};border-radius:10px;padding:12px 14px;margin:18px 0">'
              f'<b>Günün ipucu: {esc(title)}</b><br>{esc(tip)}</div>')
    op, oh = official_block(rounds, M, "bugün")
    wp, wh = exam_words_block(today, 0, M)
    plain[-3:-3] = op + wp
    inner += oh + wh
    plain += [pc["kop"], plain_text(pc["body"])] + [f"{k}. {v['vraag']}\n" + "\n".join(f"   {'ABCD'[i]}. {o}" for i, o in enumerate(v["opties"]))
                                                       for k, v in enumerate(pc["vragen"], 1)]
    inner += piece_html(pc, M)
    ap, ah = answers_block(pc, M)
    subject = f"Lezen · {('dünkü ' + str(len(wrong)) + ' yanlışın') if wrong else 'günün parçası'}" + (f" · {cd}" if cd else "")
    return subject, "\n".join(plain + ap), inner + ah


def evening_mail(u, today_att, all_att, today, exam, pc, sets, M):
    name = M.first_name(u)
    cd = countdown(today, exam)
    plain = [f"İyi akşamlar {name},", ""] + ([cd, ""] if cd else [])
    inner = _p(f"İyi akşamlar {esc(name)},") + (_p(f"<b>{esc(cd)}</b>") if cd else "")
    lez = [a for a in today_att if a.get("module") in MODULES and a.get("total")]
    if lez:
        ok, tot = sum(a["score"] for a in lez), sum(a["total"] for a in lez)
        names = ", ".join(dict.fromkeys(a.get("title", a.get("test", "")) for a in lez))
        line = f"Bugün {len(lez)} Lezen turu çözdün ({names}): {tot} sorudan {ok} doğru (%{round(100 * ok / tot)})."
        plain.append(line)
        inner += _p(esc(line))
        good = [(k, v) for k, v in pattern_stats(lez, sets).items() if v[1] and v[0] == v[1]]
        if good:
            g = "; ".join(f"{pattern_name(sets, k)['tr']} ({v[0]}/{v[1]})" for k, v in good[:4])
            plain.append(f"İyi gidenler (hepsi doğru): {g}")
            inner += _p(f'<b style="color:{M.C["a1"]}">İyi gidenler:</b> {esc(g)}')
        nwrong = sum(1 for x in lez for y in x.get("answers", []) if not y.get("correct"))
        if nwrong:
            plain.append(f"{nwrong} yanlışını yarın sabahki mailde açıklamalarıyla göreceksin.")
            inner += _p(f"{nwrong} yanlışını yarın sabahki mailde açıklamalarıyla göreceksin.")
    else:
        plain.append("Bugün Lezen çözmedin. 15 dakikan varsa bir metin yeter; aşağıdaki parça da iyi bir başlangıç.")
        inner += _p("Bugün Lezen çözmedin. 15 dakikan varsa bir metin yeter; aşağıdaki parça da iyi bir başlangıç.")
    # weakest question type over all rounds (at least 3 answers of that type)
    st = [(k, v) for k, v in pattern_stats(all_att, sets).items() if v[1] >= 3]
    weakest = min(st, key=lambda kv: kv[1][0] / kv[1][1])[0] if st else None
    if weakest:
        p = pattern_name(sets, weakest)
        v = dict(st)[weakest]
        plain += ["", f"EN ZAYIF SORU TÜRÜN: {p['tr']} – {v[0]}/{v[1]} doğru", f"İpucu: {p['tip']}"]
        inner += (f'<div style="background:{M.C["blue_soft"]};border-radius:10px;padding:12px 14px;margin:16px 0">'
                  f'<b>En zayıf soru türün:</b> {esc(p["tr"])} <span style="color:{M.C["muted"]}">({v[0]}/{v[1]} doğru)</span><br>'
                  f'<span lang="nl" style="color:{M.C["muted"]}">{esc(p["p"])}</span><br>İpucu: {esc(p["tip"])}</div>')
    t, why = next_text(all_att, sets, weakest)
    link = SITE + SETS["lezen-teksten"]["link"] + t["id"]
    plain += ["", f"YARIN ŞUNU ÇÖZ: {t['titel']}" + (f" ({why} metin)" if why else ""), link]
    inner += _p(f'<b>Yarın şunu çöz:</b> <a href="{link}" style="color:{M.C["blue"]}" lang="nl">{esc(t["titel"])}</a>'
                + (f' <span style="color:{M.C["muted"]}">({why} metin)</span>' if why else ""))
    op, oh = official_block(all_att, M, "yarın")
    wp, wh = exam_words_block(today, 1, M)
    plain += op + wp
    inner += oh + wh
    plain += ["", "OKUMA PARÇASI", pc["tekst"]["titel"], pc["kop"], plain_text(pc["body"])] + \
             [f"{k}. {v['vraag']}\n" + "\n".join(f"   {'ABCD'[i]}. {o}" for i, o in enumerate(v["opties"])) for k, v in enumerate(pc["vragen"], 1)]
    inner += piece_html(pc, M)
    ap, ah = answers_block(pc, M)
    subject = "Lezen · bugünün özeti" + (f" · {cd}" if cd else "")
    return subject, "\n".join(plain + ap), inner + ah


if __name__ == "__main__":
    # Local preview with made-up answers (no Firestore): writes two HTML files to look at in a browser
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("mailer", ROOT / "scripts" / "mailer.py")
    M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
    sets = load_sets(); pcs = pieces(sets)
    today = dt.date(2026, 11, 25)
    t = sets["lezen-teksten"]["data"]["teksten"][6]
    att = [{"module": "lezen-teksten", "test": t["id"], "title": t["titel"], "finished_at": "2026-11-24T20:00:00Z",
            "score": 4, "total": 6, "answers": [{"qid": f"{t['id']}:{v['id']}", "chosen": str((v["juist"] + (k in (1, 3))) % len(v["opties"])),
                                                   "correct": k not in (1, 3), "patroon": v["patroon"]} for k, v in enumerate(t["vragen"])]}]
    u = {"name": "Test Kişi"}
    s1, p1, h1 = morning_mail(u, wrong_answers(att, sets), today, dt.date(2026, 12, 1), piece_for(pcs, today, 0), M)
    s2, p2, h2 = evening_mail(u, att, att, today, dt.date(2026, 12, 1), piece_for(pcs, today, 1), sets, M)
    Path("/tmp/lezen_ochtend.html").write_text(M.html_wrap("Lezen · sabah", h1, "not"), encoding="utf-8")
    Path("/tmp/lezen_aksam.html").write_text(M.html_wrap("Lezen · akşam", h2, "not"), encoding="utf-8")
    print(len(pcs), "pieces |", s1, "|", s2)
    print(p1[:1500])
