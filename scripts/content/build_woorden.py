"""Build data/woorden.json: one shared word pool for the word tests (woorden/ page).

Sources:
  1. scripts/content/werk_woorden.csv  - words and phrases from Zana's work notes (bron = "werk")
  2. data/nieuws.json                   - the words (woordenschat) and idioms (uitdrukkingen) of every news item (bron = "nieuws")
     -> run build_nieuws.py first, this script reads its output.

Run:  python3 scripts/content/build_woorden.py
      python3 scripts/content/build_woorden.py --kandidaat B1   # werk words not yet used in any news text (for writing new items)

Why one pool: the test page can then mix work words and news words, filter by level/type/source,
and a news item can list which work words it uses (field werk_woorden in nNN_*.py).
"""
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
CSV = HERE / "werk_woorden.csv"
NIEUWS = ROOT / "data" / "nieuws.json"
OUT = ROOT / "data" / "woorden.json"

LEVELS = ["A0", "A1", "A2", "B1", "B2", "C1", "C2"]
SOORT = {"woord", "uitdrukking", "zin", "structuur", "afkorting"}
TEXT_LEVELS = ["a0", "a1", "a2", "b1", "b2", "c1", "c2"]
# Words that stand for "something/someone" in a dictionary form; they are not in the real sentence
PLACEHOLDERS = {"iets", "ergens", "iemand", "zich", "je", "jouw", "mijn", "zijn", "de", "het", "een", "van", "met", "op", "aan", "in", "naar", "voor", "om", "te", "tot"}


def key_tokens(nl):
    """Main words of an entry, for finding it back in a text: 'iets doorhebben' -> ['doorhebben']."""
    t = re.sub(r"\(.*?\)|\[.*?\]", " ", nl.lower())
    t = re.sub(r"[^\wà-ÿ' -]", " ", t)
    return [w for w in t.split() if len(w) >= 3 and w not in PLACEHOLDERS]


def appears_in(nl, text):
    """Check whether an entry is used in a text: all its main words occur in ONE sentence, in the same order,
    allowing a changed ending (helder -> heldere). Misses some forms (split verbs: doorhebben -> had het niet door),
    but avoids false hits from words that are spread over the whole text."""
    toks = key_tokens(nl)
    if not toks:
        return False
    stem = lambda t: t[:max(4, len(t) - 2)] if len(t) > 4 else t
    for sentence in re.split(r"[.!?\n]+", re.sub(r"<[^>]+>", " ", text.lower())):
        words, pos = re.findall(r"[\wà-ÿ']+", sentence), 0
        for t in toks:
            hit = next((k for k in range(pos, len(words)) if (words[k] == t if len(t) <= 4 else words[k].startswith(stem(t)))), None)
            if hit is None:
                break
            pos = hit + 1
        else:
            return True
    return False


def item_text(item):
    return " ".join(item.get(l, "") for l in TEXT_LEVELS)


def load_werk():
    rows = list(csv.DictReader(CSV.open(encoding="utf-8")))
    seen = set()
    for r in rows:
        assert r["id"] not in seen, f"duplicate id {r['id']}"
        seen.add(r["id"])
        assert r["niveau"] in LEVELS, f"{r['id']}: niveau {r['niveau']}"
        assert r["soort"] in SOORT, f"{r['id']}: soort {r['soort']}"
        assert r["nl"] and r["tr"] and r["voorbeeld"], f"{r['id']}: empty nl/tr/voorbeeld"
    return rows


def main():
    werk = load_werk()
    items = json.loads(NIEUWS.read_text(encoding="utf-8"))["items"]

    pool = []
    for r in werk:
        pool.append({
            "id": r["id"], "bron": "werk", "nl": r["nl"], "soort": r["soort"], "tr": r["tr"], "niveau": r["niveau"],
            "thema": r["thema"], "voorbeeld": r["voorbeeld"], "voorbeeld_tr": r["voorbeeld_tr"], "uitleg": r["uitleg"],
            "voorbeeld_door": r["voorbeeld_door"],
            # News items whose text uses this work word (direction 1: work notes -> news)
            "in_nieuws": [i["id"] for i in items if r["id"] in i.get("werk_woorden", []) or appears_in(r["nl"], item_text(i))],
        })
    for it in items:
        for k, line in enumerate(it["woordenschat"].splitlines(), 1):
            woord, zn, betekenis, voorbeeld, turks, niveau = [c.strip() for c in line.split("|")]
            pool.append({"id": f"n-{it['id']}-w{k}", "bron": "nieuws", "item": it["id"], "nr": it["nr"], "nl": woord,
                         "soort": "woord", "woordsoort": zn, "tr": turks, "niveau": niveau or "B1", "thema": "nieuws",
                         "definitie": betekenis, "voorbeeld": voorbeeld, "voorbeeld_tr": "", "uitleg": ""})
        for k, u in enumerate(it["uitdrukkingen"], 1):
            pool.append({"id": f"n-{it['id']}-u{k}", "bron": "nieuws", "item": it["id"], "nr": it["nr"], "nl": u["nl"],
                         "soort": "uitdrukking", "tr": u["tr"], "niveau": u["niveau"], "thema": "nieuws",
                         "voorbeeld": u.get("voorbeeld", ""), "voorbeeld_tr": u.get("voorbeeld_tr", ""), "uitleg": u.get("uitleg", "")})

    for w in pool:
        assert w["niveau"] in LEVELS, f"{w['id']}: niveau {w['niveau']}"

    if "--kandidaat" in sys.argv:
        lvl = sys.argv[sys.argv.index("--kandidaat") + 1].upper()
        free = [w for w in pool if w["bron"] == "werk" and w["niveau"] == lvl and not w["in_nieuws"]]
        print(f"{len(free)} werk words at {lvl} not used in any news text yet:")
        for w in free:
            print(f"  {w['id']}  {w['nl']}  = {w['tr']}")
        return

    OUT.write_text(json.dumps({
        "_about": "Shared word pool. Generated by scripts/content/build_woorden.py from werk_woorden.csv and data/nieuws.json - do not edit by hand.",
        "levels": LEVELS,
        "woorden": pool,
    }, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")

    used = sum(1 for w in pool if w.get("in_nieuws"))
    print(f"{len(pool)} entries -> {OUT}")
    print("  per source:", dict(Counter(w["bron"] for w in pool)))
    print("  per level: ", {l: c for l in LEVELS if (c := sum(w["niveau"] == l for w in pool))})
    print(f"  werk words already in a news text: {used}")


if __name__ == "__main__":
    main()
