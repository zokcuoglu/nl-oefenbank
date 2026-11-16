// Shared by every question file of kids/rekenen.html (rekenen-vragen.js, rekenen-school.js, natuur-vragen.js, natuur-78.js):
// random numbers, the question object, small SVG helpers, the question maker and the answer check.
// It is a file of its own so the question files can import it without importing each other.
//
// A question is: { id, level, nl, tr, answer, unit, ex_nl, ex_tr, fig?, opts?, show? }
//   level 1 = straight sum, 2 = the other way round, 3 = word problem
//   opts  = [{ v, nl, tr }] for a multiple-choice question; without opts the child types a number
//   show  = how the right answer is written on screen when that differs from the number (e.g. "7,50")

export const PI = 3;   // agreement on the page: pi = 3, so answers stay whole numbers

// ---------------------------------------------------------------- small helpers
export const ri = (a, b) => a + Math.floor(Math.random() * (b - a + 1));      // whole number from a to b
export const pick = arr => arr[Math.floor(Math.random() * arr.length)];
export const shuffle = arr => { const a = [...arr]; for (let i = a.length - 1; i > 0; i--) { const j = ri(0, i); [a[i], a[j]] = [a[j], a[i]]; } return a; };
export const tri = n => n * (n + 1) / 2;                                      // 1 + 2 + ... + n
export const isPrime = n => { if (n < 2) return false; for (let i = 2; i * i <= n; i++) if (n % i === 0) return false; return true; };
export const divisors = n => { const d = []; for (let i = 1; i <= n; i++) if (n % i === 0) d.push(i); return d; };
export const gcd = (a, b) => b ? gcd(b, a % b) : a;
export const Q = (nl, tr, answer, unit, ex_nl, ex_tr, extra = {}) => ({ nl, tr, answer, unit, ex_nl, ex_tr, ...extra });
export const num = v => ({ v, nl: String(v), tr: String(v) });                // a number as a multiple-choice option

// ---------------------------------------------------------------- figures (small inline SVG, colours from the page)
export const svg = body => `<svg viewBox="0 0 220 130" role="img" aria-hidden="true">${body}</svg>`;
export const T = (x, y, s, anchor = "middle") => `<text x="${x}" y="${y}" text-anchor="${anchor}">${s}</text>`;
// Euro amount as it is written in Dutch: 7.5 -> "7,50", 12 -> "12"
export const eur = x => Number.isInteger(x) ? String(x) : x.toFixed(2).replace(".", ",");
// Decimal number with a comma: 2.5 -> "2,5"
export const dec = x => String(Math.round(x * 100) / 100).replace(".", ",");
// A hand-written multiple-choice question: the first answer is the right one; options are shuffled each time.
// right / each wrong = [Dutch, Turkish]
export const MC = (nl, tr, right, wrong, ex_nl, ex_tr, extra = {}) => () => {
  const opts = shuffle([right, ...wrong].map(([n, t], i) => ({ v: "o" + i, nl: n, tr: t })));
  return Q(nl, tr, "o0", "", ex_nl, ex_tr, { opts, ...extra });
};
// Multiple choice between numbers or short texts that are the same in both languages
// (wrong answers that repeat each other or equal the right one are dropped)
export const pickOne = (right, wrong) => ({ opts: shuffle([...new Set([right, ...wrong].map(String))]).map(v => ({ v, nl: v, tr: v })) });

/** One fresh question of a topic at a level (1-3). `avoid` = ids used shortly before, to get some variety. */
// kind (optional) = index of one generator: used to give the same kind of question again with new numbers
export const maker = gen => function makeQuestion(topicId, level, avoid = [], kind = null) {
  const list = gen[topicId][level - 1];
  let i = kind !== null && list[kind] ? kind : ri(0, list.length - 1);
  for (let t = 0; kind === null && t < 6 && avoid.includes(`${topicId}:${level}:${i}`); t++) i = ri(0, list.length - 1);
  return { ...list[i](), id: `${topicId}:${level}:${i}`, topic: topicId, level };
};

/** Is the typed text (or the chosen option) the right answer? Accepts "12", " 12 ", "−3", "-3", "12,0". */
export function isCorrect(q, given) {
  if (q.opts) return String(given) === String(q.answer);
  const s = String(given ?? "").trim().replace(/[−–]/g, "-").replace(",", ".").replace(/\s+/g, "");
  if (!/^-?\d+(\.\d+)?$/.test(s)) return false;
  return Math.abs(Number(s) - q.answer) < 1e-9;   // tolerance: 0,1 + 0,2 must count as 0,3
}
