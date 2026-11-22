// Günün NT2 bulmacası: a small Dutch crossword with Turkish clues, one per level (A1 / A2 / B1) per day,
// the same for everybody. The words come from our own word list (snapshot: kruiswoord-nt2.json).
// The grid builder is the Slimspel kruiswoord engine (slimspel/kruiswoord/engine.js), with own settings per level.
// Score = letters he typed himself in the words he found (letters filled by "İpucu" do not count), total = all letters.
// "Bitir" ends the puzzle early: the words not found are shown with their answer and give no points.
import { makePuzzle, seededRandom } from "../slimspel/kruiswoord/engine.js";
import { shareText, trDate } from "./share.js";
import { esc, fmt, today, loadLocal, saveLocal, dropOldProgress, savePlay, drawRanking, resetRanking, injectCss, flash, wordButton, bindWordInfo, wordInfoOf, tagSlot } from "./common.js";

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
.kw .kbd{position:absolute;left:50%;top:0;width:1px;height:1px;opacity:0;font-size:16px;border:0;padding:0;pointer-events:none}
.kw .curwrap{position:relative}
/* Phone, while playing: the site header no longer sticks to the top, so clue bar + grid + keyboard fit on one screen */
body.kw-focus .top,body.kw-focus #viewbar{position:static}
/* ... and the clue bar sticks to the top instead, the grid scrolls under it */
body.kw-focus .kw .curwrap{position:sticky;top:0;z-index:3;padding-top:4px;background:var(--ground,#F2F4F7)}
.kw .choice{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
.kw .list{list-style:none;padding:0;margin:12px 0 0;display:grid;gap:6px}
.kw .list li.miss{background:var(--og-bad-soft)}
.kw .list li{display:flex;justify-content:space-between;gap:10px;padding:6px 10px;border-radius:8px;background:var(--og-sunk)}
.kw .sq.miss{background:var(--og-bad-soft);color:var(--og-bad);border-color:var(--og-bad)}
.kw .cw.ro .sq.on{cursor:default}
.kw .cur{display:flex;align-items:center;gap:6px;margin:0 auto 8px;max-width:calc(var(--w,7) * 50px);background:color-mix(in srgb,var(--og-accent) 14%,var(--og-card));border:1px solid var(--og-accent);border-radius:10px;padding:6px}
.kw .cur .ct{flex:1;min-width:0;display:flex;flex-direction:column;gap:1px;font-size:15px;line-height:1.3}
.kw .cur .ct b{font-size:15px}
.kw .cur .nav{flex:none;width:42px;height:42px;border-radius:8px;border:1px solid var(--og-line);background:var(--og-card);color:var(--og-ink);font-size:18px;cursor:pointer}
.kw .todaypan{margin-top:18px}
.kw .legend{display:flex;gap:14px;flex-wrap:wrap;justify-content:center;margin:10px 0 0}`;


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
      <div data-r="todayBox"></div>
      <div class="grid2"><div class="pan" data-r="mine"></div><div class="pan" data-r="rank"></div></div>
    </section>
    <section data-r="play" hidden>
      <div class="bar"><span class="pill" data-r="what"></span><span class="pill" data-r="count"></span><span class="pill" data-r="clock">0:00</span></div>
      <div class="game">
        <div><div class="curwrap"><div class="cur" data-r="cur"></div><input class="kbd" data-r="kbd" autocomplete="off" autocapitalize="characters" autocorrect="off" spellcheck="false" lang="nl" aria-label="harf yaz"></div><div class="cw" data-r="cw"></div></div>
        <div class="clues">
          <h3>Yatay →</h3><ol data-r="cluesH"></ol>
          <h3>Dikey ↓</h3><ol data-r="cluesV"></ol>
          <div class="tools"><button class="bt" data-r="hint">İpucu</button><button class="bt" data-r="giveup">Bitir, cevapları göster</button><button class="bt" data-r="stop">← Geri</button></div>
        </div>
      </div>
    </section>
    <section data-r="done" hidden>
      <div class="pan">
        <div class="big" data-r="bigText">Çözdün!</div>
        <p class="sub" data-r="resultText"></p>
        <button class="bt" data-r="share2">📤 Paylaş</button>
        <div data-r="list"></div>
      </div>
      <div style="margin-top:14px"><button class="bt pri" data-r="change">Bugünün başka bir seviyesi</button></div>
      <div class="grid2"><div class="pan" data-r="mine2"></div><div class="pan" data-r="rank2"></div></div>
    </section>`;
  const $ = r => root.querySelector(`[data-r="${r}"]`);
  bindWordInfo(root, wordInfoOf);   // click on a word = word box (meaning, examples, where on the site)

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
    (att.wordHints || []).map((h, k) => att.missed?.[k] ? "⬛" : h ? "🟨" : "🟩").join("") + `\n${shareUrl}`;

  // My own numbers for this level: days solved, best time without hints
  function drawMine(el) {
    const mine = history.filter(h => h.test === level);
    const full = h => !(h.missed || []).some(Boolean);
    const clean = mine.filter(h => !h.hints && full(h)).map(h => h.time_s);
    el.innerHTML = `<h3>İstatistiklerin · ${LEVELS[level].title}</h3>` + (mine.length
      ? `<div class="stats"><div><b>${new Set(mine.filter(full).map(h => h.day)).size}</b><span>tam çözülen gün</span></div>
         <div><b>${clean.length ? fmt(Math.min(...clean)) : "-"}</b><span>en iyi süre (ipucusuz)</span></div>
         <div><b>${mine.reduce((n, h) => n + (h.hints || 0), 0)}</b><span>toplam ipucu</span></div></div>`
      : `<p class="small">Bu seviyede henüz bulmaca çözmedin.</p>`);
  }

  // The example sentence with the answer filled in. Where the sentence needs another form of the word
  // (moet, nieuwe, handen) the data has the correct full sentence in zf; filling in the answer would be wrong Dutch.
  const fullSentence = (ex, w) => {
    const s = ex.zf || ex.z.replace("___", w.toLowerCase());
    return s.charAt(0).toUpperCase() + s.slice(1);
  };
  // The puzzle's words with their meaning and example sentence (💡 = a hint letter was used in that word)
  // missed (optional): true per word that was not found when the player pressed "Bitir"; those come first
  const wordsHtml = (P, wordHints, missed = []) => P.words.map((x, k) => [x, k]).sort((a, b) => !!missed[b[1]] - !!missed[a[1]]).map(([x, k]) => `<li class="${missed[k] ? "miss" : ""}"><span>${wordButton(x.w.toLowerCase())}${missed[k] ? " ✗ bulamadın" : wordHints[k] ? " 💡" : ""}</span><span class="small" style="margin:0">${esc(x.c)}${sentenceOf(x)?.z ? `<br><i lang="nl">${esc(fullSentence(sentenceOf(x), x.w))}</i>` : ""} ${tagSlot(x.w.toLowerCase())}</span></li>`).join("");

  // The solved grid, read-only: green = found, grey italic = found with a hint letter, red = not found.
  // The attempt does not store the typed grid, so it is rebuilt from the solution and the per-word flags.
  function gridHtml(P, wordHints = [], missed = []) {
    const numAt = {};
    P.words.forEach(x => numAt[x.cells[0]] = x.num);
    const found = new Set(), hinted = new Set();
    P.words.forEach((x, k) => { if (!missed[k]) x.cells.forEach(i => { found.add(i); if (wordHints[k]) hinted.add(i); }); });
    return `<div class="cw ro" style="--w:${P.w}">${P.solution.map((ch, i) => ch
      ? `<div class="sq on ${found.has(i) ? "ok" : "miss"}${hinted.has(i) ? " hint" : ""}">${numAt[i] ? `<span class="n">${numAt[i]}</span>` : ""}<span class="l">${esc(ch)}</span></div>`
      : `<div class="sq"></div>`).join("")}</div>`;
  }
  // Grid + legend + word list for one finished attempt (start screen and finish screen use the same view)
  const resultHtml = (P, att) => {
    const wh = att.wordHints || P.words.map(() => false), ms = att.missed || [];
    return gridHtml(P, wh, ms)
      + `<p class="small legend"><span>🟩 buldun</span>${wh.some(Boolean) ? "<span>💡 ipucuyla</span>" : ""}${ms.some(Boolean) ? "<span>🟥 bulamadın</span>" : ""}</p>`
      + `<ul class="list">${wordsHtml(P, wh, ms)}</ul>`;
  };

  function drawSetup() {
    $("levels").innerHTML = Object.entries(LEVELS).map(([k, v]) =>
      `<button class="ch${k === level ? " on" : ""}" data-v="${k}">${v.title}${doneToday(k) ? " ✓" : ""}</button>`).join("");
    $("levels").querySelectorAll("button").forEach(b => b.onclick = () => { level = b.dataset.v; saveLocal(`${GAME}:level`, level); drawSetup(); });
    $("info").textContent = LEVELS[level].info;
    const done = doneToday(level);
    $("today").hidden = !done;
    const nMiss = (done?.missed || []).filter(Boolean).length;
    if (done) $("today").textContent = (nMiss ? `Bugün ${done.missed.length - nMiss} / ${done.missed.length} kelime buldun (${fmt(done.time_s)})` : `Bugün ${fmt(done.time_s)} içinde çözdün`) + `${done.hints ? ` (${done.hints} ipucu)` : ""}. Yarın yeni bulmaca var!`;
    $("share1").hidden = !done;
    if (done) $("share1").onclick = () => shareText($("share1"), textOf(done));
    $("go").disabled = !!done;
    $("go").textContent = loadLocal(progressKey(level), null) ? "Devam et" : "Başla";
    // After solving: today's grid and words of this level, open on the page (not folded away), so coming back
    // later still shows what was done. The daily puzzle is the same for everybody, so it can be made again.
    let box = "";
    if (done) try { box = `<div class="pan todaypan"><h3>Bugünkü bulmacan · ${LEVELS[level].title}</h3>${resultHtml(puzzleOf(today(), level), done)}</div>`; } catch {}
    $("todayBox").innerHTML = box;
    drawMine($("mine"));
    drawRanking($("rank"), { game: GAME, levels: RANK_LEVELS, user });
  }
  $("go").onclick = () => start();
  const show = s => {
    ["setup", "play", "done"].forEach(x => $(x).hidden = x !== s);
    document.body.classList.toggle("kw-focus", s === "play" && matchMedia("(max-width:700px)").matches);
    if (s === "play") fitGrid();
  };
  // Grid size on a phone: as wide as the screen allows, but small enough that clue bar + grid stay above the keyboard
  // (visualViewport is the part not covered by the on-screen keyboard)
  function fitGrid() {
    if (!S || $("play").hidden) return;
    const rows = Math.ceil(S.P.solution.length / S.P.w), vh = window.visualViewport?.height || innerHeight;
    const room = vh - ($("cur").offsetHeight || 70) - 70;            // 70px: level / word count / clock row and margins
    const byHeight = Math.max(170, room) * S.P.w / rows;
    // Never smaller than 34px a square (smaller is hard to read and to tap); a taller grid then scrolls under the clue bar
    const floor = S.P.w * 34 + (S.P.w - 1) * 3;
    $("cw").style.width = `min(100%, ${S.P.w * 50}px, ${Math.round(Math.max(floor, byHeight))}px)`;
  }
  window.visualViewport?.addEventListener("resize", () => { fitGrid(); keepInView(); });

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
      return `<li data-k="${k}"><span class="num">${x.num}</span><span class="txt">${esc(x.c)}${ex?.z ? `<span class="zin" lang="nl">${esc(ex.z)}${ex.zf ? ` <span class="zt">(cümlede çekimli hâli)</span>` : ""}</span>${ex.zt ? `<span class="zt">${esc(ex.zt)}</span>` : ""}` : ""}</span><span class="len">(${x.w.length})</span></li>`; };
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
  const focusKbd = () => { $("kbd").focus({ preventScroll: true }); keepInView(); };
  // Scroll only when the clue bar is hidden under the site header or sits in the lower half (where the phone keyboard opens)
  function keepInView() {
    const bar = $("cur"); if (!bar || !bar.offsetParent) return;
    const vh = window.visualViewport?.height || innerHeight;
    if (document.body.classList.contains("kw-focus")) {
      // Phone: the bar sticks at the top; make sure the selected square is between the bar and the keyboard
      const cell = $("cw").querySelector(".sq.sel"); if (!cell) return;
      const c = cell.getBoundingClientRect(), barBottom = bar.getBoundingClientRect().bottom;
      if (c.top < barBottom + 6) scrollBy({ top: c.top - barBottom - 10, behavior: "smooth" });
      else if (c.bottom > vh - 6) scrollBy({ top: c.bottom - vh + 14, behavior: "smooth" });
      return;
    }
    const top = document.querySelector(".top")?.getBoundingClientRect().bottom || 0, r = bar.getBoundingClientRect();
    // 44px: keeps the level, word count and clock row visible above the bar
    if (r.top < top + 30 || r.top > vh * 0.4) scrollBy({ top: r.top - top - 44, behavior: "smooth" });
  }

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
    drawCur();
    if (document.body.classList.contains("kw-focus")) keepInView();   // phone: follow the cursor while typing
  }
  // Bar above the grid: the clue of the word being typed (same text as in the list) and buttons to the previous/next open word
  function drawCur() {
    const x = S.P.words[S.word], ex = sentenceOf(x);
    $("cur").style.setProperty("--w", S.P.w);
    $("cur").innerHTML = `<button class="nav" data-r="prevW" aria-label="önceki kelime">‹</button>
      <span class="ct"><b>${x.num} ${x.dir === "H" ? "→" : "↓"} ${esc(x.c)} <span class="len">(${x.w.length})</span></b>${ex?.z ? `<span class="zin" lang="nl"><i>${esc(ex.z)}</i></span>` : ""}${ex?.zt ? `<span class="zt">${esc(ex.zt)}</span>` : ""}</span>
      <button class="nav" data-r="nextW" aria-label="sonraki kelime">›</button>`;
    $("prevW").onclick = () => stepWord(-1); $("nextW").onclick = () => stepWord(1);
  }
  // Next/previous word that is not found yet (wraps around); all found: just the next one
  function stepWord(d) {
    const n = S.P.words.length;
    for (let j = 1; j <= n; j++) { const k = (S.word + d * j + n * n) % n; if (!S.okWords.has(k) || j === n) { S.word = k; break; } }
    S.cell = firstOpen(S.word); draw(); focusKbd();
  }

  // A cell is locked once it is green (part of a found word) or was given as a hint: it can no longer be changed or erased
  const locked = i => S.hinted.has(i) || [...S.okWords].some(k => S.P.words[k].cells.includes(i));
  function type(ch) {
    if (!S || S.done) return;
    const cells = S.P.words[S.word].cells;
    let pos = cells.indexOf(S.cell);
    // Typing on a locked cell writes into the next open cell of the word instead
    while (locked(S.cell) && pos < cells.length - 1) S.cell = cells[++pos];
    if (!locked(S.cell)) S.grid[S.cell] = ch;
    // Move on to the next open cell (locked ones are skipped)
    let next = pos + 1;
    while (next < cells.length && locked(cells[next])) next++;
    if (next < cells.length) S.cell = cells[next];
    afterChange(next >= cells.length);   // jump to the next word only after its LAST open letter
  }
  function backspace() {
    if (!S || S.done) return;
    const cells = S.P.words[S.word].cells;
    let pos = cells.indexOf(S.cell);
    // Empty or locked cell: step back to the previous cell that can still be erased
    if (!S.grid[S.cell] || locked(S.cell)) {
      let prev = pos - 1;
      while (prev >= 0 && locked(cells[prev])) prev--;
      if (prev >= 0) S.cell = cells[prev];
    }
    if (!locked(S.cell)) S.grid[S.cell] = "";
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
    // Turkish keyboards: with capitals on, "i" gives "İ" (and there is "ı"): both are the Dutch letter I; é/ë -> E
    const ch = e.target.value.replace(/[İIıi]/g, "I").toUpperCase().normalize("NFD").replace(/[^A-Z]/g, "").slice(-1);
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
    else if (document.activeElement !== $("kbd") && /^[a-zA-Zİı]$/.test(e.key)) { type(e.key.replace(/[İı]/g, "I").toUpperCase()); focusKbd(); }
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
  // "Bitir": first click asks to confirm (the button text changes), the second ends the puzzle
  $("giveup").onclick = () => {
    if (!S || S.done) return;
    if ($("giveup").dataset.sure) return finish(true);
    $("giveup").dataset.sure = "1"; $("giveup").textContent = "Emin misin? Evet, bitir";
    setTimeout(() => { delete $("giveup").dataset.sure; $("giveup").textContent = "Bitir, cevapları göster"; }, 4000);
  };
  $("stop").onclick = () => { saveProgress(); clearInterval(S.timer); show("setup"); drawSetup(); };
  $("change").onclick = () => { show("setup"); drawSetup(); };

  function finish(gaveUp = false) {
    S.done = true; clearInterval(S.timer);
    const time_s = played(), hints = S.hinted.size, letters = S.P.solution.filter(Boolean).length;
    // Points: every letter of a found word that he typed himself. A crossing letter of a missed word still counts
    // when it belongs to a found word. Solved completely = all letters minus the hint letters, as before.
    const foundCells = new Set([...S.okWords].flatMap(k => S.P.words[k].cells));
    const score = [...foundCells].filter(i => !S.hinted.has(i)).length;
    saveLocal(progressKey(S.level), null);
    const wordHints = S.P.words.map(x => x.cells.some(i => S.hinted.has(i)));
    const missed = S.P.words.map((x, k) => !S.okWords.has(k));
    // answers: one per word (the admin sees which words needed a hint or were not found)
    const attempt = { test: S.level, day: S.day, score, total: letters, hints, time_s, wordHints,
                      ...(gaveUp ? { missed, gave_up: true } : {}),
                      answers: S.P.words.map((x, k) => ({ qid: x.w, chosen: missed[k] ? "" : x.w, correct: !missed[k] && !wordHints[k] })), finished_at: new Date().toISOString() };
    history.unshift({ ...attempt, module: MODULE });
    api.saveAttempt(user.uid, MODULE, attempt).catch(e => $("resultText").insertAdjacentHTML("afterend", `<p class="saveerr">Sonuç kaydedilemedi (${esc(e.code || "hata")}).</p>`));
    const posted = savePlay(user, profile, { game: GAME, level: S.level, day: S.day, score, total: letters, time_s }).catch(() => {});
    setTimeout(() => {
      show("done");
      $("bigText").textContent = gaveUp ? `${S.okWords.size} / ${S.P.words.length} kelime buldun` : "Çözdün!";
      $("resultText").textContent = `${LEVELS[S.level].title} · ${S.P.words.length} kelime · ${score}/${letters} puan · süre ${fmt(time_s)} · ` + (hints ? `${hints} ipucu` : "ipucusuz");
      $("share2").onclick = () => shareText($("share2"), textOf(attempt));
      // The words with their meaning, to learn them
      $("list").innerHTML = resultHtml(S.P, { wordHints, missed: gaveUp ? missed : [] });   // grid + words
      drawSetup();   // the start screen now shows today's words too
      drawMine($("mine2"));
      posted.then(() => { resetRanking($("rank2")); drawRanking($("rank2"), { game: GAME, levels: RANK_LEVELS, user }); });
    }, gaveUp ? 0 : 900);
  }

  if (location.hostname === "localhost") (window.__ogGames ||= {}).kruiswoord = () => S && { P: S.P };
  drawSetup();
}
