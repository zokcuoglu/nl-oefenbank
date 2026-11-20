"""Which Dutch sentences on the word pages still have no Turkish translation?

    python3 scripts/content/check_vertaling.py 002        words of scripts/content/anlamlar/002.json
    python3 scripts/content/check_vertaling.py --all      every reviewed word
    python3 scripts/content/check_vertaling.py --combis   the preposition combinations

Run build_woordinfo.py (or build_voorzetsels.py) first. Prints one sentence per line, so the list can be
translated into scripts/content/zinnen_tr.json.
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
zt = json.loads((HERE / "zinnen_tr.json").read_text(encoding="utf-8"))

if "--combis" in sys.argv:
    info = json.loads((ROOT / "oyunlar/voorzetsels.json").read_text(encoding="utf-8"))["info"]
    words = list(info)
else:
    info = json.loads((ROOT / "oyunlar/woordinfo.json").read_text(encoding="utf-8"))["woorden"]
    files = sorted((HERE / "anlamlar").glob("*.json")) if "--all" in sys.argv else [HERE / "anlamlar" / f"{sys.argv[1]}.json"]
    words = [k for f in files for k in json.loads(f.read_text(encoding="utf-8"))]

missing = []
for k in words:
    i = info.get(k, {})
    for z in [t.get("z") for t in i.get("tags", [])] + [e["nl"] for e in i.get("voorbeelden", []) if not e.get("tr")]:
        if z and z not in zt and z not in missing:
            missing.append(z)
print(f"{len(missing)} sentences without Turkish", file=sys.stderr)
print("\n".join(missing))
