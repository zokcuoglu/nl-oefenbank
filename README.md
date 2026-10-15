# NT2 Oefenbank

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
| `kids/g4/eer-oor-eur.html` | Groep 4 spelling test |
| `firestore.rules` | Security rules, paste into Firebase Console > Firestore > Rules |

## Adding a kids exercise

1. Put the page under `kids/<groep>/`.
2. In its module script: `const { user } = await gate({ area: "kids" })` and save rounds with `saveAttempt(user.uid, "<module-id>", attempt)`.
3. Add an entry to `data/catalog.json` with `area: "kids"` and the right `group`.
