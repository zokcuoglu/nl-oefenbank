// "Bugünkü tekrarın": lesson questions someone got wrong come back after a few days (spaced repetition).
// Nothing extra is stored: the schedule is worked out from the saved rounds (attempts) of the lesson modules.
// Rule per question, looking at its answers from old to new:
//   - it only enters the review after it was answered wrong at least once
//   - after a wrong answer it is due the next day
//   - after 1, 2, 3 right answers in a row it comes back after 2, 5, 12 days; after 4 in a row it is learned
// Used by the home page (how many are due) and by dersler/ (the review round itself).
export const REVIEW_MODULES = ["dersler", "gramer", "konusma", "tekrar"];
const GAP_DAYS = [1, 2, 5, 12];   // index = right answers in a row since the last wrong one
export const REVIEW_SIZE = 10;    // questions per review round

// Day number in Dutch time, so "tomorrow" starts at midnight in the Netherlands
const dayNr = iso => Math.floor(Date.parse(new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/Amsterdam" }).format(new Date(iso)) + "T00:00:00Z") / 864e5);

// attempts: all rounds of one person (any order). Returns the question ids that are due today,
// the ones waiting longest first, and how many are still in the review but not due yet.
export function reviewState(attempts, now = new Date()) {
  const hist = new Map();   // qid -> [{ at, correct }] old to new
  attempts.filter(a => REVIEW_MODULES.includes(a.module) && a.finished_at)
    .sort((a, b) => a.finished_at.localeCompare(b.finished_at))
    .forEach(a => (a.answers || []).forEach(an => { if (an.qid) (hist.get(an.qid) || hist.set(an.qid, []).get(an.qid)).push({ at: a.finished_at, correct: !!an.correct }); }));
  const today = dayNr(now), due = [];
  let waiting = 0, learned = 0;
  for (const [qid, list] of hist) {
    const lastWrong = list.map(x => x.correct).lastIndexOf(false);
    if (lastWrong < 0) continue;                       // never wrong: not in the review
    const streak = list.length - 1 - lastWrong;        // right answers since the last wrong one
    if (streak >= GAP_DAYS.length) { learned++; continue; }
    const dueDay = dayNr(list[list.length - 1].at) + GAP_DAYS[streak];
    if (dueDay <= today) due.push({ qid, dueDay, streak }); else waiting++;
  }
  due.sort((a, b) => a.dueDay - b.dueDay);
  return { due: due.map(d => d.qid), waiting, learned };
}
