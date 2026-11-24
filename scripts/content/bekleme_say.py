"""Fill the 'Kaç yerde' and 'Nerede' columns of docs/bekleme_listesi.md.

Why: Zana brings words, idioms and rules heard during the day. They wait in that list and are placed on the site
bit by bit. Seeing how often (and where) an item already occurs shows where it still needs to be used, so it is
met in different places (word study, news, lezen, spreken, crossword ...) and learned better.

Run from the repo root:  python3 scripts/content/bekleme_say.py
Only the two count columns are rewritten; everything else in the file stays as written by hand.
"""
import re, json
from pathlib import Path
from site_places import all_places, ROOT, norm

LIST = ROOT / "docs" / "bekleme_listesi.md"
SITE = "https://zokcuoglu.github.io/nl-oefenbank/"
MAX_LINKS = 6   # keep the table readable: the first 6 places, then "+N"

def extra_places():
    """Places site_places does not cover: the crossword clues and sentences (one place for the whole game)."""
    p = ROOT / "oyunlar" / "kruiswoord-nt2.json"
    if not p.exists():
        return []
    return [{"t": "Bulmaca (NT2)", "href": "", "kind": "oyun", "text": norm(p.read_text(encoding="utf-8"))}]

def cells(line):
    # "| a | b |" -> ["a", "b"]; a "\|" inside a cell (used in the regex column) is kept as "|"
    parts = re.split(r"(?<!\\)\|", line.strip())[1:-1]
    return [c.strip().replace("\\|", "|") for c in parts]

def row(cs):
    return "| " + " | ".join(c.replace("|", "\\|") for c in cs) + " |"

def main():
    places = all_places() + extra_places()
    lines = LIST.read_text(encoding="utf-8").split("\n")
    head = None
    for i, line in enumerate(lines):
        if not line.startswith("|"):
            head = None                      # a new table starts after any non-table line
            continue
        cs = cells(line)
        if head is None:
            head = cs                        # first row of a table = column names
            continue
        if set(line) <= set("|-: "):         # the |---| separator row
            continue
        c = dict(zip(head, cs))
        if "Aranan" not in c:
            continue
        rx = re.compile(c["Aranan"], re.I)
        hits = [p for p in places if rx.search(p["text"])]
        links = [f"[{p['t']}]({SITE}{p['href']})" if p["href"] else p["t"] for p in hits[:MAX_LINKS]]
        if len(hits) > MAX_LINKS:
            links.append(f"+{len(hits) - MAX_LINKS}")
        c["Kaç yerde"] = str(len(hits))
        c["Nerede"] = ", ".join(links) or "—"
        lines[i] = row([c.get(h, "") for h in head])
    LIST.write_text("\n".join(lines), encoding="utf-8")
    print("updated", LIST.relative_to(ROOT))

if __name__ == "__main__":
    main()
