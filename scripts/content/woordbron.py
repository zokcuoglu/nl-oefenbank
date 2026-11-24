"""The ONE source of every Dutch word and expression on NL Oefenbank.

    scripts/content/woorden.csv        single words      (tur: zn, ww, sch_ww, bn, bw, klein, telw, tw, afk)
    scripts/content/uitdrukkingen.csv  multi-word items  (tur: uitdr = deyim, vaste_comb, zin = hazır cümle, structuur)

Why one source: a word used to live in several files (basis/werk/school lists, every news file, mails ...) and
the copies drifted apart. Now a meaning is fixed once and every page, mail and game that shows the word reads it
from here. Other files only point at a row by its id (news items, weekly mail, word study, waiting list).

Columns (same in both files):
  id            never change it: users' word status is saved per id (b001 basis, w001 work notes, s001 school,
                n-<news>-w1 / -u1 news, k001 / u001 new words and expressions)
  nl            the word in dictionary form, with de/het for nouns
  tur           grammatical type (TUREN below), decides which of the two files the row is in
  tr            Turkish meaning; several senses separated by ";"
  niveau        CEFR level for adults, A0-C2
  groep         school year in which a Dutch child knows it: 1-2, 3 ... 8, or vo (after primary school)
  thema, subthema, register   filters of the word page (THEMAS, SUBTHEMAS, REGISTERS below)
  voorbeeld, voorbeeld_tr     main example sentence + Turkish
  uitleg        short explanation in Turkish (optional)
  meer          more examples: "nl = tr | nl = tr" (optional)
  definitie     Dutch definition (school lists, news words; optional)
  woordsoort    how the news page writes the type ("zn (mv)", "vw" ...); empty = from tur
  bron          where the row came from: basis, werk, school, nieuws, mail, woordstudie, bekleme (";" = several)
  lijst         school list name (bron school)
  voorbeeld_door  who wrote the example (work notes)
  alias         old ids of copies merged into this row (";"); answers saved under them still count
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
FILES = {"woorden": HERE / "woorden.csv", "uitdrukkingen": HERE / "uitdrukkingen.csv"}
LEVELS = ["A0", "A1", "A2", "B1", "B2", "C1", "C2"]
GROEPEN = ["1-2", "3", "4", "5", "6", "7", "8", "vo"]
PHRASE_TUR = {"uitdr", "vaste_comb", "zin", "structuur"}
BRONNEN = {"basis", "werk", "school", "nieuws", "mail", "woordstudie", "bekleme"}
TUREN = {
    "zn": "Zelfstandig naamwoord · isim", "ww": "Werkwoord · fiil", "sch_ww": "Scheidbaar werkwoord · ayrılabilen fiil",
    "bn": "Bijvoeglijk naamwoord · sıfat", "bw": "Bijwoord · zarf", "klein": "Kleine woorden · zamir, edat, bağlaç",
    "telw": "Telwoord · sayı", "tw": "Tussenwerpsel · ünlem, selam", "vaste_comb": "Vaste combinatie · sabit kalıp (op zoek naar)",
    "uitdr": "Uitdrukking · deyim", "zin": "Zin · hazır cümle", "structuur": "Grammaticastructuur · dilbilgisi yapısı",
    "afk": "Afkorting · kısaltma",
}
THEMAS = {
    "werk": "Werk · iş yeri", "winkel": "Winkel & boodschappen · alışveriş", "eten": "Eten & drinken · yeme içme",
    "gezondheid": "Gezondheid · sağlık", "wonen": "Wonen · ev", "familie": "Familie · aile", "onderweg": "Onderweg · yolda, ulaşım",
    "school": "School · okul", "weer": "Weer · hava", "tijd": "Tijd & getallen · zaman, sayılar", "kleding": "Kleding · giyim",
    "lichaam": "Lichaam · vücut", "natuur": "Natuur & dieren · doğa, hayvanlar", "overheid": "Overheid & brieven · resmi kurumlar",
    "kennismaken": "Kennismaken · tanışma, selamlaşma", "maatschappij": "Nieuws & maatschappij · haber, toplum",
    "algemeen": "Algemeen · genel",
}
SUBTHEMAS = {"vergadering": "Vergadering · toplantı", "e-mail": "E-mail", "presentatie": "Presentatie · sunum", "techniek": "Techniek · teknik"}
REGISTERS = {"formeel": "Formeel · resmi", "neutraal": "Neutraal · nötr", "informeel": "Informeel · samimi"}
# How the news page writes the type when the row has no own woordsoort
TUR_KORT = {"zn": "zn", "ww": "ww", "sch_ww": "sch ww", "bn": "bn", "bw": "bw", "klein": "vw", "telw": "telw", "tw": "tw",
            "afk": "afk", "uitdr": "uitdr", "vaste_comb": "uitdr", "zin": "zin", "structuur": "structuur"}


def soort_of(tur):
    """Older field the pages still use: woord / afkorting / uitdrukking / zin / structuur."""
    return {"afk": "afkorting", "zin": "zin", "structuur": "structuur", "uitdr": "uitdrukking", "vaste_comb": "uitdrukking"}.get(tur, "woord")


def load():
    """All rows of both files as {id: row}, checked. Any problem stops the build with a clear message."""
    rows, aliases = {}, {}
    for kind, path in FILES.items():
        for n, r in enumerate(csv.DictReader(path.open(encoding="utf-8")), 2):
            where = f"{path.name}:{n} {r.get('id')} {r.get('nl')}"
            assert r["id"] and r["id"] not in rows, f"{where}: empty or duplicate id"
            assert r["nl"] and r["tr"], f"{where}: nl and tr are required"
            assert r["tur"] in TUREN, f"{where}: tur '{r['tur']}' must be one of {list(TUREN)}"
            assert (r["tur"] in PHRASE_TUR) == (kind == "uitdrukkingen"), \
                f"{where}: tur '{r['tur']}' belongs in {'uitdrukkingen' if r['tur'] in PHRASE_TUR else 'woorden'}.csv"
            assert r["niveau"] in LEVELS, f"{where}: niveau '{r['niveau']}'"
            assert r["groep"] in GROEPEN, f"{where}: groep '{r['groep']}' must be one of {GROEPEN}"
            assert r["thema"] in THEMAS, f"{where}: thema '{r['thema']}'"
            assert not r["subthema"] or r["subthema"] in SUBTHEMAS, f"{where}: subthema '{r['subthema']}'"
            assert r["register"] in REGISTERS, f"{where}: register '{r['register']}'"
            assert r["bron"] and set(r["bron"].split(";")) <= BRONNEN, f"{where}: bron '{r['bron']}' (allowed: {sorted(BRONNEN)})"
            for m in filter(None, (p.strip() for p in r["meer"].split(" | "))):
                assert " = " in m, f"{where}: meer needs 'nl = tr': {m}"
            r["kind"] = kind
            rows[r["id"]] = r
            for a in filter(None, r["alias"].split(";")):
                assert a not in aliases, f"{where}: alias {a} used twice"
                aliases[a] = r["id"]
    clash = set(aliases) & set(rows)
    assert not clash, f"alias is also a real id: {sorted(clash)}"
    return rows, aliases


def meer(r):
    out = []
    for m in filter(None, (p.strip() for p in r["meer"].split(" | "))):
        nl, tr = m.split(" = ", 1)
        out.append({"nl": nl.strip(), "tr": tr.strip()})
    return out


def resolve(rows, aliases, ref, where):
    """A reference in a news item / mail / word study: "id" or {"id": ..., "voorbeeld": own sentence ...}.
    Returns (row, extra fields). An unknown id stops the build."""
    rid = ref["id"] if isinstance(ref, dict) else ref
    rid = aliases.get(rid, rid)
    assert rid in rows, f"{where}: word id '{rid}' is not in woorden.csv / uitdrukkingen.csv"
    return rows[rid], ({k: v for k, v in ref.items() if k != "id"} if isinstance(ref, dict) else {})
