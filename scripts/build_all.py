"""Rebuild every generated file of NL Oefenbank, in the right order, with one command.

Why: the generated JSON files (data/*.json, oyunlar/woordinfo.json ...) depend on each other. When only one
builder was run after a change, the others went stale (word pages missed new lesson sentences, a corrected
meaning was lost on the next build). Running all of them in a fixed order keeps everything linked and current,
including the counters of the waiting list (docs/bekleme_listesi.md).

Run from the repo root:   python3 scripts/build_all.py
The GitHub Action .github/workflows/build.yml runs the same command on every push to main.
Stops at the first builder that fails, so a broken source never reaches the site.
"""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Order matters: texts first, then everything that reads them (word pool, games, word pages), the counters last
STEPS = [
    "scripts/content/lezen/build_teksten.py",        # Lezen B1 texts      -> data/lezen-teksten.json
    "scripts/content/lezen_a2/build_a2.py",          # Lezen A2 texts      -> data/lezen-a2.json
    "scripts/content/build_nieuws.py",               # news + word pool    -> data/nieuws.json, data/woorden.json
    "scripts/content/build_officieel.py",            # official exam guide -> data/officieel.json
    "scripts/content/build_tekst_woorden.py",        # words per Lezen text-> data/tekst-woorden.json
    "scripts/content/build_woordenboek.py",          # NL-NL dictionary   -> data/woordenboek.json
    "scripts/content/build_voorzetsels.py",          # preposition games   -> oyunlar/voorzetsels.json
    "scripts/content/build_woordinfo.py",            # word pages          -> oyunlar/woordinfo.json
    "scripts/content/bekleme_say.py",                # waiting list counts -> docs/bekleme_listesi.md
    "scripts/content/check_baglantilar.py",          # every id and link resolves (stops the build if not)
]

def main():
    for step in STEPS:
        print(f"== {step}", flush=True)
        r = subprocess.run([sys.executable, step], cwd=ROOT)
        if r.returncode != 0:
            sys.exit(f"build stopped: {step} failed")
    print("all generated files are up to date")

if __name__ == "__main__":
    main()
