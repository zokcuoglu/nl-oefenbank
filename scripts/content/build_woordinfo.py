"""Builds oyunlar/woordinfo.json: the word box of the daily games (de/het, düzensiz fiiller, Bağlantılar, NT2 Bulmaca, Woordle).

Clicking a word in a game opens a box with: meaning, level, explanation, example sentences and the places on
the site where the word is used or taught (each a link that opens that exact text or lesson).

Run after changing data/woorden.json, the news, the Lezen/Luisteren texts or a game's word list:
    python3 scripts/content/build_woordinfo.py
The preposition games have their own info block (build_voorzetsels.py), because they work with combinations.
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
load = lambda p: json.loads((ROOT / p).read_text(encoding="utf-8"))
ART = re.compile(r"^(de|het|een)\s+", re.I)
key = lambda s: ART.sub("", str(s).strip().lower())                       # "de appel" -> "appel"
TURKISH = set("şğıİŞĞç")                                                # letters Dutch does not use: a Turkish string
TR_WORDS = re.compile(r"\b(ile|ve|bir|bu|olur|için|değil|gibi|ama|da|de)\b")   # short Turkish words in mixed lesson text

# ---------- 1. Which words do the games use? ----------
POOL = load("data/woorden.json")["woorden"]
VERBS = load("oyunlar/werkwoorden.json")["werkwoorden"]
words = {}                                                              # key -> {"tr": fallback meaning, "forms": extra forms to search for}
for v in VERBS:
    words[key(v["inf"])] = {"tr": v["tr"], "verb": v}
for w in POOL:                                                          # de/het takes its nouns from the pool
    if w.get("tur") == "zn" and re.fullmatch(r"(de|het) [a-zà-ÿ-]+", w["nl"]):
        words.setdefault(key(w["nl"]), {"tr": w["tr"]})
for g in load("oyunlar/verbanden.json")["groups"]:
    for w in g["w"]:
        words.setdefault(key(w["nl"]), {"tr": w["tr"]})
# Woordle (Dutch): answers of 4-6 letters from the pool (groep 1-6) and the Slimspel crossword / word search lists
for w in POOL:
    t = key(w["nl"])
    if str(w.get("groep")) in {"1-2", "3", "4", "5", "6"} and w.get("soort", "woord") == "woord" and re.fullmatch(r"[a-z]{4,6}", t) and "ij" not in t:
        words.setdefault(t, {"tr": w["tr"]})
for x in load("slimspel/kruiswoord/woorden.json")["words"]:
    if re.fullmatch(r"[a-z]{4,6}", x["w"].lower()): words.setdefault(x["w"].lower(), {"tr": ""})
for th in load("slimspel/woordzoeker/woorden.json")["themes"]:
    for x in th["words"]:
        if re.fullmatch(r"[a-z]{4,6}", x.lower()): words.setdefault(x.lower(), {"tr": ""})
KW = load("oyunlar/kruiswoord-nt2.json")["words"]
for w in KW:
    words.setdefault(key(w["w"]), {"tr": w["c"]})
    words[key(w["w"])].setdefault("kw", w)

# ---------- 2. Where on the site can a word be found? ----------
# Item by item (one news item, one Lezen text, one KNM question, one KNM critical word ...), each with a link that
# opens exactly that item: see site_places.py (shared with build_voorzetsels.py). Teaching places come first.
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_places import all_places
PLACES = [p for p in all_places() if p["href"]]                       # no link = not shown on the site
TAUGHT = {}                                                            # word -> places that explain exactly this word
for pl in PLACES:
    if pl["kind"] in ("knm-woord", "woordstudie"): TAUGHT.setdefault(key(pl["woord"]), []).append(pl)
POOL_BY_KEY = {}
for w in POOL:
    if w.get("tur") != "uitdr": POOL_BY_KEY.setdefault(key(w["nl"]), w)
NEWS = {it["id"]: it["titel"] for it in load("data/nieuws.json")["items"]}
COMMON = 25    # a word in more places than this is too common for "used in" tags

def pattern(k, info):
    """Whole-word match on the word and, for irregular verbs, on their past forms too (liep, gelopen ...)."""
    forms = {k}
    v = info.get("verb")
    if v: forms |= {f.lower() for f in v["imp"] + [v.get("impMv") or "", v["vd"]] if f}
    return re.compile(r"(?<![\wà-ÿ-])(" + "|".join(sorted(map(re.escape, forms), key=len, reverse=True)) + r")(?![\wà-ÿ-])", re.I)

# ---------- 3. One info block per word ----------
info = {}
for k, src in sorted(words.items()):
    p = POOL_BY_KEY.get(k, {})
    v = src.get("verb")
    uitleg = p.get("uitleg", "")
    if v:   # irregular verb: the forms are the most useful explanation
        hulp = "/".join(v["hulp"])
        uitleg = (f"Düzensiz fiil. Geçmiş zaman: {'/'.join(v['imp'])}" + (f" (çoğul: {v['impMv']})" if v.get("impMv") else "")
                  + f". Perfectum: {hulp} {v['vd']}." + (f" {uitleg}" if uitleg else ""))
    ex = []
    if p.get("voorbeeld"): ex.append({"nl": p["voorbeeld"], "tr": p.get("voorbeeld_tr", "")})
    ex += [{"nl": m["nl"], "tr": m.get("tr", "")} for m in (p.get("meer") or []) if isinstance(m, dict)][:2]
    kw = src.get("kw")
    if kw and kw.get("z") and len(ex) < 3:   # crossword sentence; zf = correct sentence when the word is inflected there
        zin = kw.get("zf") or kw["z"].replace("___", kw["w"].lower())
        ex.append({"nl": zin[:1].upper() + zin[1:], "tr": kw.get("zt", "")})
    seen_ex = set()
    ex = [e for e in ex if not (e["nl"].lower() in seen_ex or seen_ex.add(e["nl"].lower()))]

    # Tags: 1) places that explain this very word (KNM critical word, word study), 2) the news items the pool
    # links it to, 3) items with a sentence containing the word. Every tag keeps that sentence (z) so the
    # player sees why it is there.
    tags = [{"t": pl["t"], "href": pl["href"], "z": ""} for pl in TAUGHT.get(k, [])]
    for nid in p.get("in_nieuws") or []:
        if nid in NEWS: tags.append({"t": f"Nieuws · {NEWS[nid]}", "href": f"nieuws/?id={nid}", "z": ""})
    rx = pattern(k, src)
    real = []                                                           # real sentences from the site, with their link
    for pl in PLACES:
        if pl["kind"] in ("knm-woord", "woordstudie"): continue
        hit = next((z for z in pl["zinnen"] if rx.search(z)), None)
        if hit:
            tags.append({"t": pl["t"], "href": pl["href"], "z": hit})
            if len(real) < 2 and hit.lower() not in seen_ex: real.append({"nl": hit, "tr": "", "t": pl["t"], "href": pl["href"]})
    # A very common word (zijn, werken) occurs everywhere: those uses say nothing, so keep only the places
    # that teach it and its news items
    if len(tags) > COMMON:
        tags = [t for t in tags if not t["z"]]
    seen, out = set(), []
    for t in tags:
        if t["href"] not in seen: seen.add(t["href"]); out.append(t)
    info[k] = {"tr": p.get("tr") or src["tr"], "niveau": p.get("niveau") or (kw or {}).get("n", ""),
               "uitleg": uitleg, "voorbeelden": ex + real, "tags": out[:6]}

data = {"_about": "Word box of the daily games. Generated by scripts/content/build_woordinfo.py - edit that script or its sources, not this file.",
        "woorden": info}
(ROOT / "oyunlar/woordinfo.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
print(f"{len(info)} words, {sum(1 for i in info.values() if i['tags'])} with tags, "
      f"{sum(1 for i in info.values() if not i['voorbeelden'])} without examples, "
      f"{(ROOT / 'oyunlar/woordinfo.json').stat().st_size // 1024} KB")
