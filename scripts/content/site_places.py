"""Every place on NL Oefenbank where a Dutch word or phrase can occur, item by item, with a link that opens
exactly that item. Shared by build_voorzetsels.py (source of a game sentence + tags) and build_woordinfo.py.

A place: {"t": label, "href": link from the site root, "kind": what it is, "text": normalised full text,
          "zinnen": the Dutch sentences in it}
Order = priority for tags: places that TEACH a word (KNM word list, word study, lessons) come before texts
that only USE it.
"""
import json, re, html, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
load = lambda p: json.loads((ROOT / p).read_text(encoding="utf-8"))
TURKISH = set("şğıİŞĞç")
TR_WORDS = re.compile(r"\b(ile|ve|bir|bu|olur|için|değil|gibi|ama|da)\b")

INLINE = re.compile(r"</?(strong|b|em|i|u|span|a|mark|abbr)\b[^>]*>", re.I)
def untag(s):
    """HTML to text: inline tags (<strong> in 'een <strong>woord</strong>:') vanish, block tags become a space."""
    return html.unescape(re.sub(r"<[^>]+>", " ", INLINE.sub("", s)))

def norm(s):
    """Lower case, no HTML/markdown, curly quotes straight, single spaces: for 'is this sentence in that text'."""
    s = untag(str(s))
    s = unicodedata.normalize("NFC", s).replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("**", "").replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip().lower()

def strings(x):
    if isinstance(x, str): yield x
    elif isinstance(x, list):
        for y in x: yield from strings(y)
    elif isinstance(x, dict):
        for y in x.values(): yield from strings(y)

def sentences(obj):
    """Dutch sentences of 4-25 words in any string of obj (Turkish explanation text is skipped)."""
    out = []
    for s in strings(obj):
        s = untag(s).replace("**", "")
        # Turkish: letters Dutch does not use; ö only in Dutch as "oö" (coördinator), ü as "uü" hardly ever
        if TURKISH & set(s) or "___" in s or re.search(r"(?<!o)ö|(?<!u)ü", s): continue
        for zin in re.split(r"(?<=[.!?])\s+|\n+", s.strip()):
            zin = zin.strip()
            n = len(zin.split())
            # a real sentence: capital (or quote) first, . ! ? at the end, no "=" glosses or source notes
            if (4 <= n <= 25 and re.match(r"^['\"‘“]?[A-Z]", zin) and re.search(r"[.!?]['\"’”]?$", zin)
                    and not any(c in zin for c in "=|/+") and not TR_WORDS.search(zin.lower())):
                out.append(zin)
    return out

def place(t, href, kind, obj):
    return {"t": t, "href": href, "kind": kind, "text": norm(" ".join(strings(obj))), "zinnen": sentences(obj)}

def all_places():
    P = []
    knm = load("data/knm.json")
    theme_tr = {k: v.get("tr", k) for k, v in knm["themes"].items()}
    # KNM critical words: one place per word (the word list row + its questions)
    for t, chunk in knm["vocab"].items():
        for w in chunk.get("words", []):
            P.append(place(f"KNM kelime · {w['nl']}", f"knm/?w={w['id']}", "knm-woord", w) | {"woord": w["nl"]})
    for w in load("data/woordstudie.json")["woorden"]:
        P.append(place(f"Kelime incelemesi · {w['woord']}", f"woordstudie/?w={w['id']}", "woordstudie", w) | {"woord": w["woord"]})
    for l in load("data/dersler.json")["lessen"]:
        P.append(place(f"Ders · {l['titel']}", f"dersler/?les={l['id']}", "ders", l))
    # KNM exam questions: one place per question
    for chunk in knm["qbank"].values():
        for q in chunk.get("items", []):
            if q.get("status") in ("old", "skip"):   # not shown on the KNM page: no link, and never used as a tag
                P.append(place("KNM (artık kullanılmayan soru)", "", "knm-oud", {"q": q.get("q"), "opts": q.get("opts")}))
                continue
            P.append(place(f"KNM soru · {theme_tr.get(q.get('theme'), 'KNM')}", f"knm/?q={q['id']}", "knm-soru",
                           {"q": q.get("q"), "opts": q.get("opts")}))
    for it in load("data/nieuws.json")["items"]:
        P.append(place(f"Nieuws · {it['titel']}", f"nieuws/?id={it['id']}", "nieuws", it))
    for f, lab, base in [("lezen-teksten.json", "Lezen B1", "lezen/teksten.html?t="), ("lezen-a2.json", "Lezen A2", "lezen/teksten.html?set=a2&t=")]:
        for t in load(f"data/{f}")["teksten"]:
            P.append(place(f"{lab} · {t['titel']}", base + t["id"], "lezen", t))
    for f, lab, base in [("luisteren-b1.json", "Luisteren B1", "luisteren/?f="), ("luisteren-a2.json", "Luisteren A2", "luisteren/?set=a2&f=")]:
        for e in load(f"data/{f}")["examens"]:
            for fr in e["fragmenten"]:
                P.append(place(f"{lab} · {fr.get('intro', '').rstrip('.')}", base + fr["id"], "luisteren", fr))
    # Spreken B1: one place per question (spreken/?v=<id> opens it); the hint box alternatives belong to their question
    hulp = load("data/spreken-hulp.json").get("alt", {})
    for v in load("data/spreken.json")["vragen"]:
        extra = hulp.get(str(v["id"])) if isinstance(hulp, dict) else None
        title = str(v.get("title", v["id"])).split("|")[0].strip()
        P.append(place(f"Spreken B1 · {title}", f"spreken/?v={v['id']}", "spreken", [v, extra]))
    # Pages without a link to one item: one place per task, opening the section
    for f, lab, href in [("schrijven-b1.json", "Schrijven B1", "schrijven/"), ("schrijven-a2.json", "Schrijven A2", "schrijven-a2/"),
                         ("spreken-a2.json", "Spreken A2", "spreken-a2/")]:
        d = load(f"data/{f}")
        listed = [k for k in ("taken", "examens", "types") if isinstance(d.get(k), list)]
        for x in (x for k in listed for x in d[k] if isinstance(x, dict)):
            P.append(place(f"{lab} · {x.get('titel') or x.get('title') or x.get('naam') or ''}".rstrip(" ·"), href, "schrijven", x))
        P.append(place(lab, href, "schrijven", {k: v for k, v in d.items() if k not in listed}))   # rules, letter parts, patterns
    P.append(place("Lezen woordenlijst", "lezen/", "lezen", load("data/lezen-bank.json")))
    return P

_TR = None
def zin_tr(z):
    """Turkish translation of a Dutch sentence of the site, or "".
    Why: a translation written once (zinnen_tr.json, or a {nl, tr} pair in a lesson, word study ...) must be
    used everywhere the sentence appears, so no word page or game tag shows the sentence without Turkish."""
    global _TR
    if _TR is None:
        _TR = {}
        def walk(x):   # every dict with a Dutch sentence and its Turkish, in any data file
            if isinstance(x, dict):
                if isinstance(x.get("nl"), str) and isinstance(x.get("tr"), str) and x["tr"]:
                    _TR.setdefault(x["nl"].strip(), x["tr"])
                for y in x.values(): walk(y)
            elif isinstance(x, list):
                for y in x: walk(y)
        for f in ("dersler.json", "woordstudie.json"):
            walk(load(f"data/{f}"))
        # hand-made translations win over pairs found in the data
        _TR.update(json.loads((ROOT / "scripts/content/zinnen_tr.json").read_text(encoding="utf-8")))
    return _TR.get(z.strip(), "")

def match_in(p, rx):
    """The first sentence of place p that matches regex rx (None if the word only occurs outside sentences)."""
    return next((z for z in p["zinnen"] if rx.search(z)), None)
