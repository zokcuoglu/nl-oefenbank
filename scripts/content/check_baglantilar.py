"""Check that everything on NL Oefenbank is linked to the one word source and that no link is dead.

Why: words are written once (woorden.csv / uitdrukkingen.csv) and every other place points at them by id or
links to their word page (kelime/?w=...). A typo in an id or a page that was never generated would silently
show "no page" to a user. This check stops the build instead (scripts/build_all.py runs it after the builders).

Checks:
  1. every word / expression of the pool has a word page (oyunlar/woordinfo.json)
  2. weekly mail (data/weekbrief.json) and word study (data/woordstudie.json) ids exist in the pool
  3. every link inside the site data and the waiting list opens an existing item:
     kelime/?w=, nieuws/?id=, woordstudie/?w=, dersler/?les=, lezen/teksten.html?t=, knm/?q= / ?w=
Run: python3 scripts/content/check_baglantilar.py
"""
import glob, json, re, sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
load = lambda p: json.loads((ROOT / p).read_text(encoding="utf-8"))
key = lambda s: re.sub(r"^(de|het|een)\s+", "", s.strip().lower())   # same key as kelime/index.html
errors = []

pool = load("data/woorden.json")
ids = {w["id"]: w for w in pool["woorden"]}
alias = pool.get("alias", {})
pages = set(load("oyunlar/woordinfo.json")["woorden"])

# 1. a word page for every pool entry
for w in pool["woorden"]:
    if key(w["nl"]) not in pages:
        errors.append(f"word page missing: {w['id']} {w['nl']}")

# 2. ids used by the mail and the word study
def known(i, where):
    if alias.get(i, i) not in ids:
        errors.append(f"{where}: id {i} is not in woorden.csv / uitdrukkingen.csv")
for wk in load("data/weekbrief.json")["weken"]:
    for k in ("woord", "deyim"):
        known(wk[k]["id"], f"weekbrief {wk['id']} {k}")
for x in load("data/woordstudie.json")["woorden"]:
    if not x.get("woorden"):
        errors.append(f"woordstudie {x['id']}: 'woorden' (pool ids) is empty")
    for i in x.get("woorden", []):
        known(i, f"woordstudie {x['id']}")

# 3. links inside the data files and the waiting list
knm = load("data/knm.json")
targets = {
    "kelime/?w=": pages,
    "nieuws/?id=": {i["id"] for i in load("data/nieuws.json")["items"]},
    "woordstudie/?w=": {w["id"] for w in load("data/woordstudie.json")["woorden"]},
    "woordstudie/?bolum=gunluk&w=": {w["id"] for w in load("data/woordstudie.json")["woorden"]},
    "dersler/?les=": {l["id"] for l in load("data/dersler.json")["lessen"]},
    "lezen/teksten.html?t=": {t["id"] for t in load("data/lezen-teksten.json")["teksten"]},
    "lezen/teksten.html?set=a2&t=": {t["id"] for t in load("data/lezen-a2.json")["teksten"]},
    "knm/?q=": {q["id"] for c in knm["qbank"].values() for q in c.get("items", [])},
    "knm/?w=": {w["id"] for c in knm["vocab"].values() for w in c.get("words", [])},
}
LINK = re.compile(r"(" + "|".join(re.escape(t).replace("\\?", "\\?") for t in sorted(targets, key=len, reverse=True)) + r")([^\"&)\s#\\]+)")
for f in sorted(glob.glob(str(ROOT / "data/*.json")) + glob.glob(str(ROOT / "oyunlar/*.json")) + [str(ROOT / "docs/bekleme_listesi.md")]):
    for m in LINK.finditer(Path(f).read_text(encoding="utf-8")):
        t, v = m.group(1), unquote(m.group(2))
        if (key(v) if t == "kelime/?w=" else v) not in targets[t]:
            errors.append(f"{Path(f).relative_to(ROOT)}: dead link {t}{m.group(2)}")

if errors:
    print("\n".join(sorted(set(errors))[:60]))
    sys.exit(f"{len(set(errors))} link problem(s)")
print(f"links ok: {len(pages)} word pages, every pool word has one, mail / word study / waiting list ids exist")
