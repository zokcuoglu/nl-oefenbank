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
| `kids/g5/eer-oor-eur.html` | Groep 5 spelling test |
| `knm/` + `data/knm.json` | KNM question bank (moved from the KNM artifact) |
| `nieuws/` + `data/nieuws.json` | Nieuws in niveaus (v1): numbered video items, text at A1-C1, idioms, words, quiz; a mixed test after every 3 items |
| `scripts/content/` | Source of the news items (`nNN_*.py`) and mixed tests (`toetsen.py`); `build_nieuws.py` checks them and writes `data/nieuws.json` |
| `js/stats.js` | Statistics helpers for the profile and admin pages |
| `manifest.json`, `icons/` | "Add to home screen" on phones |
| `firestore.rules` | Security rules, paste into Firebase Console > Firestore > Rules |

## E-mail

`scripts/mailer.py` runs every hour in GitHub Actions (`.github/workflows/mailer.yml`). Each run sends
"account approved" mails and queued announcements (admin screen, audience all/adult/child), and, when the
schedule on the admin screen says so (Firestore `settings/mail`, default Monday 08:00 and Sunday 18:00, Amsterdam time):
- the next news item to subscribers (profile setting `email_news`; logged in `nieuws_sent/{date}`)
- weekly summaries (children: also to the linked parent; logged in `mail_log/weekly-{date}`)

Secrets: `FIREBASE_SERVICE_ACCOUNT`, `GMAIL_USER`, `GMAIL_APP_PASSWORD`. If one is missing the run stops with a warning instead of failing.
Manual run (Actions > Mailer > Run workflow): `hourly`, or `news` / `weekly` to send now regardless of the schedule; dry run by default.

### News items
Edit `scripts/content/nNN_*.py`, then run `python3 scripts/content/build_nieuws.py`. Each item: `id`, `nr`, `titel`, `bron`,
`video_url`, `afbeelding_url`, `niveau_video` + `niveau_uitleg`, `a1`…`c1` (`<strong>` allowed) + `gloss_{level}`,
`uitdrukkingen` `{nl, niveau, tr, uitleg, voorbeeld, voorbeeld_tr}`, `woordenschat` (lines `woord | soort | betekenis | voorbeeld | turks | niveau`),
`grammatica`, `toets` (questions `{id, type mc|tf|gap, niveau, cat, vraag, opties, juist, uitleg}`; the page shuffles the options).
Items are mailed in `nr` order. The old items are kept in `data/nieuws-v1.json` and are not used.

## Adding a kids exercise

1. Put the page under `kids/<groep>/`.
2. In its module script: `const { user } = await gate({ area: "kids" })` and save rounds with `saveAttempt(user.uid, "<module-id>", attempt)`.
3. Add an entry to `data/catalog.json` with `area: "kids"` and the right `group`.
