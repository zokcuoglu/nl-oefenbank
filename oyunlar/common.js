// Shared parts of the daily games in the "Günün oyunları" tab (de/het, werkwoorden, kruiswoord NT2, verbanden):
// today's date, the daily pick, saving results for the rankings, the ranking and statistics boxes, and styles.
// Only imports `db` from core.js (an old name), so an older cached core.js cannot break the page.
import { db } from "../js/core.js";
import { doc, setDoc, collection, getDocs, query, where } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-firestore.js";

export const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
export const fmt = s => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`;
// Today in the Netherlands (YYYY-MM-DD): new games start at midnight Dutch time
export const today = () => new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/Amsterdam" }).format(new Date());
export const dayNr = d => Math.floor(Date.parse(d + "T00:00:00Z") / 86400000);
export const isoOf = n => new Date(n * 86400000).toISOString().slice(0, 10);
export const weekStart = day => { const n = dayNr(day), dow = (new Date(n * 86400000).getUTCDay() + 6) % 7; return isoOf(n - dow); };
export function hash(text) { let h = 2166136261; for (const ch of text) { h ^= ch.codePointAt(0); h = Math.imul(h, 16777619); } return h >>> 0; }

// The same n items for everybody today: each item gets a number from (day, game, item); the smallest n win.
// Adding items to the list later rarely changes today's choice.
export function pickDaily(items, keyOf, n, day, game) {
  return items.map(it => [hash(`${day}|${game}|${keyOf(it)}`), it]).sort((a, b) => a[0] - b[0]).slice(0, n).map(x => x[1]);
}

// Browser storage (own prefix), for unfinished games and small choices
export const loadLocal = (k, fb) => { try { const v = localStorage.getItem("nloefenbank:" + k); return v === null ? fb : JSON.parse(v); } catch { return fb; } };
export const saveLocal = (k, v) => { try { v === null ? localStorage.removeItem("nloefenbank:" + k) : localStorage.setItem("nloefenbank:" + k, JSON.stringify(v)); } catch {} };
export function dropOldProgress(game) {
  try { Object.keys(localStorage).filter(k => k.startsWith(`nloefenbank:${game}:progress:`) && !k.endsWith(today()))
    .forEach(k => localStorage.removeItem(k)); } catch {}
}

// ---------- Results for the rankings (firestore.rules: dagspel_plays) ----------
export function savePlay(user, profile, { game, level, day, score, total, time_s }) {
  const name = (profile.name || user.displayName || "?").trim().split(/\s+/)[0];
  return setDoc(doc(db, "dagspel_plays", `${game}-${level}-${day}-${user.uid}`), {
    uid: user.uid, name: name.slice(0, 40), game, level, day, score: Math.round(score), total: Math.round(total),
    time_s: Math.max(0, Math.round(time_s)), at: new Date().toISOString()
  });
}
export async function loadPlays(game, fromDay) {
  const snap = await getDocs(query(collection(db, "dagspel_plays"), where("day", ">=", fromDay)));
  return snap.docs.map(d => d.data()).filter(p => p.game === game);
}

// ---------- Ranking box: today / this week / this month, per level or all levels ----------
// levels: { key: label }. Day + one level = that game: most points, then fastest.
// Longer periods: total points, days played and the average score.
export async function drawRanking(el, { game, levels, user }) {
  const state = el._rank || (el._rank = { tab: "dag", level: Object.keys(levels).length > 1 ? "alle" : Object.keys(levels)[0], plays: null });
  const tabs = [["dag", "Bugün"], ["week", "Bu hafta"], ["maand", "Bu ay"]]
    .map(([k, t]) => `<button class="ch${k === state.tab ? " on" : ""}" data-tab="${k}">${t}</button>`).join("");
  const lvs = Object.keys(levels).length > 1 ? [["alle", "Tüm seviyeler"], ...Object.entries(levels)]
    .map(([k, t]) => `<button class="ch${k === state.level ? " on" : ""}" data-lv="${k}">${esc(t)}</button>`).join("") : "";
  el.innerHTML = `<h3>Sıralama</h3><div class="tabs2">${tabs}</div>${lvs ? `<div class="tabs2">${lvs}</div>` : ""}<div data-t><p class="small">…</p></div>`;
  el.querySelectorAll("[data-tab]").forEach(b => b.onclick = () => { state.tab = b.dataset.tab; drawRanking(el, { game, levels, user }); });
  el.querySelectorAll("[data-lv]").forEach(b => b.onclick = () => { state.level = b.dataset.lv; drawRanking(el, { game, levels, user }); });
  const out = el.querySelector("[data-t]");
  const day = today();
  try { if (!state.plays) state.plays = await loadPlays(game, [weekStart(day), day.slice(0, 8) + "01"].sort()[0]); }
  catch { out.innerHTML = `<p class="small">Sıralama şu an yüklenemiyor.</p>`; return; }
  const from = state.tab === "dag" ? day : state.tab === "week" ? weekStart(day) : day.slice(0, 8) + "01";
  const sel = state.plays.filter(p => p.day >= from && p.day <= day && (state.level === "alle" || p.level === state.level));
  const medal = ["🥇", "🥈", "🥉"];
  if (!sel.length) { out.innerHTML = `<p class="small">Bu dönemde henüz kimse yok.</p>`; return; }
  if (state.tab === "dag" && state.level !== "alle") {
    sel.sort((a, b) => b.score - a.score || a.time_s - b.time_s);
    out.innerHTML = `<table class="rank"><tr><th></th><th>İsim</th><th class="n">Puan</th><th class="n">Süre</th></tr>` +
      sel.map((p, i) => `<tr class="${p.uid === user.uid ? "me" : ""}"><td>${medal[i] || i + 1}</td><td>${esc(p.name)}</td>
        <td class="n">${p.score}/${p.total}</td><td class="n">${fmt(p.time_s)}</td></tr>`).join("") + `</table>`;
    return;
  }
  const per = new Map();
  for (const p of sel) {
    const r = per.get(p.uid) || { name: p.name, uid: p.uid, pts: 0, tot: 0, days: new Set() };
    r.pts += p.score; r.tot += p.total; r.days.add(p.day); per.set(p.uid, r);
  }
  const rows = [...per.values()].sort((a, b) => b.pts - a.pts || b.pts / (b.tot || 1) - a.pts / (a.tot || 1));
  out.innerHTML = `<table class="rank"><tr><th></th><th>İsim</th><th class="n">Puan</th><th class="n">Gün</th><th class="n">Ort.</th></tr>` +
    rows.map((r, i) => `<tr class="${r.uid === user.uid ? "me" : ""}"><td>${medal[i] || i + 1}</td><td>${esc(r.name)}</td>
      <td class="n">${r.pts}</td><td class="n">${r.days.size}</td><td class="n">%${Math.round(100 * r.pts / (r.tot || 1))}</td></tr>`).join("") + `</table>`;
}
export function resetRanking(el) { if (el._rank) el._rank.plays = null; }

// ---------- Own statistics: days played, average, streak, best ----------
// history = own attempts of this game (each with day, score, total); level = filter, or null for all
export function drawStats(el, history, levelLabel = "") {
  const rounds = history.filter(h => h.day);
  const days = [...new Set(rounds.map(h => h.day))].sort();
  const pct = rounds.length ? Math.round(100 * rounds.reduce((n, h) => n + (h.score || 0), 0) / Math.max(1, rounds.reduce((n, h) => n + (h.total || 0), 0))) : 0;
  let d = days.includes(today()) ? dayNr(today()) : dayNr(today()) - 1, cur = 0;
  while (days.includes(isoOf(d))) { cur++; d--; }
  const best = rounds.length ? Math.max(...rounds.map(h => h.total ? Math.round(100 * h.score / h.total) : 0)) : 0;
  el.innerHTML = `<h3>İstatistiklerin${levelLabel ? " · " + esc(levelLabel) : ""}</h3>` + (rounds.length ? `
    <div class="stats">
      <div><b>${days.length}</b><span>oynanan gün</span></div>
      <div><b>%${pct}</b><span>ortalama</span></div>
      <div><b>${cur}</b><span>gün serisi</span></div>
      <div><b>%${best}</b><span>en iyi</span></div>
    </div>` : `<p class="small">Henüz oynamadın.</p>`);
}

// ---------- Styles (scoped under .og, colours from the NL Oefenbank design) ----------
const CSS = `
.og{--og-card:var(--surface,#fff);--og-sunk:var(--sunk,#e6eaf0);--og-line:var(--line,#d3dae3);--og-ink:var(--ink,#142033);--og-muted:var(--muted,#566377);
  --og-accent:var(--accent,#c8551b);--og-accent-ink:var(--accent-ink,#fff);--og-ok:var(--ok,#2e7d4f);--og-ok-soft:var(--ok-soft,#ddf0e4);--og-bad:var(--bad,#b3403a);--og-bad-soft:var(--bad-soft,#f6e0de);
  --og-font:var(--display,system-ui,sans-serif)}
.og h2.ot{font-family:var(--og-font);font-size:clamp(24px,5vw,32px);margin:0}
.og .sub{color:var(--og-muted);margin:.3rem 0 0}
.og .lbl{font-family:var(--og-font);font-weight:600;margin:18px 0 8px}
.og .choice,.og .tabs2{display:flex;flex-wrap:wrap;gap:6px}
.og .tabs2{margin-bottom:8px}
.og .ch{font:inherit;font-weight:500;font-size:14px;background:var(--og-card);color:var(--og-ink);border:1px solid var(--og-line);border-radius:999px;padding:5px 13px;cursor:pointer}
.og .ch.on{background:var(--og-accent);border-color:var(--og-accent);color:var(--og-accent-ink)}
.og .tabs2 .ch{font-size:13px;padding:3px 11px}
.og .bt{font:inherit;font-weight:600;font-size:15px;background:var(--og-card);color:var(--og-ink);border:1px solid var(--og-line);border-radius:8px;padding:9px 16px;cursor:pointer}
.og .bt.pri{background:var(--og-accent);border-color:var(--og-accent);color:var(--og-accent-ink)}
.og .bt:disabled{opacity:.45;cursor:not-allowed}
.og .today{margin-top:12px;font-weight:600}
.og .bar{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:12px;flex-wrap:wrap}
.og .pill{font-family:var(--mono,monospace);font-size:13px;background:var(--og-sunk);border-radius:999px;padding:3px 10px;font-variant-numeric:tabular-nums}
.og .pan{background:var(--og-card);border:1px solid var(--og-line);border-radius:10px;padding:18px}
.og .pan h3{font-family:var(--og-font);font-size:17px;margin:0 0 8px}
.og .stats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;text-align:center}
.og .stats b{display:block;font-family:var(--og-font);font-size:24px}
.og .stats span{font-size:12px;color:var(--og-muted)}
.og .rank{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums}
.og .rank td,.og .rank th{padding:6px;border-bottom:1px solid var(--og-line);text-align:left}
.og .rank th{font-size:11px;color:var(--og-muted);text-transform:uppercase;letter-spacing:.05em}
.og .rank .n{text-align:right}
.og .rank tr.me td{background:color-mix(in srgb,var(--og-accent) 14%,var(--og-card));font-weight:700}
.og .small{color:var(--og-muted);font-size:13px;margin:6px 0 0}
.og .grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:18px}
@media (max-width:720px){.og .grid2{grid-template-columns:1fr}}
.og .big{font-family:var(--og-font);font-weight:700;font-size:clamp(28px,7vw,40px);line-height:1.15}
.og .good{color:var(--og-ok)} .og .bad{color:var(--og-bad)}
.og .saveerr{color:var(--og-bad);font-size:14px;margin:8px 0 0}
@keyframes og-pop{0%{transform:scale(1)}40%{transform:scale(1.06)}100%{transform:scale(1)}}
@keyframes og-shake{0%,100%{transform:translateX(0)}25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}
.og .pop{animation:og-pop .3s ease}.og .shake{animation:og-shake .25s ease 2}
@media (prefers-reduced-motion: reduce){.og .pop,.og .shake{animation:none}}
.og [hidden]{display:none!important}`;
export function injectCss(extra = "", id = "") {
  if (!document.getElementById("og-css")) { const st = document.createElement("style"); st.id = "og-css"; st.textContent = CSS; document.head.appendChild(st); }
  if (extra && id && !document.getElementById(id)) { const st = document.createElement("style"); st.id = id; st.textContent = extra; document.head.appendChild(st); }
}
export const flash = (el, cls) => { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); };
