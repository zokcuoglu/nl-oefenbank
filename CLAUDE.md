# Rules for working in this repo

## Sitede yeni (`data/weekbrief.json` → `nieuw`)

`nieuw` is the site's change log for users. The Thursday mail ("Haftanın Hollandacası") shows the
lines added since the previous mail under "Sitede yeni", and Zana uses the list as the reference for
what changed each week.

**When:** every change that a user can see or use adds one line, in the same commit / PR as the change.
Before finishing a session, compare `git log` since the newest `datum` with the list and add what is missing.

**Add a line for:** a new section, page, lesson, text, game or mail; a new feature in an existing page;
a clearly noticeable improvement (e.g. the crossword on phones).

**No line for:** build scripts, refactors, data checks, waiting-list counters, admin-only screens,
small fixes nobody notices, and single news items / word study words (those have their own mails).

**Format:** `{ "datum": "YYYY-MM-DD", "tekst": "...", "href": "..." }`, one entry per line, sorted by date.
- `datum`: the day users can see it (Amsterdam time). Content released later (word study, idioms with a
  future date) gets its line on its release date, not earlier.
- `tekst`: Turkish, one or two short sentences: what is new and what you can do with it.
- `href`: relative link to the exact page (empty only if there is no page).
- Several commits about one feature → one line. Do not change lines of weeks that were already mailed,
  except typos.
