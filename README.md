# Lezen Oefenbank

Practice site for the **Staatsexamen NT2 Lezen I (B1)** reading exam.

- **Word bank:** 302 words and 17 question patterns, counted from the official public exams 2023, 2024 and 2025 (CvTE). Example sentences are newly written, not copied from the exams.
- **Login:** Google sign-in through Firebase Authentication.
- **Storage:** each user's exam date and results are stored in Firestore under `users/{uid}`; nobody else can read them (see `firestore.rules`).

## Files

| File | What it is |
|---|---|
| `index.html` | The whole site (HTML, CSS and JavaScript). Firebase is loaded from Google's CDN, so there is no build step. |
| `data/bank.json` | Shared word bank. Edit this file to fix a word or translation. |
| `firestore.rules` | Security rules. Paste into Firebase Console > Firestore Database > Rules. |

## Hosting

GitHub Pages: Settings > Pages > Deploy from a branch > `main` / root.
The Pages domain (`zokcuoglu.github.io`) must be listed in Firebase Authentication > Settings > Authorized domains.
