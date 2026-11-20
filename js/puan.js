// Points for every finished round (users/{uid}/attempts). Admin only for now.
// Nothing is stored: points are computed from the saved result (module, score, total), so changing a number
// here changes all points, also of old rounds.
//
// points = (finish + accuracy x max) x difficulty, rounded
//   daily games ("oyun-*", Woordle)   10 + 10        x1
//   news quiz                         15 + 10        x1   (a news item is worth at least a daily game)
//   Lezen A2 (one text = 3 questions) 15 + 10        x1.0 per text
//   Lezen B1 (one text = 6 questions) 15 + 10        x1.5 per text   (B1 texts are ~5x longer, twice the questions)
//   KNM (10 questions = one round)    10 + 10        x1.2 per 10 questions
//   everything else                   10 + 10        x1
// plus a streak bonus: the 2nd day in a row +2, the 3rd +4 ... at most +10 a day.

const DAY = iso => new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/Amsterdam" }).format(new Date(iso));

export function pointsOf(a) {
  const m = a.module || "", tot = a.total || 0;
  // A round without questions (2048, memory) counts as fully done
  const acc = tot ? Math.max(0, Math.min(1, (a.score || 0) / tot)) : 1;
  const base = (finish, max) => finish + max * acc;
  let p;
  if (m.startsWith("oyun-") || m.startsWith("slimspel-woordle")) p = base(10, 10);
  else if (m === "nieuws") p = base(15, 10);
  else if (m === "lezen-a2") p = base(15, 10) * Math.max(1, tot / 3);
  else if (m === "lezen" || m === "lezen-teksten") p = base(15, 10) * 1.5 * Math.max(1, tot / 6);
  else if (m === "knm") p = base(10, 10) * 1.2 * Math.max(1, tot / 10);
  else p = base(10, 10);
  return Math.round(p);
}

// All rounds of one person -> totals. today / week: Amsterdam days; week = the last 7 days including today.
export function pointsSummary(attempts, now = new Date()) {
  const done = attempts.filter(a => a.finished_at).sort((a, b) => a.finished_at < b.finished_at ? -1 : 1);
  const byDay = new Map();
  for (const a of done) {
    const d = DAY(a.finished_at);
    byDay.set(d, (byDay.get(d) || 0) + pointsOf(a));
  }
  // Streak bonus per day: consecutive days with at least one round
  const days = [...byDay.keys()].sort();
  let run = 0, prev = null;
  for (const d of days) {
    const gap = prev ? Math.round((new Date(d) - new Date(prev)) / 864e5) : null;
    run = gap === 1 ? run + 1 : 1;
    byDay.set(d, byDay.get(d) + Math.min(10, 2 * (run - 1)));
    prev = d;
  }
  const today = DAY(now.toISOString());
  const weekStart = DAY(new Date(now - 6 * 864e5).toISOString());
  const sum = f => [...byDay].filter(([d]) => f(d)).reduce((n, [, p]) => n + p, 0);
  // Current streak: ends today or yesterday
  const yesterday = DAY(new Date(now - 864e5).toISOString());
  const streak = days.length && [today, yesterday].includes(days[days.length - 1]) ? run : 0;
  return { today: sum(d => d === today), week: sum(d => d >= weekStart), total: sum(() => true), streak, byDay };
}
