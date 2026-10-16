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
  const max = Math.max(1, ...vals.map(x => x.v));
  return `<div class="daybars" role="img" aria-label="Son ${n} gün">${vals.map(x => {
    const d = new Date(x.k + "T12:00:00");
    return `<div title="${d.toLocaleDateString("tr-TR", { day: "numeric", month: "short" })}: ${x.v} tur"><i style="height:${x.v ? Math.max(8, Math.round(100 * x.v / max)) : 0}%"></i><span>${d.getDate()}</span></div>`;
  }).join("")}</div>`;
}
