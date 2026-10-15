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
| `nieuws/` + `data/nieuws.json` | Lezen en kijken in niveaus: daily video + text at A1-C1, idioms, quiz |
| `manifest.json`, `icons/` | "Add to home screen" on phones |
| `firestore.rules` | Security rules, paste into Firebase Console > Firestore > Rules |

## E-mail

`scripts/mailer.py` runs in GitHub Actions (`.github/workflows/mailer.yml`):
every hour it sends "account approved" mails and queued announcements (admin screen, audience all/adult/child),
every morning the next news item from `data/nieuws.json` to subscribers (profile setting; logged in `nieuws_sent/{date}`),
every Sunday weekly summaries (children: also to the linked parent).
Secrets: `FIREBASE_SERVICE_ACCOUNT`, `GMAIL_USER`, `GMAIL_APP_PASSWORD`, optional `NEWS_EXTRA_RECIPIENTS` (comma separated, news only).

### News item format (`data/nieuws.json`)
`id`, `titel`, `bron`, `video_url`, `afbeelding_url`, optional `video_start` (s);
`a1`…`c1` (text, `<strong>` allowed), `gloss.{level}`; `uitdrukkingen`: list of `{nl, tr, uitleg, voorbeeld, voorbeeld_tr}`;
`woordenschat` (lines `woord | soort | betekenis | voorbeeld | turks`), `b1_woorden`/`b2_woorden`/`c1_woorden`
(lines `woord | turks | makkelijker1 | makkelijker2 | voorbeeld | vertaling`), `grammatica`, `vragen`, `antwoorden`,
`quiz.{a2,b1,b2,c1}.{woorden,grammatica,lezen}`: list of `{vraag, opties[], juist, uitleg}`.
New items are sent in file order; after all have been sent, the one sent longest ago goes again.
A manual run (Actions > Mailer > Run workflow) is a dry run by default.

## Adding a kids exercise

1. Put the page under `kids/<groep>/`.
2. In its module script: `const { user } = await gate({ area: "kids" })` and save rounds with `saveAttempt(user.uid, "<module-id>", attempt)`.
3. Add an entry to `data/catalog.json` with `area: "kids"` and the right `group`.
