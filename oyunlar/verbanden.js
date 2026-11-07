// Günün bağlantıları (like "Connections"): 16 Dutch words, find the 4 groups of 4. 4 mistakes allowed.
// Every day one group of each difficulty (1 easy … 4 tricky), the same for everybody.
// Groups are hand-written in verbanden.json. Groups that could be confused never meet on the same day:
//   - k (kinds): two groups that share a kind are never together (e.g. two animal groups),
//   - x: kinds a group must not meet (its words could seem to fit there),
//   - r: a rule the code can check (het, -je, ui, ij, oo, 3 letters): no other word that day may fit it.
// Score: 3 points per group found + 1 per mistake left (max 16).
import { shareText, trDate } from "./share.js";
import { esc, fmt, today, hash, loadLocal, saveLocal, dropOldProgress, savePlay, drawRanking, resetRanking, drawStats, injectCss, flash } from "./common.js";

const GAME = "verbanden", MODULE = "oyun-verbanden", LEVEL = "dag", LIVES = 4;
const COLORS = { 1: "#f4d35e", 2: "#7cc47f", 3: "#6fa8dc", 4: "#b48ad6" };   // easy → tricky
const SQUARE = { 1: "🟨", 2: "🟩", 3: "🟦", 4: "🟪" };
const CSS = `
.vb .grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin-top:10px}
.vb .tile{font:inherit;font-family:var(--og-font);font-weight:700;font-size:clamp(13px,3.6vw,18px);min-height:62px;padding:6px 4px;border-radius:10px;
  border:0;background:var(--og-sunk);color:var(--og-ink);cursor:pointer;overflow-wrap:anywhere;text-transform:uppercase;letter-spacing:.02em}
.vb .tile.on{background:#5a5f73;color:#fff}
.vb .found{border-radius:10px;padding:10px 12px;margin-top:8px;text-align:center;color:#1d2a4d}
.vb .found b{display:block;font-family:var(--og-font);font-size:15px;text-transform:uppercase;letter-spacing:.04em}
.vb .found span{font-size:15px}
.vb .lives{display:flex;gap:6px;align-items:center;justify-content:center;margin:14px 0 6px;color:var(--og-muted);font-size:14px}
.vb .lives i{width:12px;height:12px;border-radius:50%;background:#5a5f73}.vb .lives i.gone{background:var(--og-line)}
.vb .msg{text-align:center;min-height:1.5em;font-weight:600;color:var(--og-bad)}
.vb .acts{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:8px}
.vb .list{margin-top:12px;display:grid;gap:10px}
.vb .list .g{border-radius:10px;padding:10px 12px}
.vb .list .g h4{margin:0 0 6px;font-family:var(--og-font);font-size:15px;color:#1d2a4d}
.vb .list .g ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:4px 12px;font-size:14px;color:#1d2a4d}
@media (max-width:520px){.vb .list .g ul{grid-template-columns:1fr}}
.og details.tbox{margin-top:18px;background:var(--og-card);border:1px solid var(--og-line);border-radius:10px;padding:0 18px}
.og details.tbox>summary{cursor:pointer;font-family:var(--og-font);font-weight:600;font-size:17px;padding:14px 0;list-style-position:inside}
.og details.tbox[open]>summary{border-bottom:1px solid var(--og-line);margin-bottom:10px}
.og details.tbox>div{padding-bottom:16px}`;
// Collapsible box with today's answers on the start screen (after playing), to learn from them
const todayBox = inner => `<details class="tbox"><summary>Bugünkü cevapların</summary><div>${inner}</div></details>`;


// Small seeded random from a text (same text → same numbers), for the daily choice
function rng(seed) {
  let a = hash(seed);
  return () => { a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
}
const bare = nl => nl.replace(/^(de|het) /, "");
const RULES = {
  het: w => w.nl.startsWith("het "),
  je: w => bare(w.nl).toLowerCase().endsWith("je"),
  ui: w => bare(w.nl).toLowerCase().includes("ui"),
  ij: w => bare(w.nl).toLowerCase().includes("ij"),
  oo: w => bare(w.nl).toLowerCase().includes("oo"),
  len3: w => [...bare(w.nl)].length === 3
};
// Can these 4 groups be on the same day without two right answers?
export function fitsTogether(gs) {
  for (const a of gs) for (const b of gs) {
    if (a === b) continue;
    if (a.k.some(k => b.k.includes(k)) || a.x.some(k => b.k.includes(k))) return false;
    if (a.r && b.w.some(RULES[a.r])) return false;
  }
  return true;
}
// Today's 4 groups: one of each difficulty, picked with the day as seed
export function dailyGroups(groups, day) {
  const rnd = rng(`${day}|verbanden`);
  for (let t = 0; t < 2000; t++) {
    const pick = [1, 2, 3, 4].map(d => { const c = groups.filter(g => g.d === d); return c[Math.floor(rnd() * c.length)]; });
    if (fitsTogether(pick)) return pick;
  }
  throw new Error("no puzzle possible");
}

export async function mountVerbanden(root, { user, profile, api, shareUrl = location.href }) {
  injectCss(CSS, "og-vb-css");
  root.classList.add("og", "vb");
  root.innerHTML = `
    <section data-r="setup">
      <h2 class="ot">Günün bağlantıları</h2>
      <p class="sub">16 Hollandaca kelime var. Bunları 4'erli 4 gruba ayır: 4 kelime seç ve <b>Kontrol et</b>'e bas.
        4 yanlış hakkın var. Gruplar kolaydan (sarı) zora (mor) doğru gider; bazıları anlamla, bazıları yazılışla ilgilidir.
        Her gün yeni bulmaca, herkes için aynı.</p>
      <p class="today" data-r="today" hidden></p>
      <button class="bt" data-r="share1" hidden>📤 Paylaş</button>
      <div style="margin-top:14px"><button class="bt pri" data-r="go">Başla</button></div>
      <div data-r="todayBox"></div>
      <div class="grid2"><div class="pan" data-r="stats"></div><div class="pan" data-r="rank"></div></div>
    </section>
    <section data-r="play" hidden>
      <div class="bar"><span class="pill" data-r="count"></span><span class="pill" data-r="clock">0:00</span></div>
      <div data-r="foundBox"></div>
      <div class="grid" data-r="grid"></div>
      <div class="lives" data-r="lives"></div>
      <div class="msg" data-r="msg"></div>
      <div class="acts"><button class="bt" data-r="shuffle">Karıştır</button><button class="bt" data-r="clear">Seçimi kaldır</button>
        <button class="bt pri" data-r="check" disabled>Kontrol et</button></div>
    </section>
    <section data-r="done" hidden>
      <div class="pan">
        <div class="big" data-r="result"></div>
        <p class="sub" data-r="resultText"></p>
        <button class="bt" data-r="share2">📤 Paylaş</button>
        <div class="list" data-r="list"></div>
      </div>
      <div class="grid2"><div class="pan" data-r="stats2"></div><div class="pan" data-r="rank2"></div></div>
    </section>`;
  const $ = r => root.querySelector(`[data-r="${r}"]`);

  let groups;
  try { groups = (await fetch(new URL("./verbanden.json", import.meta.url)).then(r => r.json())).groups; }
  catch { root.innerHTML = `<p class="notice">Kelimeler yüklenemedi. Sayfayı yenile.</p>`; return; }
  let history = [];
  try { history = (await api.loadAttempts(user.uid, MODULE)).filter(h => h.day); } catch {}
  dropOldProgress(GAME);
  const progressKey = () => `${GAME}:progress:${today()}`;
  const playedToday = () => history.find(h => h.day === today());
  let S = null;

  // Share: one row per guess, a square in the colour of each chosen word's group (like the original game)
  const textOf = att => `Bağlantılar · ${trDate(att.day)} · ${att.found}/4 grup${att.mistakes ? ` · ${att.mistakes} hata` : " · hatasız"}\n` +
    (att.rows || []).map(r => [...r].map(d => SQUARE[d]).join("")).join("\n") + `\n${shareUrl}`;

  // All groups of the day with the meaning of every word; ✓ found, ✗ not found
  const groupsHtml = (gs, found) => gs.map((g, gi) => `<div class="g" style="background:${COLORS[g.d]}"><h4>${found.includes(gi) ? "✓" : "✗"} ${esc(g.t)}</h4>
        <ul>${g.w.map(w => `<li><b>${esc(w.nl)}</b> = ${esc(w.tr)}</li>`).join("")}</ul></div>`).join("");

  function drawSetup() {
    const done = playedToday();
    $("today").hidden = !done;
    if (done) $("today").textContent = `Bugün ${done.found}/4 grup buldun (${done.score}/${done.total} puan). Yarın yeni bulmaca var!`;
    $("share1").hidden = !(done && done.rows);
    if (done) $("share1").onclick = () => shareText($("share1"), textOf(done));
    $("go").disabled = !!done;
    $("go").textContent = loadLocal(progressKey(), null) ? "Devam et" : "Başla";
    // After playing: today's groups again (the same for everybody, so they can be made again); found = answers marked correct
    let box = "";
    if (done?.answers?.length) try {
      const gs = dailyGroups(groups, today());
      box = todayBox(`<div class="list">${groupsHtml(gs, gs.map((g, gi) => done.answers.find(a => a.qid === g.t)?.correct ? gi : -1))}</div>`);
    } catch {}
    $("todayBox").innerHTML = box;
    drawStats($("stats"), history);
    drawRanking($("rank"), { game: GAME, levels: { dag: "" }, user });
  }
  $("go").onclick = () => start();
  const show = s => ["setup", "play", "done"].forEach(x => $(x).hidden = x !== s);

  function start() {
    if (playedToday()) return drawSetup();
    const day = today(), gs = dailyGroups(groups, day), saved = loadLocal(progressKey(), null);
    // Every word knows its group (index 0-3); the order on screen is random for each player
    const words = gs.flatMap((g, gi) => g.w.map(w => ({ nl: w.nl, word: bare(w.nl), gi })));
    S = { day, gs, words, order: saved?.order || shuffle(words.map((_, i) => i)), found: saved?.found || [],
          mistakes: saved?.mistakes || 0, rows: saved?.rows || [], tried: saved?.tried || [], sel: new Set(),
          elapsed: saved?.elapsed || 0, resumedAt: Date.now(), done: false };
    clearInterval(S.timer); S.timer = setInterval(tick, 500); tick();
    show("play"); draw();
  }
  function shuffle(a) { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
  const played = () => S.elapsed + Math.floor((Date.now() - S.resumedAt) / 1000);
  function tick() { $("clock").textContent = fmt(played()); }
  const saveProgress = () => S && !S.done && saveLocal(progressKey(), { order: S.order, found: S.found, mistakes: S.mistakes, rows: S.rows, tried: S.tried, elapsed: played() });

  const foundHtml = gi => { const g = S.gs[gi];
    return `<div class="found" style="background:${COLORS[g.d]}"><b>${esc(g.t)}</b><span>${g.w.map(w => esc(bare(w.nl))).join(", ")}</span></div>`; };
  function draw() {
    $("foundBox").innerHTML = S.found.map(foundHtml).join("");
    const left = S.order.filter(i => !S.found.includes(S.words[i].gi));
    $("grid").innerHTML = left.map(i => `<button class="tile${S.sel.has(i) ? " on" : ""}" data-i="${i}">${esc(S.words[i].word)}</button>`).join("");
    $("grid").querySelectorAll(".tile").forEach(b => b.onclick = () => toggle(Number(b.dataset.i)));
    $("lives").innerHTML = `Kalan hak: ${[...Array(LIVES)].map((_, k) => `<i class="${k < LIVES - S.mistakes ? "" : "gone"}"></i>`).join("")}`;
    $("count").textContent = `${S.found.length} / 4 grup`;
    $("check").disabled = S.sel.size !== 4;
  }
  function toggle(i) {
    if (S.done) return;
    if (S.sel.has(i)) S.sel.delete(i); else if (S.sel.size < 4) S.sel.add(i);
    $("msg").textContent = ""; draw();
  }
  $("shuffle").onclick = () => { if (!S) return; const left = S.order.filter(i => !S.found.includes(S.words[i].gi)); shuffle(left);
    S.order = [...S.order.filter(i => S.found.includes(S.words[i].gi)), ...left]; draw(); saveProgress(); };
  $("clear").onclick = () => { if (!S) return; S.sel.clear(); $("msg").textContent = ""; draw(); };
  $("check").onclick = () => {
    if (!S || S.done || S.sel.size !== 4) return;
    const pick = [...S.sel], key = pick.slice().sort((a, b) => a - b).join(",");
    if (S.tried.includes(key)) { $("msg").textContent = "Bunu zaten denedin."; return; }   // the same wrong guess costs nothing twice
    S.tried.push(key);
    S.rows.push(pick.map(i => S.gs[S.words[i].gi].d).join(""));
    const count = {}; pick.forEach(i => count[S.words[i].gi] = (count[S.words[i].gi] || 0) + 1);
    const best = Math.max(...Object.values(count));
    if (best === 4) {
      S.found.push(S.words[pick[0]].gi); S.sel.clear(); $("msg").textContent = "";
      draw(); flash($("foundBox").lastElementChild, "pop");
      if (S.found.length === 4) return finish();
    } else {
      S.mistakes++;
      $("msg").textContent = best === 3 ? "Bir kelime eksik!" : "Olmadı.";
      flash($("grid"), "shake"); draw();
      if (S.mistakes >= LIVES) return finish();
    }
    saveProgress();
  };

  function finish() {
    S.done = true; clearInterval(S.timer);
    const found = S.found.length, score = found * 3 + (LIVES - S.mistakes), total = 4 * 3 + LIVES, time_s = played(), day = today();
    saveLocal(progressKey(), null);
    const attempt = { test: LEVEL, day, score, total, time_s, found, mistakes: S.mistakes, rows: S.rows, finished_at: new Date().toISOString(),
                      answers: S.gs.map((g, gi) => ({ qid: g.t, chosen: g.w.map(w => bare(w.nl)).join(","), correct: S.found.includes(gi) })) };
    history.unshift({ ...attempt, module: MODULE });
    api.saveAttempt(user.uid, MODULE, attempt).catch(e => $("resultText").insertAdjacentHTML("afterend", `<p class="saveerr">Sonuç kaydedilemedi (${esc(e.code || "hata")}).</p>`));
    const posted = savePlay(user, profile, { game: GAME, level: LEVEL, day, score, total, time_s }).catch(() => {});
    setTimeout(() => {
      show("done");
      $("result").textContent = found === 4 ? (S.mistakes ? "Hepsini buldun!" : "Hatasız!") : "Yarın yeniden dene!";
      $("resultText").textContent = `${found}/4 grup · ${S.mistakes} hata · ${score}/${total} puan · süre ${fmt(time_s)}`;
      $("share2").onclick = () => shareText($("share2"), textOf(attempt));
      // All groups with the meaning of every word (nouns with de/het), to learn them
      $("list").innerHTML = groupsHtml(S.gs, S.found);
      drawSetup();   // the start screen now shows today's groups too
      drawStats($("stats2"), history);
      posted.then(() => { resetRanking($("rank2")); drawRanking($("rank2"), { game: GAME, levels: { dag: "" }, user }); });
    }, found === 4 ? 700 : 300);
  }

  if (location.hostname === "localhost") (window.__ogGames ||= {}).verbanden = () => S && { gs: S.gs, words: S.words };
  drawSetup();
}
