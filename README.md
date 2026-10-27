# NL Oefenbank

Dutch practice site for the family and friends: NT2 exam practice for adults, school exercises for children.

- **Login:** Google sign-in (Firebase Authentication).
- **Storage:** Firestore. Each person's profile and results live under `users/{uid}`; see `firestore.rules`.
- **Hosting:** GitHub Pages, no build step. Firebase is loaded from Google's CDN.

## Accounts

| Field | Values | Who sets it |
|---|---|---|
| `type` | `adult`, `child` | The person, once at first login. After that only an admin. |
| `role` | `member`, `teacher`, `admin` | Only an admin (admin screen). |

Children only see the kids area; NT2 pages send them back to the home page.
The page files are public (public repo), so this is a menu rule, not secrecy.

**First admin:** sign in once, then in Firebase Console > Firestore > `users` > your document, add the field `role` = `admin`.

## Files

| Path | What it is |
|---|---|
| `index.html` | Home: exercise cards, filtered by account type |
| `profile.html` | Own name, groep, exam dates, progress |
| `admin.html` | Admin only: change type and role of every account |
| `js/core.js` | Shared: Firebase config, login gate, profile and attempt helpers |
| `css/site.css` | Shared design for home, profile and admin |
| `data/catalog.json` | List of exercises shown on the home page (add new ones here) |
| `lezen/` + `data/lezen-bank.json` | NT2 Lezen I (B1) word practice |
| `lezen/teksten.html` + `data/lezen-teksten.json` | Exam-style reading texts with questions and a 110-minute practice exam; source in `scripts/content/lezen/` (`build_teksten.py`) |
| `kids/g5/eer-oor-eur.html` | Groep 5 spelling test |
| Slimspel (`../slimspel/`) | Separate repo [slimspel](https://github.com/zokcuoglu/slimspel), same accounts; its modules (`slimspel-*`) are listed in `data/catalog.json` and appear in the statistics and the weekly mail (tafels: most-missed sums) |
| `knm/` + `data/knm.json` | KNM question bank (moved from the KNM artifact) |
| `nieuws/` + `data/nieuws.json` | Nieuws in niveaus (v1): numbered video items, text at A1-C1, idioms, words, quiz; a mixed test after every 3 items |
| `scripts/content/` | Source of the news items (`nNN_*.py`) and mixed tests (`toetsen.py`); `build_nieuws.py` checks them and writes `data/nieuws.json` |
| `woorden/` + `data/woorden.json` | Word test: one pool of work-note words (`scripts/content/werk_woorden.csv`) and news words/idioms; filters for source, level (A1–C2), type and count; learning or exam mode, hints, full review at the end |
| `lezen/teksten.html?set=a2` + `data/lezen-a2.json` | Lezen A2 (inburgeringsexamen): 16 short everyday texts, 2 practice exams of 8 texts / 25 questions / 65 minutes; source in `scripts/content/lezen_a2/` (`build_a2.py`) |
| `schrijven-a2/` + `data/schrijven-a2.json` | Schrijven A2: 16 tasks (form, e-mail, note, message), 4 practice exams of 4 tasks / 40 minutes, model answer, self-check list, AI scoring prompt; source `scripts/content/schrijven_a2/build_schrijven_a2.py` |
| `luisteren/?set=a2` / `?set=b1` + `data/luisteren-a2.json`, `data/luisteren-b1.json` | Listening, one page for both levels. A2: 40 short fragments (1 question), 2 exams of 20 / 45 min, 2 plays. B1: 20 longer texts (4 questions), 2 exams of 40 questions / 90 min, 25 s reading time per question, text plays once. Read aloud by the browser's Dutch voice(s); a text with `video_url` (+ `video_start`/`video_end`) plays as a YouTube video instead. Sources `scripts/content/luisteren_a2/`, `scripts/content/luisteren_b1/`. `luisteren-a2/` only redirects |
| `spreken-a2/` + `data/spreken-a2.json` | Spreken A2: 32 tasks in 4 types (question about yourself, 1/2/3 pictures described in words), 2 practice exams (16 tasks, 35 min), typed or dictated answers, model answers, AI scoring prompt; source `scripts/content/spreken_a2/build_spreken_a2.py` |
| `js/stats.js` | Statistics helpers for the profile and admin pages |
| `manifest.json`, `icons/` | "Add to home screen" on phones |
| `firestore.rules` | Security rules, paste into Firebase Console > Firestore > Rules (also covers the Slimspel daily ranking: `leaderboard/{day}/entries`) |

## E-mail

`scripts/mailer.py` runs every hour in GitHub Actions (`.github/workflows/mailer.yml`). Each run sends
"account approved" mails and queued announcements (admin screen, audience all/adult/child), and, when the
schedule on the admin screen says so (Firestore `settings/mail`, default Monday 08:00 and Sunday 18:00, Amsterdam time):
- the next news item to subscribers (profile setting `email_news`; logged in `nieuws_sent/{date}`)
- weekly summaries (children: also to the linked parent; logged in `mail_log/weekly-{date}`)

Secrets: `FIREBASE_SERVICE_ACCOUNT`, `GMAIL_USER`, `GMAIL_APP_PASSWORD`. If one is missing the run stops with a warning instead of failing.
Manual run (Actions > Mailer > Run workflow): `test` sends preview mails to one address only (default the sending Gmail) and writes nothing; `hourly`, or `news` / `weekly` to send to everyone now regardless of the schedule (dry run by default).

### News items
Edit `scripts/content/nNN_*.py`, then run `python3 scripts/content/build_nieuws.py`. Each item: `id`, `nr`, `titel`, `bron`,
`video_url`, `afbeelding_url`, `niveau_video` + `niveau_uitleg`, `a0`…`c1` (`<strong>` allowed) + `gloss_{level}` (the words the text uses, in dictionary form; the page also shows these words at a lower level),
`uitdrukkingen` `{nl, niveau, tr, uitleg, voorbeeld, voorbeeld_tr}`, `woordenschat` (lines `woord | soort | betekenis | voorbeeld | turks | niveau | groep`),
`grammatica`, `toets` (questions `{id, type mc|tf|gap, niveau, cat, vraag, opties, juist, uitleg}`; the page shuffles the options).
Items are mailed in `nr` order. The old items are kept in `data/nieuws-v1.json` and are not used.
Item quizzes always have 18 questions (5 begrip, 4 woorden, 5 uitdrukkingen, 4 grammatica); the builder checks this.
Mixed tests (`toetsen.py`) always have 20 questions (6/5/5/4): Test 1 covers news 1–3 (all from those items),
then one test per new item covering 1–4, 1–5, 1–6 …: 12 from the newest item and 8 review questions from all earlier
items, where the page picks questions the user answered wrong last time first. A test opens with its newest item.
Optional `video_start`/`video_end`
(seconds) show only part of a video.

## Adding a kids exercise

1. Put the page under `kids/<groep>/`.
2. In its module script: `const { user } = await gate({ area: "kids" })` and save rounds with `saveAttempt(user.uid, "<module-id>", attempt)`.
3. Add an entry to `data/catalog.json` with `area: "kids"` and the right `group`.

## Word pool (woorden)

Three sources: `scripts/content/basis_woorden.csv` (basic everyday words, A0–A1), `scripts/content/werk_woorden.csv` (work notes) and the news items.
Every entry has a CEFR level (`niveau`, A0–C2, for adults) and a school year (`groep`: `1-2`, `3` … `8`, or `vo` = after primary school).
Child accounts choose groep instead of level and never see `vo` words; the home page has a word-test card per groep (`woorden/?groep=5`).
News words carry the groep as 7th column of `woordenschat` and as `groep` in each idiom; the builders stop when a word has no groep.

`scripts/content/werk_woorden.csv` holds the words and phrases from the work notes (one row each: `nl, soort, tr, niveau A0–C2, groep, thema, voorbeeld, voorbeeld_tr, uitleg, voorbeeld_door`).
`python3 scripts/content/build_nieuws.py` rebuilds `data/nieuws.json` and then `data/woorden.json` (work words + every news item's words and idioms).
New work words: add rows to the CSV with the next free id (`w416`, ...), then run the builder.

Work words in news: a news item may list `werk_woorden: ["w012", ...]`; the builder checks that each word occurs in the item's texts
and the news page shows them under "İş notlarından kelimeler". `python3 scripts/content/build_woorden.py --kandidaat B1` lists work
words at a level that no news text uses yet. News items may also have an optional `c2` text (+ `gloss_c2`).

## Exam level (B1 / A2)

Adults choose their exam level on the profile (`examen_niveau`: `B1` = Staatsexamen NT2 I, `A2` = inburgeringsexamen, `beide`).
NT2 modules in `data/catalog.json` may have `niveau` (`B1` or `A2`); the home page shows only the matching ones. No `niveau` = both (KNM).
A2 facts used (DUO / inburgeren.nl via practice sites): Lezen 65 min on the computer, Schrijven 40 min on paper with 4 tasks,
Luisteren 45 min, Spreken 35 min with 16 tasks, KNM 45 min. DUO publishes no fixed number of questions or pass mark for A2 Lezen;
the pages show "about 18 of 25" only as a rough guideline. The writing criteria follow the CEFR A2 description, not DUO's own model.
