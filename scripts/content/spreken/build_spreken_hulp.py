"""Build data/spreken-hulp.json: extra help for every Spreken I task.

Why a separate file: data/spreken.json is generated from an older repo (build_spreken.py
needs that repo), so the new hint content lives next to it and is merged in the page.

Output:
  handelingen: {handeling: {wat, kaliplar, tip, valkuil}}   (see handelingen.py)
  alt: {id: [answer, answer, ...]}   extra model answers per task (besides 'voorbeeld')
Every task must end up with at least 3 answers (voorbeeld + 2 alternatives).
Run from the repo root: python3 scripts/content/spreken/build_spreken_hulp.py
"""
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parents[2]


def load(name):
    # import a module file from this folder without making it a package
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ALT = {}
for n in range(1, 7):
    part = load(f"alt_{n}").ALT
    dup = set(ALT) & set(part)
    assert not dup, f"duplicate ids in alt_{n}: {sorted(dup)}"
    ALT.update(part)
HANDELINGEN = load("handelingen").HANDELINGEN
FIX = load("alt_fix").FIX   # reviewed alternatives (different ideas per answer) replace the earlier ones

vragen = json.loads((ROOT / "data/spreken.json").read_text())["vragen"]
alt, missing = {}, []
for q in vragen:
    answers = []
    hulp = q.get("hulp") or {}
    if q["id"] in FIX:
        alt[str(q["id"])] = list(FIX[q["id"]])
        assert not q["image"], f"FIX is only for tasks without a picture: {q['id']}"
        continue
    # the 19 tasks with old 'hulp' already have two extra models
    for k in ("model_2", "model_3"):
        if hulp.get(k):
            answers.append(hulp[k])
    answers += list(ALT.get(q["id"], ()))
    if len(answers) < 2:
        missing.append(q["id"])
    alt[str(q["id"])] = answers
    assert q["handeling"] in HANDELINGEN, f"no help for handeling {q['handeling']}"

assert not missing, f"tasks with fewer than 3 answers: {missing}"
unknown = set(ALT) - {q["id"] for q in vragen}
assert not unknown, f"ALT ids that are not tasks: {sorted(unknown)}"

out = {"_about": "Hint box content for spreken/: speech-act help + extra model answers. Built by scripts/content/spreken/build_spreken_hulp.py",
       "handelingen": HANDELINGEN, "alt": alt}
(ROOT / "data/spreken-hulp.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(f"{len(alt)} tasks, {sum(len(v) for v in alt.values())} alternative answers")
