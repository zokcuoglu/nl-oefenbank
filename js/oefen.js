// Shared word practice: word status (what someone knows), flashcards and the matching game.
// Used by woorden/index.html (adults and children) and kids/woordkaarten.html (school lists).
// Works with both page styles: colours fall back from the site names (--surface, --ok) to the kids names (--card, --good).
import { esc } from "./core.js";

// ---------- Word status ----------
// Built from all saved rounds (every answer with a word id "w"), oldest first:
//   wrong answer          -> streak 0 ("zayıf")
//   right answer          -> streak + 1
//   "Ken ik" on a card    -> streak + 1, but at most 2: a card is your own judgement, so it can make a word
//                            "öğreniliyor" but never "biliyor"; that needs a right answer in a test or the matching game.
//   streak 3 or more      -> "biliyor"
export const STATUS = {
  nieuw: { icon: "🆕", label: "Yeni", hint: "hiç sorulmadı" },
  zwak: { icon: "🔴", label: "Zayıf", hint: "son cevap yanlış" },
  bezig: { icon: "🟡", label: "Öğreniliyor", hint: "arka arkaya 1–2 doğru" },
  kent: { icon: "🟢", label: "Biliyor", hint: "arka arkaya 3 doğru (test veya eşleştirme)" },
};
export const KNOWN_AFTER = 3;

export function wordStatus(attempts) {
  const streak = {};
  const oldestFirst = [...attempts].sort((a, b) => (a.finished_at || "").localeCompare(b.finished_at || ""));
  for (const a of oldestFirst) {
    const selfJudged = a.test === "kaarten";
    for (const x of a.answers || []) {
      if (!x.w) continue;
      const s = streak[x.w] ?? 0;
      streak[x.w] = !x.correct ? 0 : selfJudged ? Math.max(s, Math.min(s + 1, KNOWN_AFTER - 1)) : s + 1;
    }
  }
  return streak; // id -> streak; a missing id = never asked
}
export const statusOf = (streak, id) => !(id in streak) ? "nieuw" : streak[id] >= KNOWN_AFTER ? "kent" : streak[id] >= 1 ? "bezig" : "zwak";
// Order for practice: weak first, then new, then learning, known last
export const STATUS_ORDER = { zwak: 0, nieuw: 1, bezig: 2, kent: 3 };

// ---------- Small helpers ----------
export const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
export const fmtTime = ms => { const s = Math.round(ms / 1000); return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0"); };
export const speak = t => { if (!("speechSynthesis" in window)) return; speechSynthesis.cancel(); const u = new SpeechSynthesisUtterance(t); u.lang = "nl-NL"; u.rate = .9; speechSynthesis.speak(u); };
// What the back of a card / the matching tile shows: Turkish, or the Dutch definition when there is one
export const meaningOf = (w, side) => side === "def" && w.definitie ? w.definitie : w.tr;

// ---------- Styles (injected once) ----------
const CSS = `
.of-bar{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
.of-chip{font-family:var(--display,var(--f-display));font-weight:600;background:var(--surface,var(--card));border:2px solid var(--line);border-radius:999px;padding:3px 12px;font-variant-numeric:tabular-nums;font-size:15px}
.of-link{background:none;border:none;color:var(--muted);text-decoration:underline;padding:0;cursor:pointer;font:inherit}
.of-prog{height:8px;background:var(--line);border-radius:99px;margin:12px 0 18px;overflow:hidden}
.of-prog span{display:block;height:100%;background:var(--ink);width:0;transition:width .25s}
.of-flip{perspective:1200px;height:clamp(260px,46vh,360px);cursor:pointer}
.of-in{position:relative;width:100%;height:100%;transition:transform .45s;transform-style:preserve-3d}
.of-flip.back .of-in{transform:rotateY(180deg)}
.of-face{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;background:var(--surface,var(--card));border:2px solid var(--line);border-radius:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;padding:22px;text-align:center}
.of-face.b{transform:rotateY(180deg)}
.of-word{font-family:var(--display,var(--f-display));font-weight:700;font-size:clamp(28px,7vw,48px);line-height:1.15}
.of-main{font-size:clamp(20px,4.4vw,27px);font-weight:700;line-height:1.3}
.of-sub{color:var(--muted);font-size:15px}
.of-ex{font-size:15px;max-height:9.5em;overflow:auto;border-left:3px solid var(--line);padding-left:10px;text-align:left;max-width:52ch}
.of-ex em{color:var(--muted)}
.of-tap{position:absolute;bottom:10px;font-size:13px;color:var(--muted)}
.of-say{position:absolute;top:10px;right:12px;background:none;border:none;font-size:22px;cursor:pointer}
.of-tags{position:absolute;top:12px;left:14px;font-size:12px;color:var(--muted)}
.of-judge{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px}
.of-judge button{border-radius:14px;padding:13px;font-family:var(--display,var(--f-display));font-weight:600;font-size:18px;border:2px solid;cursor:pointer}
.of-judge .no{background:var(--bad-soft,var(--bad-bg));color:var(--bad);border-color:var(--bad)}
.of-judge .ok{background:var(--ok-soft,var(--good-bg));color:var(--ok,var(--good));border-color:var(--ok,var(--good))}
.of-match{display:grid;grid-template-columns:1fr 1.4fr;gap:10px}
.of-col{display:flex;flex-direction:column;gap:10px}
.of-tile{background:var(--surface,var(--card));border:2px solid var(--line);border-radius:12px;padding:11px 10px;min-height:56px;font:inherit;font-size:15.5px;line-height:1.3;color:inherit;cursor:pointer;transition:background .15s,border-color .15s,opacity .3s}
.of-tile.w{font-family:var(--display,var(--f-display));font-weight:600;font-size:18px}
.of-tile:hover:not(:disabled){border-color:var(--ink)}
.of-tile.sel{border-color:var(--ink);background:var(--accent);color:var(--accent-ink)}
.of-tile.ok{background:var(--ok-soft,var(--good-bg));border-color:var(--ok,var(--good));color:var(--ok,var(--good));opacity:.45;cursor:default}
.of-tile.no{background:var(--bad-soft,var(--bad-bg));border-color:var(--bad);color:var(--bad);animation:of-shake .35s}
@keyframes of-shake{25%{transform:translateX(-5px)}75%{transform:translateX(5px)}}
@media (prefers-reduced-motion:reduce){.of-in,.of-tile{transition:none!important;animation:none!important}}`;
function injectCss() {
  if (document.getElementById("oefen-css")) return;
  const s = document.createElement("style"); s.id = "oefen-css"; s.textContent = CSS; document.head.appendChild(s);
}

// ---------- Flashcards ----------
// words: entries from woorden.json. side: "tr" or "def". onDone({ ms, first: {id: bool}, words }), onQuit().
// "Nog oefenen" puts the card back 3 places later, so the round ends only when every card was "Ken ik".
export function mountCards(el, words, { side = "tr", tags = () => "", onDone, onQuit }) {
  injectCss();
  const C = { queue: shuffle(words), first: {}, known: 0, t0: Date.now() };
  el.innerHTML = `<div class="of-bar"><button class="of-link" data-q>← Stoppen</button><span class="of-chip" data-count></span><span class="of-chip" data-known></span></div>
    <div class="of-prog"><span data-prog></span></div>
    <div class="of-flip" tabindex="0" role="button" aria-label="Kaart omdraaien">
      <div class="of-in">
        <div class="of-face"><span class="of-tags" data-tags></span><button class="of-say" data-say aria-label="Voorlezen">🔊</button><div class="of-word" lang="nl" data-word></div><span class="of-tap">Tik om te draaien · spatie</span></div>
        <div class="of-face b"><button class="of-say" data-say aria-label="Voorlezen">🔊</button><div class="of-main" data-main></div><div class="of-sub" data-sub></div><div class="of-ex" data-ex></div></div>
      </div></div>
    <div class="of-judge"><button class="no" data-no>✗ Nog oefenen <small>←</small></button><button class="ok" data-ok>✓ Ken ik <small>→</small></button></div>`;
  const $ = s => el.querySelector(s), flip = $(".of-flip");
  function draw() {
    const w = C.queue[0];
    flip.classList.remove("back");
    $("[data-word]").textContent = w.nl;
    $("[data-tags]").innerHTML = tags(w);
    $("[data-main]").textContent = meaningOf(w, side);
    // The other meaning, small: Turkish under a definition, the definition under Turkish
    $("[data-sub]").textContent = meaningOf(w, side) === w.tr ? (w.definitie || "") : w.tr;
    // Main example plus up to 2 extra examples (other meanings / uses), so the meaning sticks
    const ex = [{ nl: w.voorbeeld, tr: w.voorbeeld_tr }, ...shuffle(w.meer || []).slice(0, 2)].filter(e => e.nl);
    $("[data-ex]").innerHTML = ex.map(e => `<span lang="nl">${esc(e.nl)}</span>${e.tr ? `<br><em>${esc(e.tr)}</em>` : ""}`).join("<br>");
    $("[data-count]").textContent = `Nog ${C.queue.length}`;
    $("[data-known]").textContent = `✓ ${C.known}/${words.length}`;
    $("[data-prog]").style.width = (C.known / words.length * 100) + "%";
  }
  function judge(ok) {
    const w = C.queue.shift();
    if (!(w.id in C.first)) C.first[w.id] = ok;   // the first answer counts for the score and the word status
    if (ok) C.known++; else C.queue.splice(Math.min(3, C.queue.length), 0, w);
    if (C.queue.length) draw(); else { stop(); onDone({ ms: Date.now() - C.t0, first: C.first, words }); }
  }
  const key = e => {
    if (["INPUT", "TEXTAREA"].includes(e.target.tagName)) return;
    if (e.key === "ArrowRight") judge(true);
    else if (e.key === "ArrowLeft") judge(false);
    else if (e.key === " ") { e.preventDefault(); flip.classList.toggle("back"); }
  };
  function stop() { document.removeEventListener("keydown", key); }
  flip.onclick = e => { if (!e.target.closest("[data-say]")) flip.classList.toggle("back"); };
  el.querySelectorAll("[data-say]").forEach(b => b.onclick = () => speak(C.queue[0].nl));
  $("[data-ok]").onclick = () => judge(true);
  $("[data-no]").onclick = () => judge(false);
  $("[data-q]").onclick = () => { stop(); onQuit(); };
  document.addEventListener("keydown", key);
  draw();
  return { stop };
}

// ---------- Matching game ----------
// Rounds of `pairs` words: click a word, then its meaning (or the other way round).
// onDone({ ms, errors, wrong: Set(ids), words }). Words whose meaning text is already in a round wait for the next round,
// so two tiles with the same text never appear together.
export function mountMatch(el, words, { side = "tr", pairs = 6, onDone, onQuit }) {
  injectCss();
  const rounds = [];
  let rest = shuffle(words);
  while (rest.length) {
    const round = [], seen = new Set(), later = [];
    for (const w of rest) { const m = meaningOf(w, side).toLowerCase(); if (round.length < pairs && !seen.has(m)) { round.push(w); seen.add(m); } else later.push(w); }
    rounds.push(round); rest = later;
  }
  // A last round of 1-2 words is too easy: merge it into the round before (when the texts stay unique)
  if (rounds.length > 1 && rounds.at(-1).length < 3) {
    const last = rounds.at(-1), prev = rounds.at(-2), seen = new Set(prev.map(w => meaningOf(w, side).toLowerCase()));
    if (last.every(w => !seen.has(meaningOf(w, side).toLowerCase()))) { prev.push(...last); rounds.pop(); }
  }
  const M = { r: 0, errors: 0, wrong: new Set(), done: 0, sel: null, t0: Date.now() };
  el.innerHTML = `<div class="of-bar"><button class="of-link" data-q>← Stoppen</button><span class="of-chip" data-round></span><span class="of-chip" data-time>⏱ 0:00</span><span class="of-chip" data-err>0 fout</span></div>
    <div class="of-prog"><span data-prog></span></div>
    <div class="of-match"><div class="of-col" data-l></div><div class="of-col" data-r></div></div>`;
  const $ = s => el.querySelector(s);
  const timer = setInterval(() => $("[data-time]").textContent = "⏱ " + fmtTime(Date.now() - M.t0), 500);
  const tile = (w, kind) => `<button class="of-tile ${kind === "w" ? "w" : ""}" data-id="${esc(w.id)}" data-kind="${kind}" ${kind === "w" ? 'lang="nl"' : ""}>${esc(kind === "w" ? w.nl : meaningOf(w, side))}</button>`;
  function draw() {
    const set = rounds[M.r];
    $("[data-l]").innerHTML = shuffle(set).map(w => tile(w, "w")).join("");
    $("[data-r]").innerHTML = shuffle(set).map(w => tile(w, "m")).join("");
    $("[data-round]").textContent = `Ronde ${M.r + 1}/${rounds.length}`;
  }
  el.onclick = e => {
    const b = e.target.closest(".of-tile"); if (!b || b.disabled) return;
    if (!M.sel || M.sel.dataset.kind === b.dataset.kind) {   // first pick, or another pick in the same column
      M.sel?.classList.remove("sel"); M.sel = b; b.classList.add("sel");
      if (b.dataset.kind === "w") speak(b.textContent);
      return;
    }
    const a = M.sel; M.sel = null; a.classList.remove("sel");
    if (a.dataset.id === b.dataset.id) {
      [a, b].forEach(x => { x.classList.add("ok"); x.disabled = true; });
      M.done++; $("[data-prog]").style.width = (M.done / words.length * 100) + "%";
      if (![...el.querySelectorAll(".of-tile.w")].some(x => !x.disabled)) {
        M.r++;
        setTimeout(() => { if (M.r < rounds.length) draw(); else { clearInterval(timer); onDone({ ms: Date.now() - M.t0, errors: M.errors, wrong: M.wrong, words }); } }, 400);
      }
    } else {
      M.errors++;
      [a, b].forEach(x => { M.wrong.add(x.dataset.id); x.classList.add("no"); setTimeout(() => x.classList.remove("no"), 450); });
      $("[data-err]").textContent = `${M.errors} fout`;
    }
  };
  $("[data-q]").onclick = e => { e.stopPropagation(); clearInterval(timer); onQuit(); };
  draw();
  return { stop: () => clearInterval(timer) };
}
