// Günün NT2 bulmacası: a small Dutch crossword with Turkish clues, one per level (A1 / A2 / B1) per day,
// the same for everybody. The words come from our own word list (snapshot: kruiswoord-nt2.json).
// The grid builder is the Slimspel kruiswoord engine (slimspel/kruiswoord/engine.js), with own settings per level.
// Score = letters he typed himself (letters filled by "İpucu" do not count), total = all letters.
import { makePuzzle, seededRandom } from "../../slimspel/kruiswoord/engine.js";
import { shareText, trDate } from "./share.js";
import { esc, fmt, today, loadLocal, saveLocal, dropOldProgress, savePlay, drawRanking, resetRanking, injectCss, flash } from "./common.js";

const GAME = "kruiswoord", MODULE = "oyun-kruiswoord";
// niv = which word levels may be used; count = words, maxLen = longest word, size = build space (cropped after)
// WARNING: changing these (or kruiswoord-nt2.json) changes the daily puzzles: only do it between days.
const LEVELS = {
  a1: { title: "A1", info: "6 kelime, kolay (A0–A1).", niv: ["A0", "A1"], cfg: { count: 6, maxLen: 7, size: 10 } },
  a2: { title: "A2", info: "7 kelime (A1–A2).", niv: ["A1", "A2"], cfg: { count: 7, maxLen: 8, size: 11 } },
  b1: { title: "B1", info: "8 kelime, daha uzun (A2–B1).", niv: ["A2", "B1"], cfg: { count: 8, maxLen: 9, size: 12 } }
};
const RANK_LEVELS = Object.fromEntries(Object.entries(LEVELS).map(([k, v]) => [k, v.title]));

const CSS = `
.kw .game{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:18px;align-items:start}
@media (max-width:700px){.kw .game{grid-template-columns:1fr}}
.kw .cw{--w:7;display:grid;grid-template-columns:repeat(var(--w),minmax(0,1fr));gap:3px;width:min(100%,calc(var(--w) * 50px));margin:0 auto}
.kw .sq{position:relative;aspect-ratio:1;border-radius:6px}
.kw .sq.on{background:var(--og-card);border:2px solid var(--og-ink);cursor:pointer;display:grid;place-items:center;font-family:var(--og-font);font-weight:700;font-size:clamp(15px,4vw,24px);color:#2f5bd3}
.kw .sq .n{position:absolute;top:1px;left:3px;font-size:10px;font-weight:600;color:var(--og-muted)}
.kw .sq.word{background:color-mix(in srgb,var(--og-accent) 22%,var(--og-card))}
.kw .sq.sel{background:var(--og-accent);color:var(--og-accent-ink)}
.kw .sq.sel .n{color:var(--og-accent-ink)}
.kw .sq.ok{background:var(--og-ok-soft);color:var(--og-ok);border-color:var(--og-ok)}
.kw .sq.hint{color:var(--og-muted);font-style:italic}
@keyframes kw-good{0%,60%{background:var(--og-ok);color:#fff}100%{}}
.kw .sq.flashgood{animation:kw-good 1s ease-out}
@media (prefers-reduced-motion: reduce){.kw .sq.flashgood{animation:none}}
.kw .clues h3{font-family:var(--og-font);font-size:16px;margin:4px 0 6px}
.kw .clues ol{list-style:none;margin:0 0 14px;padding:0;display:grid;gap:6px}
.kw .clues li{display:flex;gap:10px;align-items:center;background:var(--og-card);border:1px solid var(--og-line);border-radius:8px;padding:6px 10px;cursor:pointer}
.kw .clues li.act{border-color:var(--og-accent);background:color-mix(in srgb,var(--og-accent) 14%,var(--og-card))}
.kw .clues li.done{color:var(--og-muted);text-decoration:line-through;background:var(--og-ok-soft);border-color:var(--og-ok-soft)}
.kw .clues .num{font-weight:700;min-width:20px}
.kw .clues .len{color:var(--og-muted);font-size:13px;white-space:nowrap}
.kw .clues .txt{flex:1;display:flex;flex-direction:column;gap:1px}
.kw .clues .zin{font-style:italic;font-size:14.5px}
.kw .clues .zt{font-size:12.5px;color:var(--og-muted)}
.kw .clues li.done .zin,.kw .clues li.done .zt{display:none}
.kw .tools{display:flex;gap:10px;flex-wrap:wrap}
.kw .kbd{position:fixed;left:-200px;top:0;width:40px;height:20px;opacity:0}
.kw .choice{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
.kw .list{list-style:none;padding:0;margin:12px 0 0;display:grid;gap:6px}
.kw .list li{display:flex;justify-content:space-between;gap:10px;padding:6px 10px;border-radius:8px;background:var(--og-sunk)}`;

export async function mountKruiswoord(root, { user, profile, api, shareUrl = location.href }) {
  injectCss(CSS, "og-kw-css");
  root.classList.add("og", "kw");
  root.innerHTML = `
    <section data-r="setup">
      <h2 class="ot">Günün NT2 bulmacası</h2>
      <p class="sub">Hollandaca kelimeleri Türkçe ipuçlarıyla bul. Bir kareye tıkla ve yaz; aynı kareye tekrar tıklarsan yön değişir.
        Her gün her seviye için bir bulmaca var, herkes için aynı.</p>
      <div class="choice" data-r="levels"></div>
      <p class="sub" data-r="info"></p>
      <p class="today" data-r="today" hidden></p>
      <button class="bt" data-r="share1" hidden>📤 Paylaş</button>
      <div style="margin-top:14px"><button class="bt pri" data-r="go">Başla</button></div>
      <div class="grid2"><div class="pan" data-r="mine"></div><div class="pan" data-r="rank"></div></div>
    </section>
    <section data-r="play" hidden>
      <div class="bar"><span class="pill" data-r="what"></span><span class="pill" data-r="count"></span><span class="pill" data-r="clock">0:00</span></div>
      <div class="game">
        <div><div class="cw" data-r="cw"></div></div>
        <div class="clues">
          <h3>Yatay →</h3><ol data-r="cluesH"></ol>
          <h3>Dikey ↓</h3><ol data-r="cluesV"></ol>
          <div class="tools"><button class="bt" data-r="hint">İpucu</button><button class="bt" data-r="stop">← Geri</button></div>
        </div>
      </div>
      <input class="kbd" data-r="kbd" autocomplete="off" autocapitalize="characters" spellcheck="false" aria-label="harf yaz">
    </section>
    <section data-r="done" hidden>
      <div class="pan">
        <div class="big">Çözdün!</div>
        <p class="sub" data-r="resultText"></p>
        <button class="bt" data-r="share2">📤 Paylaş</button>
        <ul class="list" data-r="list"></ul>
      </div>
      <div style="margin-top:14px"><button class="bt pri" data-r="change">Bugünün başka bir seviyesi</button></div>
      <div class="grid2"><div class="pan" data-r="mine2"></div><div class="pan" data-r="rank2"></div></div>
    </section>`;
  const $ = r => root.querySelector(`[data-r="${r}"]`);

  let bank;
  try { bank = await fetch(new URL("./kruiswoord-nt2.json", import.meta.url), { cache: "no-cache" }).then(r => r.json()); }
  catch { root.innerHTML = `<p class="notice">Kelimeler yüklenemedi. Sayfayı yenile.</p>`; return; }
  let history = [];
  try { history = (await api.loadAttempts(user.uid, MODULE)).filter(h => h.day); } catch {}
  dropOldProgress(GAME);
  let level = loadLocal(`${GAME}:level`, "a1");
  if (!LEVELS[level]) level = "a1";
  let S = null;
  const doneToday = lv => history.find(h => h.test === lv && h.day === today());
  const progressKey = lv => `${GAME}:progress:${lv}:${today()}`;
  // Example sentences live in the snapshot next to each word (z, zt); the puzzle engine only passes w and c on
  const SENT = new Map(bank.words.map(x => [x.w + "|" + x.c, x]));
  const sentenceOf = x => SENT.get(x.w + "|" + x.c);
  const puzzleOf = (day, lv) => makePuzzle(LEVELS[lv].cfg, { words: bank.words.filter(x => LEVELS[lv].niv.includes(x.n)) },
    seededRandom(`${day}|kruiswoord-nt2|${lv}`));

  // Share: one square per word, 🟩 = typed himself, 🟨 = with a hint letter
  const textOf = att => `NT2 Bulmaca ${LEVELS[att.test].title} · ${trDate(att.day)} · ${fmt(att.time_s)}${att.hints ? "" : " · ipucusuz"}\n` +
    (att.wordHints || []).map(h => h ? "🟨" : "🟩").join("") + `\n${shareUrl}`;

  // My own numbers for this level: days solved, best time without hints
  function drawMine(el) {
    const mine = history.filter(h => h.test === level);
    const clean = mine.filter(h => !h.hints).map(h => h.time_s);
    el.innerHTML = `<h3>İstatistiklerin · ${LEVELS[level].title}</h3>` + (mine.length
      ? `<div class="stats"><div><b>${new Set(mine.map(h => h.day)).size}</b><span>çözülen gün</span></div>
         <div><b>${clean.length ? fmt(Math.min(...clean)) : "-"}</b><span>en iyi süre (ipucusuz)</span></div>
         <div><b>${mine.reduce((n, h) => n + (h.hints || 0), 0)}</b><span>toplam ipucu</span></div></div>`
      : `<p class="small">Bu seviyede henüz bulmaca çözmedin.</p>`);
  }

  function drawSetup() {
    $("levels").innerHTML = Object.entries(LEVELS).map(([k, v]) =>
      `<button class="ch${k === level ? " on" : ""}" data-v="${k}">${v.title}${doneToday(k) ? " ✓" : ""}</button>`).join("");
    $("levels").querySelectorAll("button").forEach(b => b.onclick = () => { level = b.dataset.v; saveLocal(`${GAME}:level`, level); drawSetup(); });
    $("info").textContent = LEVELS[level].info;
    const done = doneToday(level);
    $("today").hidden = !done;
    if (done) $("today").textContent = `Bugün ${fmt(done.time_s)} içinde çözdün${done.hints ? ` (${done.hints} ipucu)` : ""}. Yarın yeni bulmaca var!`;
    $("share1").hidden = !done;
    if (done) $("share1").onclick = () => shareText($("share1"), textOf(done));
    $("go").disabled = !!done;
    $("go").textContent = loadLocal(progressKey(level), null) ? "Devam et" : "Başla";
    drawMine($("mine"));
    drawRanking($("rank"), { game: GAME, levels: RANK_LEVELS, user });
  }
  $("go").onclick = () => start();
  const show = s => ["setup", "play", "done"].forEach(x => $(x).hidden = x !== s);

  function start() {
    if (doneToday(level)) return drawSetup();
    const day = today(), P = puzzleOf(day, level), saved = loadLocal(progressKey(level), null);
    S = { day, level, P, done: false,
          grid: saved?.grid?.length === P.solution.length ? saved.grid : P.solution.map(() => ""),
          hinted: new Set(saved?.hinted || []), elapsed: saved?.elapsed || 0, resumedAt: Date.now(),
          word: 0, cell: P.words[0].cells[0] };
    S.okWords = new Set(P.words.map((w, k) => k).filter(isRight));
    clearInterval(S.timer); S.timer = setInterval(tick, 500); tick();
    $("what").textContent = LEVELS[level].title;
    $("cw").style.setProperty("--w", P.w);
    const numAt = {};
    P.words.forEach(x => numAt[x.cells[0]] = x.num);
    $("cw").innerHTML = P.solution.map((ch, i) => ch
      ? `<div class="sq on" data-i="${i}">${numAt[i] ? `<span class="n">${numAt[i]}</span>` : ""}<span class="l"></span></div>`
      : `<div class="sq"></div>`).join("");
    $("cw").querySelectorAll(".sq.on").forEach(el => el.onclick = () => pickCell(Number(el.dataset.i)));
    // Clue = Turkish meaning + a Dutch example sentence with the answer blanked (and its Turkish), when the word list has one
    const li = (x, k) => { const ex = sentenceOf(x);
      return `<li data-k="${k}"><span class="num">${x.num}</span><span class="txt">${esc(x.c)}${ex?.z ? `<span class="zin" lang="nl">${esc(ex.z)}</span>${ex.zt ? `<span class="zt">${esc(ex.zt)}</span>` : ""}` : ""}</span><span class="len">(${x.w.length})</span></li>`; };
    $("cluesH").innerHTML = P.words.map((x, k) => x.dir === "H" ? li(x, k) : "").join("");
    $("cluesV").innerHTML = P.words.map((x, k) => x.dir === "V" ? li(x, k) : "").join("");
    root.querySelectorAll(".clues li").forEach(el => el.onclick = () => { S.word = Number(el.dataset.k); S.cell = firstOpen(S.word); draw(); focusKbd(); });
    show("play");
    hintLabel();
    draw();
    focusKbd();
  }
  const played = () => S.elapsed + Math.floor((Date.now() - S.resumedAt) / 1000);
  function tick() { $("clock").textContent = fmt(played()); }
  function saveProgress() { if (S && !S.done) saveLocal(progressKey(S.level), { grid: S.grid, hinted: [...S.hinted], elapsed: played() }); }
  addEventListener("pagehide", saveProgress);
  document.addEventListener("visibilitychange", () => { if (document.hidden) saveProgress(); });

  const isRight = k => S.P.words[k].cells.every(i => S.grid[i] === S.P.solution[i]);
  const wordsAt = i => S.P.words.map((w, k) => k).filter(k => S.P.words[k].cells.includes(i));
  const firstOpen = k => S.P.words[k].cells.find(i => !S.grid[i]) ?? S.P.words[k].cells[0];
  // Clicking the selected cell again switches across <-> down where two words cross
  function pickCell(i) {
    const ws = wordsAt(i);
    if (i === S.cell && ws.length > 1) S.word = ws.find(k => k !== S.word) ?? ws[0];
    else if (!ws.includes(S.word)) S.word = ws[0];
    S.cell = i; draw(); focusKbd();
  }
  const focusKbd = () => $("kbd").focus({ preventScroll: true });

  function draw() {
    const active = new Set(S.P.words[S.word].cells);
    const okCells = new Set([...S.okWords].flatMap(k => S.P.words[k].cells));
    $("cw").querySelectorAll(".sq.on").forEach(el => {
      const i = Number(el.dataset.i);
      el.querySelector(".l").textContent = S.grid[i];
      el.classList.toggle("ok", okCells.has(i));
      el.classList.toggle("word", active.has(i) && !okCells.has(i));
      el.classList.toggle("sel", i === S.cell);
      el.classList.toggle("hint", S.hinted.has(i));
    });
    root.querySelectorAll(".clues li").forEach(el => {
      const k = Number(el.dataset.k);
      el.classList.toggle("act", k === S.word);
      el.classList.toggle("done", S.okWords.has(k));
    });
    $("count").textContent = `${S.okWords.size} / ${S.P.words.length} kelime`;
  }

  function type(ch) {
    if (!S || S.done) return;
    if (!S.hinted.has(S.cell)) S.grid[S.cell] = ch;
    const cells = S.P.words[S.word].cells, pos = cells.indexOf(S.cell);
    if (pos < cells.length - 1) S.cell = cells[pos + 1];
    afterChange(pos === cells.length - 1);   // jump to the next word only after its LAST letter
  }
  function backspace() {
    if (!S || S.done) return;
    const cells = S.P.words[S.word].cells, pos = cells.indexOf(S.cell);
    if ((!S.grid[S.cell] || S.hinted.has(S.cell)) && pos > 0) S.cell = cells[pos - 1];
    if (!S.hinted.has(S.cell)) S.grid[S.cell] = "";
    afterChange();
  }
  function afterChange(mayJump = false) {
    const before = S.okWords;
    S.okWords = new Set(S.P.words.map((w, k) => k).filter(isRight));
    draw();
    for (const k of S.okWords) if (!before.has(k)) {
      S.P.words[k].cells.forEach(i => flash($("cw").querySelector(`[data-i="${i}"]`), "flashgood"));
      const next = S.P.words.findIndex((w, j) => !S.okWords.has(j));
      if (mayJump && k === S.word && next >= 0) { S.word = next; S.cell = firstOpen(next); draw(); }
    }
    saveProgress();
    if (S.okWords.size === S.P.words.length) finish();
  }
  function move(dr, dc) {
    const { w, h, solution } = S.P;
    let r = Math.floor(S.cell / w) + dr, c = S.cell % w + dc;
    while (r >= 0 && c >= 0 && r < h && c < w) {
      const i = r * w + c;
      if (solution[i]) {
        const ws = wordsAt(i), want = dr ? "V" : "H";
        S.word = ws.find(k => S.P.words[k].dir === want) ?? ws[0];
        S.cell = i; draw(); return;
      }
      r += dr; c += dc;
    }
  }
  // Letters come in through the hidden input (also brings up tablet keyboards)
  $("kbd").addEventListener("input", e => {
    const ch = e.target.value.toUpperCase().replace(/[^A-Z]/g, "").slice(-1);
    e.target.value = "";
    if (ch) type(ch);
  });
  // Keys only when this game is on screen (other games sit in hidden tabs of the same page)
  document.addEventListener("keydown", e => {
    if (!S || S.done || $("play").hidden || !root.offsetParent || e.ctrlKey || e.metaKey || e.altKey) return;
    if (e.key === "Backspace") { e.preventDefault(); backspace(); }
    else if (e.key === "ArrowRight") { e.preventDefault(); move(0, 1); }
    else if (e.key === "ArrowLeft") { e.preventDefault(); move(0, -1); }
    else if (e.key === "ArrowDown") { e.preventDefault(); move(1, 0); }
    else if (e.key === "ArrowUp") { e.preventDefault(); move(-1, 0); }
    else if (e.key === "Enter" || e.key === "Tab") {
      e.preventDefault();
      const n = S.P.words.length, next = [...Array(n).keys()].map(j => (S.word + 1 + j) % n).find(j => !S.okWords.has(j));
      if (next !== undefined) { S.word = next; S.cell = firstOpen(next); draw(); }
    }
    else if (document.activeElement !== $("kbd") && /^[a-zA-Z]$/.test(e.key)) { type(e.key.toUpperCase()); focusKbd(); }
  });
  // Hint: fills one letter (the selected cell if wrong/empty, else the first wrong cell of the word, else anywhere)
  // At most 3 hint letters per puzzle: with unlimited hints the daily puzzle (and the ranking) means nothing
  const MAX_HINTS = 3;
  function hintLabel() {
    const left = Math.max(0, MAX_HINTS - S.hinted.size);
    $("hint").textContent = `İpucu (${left} kaldı)`;
    $("hint").disabled = left === 0;
  }
  $("hint").onclick = () => {
    if (!S || S.done || S.hinted.size >= MAX_HINTS) return;
    const wrong = i => S.grid[i] !== S.P.solution[i];
    let i = wrong(S.cell) ? S.cell : S.P.words[S.word].cells.find(wrong);
    if (i === undefined) i = S.P.solution.findIndex((ch, j) => ch && wrong(j));
    if (i < 0) return;
    S.grid[i] = S.P.solution[i]; S.hinted.add(i); S.cell = i; hintLabel();
    afterChange(); focusKbd();
  };
  $("stop").onclick = () => { saveProgress(); clearInterval(S.timer); show("setup"); drawSetup(); };
  $("change").onclick = () => { show("setup"); drawSetup(); };

  function finish() {
    S.done = true; clearInterval(S.timer);
    const time_s = played(), hints = S.hinted.size, letters = S.P.solution.filter(Boolean).length;
    const score = Math.max(0, letters - hints);
    saveLocal(progressKey(S.level), null);
    const wordHints = S.P.words.map(x => x.cells.some(i => S.hinted.has(i)));
    // answers: one per word (the admin sees which words needed a hint)
    const attempt = { test: S.level, day: S.day, score, total: letters, hints, time_s, wordHints,
                      answers: S.P.words.map((x, k) => ({ qid: x.w, chosen: x.w, correct: !wordHints[k] })), finished_at: new Date().toISOString() };
    history.unshift({ ...attempt, module: MODULE });
    api.saveAttempt(user.uid, MODULE, attempt).catch(e => $("resultText").insertAdjacentHTML("afterend", `<p class="saveerr">Sonuç kaydedilemedi (${esc(e.code || "hata")}).</p>`));
    const posted = savePlay(user, profile, { game: GAME, level: S.level, day: S.day, score, total: letters, time_s }).catch(() => {});
    setTimeout(() => {
      show("done");
      $("resultText").textContent = `${LEVELS[S.level].title} · ${S.P.words.length} kelime · süre ${fmt(time_s)} · ` + (hints ? `${hints} ipucu` : "ipucusuz");
      $("share2").onclick = () => shareText($("share2"), textOf(attempt));
      // The words with their meaning, to learn them
      $("list").innerHTML = S.P.words.map((x, k) => `<li><span><b>${esc(x.w.toLowerCase())}</b>${wordHints[k] ? " 💡" : ""}</span><span class="small" style="margin:0">${esc(x.c)}${sentenceOf(x)?.z ? `<br><i lang="nl">${esc(sentenceOf(x).z.replace("___", x.w.toLowerCase()))}</i>` : ""}</span></li>`).join("");
      drawMine($("mine2"));
      posted.then(() => { resetRanking($("rank2")); drawRanking($("rank2"), { game: GAME, levels: RANK_LEVELS, user }); });
    }, 900);
  }

  if (location.hostname === "localhost") (window.__ogGames ||= {}).kruiswoord = () => S && { P: S.P };
  drawSetup();
}
