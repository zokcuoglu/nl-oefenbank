// Small statistics helpers shared by the profile page (own numbers) and the admin page (everyone's).
// Input is a list of attempts: { module, test, score, total, finished_at }.

// Local calendar day (YYYY-MM-DD) of an ISO time, so "today" matches the user's clock
export const dayKey = iso => { const d = new Date(iso); return isNaN(d) ? "" : `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`; };
const daysAgoKey = n => { const d = new Date(); d.setDate(d.getDate() - n); return dayKey(d.toISOString()); };

export function summarize(attempts) {
  const s = { rounds: 0, ok: 0, tot: 0, last: "", days: {}, byModule: {}, byTest: {} };
  for (const a of attempts) {
    const ok = a.score || 0, tot = a.total || 0, mod = a.module || "lezen", day = dayKey(a.finished_at);
    s.rounds++; s.ok += ok; s.tot += tot;
    if ((a.finished_at || "") > s.last) s.last = a.finished_at;
    if (day) s.days[day] = (s.days[day] || 0) + 1;
    const m = s.byModule[mod] = s.byModule[mod] || { rounds: 0, ok: 0, tot: 0, last: "" };
    m.rounds++; m.ok += ok; m.tot += tot; if ((a.finished_at || "") > m.last) m.last = a.finished_at;
    if (a.test) {
      const k = mod + "/" + a.test, t = s.byTest[k] = s.byTest[k] || { module: mod, test: a.test, rounds: 0, best: 0, lastPct: 0, last: "" };
      const pct = tot ? ok / tot : 0;
      t.rounds++; t.best = Math.max(t.best, pct);
      if ((a.finished_at || "") >= t.last) { t.last = a.finished_at || ""; t.lastPct = pct; }
    }
  }
  return s;
}

export const pct = (ok, tot) => tot ? Math.round(100 * ok / tot) : 0;

// Rounds in the last n days (today included)
export const recentRounds = (s, n) => Array.from({ length: n }, (_, i) => s.days[daysAgoKey(i)] || 0).reduce((a, b) => a + b, 0);

// Days in a row with at least one round, ending today (or yesterday, so the streak is not lost before you study today)
export function streak(s) {
  let i = s.days[daysAgoKey(0)] ? 0 : 1, n = 0;
  while (s.days[daysAgoKey(i)]) { n++; i++; }
  return n;
}

// Bar chart of rounds per day for the last n days (plain divs, no chart library)
export function dayBars(s, n = 14) {
  const vals = Array.from({ length: n }, (_, i) => { const k = daysAgoKey(n - 1 - i); return { k, v: s.days[k] || 0 }; });
  const max = Math.max(1, ...vals.map(x => x.v)), every = n > 14 ? 5 : 1;  // long ranges: a day label every 5 days
  return `<div class="daybars" style="grid-template-columns:repeat(${n},1fr)" role="img" aria-label="Son ${n} gün">${vals.map((x, i) => {
    const d = new Date(x.k + "T12:00:00");
    return `<div title="${d.toLocaleDateString("tr-TR", { day: "numeric", month: "short" })}: ${x.v} tur"><i style="height:${x.v ? Math.max(8, Math.round(100 * x.v / max)) : 0}%"></i><span>${(n - 1 - i) % every === 0 ? d.getDate() : "&nbsp;"}</span></div>`;
  }).join("")}</div>`;
}

// ---------- News quiz scores per level, fading when not repeated ----------
// The level filter chosen when starting a quiz (A2 = questions up to A2, ... "all" = every question)
export const QUIZ_LEVELS = [["A2", "A2", "a2"], ["B1", "B1", "b1"], ["B2", "B2", "b2"], ["all", "Hepsi", "c1"]];

// Share of a score that still counts after `days` without practice: full for a week,
// then it halves every 30 days (a simple forgetting curve), so old results slowly fade
export const retention = days => days <= 7 ? 1 : Math.pow(0.5, (days - 7) / 30);

const daysSince = iso => Math.max(0, Math.floor((Date.now() - new Date(iso)) / 864e5));
const toneVar = p => `var(--${p >= 80 ? "ok" : p >= 60 ? "warn" : "bad"})`;

// Best score of one test (and level), plus the faded value; null when never done
export function scoreFor(attempts, test, level = null) {
  const tries = attempts.filter(a => a.test === test && a.total && (level === null || (a.level || "all") === level));
  if (!tries.length) return null;
  const best = Math.max(...tries.map(a => a.score / a.total));
  const last = tries.reduce((m, a) => (a.finished_at || "") > m ? a.finished_at : m, "");
  const days = daysSince(last);
  return { n: tries.length, best: Math.round(100 * best), days, shown: Math.round(100 * best * retention(days)) };
}

function chip(label, col, s) {
  if (!s) return `<span class="lvlscore num" style="--lc:var(--line);--tone:var(--muted);color:var(--muted)" title="${label}: henüz çözülmedi">${label} <b>–</b></span>`;
  const faded = s.shown < s.best;
  const title = `${label}: en iyi %${s.best}, ${s.n} deneme, son deneme ${s.days === 0 ? "bugün" : s.days + " gün önce"}` +
    (faded ? ` · tekrar etmediğin için şu an %${s.shown}; tekrar çözersen yükselir` : "");
  return `<span class="lvlscore num${faded ? " faded" : ""}" style="--lc:var(--${col});--tone:${toneVar(s.shown)}" title="${title}">${label} <b>${faded ? "↻" : ""}%${s.shown}</b></span>`;
}

// Chips for an item quiz: one per level (also the ones not done yet); for a mixed test one chip
export function scoreChips(attempts, test) {
  if (test.startsWith("toets")) return `<span class="scores">${chip("en iyi", "ink", scoreFor(attempts, test))}</span>`;
  return `<span class="scores">${QUIZ_LEVELS.map(([lv, label, col]) => chip(label, col, scoreFor(attempts, test, lv))).join("")}</span>`;
}
