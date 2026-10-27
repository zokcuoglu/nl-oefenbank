"""
Build data/spreken.json from the old nt2-spreken repo.

Why: the old site kept questions in JS files (spreken_data.js, spreken_extra.js).
The new site reads plain JSON like the Lezen section does, so we convert once here.

Usage:
    python3 scripts/content/spreken/build_spreken.py <path-to-old-nt2-spreken-repo>

What it does:
  1. Reads all 368 questions, the kort/middel type map and the 23 mock exams.
  2. Adds two new fields per question, guessed from the instruction lines:
       - handeling: which speech act the task asks for (advice, preference, ...)
       - eis: what exactly is required (number of reasons / pictures / things)
     These are guesses; we review them by hand afterwards.
  3. Adds the official 2025 points -> score (500 scale) table.
  4. Copies the question images into spreken/img/.
"""
import json
import re
import shutil
import sys
from pathlib import Path

OLD = Path(sys.argv[1])
SITE = Path(__file__).resolve().parents[3]          # repo root of nl-oefenbank
OUT_JSON = SITE / "data" / "spreken.json"
OUT_IMG = SITE / "spreken" / "img"


def js_const(src: str, name: str):
    """Read a `const NAME = <json>` value out of a JS file without running JS."""
    m = re.search(r"const " + name + r"\s*=\s*", src)
    value, _ = json.JSONDecoder().raw_decode(src[m.end():])
    return value


# ---------- 1. load old data ----------
data_js = (OLD / "spreken_data.js").read_text(encoding="utf-8")
extra_js = (OLD / "spreken_extra.js").read_text(encoding="utf-8")
items = js_const(data_js, "DATA") + js_const(extra_js, "EXTRA_DATA")
type_map = js_const(extra_js, "TYPE_MAP")          # id -> "kort" | "middel"
exams = js_const(extra_js, "EXAMS")                # 23 lists of 16 ids
official = js_const(extra_js, "OFFICIAL_TAGS")     # pool ids that match a real exam task
hulp = json.loads((OLD / "spreken.json").read_text(encoding="utf-8"))["verrijking"]

# ---------- 2. guess the speech act (handeling) ----------
# Order matters: the first matching rule wins. Each rule looks at the
# instruction text (situatie), lower-cased.
HANDELING_RULES = [
    ("overtuigen",  r"\bovertuig"),
    ("advies",      r"\badvi(es|ezen|seer)|\braad\b|volgens u .*(moet|kan|best)|het best(e)? kan|wat (hij|zij|ze) kan doen"),
    ("voorstel",    r"\bvoorstel|\bstel (iets|een \w+) voor\b"),
    ("troosten",    r"\btroost"),
    ("voorkeur",    r"\bliefst\b|\bliever\b|\bfijner\b|\bleukst|beste idee|\bkiest\b|\bkiezen\b|\bkeuze\b|\bvoorkeur\b|welke? .* (u|je) (wilt|kiest)"),
    ("mening",      r"\bmening\b|wat u (er|daar|hier)?van .*vindt|wat vindt u|waarom u vindt|geen goed idee vindt|belangrijk vindt|het (wel|niet) eens|geschikt is|bij u past"),
    ("instructie",  r"\bleg .*uit\b|\buitleg\b|wat (hij|zij|ze|hem|haar|de \w+) moet doen|hoe (hij|zij|ze|de \w+) .* moet|\binstructie|mee moet|op moet letten"),
    ("beschrijving", r"\bbeschrijf|wat u .* (gedaan|gezien|meegemaakt)|wat er (is )?gebeurd|hoe .* eruitzi|hoe een dag|er gebeurt iets"),
    # imperative "Vraag uw collega ..." (lines are joined, so it can be anywhere, not only at ^)
    ("vraag",       r"(^|\s)vraag (uw|hem|haar|om|of|een)\b|stel .*vra(ag|gen)|wat vraagt u|\bverzoek"),
    ("reageren",    r"wat zegt u|\bsorry\b|bedank|feliciteer|excuses|niet mee eens"),
]


def guess_handeling(text: str) -> str:
    # Only look at instruction lines; skip the generic "Vertel ook waarom (u dat vindt)"
    # line, because it appears in many task types and would trigger 'mening' wrongly.
    lines = [ln for ln in text.lower().split("\n") if not ln.strip().startswith("vertel ook waarom")]
    t = " ".join(ln.strip() for ln in lines)   # join wrapped lines so phrases split over 2 lines still match
    for name, pattern in HANDELING_RULES:
        if re.search(pattern, t, flags=re.M):
            return name
    return "informeren"            # fallback: just give information


# Hand-checked tags for questions the rules above could not place (they fell to 'informeren').
# 'uitleg' = explain a reason or what something means ("Waarom ...?", "Wat betekent dit bord?").
HANDELING_OVERRIDE = {
    "beschrijving": [27, 35, 40, 52, 86, 87, 108, 115, 136, 211, 214, 248, 259, 274, 307, 312, 314, 317, 336, 339],
    "instructie":   [25, 67, 69, 106, 186, 201, 234, 272, 281, 297, 308, 323, 342, 343, 348, 349],
    "uitleg":       [16, 77, 94, 114, 155, 176, 180, 220, 225, 228, 293, 298, 311],
    "voorkeur":     [46, 51, 53, 95, 98, 142, 151, 157, 304, 333, 340, 1004],
    "mening":       [61, 88, 144, 160, 169, 172, 250, 251, 338],
    "advies":       [141, 148, 159, 204, 209, 236, 273],
    "vraag":        [32, 85, 200, 207, 208, 210, 217, 240, 268, 287, 347],
    "overtuigen":   [171, 326, 332],
    "voorstel":     [99, 133],
    "reageren":     [38, 195],
    # left as real 'informeren' on purpose: 19, 66, 73, 104, 109, 116, 130, 135, 153, 219, 222,
    # 230, 247, 252, 253, 291, 319, 321, 337, 1016
}
OVERRIDE = {qid: tag for tag, ids in HANDELING_OVERRIDE.items() for qid in ids}


# ---------- 3. guess the requirement (eis) ----------
NUM = {"één": 1, "een": 1, "twee": 2, "drie": 3}


def guess_eis(text: str) -> dict:
    t = text.lower()
    eis = {}
    m = re.search(r"(ten ?minste )?(één|een|twee|drie) (redenen|reden|argumenten|argument|adviezen|advies|dingen|oplossingen)", t)
    if m:
        eis["aantal"] = NUM[m.group(2)]
        eis["wat"] = m.group(3)
    elif "vertel ook waarom" in t or "leg ook uit waarom" in t:
        eis["aantal"] = 1
        eis["wat"] = "reden"
    if re.search(r"alle plaatjes|de drie plaatjes", t):
        eis["plaatjes"] = 3
    elif re.search(r"beide plaatjes|de twee plaatjes", t):
        eis["plaatjes"] = 2
    elif re.search(r"het plaatje|de plaatjes", t):
        eis["plaatjes"] = "ja"
    return eis


# ---------- 4. build the question list ----------
vragen = []
for it in items:
    qid = str(it["id"])
    if it.get("tag"):                     # extra items carry their own source note
        bron = "officieel-reconstructie" if "ECHT" in it["tag"] else "nieuw"
    elif qid in official:
        bron = "ad-appel (=officieel " + official[qid].replace("ECHT EXAMEN ", "") + ")"
    else:
        bron = "ad-appel"
    q = {
        "id": it["id"],
        "title": it["title"],
        "type": type_map[qid],
        "handeling": OVERRIDE.get(it["id"]) or guess_handeling(it["situatie"]),   # hand-check wins
        "eis": guess_eis(it["situatie"]),
        "situatie": it["situatie"],
        "vraag": it["vraag"],
        "image": ("img/" + Path(it["image"]).name) if it["image"] else None,
        "voorbeeld": it["antwoord"],
        "bron": bron,
    }
    if qid in hulp:                       # optional study help written earlier for 19 items
        q["hulp"] = hulp[qid]
    vragen.append(q)

# ---------- 5. official 2025 conversion table (beoordelingsmodel Spreken I 2025) ----------
SCORE_2025 = [213, 253, 279, 295, 307, 317, 324, 331, 338, 343, 348, 353, 357, 362, 366, 369,
              373, 376, 379, 383, 386, 389, 392, 394, 397, 400, 402, 405, 408, 410, 413, 415,
              418, 420, 422, 424, 427, 429, 431, 433, 436, 438, 440, 442, 444, 446, 448, 450,
              452, 454, 456, 458, 460, 462, 463, 465, 467, 469, 471, 473, 475, 476, 478, 480,
              482, 483, 485, 487, 489, 490, 492, 494, 495, 497, 499, 500, 502, 504, 505, 507,
              509, 510, 512, 514, 515, 517, 519, 520, 522, 524, 525, 527, 529, 531, 532, 534,
              536, 538, 540, 542, 544, 546, 548, 550, 552, 554, 556, 559, 561, 564, 566, 569,
              572, 576, 579, 583, 587, 591, 595, 600, 605, 611, 618, 626, 635, 647, 663, 687, 727]
assert len(SCORE_2025) == 129          # 0..128 points

out = {
    "_about": "Spreken I (B1) question bank. Built by scripts/content/spreken/build_spreken.py "
              "from the old nt2-spreken repo. handeling/eis are rule-based guesses, reviewed by hand.",
    "vragen": vragen,
    "examens": exams,
    "score": {"bron": "Beoordelingsmodel Spreken I 2025", "max": 128, "cesuur": 75, "tabel": SCORE_2025},
}
OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------- 6. copy images ----------
OUT_IMG.mkdir(parents=True, exist_ok=True)
for q in vragen:
    if q["image"]:
        shutil.copy2(OLD / "images" / Path(q["image"]).name, OUT_IMG / Path(q["image"]).name)

print(f"{len(vragen)} vragen, {len(exams)} examens -> {OUT_JSON}")
