"""Build data/woorden.json: one shared word pool for the word tests (woorden/ page), word pages and games.

Source: scripts/content/woorden.csv + scripts/content/uitdrukkingen.csv (read and checked by woordbron.py).
Those two files are the only place where a word's meaning, level, groep and labels are written; news items,
the weekly mail and the word study only point at a row by id. Run build_nieuws.py first (or scripts/build_all.py):
this script reads data/nieuws.json to know which news items use which word.

Run:  python3 scripts/content/build_woorden.py
      python3 scripts/content/build_woorden.py --kandidaat B1   # werk/school words not yet used in any news text

Every entry has two levels:
  niveau = CEFR level for adult learners (A0-C2)
  groep  = school year in which a Dutch child typically knows the word: 1-2, 3 ... 8, or "vo" (after primary
           school: office, formal or technical language). Child accounts only get words up to their own groep, never "vo".
  The groep labels follow the logic of the Dutch school word lists (BAK for groep 1-2, WAK for groep 3-8); they are
  our own judgement, not copied from those lists.

Output per entry: the source row plus bron (first source, for the page labels), bronnen (all sources),
in_nieuws (news items that use it), item/nr (first such item, for the "Haber #n" label).
Top level "alias": old id -> id, for copies that were merged (word status saved under an old id still counts).
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
NIEUWS = ROOT / "data" / "nieuws.json"
OUT = ROOT / "data" / "woorden.json"
sys.path.insert(0, str(HERE))
import woordbron
from woordbron import LEVELS, GROEPEN, TUREN, THEMAS, SUBTHEMAS, REGISTERS

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


def main():
    rows, aliases = woordbron.load()
    items = json.loads(NIEUWS.read_text(encoding="utf-8"))["items"]
    # Hand-written meanings for the word page (scripts/content/anlamlar/*.json): their short meaning wins for
    # words that are not only news words (a news-only word keeps the meaning it has in that one text)
    hand = {}
    for f in sorted((HERE / "anlamlar").glob("*.json")):
        hand.update(json.loads(f.read_text(encoding="utf-8")))
    bare = lambda nl: re.sub(r"^(de|het|een)\s+", "", nl.strip().lower())

    pool = []
    for r in rows.values():
        bronnen = r["bron"].split(";")
        used = [i for i in items if r["id"] in i.get("woord_ids", []) + i.get("uitdr_ids", []) + i.get("werk_woorden", [])]
        if any(b in ("werk", "school") for b in bronnen):   # work/school words: also news texts that just use them
            used += [i for i in items if i not in used and appears_in(r["nl"], item_text(i))]
        used.sort(key=lambda i: i["nr"])
        w = {"id": r["id"], "bron": bronnen[0], "bronnen": bronnen, "nl": r["nl"], "soort": woordbron.soort_of(r["tur"]),
             "tr": r["tr"], "niveau": r["niveau"], "groep": r["groep"], "thema": r["thema"], "subthema": r["subthema"],
             "register": r["register"], "tur": r["tur"], "voorbeeld": r["voorbeeld"], "voorbeeld_tr": r["voorbeeld_tr"],
             "uitleg": r["uitleg"], "meer": woordbron.meer(r), "in_nieuws": [i["id"] for i in used]}
        for f in ("definitie", "lijst", "voorbeeld_door", "woordsoort"):
            if r[f]: w[f] = r[f]
        if used: w["item"], w["nr"] = used[0]["id"], used[0]["nr"]
        h = hand.get(bare(r["nl"]))
        if h and bronnen != ["nieuws"] and w["soort"] == "woord":
            w["tr"] = h["kort"]
        pool.append(w)

    if "--kandidaat" in sys.argv:
        lvl = sys.argv[sys.argv.index("--kandidaat") + 1].upper()
        # Candidates for new news texts: work and school words of this level that no news text uses yet
        free = [w for w in pool if set(w["bronnen"]) & {"werk", "school"} and w["niveau"] == lvl and not w["in_nieuws"]]
        print(f"{len(free)} werk/school words at {lvl} not used in any news text yet:")
        for w in free:
            print(f"  {w['id']}  {w['nl']}  = {w['tr']}  (groep {w['groep']})")
        return

    OUT.write_text(json.dumps({
        "_about": "Shared word pool. Generated by scripts/content/build_woorden.py from scripts/content/woorden.csv + uitdrukkingen.csv - do not edit by hand.",
        "levels": LEVELS,
        "groepen": GROEPEN,
        "turen": TUREN, "themas": THEMAS, "subthemas": SUBTHEMAS, "registers": REGISTERS,
        "alias": aliases,
        "woorden": pool,
    }, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")

    print(f"{len(pool)} entries ({len(aliases)} merged ids) -> {OUT}")
    print("  per source:", dict(Counter(b for w in pool for b in w["bronnen"])))
    print("  per level: ", {l: c for l in LEVELS if (c := sum(w["niveau"] == l for w in pool))})
    print("  per groep: ", {g: c for g in GROEPEN if (c := sum(w["groep"] == g for w in pool))})
    print("  per tur:   ", dict(Counter(w["tur"] for w in pool)))
    print("  per thema: ", dict(Counter(w["thema"] for w in pool)))
    print(f"  words used in a news text: {sum(1 for w in pool if w['in_nieuws'])}")


if __name__ == "__main__":
    main()
