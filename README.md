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
| `index.html` | Home with three tabs: *Hollandaca* (general Dutch: news, words, kids area, Slimspel links, in foldable sections), *NT2 sınavı* (`#nt2`: exam cards for the level on the profile) and *Uitdaging van de dag* (`#oyunlar`: the daily challenges, introduced from `data/oyunlar.json`; Woordle uses `slimspel/woordle/game.js`). A "Devam et" row shows the three exercises used last. Child accounts see no tabs, only the kids area and Slimspel |
| `profile.html` | Own name, groep, exam dates, progress. Parents see their linked children ("Çocuklarım"): groep, weekly summary, today's play time and a button for 10 extra minutes today |
| `admin.html` | Admin only: change type and role of every account, statistics, mail, extra play time for children, and (tab *İçerik*) which Rekenen topics students see |
| `js/core.js` | Shared: Firebase config, login gate, profile and attempt helpers |
| `css/site.css` | Shared design for home, profile and admin |
| `data/catalog.json` | List of exercises shown on the home page (add new ones here) |
| `lezen/` + `data/lezen-bank.json` | NT2 Lezen I (B1) word practice |
| `lezen/teksten.html` + `data/lezen-teksten.json` | Exam-style reading texts with questions and a 110-minute practice exam; source in `scripts/content/lezen/` (`build_teksten.py`) |
| `kids/g5/eer-oor-eur.html` | Groep 5 spelling test |
| `kids/rekenen.html` + `kids/rekenen-vragen.js`, `kids/rekenen-school.js`, `kids/vragen-basis.js` | Rekenen & meetkunde (card in Groep 5-8, module `g5-rekenen`). Topics have a `band` ("5-6" or "7-8") and `school` (true = ordinary school material, chosen from the SLO tussendoelen and the domains of the doorstroomtoets; false = enrichment); the menu is grouped by these, the student's own years first. School topics groep 5-6 (open): handig rekenen, delen, klok en tijd, geld, meten, breuken, afronden, grote getallen. School topics groep 7-8 (hidden): breuken-kommagetallen-procenten, procenten, kommagetallen, verhoudingen, gemiddelde, snelheid, rekenen met letters, plus inhoud, priem, schaal, negatief. **Herhalen**: kinds of question answered wrong come back the next day and then after 2, 5 and 12 days (worked out from the saved rounds, same rule as `js/tekrar.js`); saved as `test` = `herhaal`. Shared helpers live in `vragen-basis.js`; new generators must be added at the END of a level's list, because the position is part of the saved question id. After adding or renaming a topic run `node scripts/build_konular.mjs` (writes `data/rekenen-konular.json` for the weekly mail). Per topic: per topic a short explanation in Dutch and Turkish with figures and a word list, practice rounds of 5 at one level (1 straight sum, 2 the other way round, 3 word problem) and a test of 5 or 10 questions that starts easy, goes one level up after two right answers in a row and one down after a wrong one; the next test starts one level below where the last ended. Also a mixed test over all open topics. Every topic ends its explanation with one or two everyday examples (`eg: true` blocks: football field, iron ship, Madurodam ...). In practice a wrong typed answer gets one second try with the cheat sheet opened (the first try decides the score); the result page can repeat the kinds of question that went wrong with new numbers; the Dutch question can be read aloud. The card is shown in Groep 5 and Groep 6 (`group` may be a list in the catalog). Questions are made by generators with random numbers (pi = 3, so answers are whole numbers); `?konu=<id>` opens one topic. Area is first explained as counting 1 × 1 squares (grid figure, also in the easy area questions). Four topics are open by default (omtrek en oppervlakte, optellen van 1 tot n, machten en wortels, de rij van Fibonacci), nine more are hidden; the admin page tab *İçerik* switches topics on and off (Firestore `settings/rekenen`), admins see hidden topics on the page marked "gizli". Rounds are saved with `test` = topic id (or `gemengd`), `kind` = `toets` / `oefen` and `qid` = `topic:level:kind` |
| `kids/rekenen.html?vak=natuur` + `kids/natuur-vragen.js`, `kids/natuur-78.js` | Natuur & techniek (module `g5-natuur`), the same page with another question file: licht, massa-gewicht-dichtheid, drijven en zinken, atomen en moleculen (groep 5-6, enrichment) and elektriciteit, magnetisme, krachten en hefbomen, geluid, vast-vloeibaar-gas, zonnestelsel (groep 7-8). Mostly hand-written multiple-choice questions (understanding), with random numbers only where there is a calculation. All four topics start hidden; the catalog card has `open_any` and appears on a student's home page once the admin opens at least one topic (tab *İçerik*) |
| `kids/woordkaarten.html?lijst=weer` | School word lists (rows with bron "school" in `scripts/content/woorden.csv`): flashcards, matching game and a link to the word test (`woorden/?lijst=weer`). Back side: Dutch definition or Turkish. One catalog card per list (id `school-<thema>`) |
| Slimspel (`slimspel/`) | Kids' games and puzzles, see `slimspel/README.md`. Was the separate repo [slimspel](https://github.com/zokcuoglu/slimspel) until Nov 2026 (that repo now only redirects to here); same accounts; its modules (`slimspel-*`) are listed in `data/catalog.json` and appear in the statistics and the weekly mail (tafels: most-missed sums) |
| `knm/` + `data/knm.json` | KNM question bank (moved from the KNM artifact) |
| `nieuws/` + `data/nieuws.json` | Nieuws in niveaus (v1): numbered video items, text at A1-C1, idioms, words, quiz; a mixed test after every 3 items |
| `scripts/content/` | Source of the news items (`nNN_*.py`) and mixed tests (`toetsen.py`); `build_nieuws.py` checks them and writes `data/nieuws.json` |
| `woorden/` + `data/woorden.json` | Word practice: one pool (basis, werk, school, nieuws). Every entry has `tur` (grammatical type), `thema` (+ `subthema` inside werk) and `register`; the build stops when one is missing. Filters for topic, type, source, register, level and status; flashcards, matching game or test (learning / exam mode) |
| `js/oefen.js` | Shared by the word pages: word status from all saved answers (🆕 new, 🔴 weak, 🟡 learning, 🟢 known = 3 right in a row in a test or matching game; a flashcard "Ken ik" counts at most up to 🟡), flashcards and matching game |
| `lezen/teksten.html?set=a2` + `data/lezen-a2.json` | Lezen A2 (inburgeringsexamen): 16 short everyday texts, 2 practice exams of 8 texts / 25 questions / 65 minutes; source in `scripts/content/lezen_a2/` (`build_a2.py`) |
| `schrijven-a2/` + `data/schrijven-a2.json` | Schrijven A2: 16 tasks (form, e-mail, note, message), 4 practice exams of 4 tasks / 40 minutes, model answer, self-check list, AI scoring prompt; source `scripts/content/schrijven_a2/build_schrijven_a2.py` |
| `luisteren/?set=a2` / `?set=b1` + `data/luisteren-a2.json`, `data/luisteren-b1.json` | Listening, one page for both levels. A2: 40 short fragments (1 question), 2 exams of 20 / 45 min, 2 plays. B1: 20 longer texts (4 questions), 2 exams of 40 questions / 90 min, 25 s reading time per question, text plays once. Read aloud by the browser's Dutch voice(s); a text with `video_url` (+ `video_start`/`video_end`) plays as a YouTube video instead. Sources `scripts/content/luisteren_a2/`, `scripts/content/luisteren_b1/`. `luisteren-a2/` only redirects |
| `spreken-a2/` + `data/spreken-a2.json` | Spreken A2: 32 tasks in 4 types (question about yourself, 1/2/3 pictures described in words), 2 practice exams (16 tasks, 35 min), typed or dictated answers, model answers, AI scoring prompt; source `scripts/content/spreken_a2/build_spreken_a2.py` |
| `schrijven/` + `data/schrijven-b1.json` | Schrijven I (B1): 3 practice exams of 12 tasks like the official exam (8 sentence tasks, a form, 3 short texts; 100 min; 47 points, pass 25) plus random exams of 4/8/12 tasks, a simple tactics page (`?taktik`: 3 rules, e-mail/letter skeleton with je/u phrases, ready sentences per situation, sentence-task table; data in `kaliplar.py`) and an optional hint box per task, self-check, AI prompt with the CvTE 2025 rules and score table; source `scripts/content/schrijven_b1/` |
| `spreken/` + `data/spreken.json`, `data/spreken-hulp.json` | Spreken I (B1): 368 tasks, 23 mock exams + random exams of 4/8/12/16 tasks, AI scoring prompt; optional hint box per task with speech-act patterns and 3+ model answers (`scripts/content/spreken/build_spreken_hulp.py` merges `alt_1..6.py` and `handelingen.py`) |
| `dersler/` + `data/dersler.json` | Lessons of three kinds (`soort`): `video` (below), `gramer` (grammar topics) and `konusma` (everyday conversation); the last two have no video and come from the owner's own notes. `?soort=gramer` lists one kind; rounds are saved as module `dersler` / `gramer` / `konusma`. Video lessons (Goed Bezig channel): YouTube video on top, a short summary in parts, then questions of three types (choose, put the words in order, type the Dutch sentence; a typed answer marked wrong can be overruled with "Cevabım da doğruydu"). `?les=<id>` opens one lesson. The Dutch in the automatic Turkish captions is garbled, so the Dutch sentences are written by hand; add a lesson by adding an object to `lessen`. Attempts are saved as module `dersler` with `test` = lesson id |
| "View as" (in `js/core.js`) | Admins get a thin bar on every page to look at the site as an adult member or as a student of one groep. The choice is stored in the browser (`localStorage` key `nloefenbank:view`), the account does not change. `gate()` then returns a changed copy of the profile (`_view: true`) and nothing is written: `saveAttempt` and `updateProfile` do nothing, the daily games and Woordle skip their result, and the play-time clock does not start. It does not reach the separate Slimspel site |
| `woordstudie/` + `data/woordstudie.json` | Weekly word study ("Kelime incelemesi"): one word taken apart (parts, history, relatives in other languages, word family, examples, grammar note, a 'weetje') with 5 questions, saved as module `woordstudie`. A word is visible to members from its `datum` (the Tuesday it is mailed), to admins always. Mailer job `woord` (default Tuesday 19:00) sends the oldest due word not yet mailed; adults can turn it off on the profile page (`email_woord`). The same page with `?bolum=gunluk` is the daily-speech page (patterns only, all open at once, tips at the top, quiz module `gunluk`); patterns are not listed on the word study page. Entries have a `soort`: `woord` (default), `kalip` (daily-speech pattern, e.g. "het gaat om": `betekenissen`, `opsite`, `dialoog`) or `deyim` (idiom). The Tuesday mail is mostly the word, then this week's pattern, the idiom at the bottom (ids logged in `extra_ids`). Only add etymology a source confirms, and list the sources in `bronnen` |
| `js/tekrar.js` | "Bugünkü tekrarın": lesson questions answered wrong come back the next day, then after 2, 5 and 12 days; four right answers in a row and a question is learned. Nothing extra is stored: the schedule is computed from the attempts of modules `dersler`, `gramer`, `konusma` and `tekrar`. The home page shows a card when questions are due; `dersler/?tekrar=1` runs a round of at most 10 and saves it as module `tekrar` |
| `js/stats.js` | Statistics helpers for the profile and admin pages |
| `manifest.json`, `icons/` | "Add to home screen" on phones |
| `data/weekbrief.json` | Weekly Thursday mail for adults, "Haftanın Hollandacası" (mailer job `brief`, default Thursday 19:00, editable on the admin page): per week an idiom, a word, a culture note and one thing to try on the site, each with a `datum` (the Thursday it belongs to; only the current week is sent, a missed week is skipped), plus `nieuw`: lines about what changed on the site, shown in the next mail. Adults can turn it off on the profile page (`email_brief`). When the list runs out the admins get one notice |
| `firestore.rules` | Security rules, paste into Firebase Console > Firestore > Rules (also covers the Slimspel daily ranking `leaderboard/{day}/entries` and the Woordle results `woordle_plays`) |

## E-mail

`scripts/mailer.py` runs every hour in GitHub Actions (`.github/workflows/mailer.yml`). Each run sends
"account approved" mails and queued announcements (admin screen, audience all/adult/child), and, when the
schedule on the admin screen says so (Firestore `settings/mail`, default Monday 08:00 and Sunday 18:00, Amsterdam time):
- the next news item to subscribers (profile setting `email_news`; logged in `nieuws_sent/{date}`)
- weekly summaries (children: also to the linked parent; logged in `mail_log/weekly-{date}`). For Rekenen & meetkunde and Natuur & techniek the summary has one line per topic, weakest first, with the number of wrong answers per level (straight sum, the other way round, word problem)

Secrets: `FIREBASE_SERVICE_ACCOUNT`, `GMAIL_USER`, `GMAIL_APP_PASSWORD`. If one is missing the run stops with a warning instead of failing.
Manual run (Actions > Mailer > Run workflow): `test` sends preview mails to one address only (default the sending Gmail) and writes nothing; `hourly`, or `news` / `weekly` to send to everyone now regardless of the schedule (dry run by default).

### News items
Edit `scripts/content/nNN_*.py`, then run `python3 scripts/build_all.py`. Each item: `id`, `nr`, `titel`, `bron`,
`video_url`, `afbeelding_url`, `niveau_video` + `niveau_uitleg`, `a0`…`c1` (`<strong>` allowed) + `gloss_{level}` (the words the text uses, in dictionary form; the page also shows these words at a lower level),
`uitdrukkingen` and `woordenschat`: lists of word ids from the word source (see *Word pool*); an entry may be `{"id": …, "voorbeeld": …, "voorbeeld_tr": …, "definitie": …}` to give this item's own sentence or meaning note. The builder turns them back into the shapes the page reads and keeps the ids as `woord_ids` / `uitdr_ids`,
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
3. Add an entry to `data/catalog.json` with `area: "kids"` and the right `group` (one groep, or a list such as `["groep5", "groep6"]`).

## Word pool (woorden) – one source

Every Dutch word and expression has exactly ONE row, in one of two files (read and checked by `scripts/content/woordbron.py`):
- `scripts/content/woorden.csv` – single words (`tur`: zn, ww, sch_ww, bn, bw, klein, telw, tw, afk)
- `scripts/content/uitdrukkingen.csv` – expressions (`tur`: uitdr = deyim, vaste_comb, zin = hazır cümle / kalıp, structuur = yapı)

Columns: `id, nl, tur, tr, niveau (A0–C2), groep (1-2 … 8, vo), thema, subthema, register, voorbeeld, voorbeeld_tr, uitleg, meer, definitie, woordsoort, bron, lijst, voorbeeld_door, alias`.
Everything else points at a row by id and never copies its meaning: news items (`woordenschat` / `uitdrukkingen`), the Thursday mail (`data/weekbrief.json`, `woord` / `deyim` = `{"id": …}`), the word study (`data/woordstudie.json`, `woorden`: ids) and the waiting list (`Id` column).
Ids never change (word status is saved per id): new words get the next `k###`, new expressions the next `u###`. When two rows turn out to be the same word, merge them into one and put the old id in `alias` (answers saved under it still count).
`bron` = where a row came from (basis, werk, school, nieuws, mail, woordstudie, bekleme; `;` for several).
Child accounts choose groep instead of level and never see `vo` words; the home page has a word-test card per groep (`woorden/?groep=5`).
`python3 scripts/content/build_woorden.py --kandidaat B1` lists work/school words at a level that no news text uses yet.

Every pool row gets a word page (`kelime/?w=<word without de/het/een>`): meanings, examples, where it is used on the site, and the word study that explains it (from its date on). Words link to it from the news page, the word test explanations, the Thursday mail and, after "Bitir", the Lezen review (`data/tekst-woorden.json`).
Finding a word in a text uses one strict rule (`woordbron.found_in`): single words with ordinary endings, expressions with all their words in order in one sentence, entries made only of small function words never.

## Build

`python3 scripts/build_all.py` rebuilds every generated file in order and ends with `scripts/content/check_baglantilar.py`, which stops when a pool word has no word page or an id / link in the data, the mail, the word study or the waiting list points at nothing. The *Build* workflow (`.github/workflows/build.yml`) runs it on every push to main and commits the result, so counts and links stay current.

## Exam level (B1 / A2)

Adults choose their exam level on the profile (`examen_niveau`: `B1` = Staatsexamen NT2 I, `A2` = inburgeringsexamen, `beide`).
NT2 modules in `data/catalog.json` may have `niveau` (`B1` or `A2`); the home page shows only the matching ones. No `niveau` = both (KNM).
A2 facts used (DUO / inburgeren.nl via practice sites): Lezen 65 min on the computer, Schrijven 40 min on paper with 4 tasks,
Luisteren 45 min, Spreken 35 min with 16 tasks, KNM 45 min. DUO publishes no fixed number of questions or pass mark for A2 Lezen;
the pages show "about 18 of 25" only as a rough guideline. The writing criteria follow the CEFR A2 description, not DUO's own model.

## İstek kutusu (wish box)

`js/talep.js`: under the word study and daily-speech lists, approved adults ask for a word, idiom, pattern or topic (text up to 4000 characters, up to 2 screenshots shrunk in the browser to JPEG and stored in the same document). Firestore collection `talepler` (rules: own create/read, admin reads, marks `yapildi` or deletes). The admin sees them on the "Bugün" tab; mailer job `talep` (default Monday 09:00) mails the admins the open wishes that arrived since the last summary, no mail when there are none.

## Mail record

`scripts/mailer.py` wraps the sender in `LoggingSender`; at the end of every run `save_sent` writes one document per kind of mail and subject to `mail_sent` (recipients with names, count, the text of the first mail). The admin panel shows them on the E-posta tab ("Mail kaydı") and today's on the Bugün tab. Firestore rule: admins read, nobody writes from the browser.

## Word links in the games

`oyunlar/common.js` `wordInfoOf` adds two kinds of tags at run time: "Kelime incelemesi" (from `studie` in `oyunlar/woordinfo.json`, built from the word study's `woorden` ids; shown from the study's date on) and "Gramer · almak" for the verbs of the lesson `dersler/?les=almak`. The word page (`kelime/`) shows them as "Ayrıntılı anlatım".

## Waiting list (`docs/bekleme_listesi.md`)

Words, idioms and rules Zana hears or reads during the day first go into `docs/bekleme_listesi.md` (status `bekliyor`), each with a row in the word source and its id in the `Id` column. They are placed on the site bit by bit, in the existing place for their type (word / idiom → `woordstudie`, pattern → daily-speech page, grammar → `dersler`); idioms and words can get a future Tuesday `datum` and are then mailed that week. `python3 scripts/content/bekleme_say.py` (part of the build) checks the ids, writes them as word-page links and fills the columns `Kaç yerde` / `Nerede`: in how many places on the site (via `site_places.py`, plus the NT2 crossword) the `Aranan` regex occurs, so it is clear where an item still needs to be used.
