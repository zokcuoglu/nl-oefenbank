// Two daily games with the same page, data file and code (only the settings differ):
//   "voorzetsels" - Günün edatları: 10 sentences a day, type the fixed preposition (denken ___ → aan)
//   "erop"        - er + edat: 5 sentences a day, type erop / eraan / ermee … or, when "er" is already
//                   in the sentence, only the preposition part (er … over, er … mee)
// Sentences: voorzetsels.json (built by scripts/content/build_voorzetsels.py), mostly from our own texts.
// Every day is the same for everybody. Questions that many players got wrong YESTERDAY come back today
// (each player's wrong ids are saved with the result in dagspel_plays.wrong).
// After playing, today's answers stay visible on this page (taken from the saved attempt), to learn from them.
import { shareText, trDate, squares } from "./share.js";
import { esc, fmt, today, dayNr, isoOf, hash, loadLocal, saveLocal, dropOldProgress, savePlay, loadPlays,
         drawRanking, resetRanking, drawStats, injectCss, flash } from "./common.js";

const SETTINGS = {
  voorzetsels: {
    count: 10, repeatMax: 4, title: "Günün edatları", shareTitle: "Edatlar",
    intro: `Her gün 10 cümle, herkes için aynı. Bazı fiil ve sıfatlar hep aynı edatla kullanılır
      (<i>vaste voorzetsels</i>): <b>denken aan</b>, <b>luisteren naar</b>, <b>wachten op</b>.
      Boşluğa doğru edatı yaz ve <b>Enter</b>'a bas. Cümleler çoğunlukla sitedeki kendi metinlerimizden.`,
    example: `<div class="hd">Örnek</div><div><i>Daar zorgen ze <u>&nbsp;voor&nbsp;</u> jonge zeehonden.</i></div>
      <div class="small">zorgen voor = bakmak, ilgilenmek · Nieuws: Zeehondencentrum</div>`
  },
  erop: {
    count: 5, repeatMax: 2, title: "Günün er + edatı", shareTitle: "er + edat",
    intro: `Her gün 5 cümle, herkes için aynı. <i>Ik wacht <b>op</b> de bus</i> → <i>Ik wacht <b>erop</b></i>:
      bir şeyin yerine <b>er</b> gelir ve edata yapışır. İki durum var:`,
    example: `<div>① Cümlede <b>er</b> yok, tek boşluk var → bütün kelimeyi yaz: <i>Ik wacht <u>&nbsp;erop&nbsp;</u> dat hij belt.</i></div>
      <div>② <b>er</b> cümlede ayrı duruyor → sadece edat kısmını yaz: <i>Ik heb er niet <u>&nbsp;aan&nbsp;</u> gedacht.</i></div>
      <div class="small">Dikkat: <b>met → mee</b> (ermee), <b>tot → toe</b> (ertoe).</div>`
  }
};
const LEVEL = "dag";
const CSS = `
.vz .zin{font-size:clamp(19px,4.6vw,24px);line-height:1.7;margin:8px 0 4px}
.vz .zin input{font:inherit;width:6.5em;max-width:40vw;padding:2px 8px;margin:0 4px;border-radius:8px;border:2px solid var(--og-line);
  background:var(--og-card);color:var(--og-ink);text-align:center}
.vz .zin input:focus{outline:none;border-color:var(--og-accent)}
.vz .zin input.right{border-color:var(--og-ok);background:var(--og-ok-soft)}
.vz .zin input.wrong{border-color:var(--og-bad);background:var(--og-bad-soft);text-decoration:line-through}
.vz .zin b.ans{color:var(--og-ok)}
.vz .again{display:inline-block;font-size:13px;background:var(--og-sunk);border-radius:999px;padding:2px 10px;margin-bottom:6px}
.vz .fb{min-height:3.2em;margin-top:10px}
.vz .fb .k{font-family:var(--og-font);font-weight:700;font-size:18px}
.vz .fb .k.good{color:var(--og-ok)} .vz .fb .k.bad{color:var(--og-bad)}
.vz .act{margin-top:12px;display:flex;gap:8px;flex-wrap:wrap}
.vz .dots{display:flex;gap:6px;margin-top:14px}
.vz .dots i{width:12px;height:12px;border-radius:50%;background:var(--og-line)}
.vz .dots i.ok{background:var(--og-ok)}.vz .dots i.no{background:var(--og-bad)}
.vz .example{border:2px dashed var(--og-line);border-radius:12px;padding:12px 14px;margin:12px 0;display:grid;gap:6px}
.vz .example .hd{font-weight:700;font-family:var(--og-font)}
.vz .review{list-style:none;padding:0;margin:12px 0 0;display:grid;gap:8px}
.vz .review li{padding:10px 12px;border-radius:8px;background:var(--og-sunk);border-left:4px solid var(--og-ok)}
.vz .review li.no{background:var(--og-bad-soft);border-left-color:var(--og-bad)}
.vz .review .s{font-size:16px;line-height:1.5}
.vz .review .m{font-size:13.5px;color:var(--og-muted);margin-top:3px}
.vz .review s{color:var(--og-bad)}`;

// Lower case, no spaces, curly quotes made straight: " Aan " counts as "aan"
const norm = s => String(s || "").trim().toLowerCase().replace(/\s+/g, "");
const isRight = (q, typed) => [q.a, ...(q.alt || [])].includes(norm(typed));
// The sentence with the gap filled in: the answer in bold (and the wrong answer struck through, if any)
const filled = (q, wrongTyped) => esc(q.zin).replace("___",
  (wrongTyped ? `<s>${esc(wrongTyped)}</s> ` : "") + `<b class="ans">${esc(q.a)}</b>`);

// Today's questions, the same for everybody:
// 1) up to repeatMax questions that at least half of yesterday's players got wrong (most missed first),
// 2) the rest picked by a number from (day, game, question), with every combination only once a day.
function pickToday(items, s, day, game, yesterdayPlays) {
  const byId = new Map(items.map(q => [q.id, q]));
  const players = yesterdayPlays.length, wrongCount = new Map();
  for (const p of yesterdayPlays) for (const id of new Set(p.wrong || [])) wrongCount.set(id, (wrongCount.get(id) || 0) + 1);
  const again = [...wrongCount.entries()]
    .filter(([id, n]) => byId.has(id) && n * 2 >= players)
    .sort((a, b) => b[1] - a[1] || hash(`${day}|${a[0]}`) - hash(`${day}|${b[0]}`))
    .slice(0, s.repeatMax).map(([id]) => byId.get(id));
  const list = [...again], usedK = new Set(again.map(q => q.k));
  for (const q of [...items].sort((a, b) => hash(`${day}|${game}|${a.id}`) - hash(`${day}|${game}|${b.id}`))) {
    if (list.length >= s.count) break;
    if (!usedK.has(q.k)) { usedK.add(q.k); list.push(q); }
  }
  return { list, again: new Set(again.map(q => q.id)) };
}

export async function mountVoorzetsels(root, { game = "voorzetsels", user, profile, api, shareUrl = location.href }) {
  const s = SETTINGS[game], MODULE = "oyun-" + game;
  const textOf = att => `${s.shareTitle} · ${trDate(att.day)} · ${att.score}/${att.total}\n${squares(att.answers.map(a => a.correct))}\n${shareUrl}`;
  injectCss(CSS, "og-vz-css");
  root.classList.add("og", "vz");
  root.innerHTML = `
    <section data-r="setup">
      <h2 class="ot">${s.title}</h2>
      <p class="sub">${s.intro}</p>
      <div class="example">${s.example}</div>
      <p class="sub">Dün çok yanlış yapılan cümleler bugün tekrar gelir (🔁 işaretli).</p>
      <p class="today" data-r="today" hidden></p>
      <button class="bt" data-r="share1" hidden>📤 Paylaş</button>
      <div style="margin-top:14px"><button class="bt pri" data-r="go">Başla</button></div>
      <div class="pan" data-r="todayReview" style="margin-top:18px" hidden></div>
      <div class="grid2"><div class="pan" data-r="stats"></div><div class="pan" data-r="rank"></div></div>
    </section>
    <section data-r="play" hidden>
      <div class="bar"><span class="pill" data-r="count"></span><span class="pill" data-r="clock">0:00</span></div>
      <div class="pan">
        <span class="again" data-r="again" hidden>🔁 Dün çok yanlış yapıldı</span>
        <div class="zin" data-r="zin"></div>
        <div class="fb" data-r="fb"></div>
        <div class="act"><button class="bt pri" data-r="check">Kontrol et</button><button class="bt pri" data-r="next" hidden>Sonraki →</button></div>
        <div class="dots" data-r="dots"></div>
      </div>
    </section>
    <section data-r="done" hidden>
      <div class="pan">
        <div class="big" data-r="result"></div>
        <p class="sub" data-r="resultText"></p>
        <button class="bt" data-r="share2">📤 Paylaş</button>
        <ul class="review" data-r="list"></ul>
      </div>
      <div class="grid2"><div class="pan" data-r="stats2"></div><div class="pan" data-r="rank2"></div></div>
    </section>`;
  const $ = r => root.querySelector(`[data-r="${r}"]`);

  let items = [];
  try {
    const data = await fetch(new URL("./voorzetsels.json", import.meta.url), { cache: "no-cache" }).then(r => r.json());
    items = data[game];
  } catch { root.innerHTML = `<p class="notice">Cümleler yüklenemedi. Sayfayı yenile.</p>`; return; }
  const byId = new Map(items.map(q => [q.id, q]));

  let history = [];
  try { history = (await api.loadAttempts(user.uid, MODULE)).filter(h => h.day); } catch {}
  dropOldProgress(game);
  const progressKey = () => `${game}:progress:${today()}`;
  const playedToday = () => history.find(h => h.day === today());
  let S = null;

  // Review list: every question with the right answer; wrong ones in red with what was typed
  const reviewHtml = answers => answers.map(a => {
    const q = byId.get(a.qid); if (!q) return "";
    return `<li class="${a.correct ? "" : "no"}"><div class="s">${filled(q, a.correct ? "" : a.chosen || "—")}</div>
      <div class="m"><b>${esc(q.k)}</b> = ${esc(q.tr)} · ${esc(q.bron)}</div></li>`;
  }).join("");

  function drawSetup() {
    const done = playedToday();
    $("today").hidden = !done;
    if (done) $("today").textContent = `Bugün ${done.score}/${done.total} yaptın. Yarın yeni cümleler var!`;
    $("share1").hidden = !(done && done.answers?.length);
    $("share1").onclick = () => shareText($("share1"), textOf(done));
    $("go").disabled = !!done;
    $("go").textContent = loadLocal(progressKey(), null) ? "Devam et" : "Başla";
    // Today's answers stay visible after playing
    $("todayReview").hidden = !(done && done.answers?.length);
    if (done?.answers?.length) $("todayReview").innerHTML = `<h3>Bugünkü cevapların</h3><ul class="review">${reviewHtml(done.answers)}</ul>`;
    drawStats($("stats"), history);
    drawRanking($("rank"), { game, levels: { dag: "" }, user });
  }
  $("go").onclick = () => start();
  const show = x => ["setup", "play", "done"].forEach(k => $(k).hidden = k !== x);

  async function start() {
    if (playedToday()) return drawSetup();
    $("go").disabled = true;
    const saved = loadLocal(progressKey(), null);
    let list, again;
    if (saved?.ids?.every(id => byId.has(id))) {   // continue: the same questions as when this game was started
      list = saved.ids.map(id => byId.get(id)); again = new Set(saved.again || []);
    } else {
      const day = today(), yesterday = isoOf(dayNr(day) - 1);
      let plays = [];
      try { plays = (await loadPlays(game, yesterday)).filter(p => p.day === yesterday); } catch {}
      ({ list, again } = pickToday(items, s, day, game, plays));
    }
    S = { list, again, answers: saved?.answers || [], elapsed: saved?.elapsed || 0, resumedAt: Date.now() };
    clearInterval(S.timer); S.timer = setInterval(tick, 500); tick();
    show("play");
    next();
  }
  const played = () => S.elapsed + Math.floor((Date.now() - S.resumedAt) / 1000);
  function tick() { $("clock").textContent = fmt(played()); }
  const saveProgress = () => S && !S.done && saveLocal(progressKey(),
    { ids: S.list.map(q => q.id), again: [...S.again], answers: S.answers, elapsed: played() });

  function next() {
    const i = S.answers.length;
    if (i >= S.list.length) return finish();
    const q = S.list[i];
    S.checked = false;
    $("count").textContent = `${i + 1} / ${S.list.length}`;
    $("again").hidden = !S.again.has(q.id);
    $("zin").innerHTML = esc(q.zin).replace("___", `<input data-r="inp" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="edat">`);
    $("fb").innerHTML = "";
    $("check").hidden = false; $("next").hidden = true;
    $("dots").innerHTML = S.list.map((_, k) => `<i class="${k < i ? (S.answers[k].ok ? "ok" : "no") : ""}"></i>`).join("");
    const inp = $("inp");
    inp.onkeydown = e => { if (e.key === "Enter") { e.preventDefault(); check(); } };
    inp.focus();
  }
  function check() {
    if (!S || S.done) return;
    if (S.checked) return next();
    const inp = $("inp"), typed = inp.value.trim();
    if (!typed) { flash(inp, "shake"); return; }
    S.checked = true;
    const q = S.list[S.answers.length], ok = isRight(q, typed);
    S.answers.push({ id: q.id, typed, ok });
    inp.readOnly = true;
    inp.classList.add(ok ? "right" : "wrong");
    flash(inp, ok ? "pop" : "shake");
    $("fb").innerHTML = `<div class="k ${ok ? "good" : "bad"}">${ok ? "Doğru!" : "Doğrusu: " + esc(q.a)}${q.alt?.length ? ` <span class="small">(${esc(q.alt.join(" / "))} da olur)</span>` : ""}</div>
      ${ok ? "" : `<div>${filled(q)}</div>`}
      <div class="small"><b>${esc(q.k)}</b> = ${esc(q.tr)} · ${esc(q.bron)}</div>`;
    $("check").hidden = true; $("next").hidden = false;
    $("next").textContent = S.answers.length >= S.list.length ? "Sonucu gör" : "Sonraki →";
    $("next").focus();   // Enter goes on to the next sentence
    saveProgress();
  }
  $("check").onclick = check;
  $("next").onclick = next;

  function finish() {
    S.done = true; clearInterval(S.timer);
    const score = S.answers.filter(a => a.ok).length, total = S.list.length, time_s = played(), day = today();
    saveLocal(progressKey(), null);
    const attempt = { test: LEVEL, day, score, total, time_s, finished_at: new Date().toISOString(),
                      answers: S.answers.map(a => ({ qid: a.id, chosen: a.typed, correct: a.ok })) };
    history.unshift({ ...attempt, module: MODULE });
    api.saveAttempt(user.uid, MODULE, attempt).catch(e => $("resultText").insertAdjacentHTML("afterend", `<p class="saveerr">Sonuç kaydedilemedi (${esc(e.code || "hata")}).</p>`));
    const wrong = S.answers.filter(a => !a.ok).map(a => a.id);
    const posted = savePlay(user, profile, { game, level: LEVEL, day, score, total, time_s, wrong }).catch(() => {});
    show("done");
    $("share2").onclick = () => shareText($("share2"), textOf(attempt));
    const pct = score / total;
    $("result").textContent = score === total ? "Hepsi doğru!" : pct >= 0.8 ? "Çok iyi!" : pct >= 0.5 ? "İyi gidiyor." : "Yarın daha iyi olacak!";
    $("resultText").textContent = `${score}/${total} doğru · süre ${fmt(time_s)}`;
    $("list").innerHTML = reviewHtml(attempt.answers);
    drawStats($("stats2"), history);
    posted.then(() => { resetRanking($("rank2")); drawRanking($("rank2"), { game, levels: { dag: "" }, user }); });
    // Going back to the start screen later shows today's answers there as well
    drawSetup();
  }

  drawSetup();
}
