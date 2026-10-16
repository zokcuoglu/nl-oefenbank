// Shared core for every page of the site.
// - Firebase setup (one place for the config)
// - gate(): login, first-time onboarding (account type), and area checks
// - helpers for the user's profile document and saved attempts
//
// Data model (Firestore):
//   users/{uid}              name, email, photo, type, role, groep, exams{}, created_at, last_active, seen{module: time}
//   users/{uid}/attempts/*   one finished practice round (module, score, total, answers, ...)
// type  = "adult" | "child"            chosen once by the user, later only by admin
// role  = "member" | "teacher" | "admin"  set only by admin (enforced in firestore.rules)

import { initializeApp } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup, signInWithRedirect, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-auth.js";
import { getFirestore, doc, getDoc, setDoc, collection, addDoc, getDocs, query, where } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-firestore.js";

// Public web config (not a secret: access is controlled by firestore.rules)
const firebaseConfig = {
  apiKey: "AIzaSyAdTzM00PphCzTBinqL_KjyAJGwJgevH4k",
  authDomain: "nt2-lezen.firebaseapp.com",
  projectId: "nt2-lezen",
  storageBucket: "nt2-lezen.firebasestorage.app",
  messagingSenderId: "574362574093",
  appId: "1:574362574093:web:615c5761f2f29fc9cba444"
};
export const fb = initializeApp(firebaseConfig);
window.__coreReady = true; // seen by the page watchdog
export const auth = getAuth(fb);
export const db = getFirestore(fb);

// Site root URL, so pages at any depth can link home (core.js lives in /js/)
export const ROOT = new URL("../", import.meta.url).href;

export const TYPES = { adult: "Yetişkin", child: "Öğrenci (çocuk)" };
export const ROLES = { member: "Üye", teacher: "Öğretmen", admin: "Admin" };
export const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

export const userRef = uid => doc(db, "users", uid);
export const attemptsCol = uid => collection(db, "users", uid, "attempts");
export const STATUSES = { pending: "Onay bekliyor", approved: "Onaylı", blocked: "Engelli" };
export const roleOf = p => p?.role || "member";
export const isAdmin = p => roleOf(p) === "admin";
// New accounts start as "pending" until an admin approves them; admins are always in
export const statusOf = p => isAdmin(p) ? "approved" : (p?.status || "pending");

// Save one finished round. `module` says which exercise it belongs to.
export async function saveAttempt(uid, module, attempt) {
  return addDoc(attemptsCol(uid), { ...attempt, module });
}
// Load this user's attempts for one module (old Lezen rounds have no module field)
export async function loadAttempts(uid, module) {
  const snap = module === "lezen" ? await getDocs(attemptsCol(uid)) : await getDocs(query(attemptsCol(uid), where("module", "==", module)));
  return snap.docs.map(d => ({ id: d.id, ...d.data() }))
    .filter(a => module !== "lezen" || !a.module || a.module === "lezen")
    .sort((a, b) => (b.finished_at || "").localeCompare(a.finished_at || ""));
}
// All attempts of this user, newest first (used by home and profile pages)
export async function loadAllAttempts(uid) {
  const snap = await getDocs(attemptsCol(uid));
  return snap.docs.map(d => ({ id: d.id, ...d.data(), module: d.data().module || "lezen" }))
    .sort((a, b) => (b.finished_at || "").localeCompare(a.finished_at || ""));
}
// Record that the user opened something inside a page (e.g. one news item): seen.{key} = now
export function markSeen(uid, key) {
  return updateProfile(uid, { seen: { [key]: new Date().toISOString() } }).catch(() => {});
}
export async function updateProfile(uid, data) {
  return setDoc(userRef(uid), data, { merge: true });
}
export function logout() { signOut(auth).then(() => location.href = ROOT); }

// Small user box for page headers: photo, name, links, sign out
export function userBox(user, profile) {
  const admin = isAdmin(profile) ? `<a href="${ROOT}admin.html">Yönetim</a>` : "";
  return `<span class="ub">${user.photoURL ? `<img src="${esc(user.photoURL)}" alt="">` : ""}
    <a href="${ROOT}profile.html">${esc(profile.name || user.displayName || "Profil")}</a>${admin}
    <button type="button" class="ub-out" data-core="logout">Çıkış</button></span>`;
}
document.addEventListener("click", e => { if (e.target.closest("[data-core='logout']")) logout(); });

// Icons for the first-login choice
const ICON_CHILD = `<svg viewBox="0 0 48 48" width="56" height="56" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="12" y="14" width="24" height="28" rx="6"/><path d="M18 14v-3a6 6 0 0 1 12 0v3"/><path d="M12 26h24"/><rect x="20" y="26" width="8" height="6" rx="1.5"/></svg>`;
const ICON_ADULT = `<svg viewBox="0 0 48 48" width="56" height="56" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="24" cy="15" r="7"/><path d="M10 42c0-8 6-14 14-14s14 6 14 14"/></svg>`;

// ---------- Gate overlay (works on any page, has its own styles) ----------
const GATE_CSS = `
#gate{position:fixed;inset:0;z-index:100;background:var(--ground,var(--paper,#F2F4F7));color:var(--ink,#142033);display:grid;place-items:center;padding:16px;overflow:auto;font-family:"IBM Plex Sans","Segoe UI",system-ui,sans-serif}
#gate .gc{background:var(--surface,var(--card,#fff));border:1px solid var(--line,#D3DAE3);border-radius:12px;padding:24px;max-width:460px;width:100%;display:flex;flex-direction:column;gap:14px}
#gate h2{font-family:"Bricolage Grotesque","Segoe UI",system-ui,sans-serif;font-size:22px;margin:0}
#gate p{margin:0;color:var(--muted,#566377)}
#gate .eb{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted,#566377)}
#gate button{font:inherit;cursor:pointer;border-radius:8px;padding:10px 14px;border:1px solid var(--line,#D3DAE3);background:var(--surface,#fff);color:inherit;text-align:left}
#gate button.pri{background:#C8551B;border-color:#C8551B;color:#fff;text-align:center;font-weight:600}
#gate button:hover{border-color:#C8551B}
#gate .tiles{display:grid;grid-template-columns:1fr 1fr;gap:12px}
#gate .tile{display:flex;flex-direction:column;align-items:center;gap:10px;padding:22px 10px;text-align:center;border-width:2px;border-radius:12px}
#gate .tile span{font-family:"Bricolage Grotesque","Segoe UI",system-ui,sans-serif;font-size:19px;font-weight:600}
#gate .tile svg{color:#C8551B}
#gate .err{background:#F6E0DE;color:#B3403A;border-radius:8px;padding:10px 12px}
@media (prefers-color-scheme:dark){#gate .err{background:#3A1E1C;color:#E58A83}}
.ub{display:inline-flex;align-items:center;gap:8px;font-size:13px;flex-wrap:wrap}
.ub img{width:26px;height:26px;border-radius:50%}
.ub a{color:inherit}
.ub-out{font:inherit;font-size:13px;border:1px solid var(--line,#D3DAE3);background:none;color:inherit;border-radius:8px;padding:4px 10px;cursor:pointer}`;

function overlay(html) {
  if (!document.getElementById("gate-css")) {
    const st = document.createElement("style"); st.id = "gate-css"; st.textContent = GATE_CSS; document.head.appendChild(st);
  }
  let g = document.getElementById("gate");
  if (!g) { g = document.createElement("div"); g.id = "gate"; document.body.appendChild(g); }
  g.innerHTML = `<div class="gc">${html}</div>`;
  return g;
}
const closeOverlay = () => document.getElementById("gate")?.remove();

async function googleLogin() {
  const p = new GoogleAuthProvider();
  try { await signInWithPopup(auth, p); }
  catch (e) {
    // Some phones block popups: fall back to a full-page redirect
    if (["auth/popup-blocked", "auth/operation-not-supported-in-this-environment"].includes(e.code)) return signInWithRedirect(auth, p);
    if (e.code !== "auth/popup-closed-by-user") throw e;
  }
}

/**
 * Wait until the visitor is signed in and has a complete profile.
 * area: "nt2" (adults only), "kids" (everyone), "any" (everyone), "admin" (admin only)
 * seen: module id to record as visited (users/{uid}.seen.{id} = time), e.g. "lezen"
 * Resolves with { user, profile }.
 */
export function gate({ area = "any", title = "NL Oefenbank", seen = "" } = {}) {
  overlay(`<p>Yükleniyor…</p>`);
  return new Promise(resolve => {
    onAuthStateChanged(auth, async user => {
      if (!user) { showLogin(title); return; }
      try {
        const ref = userRef(user.uid);
        const snap = await getDoc(ref);
        let profile = snap.exists() ? snap.data() : null;
        if (!profile) {
          // First visit: create the document with the safe defaults the rules allow
          profile = { name: user.displayName || "", email: user.email || "", photo: user.photoURL || "", role: "member", status: "pending", created_at: new Date().toISOString() };
          await setDoc(ref, profile);
        }
        if (!profile.type) profile = await askType(user, profile);
        // Not approved yet (or blocked): stop here and show a waiting screen
        if (statusOf(profile) !== "approved") {
          updateProfile(user.uid, { name: profile.name || user.displayName || "", email: user.email || "", photo: user.photoURL || "", last_active: new Date().toISOString() }).catch(() => {});
          showWaiting(user, profile); return;
        }
        // Child accounts only see the kids area
        if (area === "nt2" && profile.type === "child") { location.href = ROOT; return; }
        if (area === "admin" && !isAdmin(profile)) { overlay(`<span class="eb">Yönetim</span><h2>Bu sayfa sadece admin için</h2><p>Hesabına admin rolü verilmemiş.</p><button class="pri" onclick="location.href='${ROOT}'">Ana sayfaya dön</button>`); return; }
        // Keep name/photo fresh and record activity (one small write per page load).
        // seen.{module} = last visit of this page; the admin statistics use it to find pages nobody opens.
        const now = new Date().toISOString();
        updateProfile(user.uid, { name: profile.name || user.displayName || "", email: user.email || "", photo: user.photoURL || "", last_active: now, ...(seen ? { seen: { [seen]: now } } : {}) }).catch(() => {});
        closeOverlay();
        resolve({ user, profile });
      } catch (e) {
        overlay(`<span class="eb">Hata</span><h2>Bir sorun oluştu</h2><p class="err">${esc(e.code || e.message || e)}</p><p>Sayfayı yenile. Devam ederse bu kodu Zana'ya gönder.</p><button data-core="logout">Çıkış yap</button>`);
      }
    });
  });
}

function showLogin(title) {
  const g = overlay(`<span class="eb">Hollandaca çalışma</span><h2>${esc(title)}</h2>
    <p>Devam etmek için Google hesabınla giriş yap. Sonuçların sadece senin hesabında saklanır.</p>
    <button class="pri" id="g-login">Google ile giriş yap</button><div id="g-err"></div>`);
  g.querySelector("#g-login").onclick = () => googleLogin().catch(e => {
    g.querySelector("#g-err").innerHTML = `<p class="err">Giriş yapılamadı: ${esc(e.code || e.message)}</p>`;
  });
}

function showWaiting(user, profile) {
  const blocked = statusOf(profile) === "blocked";
  overlay(`<span class="eb">${blocked ? "Erişim kapalı" : "Onay bekleniyor"}</span>
    <h2>${blocked ? "Bu hesabın erişimi kapatıldı" : "Hesabın henüz onaylanmadı"}</h2>
    <p>${blocked ? "Bir yanlışlık olduğunu düşünüyorsan Zana'ya yaz." : "Kaydın alındı. Zana onayladıktan sonra siteye girebilirsin. Onaylandığını öğrenince bu sayfayı yenile."}</p>
    <p style="font-size:13px">${esc(user.email || "")}</p>
    ${blocked ? "" : `<button class="pri" onclick="location.reload()">Tekrar kontrol et</button>`}
    <button data-core="logout">Çıkış yap</button>`);
}

// First-time question: who uses this account? Stored once; later only admin can change it.
function askType(user, profile) {
  return new Promise(resolve => {
    const g = overlay(`<span class="eb">İlk giriş</span><h2>Sen kimsin?</h2>
      <div class="tiles">
        <button class="tile" data-t="child">${ICON_CHILD}<span>Öğrenci</span></button>
        <button class="tile" data-t="adult">${ICON_ADULT}<span>Yetişkin</span></button>
      </div>
      <div id="g-err"></div>`);
    g.querySelectorAll("[data-t]").forEach(b => b.onclick = async () => {
      try { await updateProfile(user.uid, { type: b.dataset.t }); resolve({ ...profile, type: b.dataset.t }); }
      catch (e) { g.querySelector("#g-err").innerHTML = `<p class="err">Kaydedilemedi: ${esc(e.code || e.message)}</p>`; }
    });
  });
}
