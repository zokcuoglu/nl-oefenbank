// Günün de/het'i: 10 nouns a day (the same for everybody), choose "de" or "het".
// Words: all nouns with de/het in the nl-oefenbank word pool (data/woorden.json), read live.
import { esc, fmt, today, pickDaily, loadLocal, saveLocal, dropOldProgress, savePlay, drawRanking, resetRanking, drawStats, injectCss, flash } from "./common.js";

const GAME = "dehet", MODULE = "oyun-dehet", LEVEL = "dag", COUNT = 10;
const CSS = `
.dh .word{font-family:var(--og-font);font-weight:700;font-size:clamp(34px,9vw,52px);text-align:center;margin:18px 0 6px}
.dh .tr{text-align:center;color:var(--og-muted);min-height:1.5em}
.dh .two{display:grid;grid-template-columns:1fr 1fr;gap:12px;max-width:420px;margin:18px auto 0}
.dh .two button{font:inherit;font-family:var(--og-font);font-weight:700;font-size:30px;padding:18px 0;border-radius:12px;border:2px solid var(--og-line);background:var(--og-card);color:var(--og-ink);cursor:pointer}
.dh .two button:hover{border-color:var(--og-accent)}
.dh .two button.right{background:var(--og-ok-soft);border-color:var(--og-ok);color:var(--og-ok)}
.dh .two button.wrong{background:var(--og-bad-soft);border-color:var(--og-bad);color:var(--og-bad)}
.dh .dots{display:flex;gap:6px;justify-content:center;margin-top:10px}
.dh .dots i{width:12px;height:12px;border-radius:50%;background:var(--og-line)}
.dh .dots i.ok{background:var(--og-ok)}.dh .dots i.no{background:var(--og-bad)}
.dh .list{list-style:none;padding:0;margin:12px 0 0;display:grid;gap:6px}
.dh .list li{display:flex;justify-content:space-between;gap:10px;padding:6px 10px;border-radius:8px;background:var(--og-sunk)}
.dh .list li.no{background:var(--og-bad-soft)}
.dh .tip{font-size:14px;color:var(--og-muted);margin-top:14px}`;

export async function mountDeHet(root, { user, profile, api }) {
  injectCss(CSS, "og-dehet-css");
  root.classList.add("og", "dh");
  root.innerHTML = `
    <section data-r="setup">
      <h2 class="ot">Günün de/het'i</h2>
      <p class="sub">Her gün 10 kelime, herkes için aynı. Kelimenin önüne <b>de</b> mi gelir, <b>het</b> mi? Klavyeden <b>D</b> ve <b>H</b> tuşlarıyla da cevaplayabilirsin.</p>
      <p class="today" data-r="today" hidden></p>
      <div style="margin-top:14px"><button class="bt pri" data-r="go">Başla</button></div>
      <div class="grid2"><div class="pan" data-r="stats"></div><div class="pan" data-r="rank"></div></div>
    </section>
    <section data-r="play" hidden>
      <div class="bar"><span class="pill" data-r="count"></span><span class="pill" data-r="clock">0:00</span></div>
      <div class="pan">
        <div class="word" data-r="word"></div>
        <div class="tr" data-r="tr"></div>
        <div class="two"><button data-a="de">de</button><button data-a="het">het</button></div>
        <div class="dots" data-r="dots"></div>
      </div>
    </section>
    <section data-r="done" hidden>
      <div class="pan">
        <div class="big" data-r="result"></div>
        <p class="sub" data-r="resultText"></p>
        <ul class="list" data-r="list"></ul>
        <p class="tip">İpucu: <b>het</b> alan kelimeler daha az; küçültme ekli kelimeler (-je, -tje) her zaman <b>het</b> alır.</p>
      </div>
      <div class="grid2"><div class="pan" data-r="stats2"></div><div class="pan" data-r="rank2"></div></div>
    </section>`;
  const $ = r => root.querySelector(`[data-r="${r}"]`);

  // Words: "de fiets" / "het huis" nouns from the pool
  let words = [];
  try {
    const pool = await fetch(new URL("../data/woorden.json", import.meta.url), { cache: "no-cache" }).then(r => r.json());
    const seen = new Set();
    for (const w of pool.woorden) {
      const m = w.tur === "zn" && /^(de|het) ([a-zà-ÿ-]+)$/.exec(w.nl);
      if (m && !seen.has(m[2])) { seen.add(m[2]); words.push({ art: m[1], w: m[2], tr: w.tr || "" }); }
    }
  } catch { root.innerHTML = `<p class="notice">Kelimeler yüklenemedi. Sayfayı yenile.</p>`; return; }

  let history = [];
  try { history = (await api.loadAttempts(user.uid, MODULE)).filter(h => h.day); } catch {}
  dropOldProgress(GAME);
  const progressKey = () => `${GAME}:progress:${today()}`;
  const playedToday = () => history.find(h => h.day === today());
  let S = null;

  function drawSetup() {
    const done = playedToday();
    $("today").hidden = !done;
    if (done) $("today").textContent = `Bugün ${done.score}/${done.total} yaptın. Yarın yeni kelimeler var!`;
    $("go").disabled = !!done;
    $("go").textContent = loadLocal(progressKey(), null) ? "Devam et" : "Başla";
    drawStats($("stats"), history);
    drawRanking($("rank"), { game: GAME, levels: { dag: "" }, user });
  }
  $("go").onclick = () => start();
  const show = s => ["setup", "play", "done"].forEach(x => $(x).hidden = x !== s);

  function start() {
    if (playedToday()) return drawSetup();
    const saved = loadLocal(progressKey(), null);
    S = { list: pickDaily(words, x => x.w, COUNT, today(), GAME), answers: saved?.answers || [], elapsed: saved?.elapsed || 0, resumedAt: Date.now(), busy: false };
    clearInterval(S.timer); S.timer = setInterval(tick, 500); tick();
    show("play");
    next();
  }
  const played = () => S.elapsed + Math.floor((Date.now() - S.resumedAt) / 1000);
  function tick() { $("clock").textContent = fmt(played()); }
  const saveProgress = () => S && !S.done && saveLocal(progressKey(), { answers: S.answers, elapsed: played() });

  function next() {
    const i = S.answers.length;
    if (i >= S.list.length) return finish();
    $("count").textContent = `${i + 1} / ${S.list.length}`;
    $("word").textContent = S.list[i].w;
    $("tr").textContent = "";
    root.querySelectorAll("[data-a]").forEach(b => b.className = "");
    $("dots").innerHTML = S.list.map((_, k) => `<i class="${k < i ? (S.answers[k].ok ? "ok" : "no") : ""}"></i>`).join("");
    S.busy = false;
  }
  function answer(a) {
    if (!S || S.busy || S.done) return;
    S.busy = true;
    const q = S.list[S.answers.length], ok = a === q.art;
    S.answers.push({ w: q.w, chosen: a, ok });
    root.querySelector(`[data-a="${q.art}"]`).className = "right";
    if (!ok) root.querySelector(`[data-a="${a}"]`).className = "wrong";
    flash($("word"), ok ? "pop" : "shake");
    $("word").textContent = `${q.art} ${q.w}`;
    $("tr").textContent = q.tr;
    saveProgress();
    setTimeout(next, ok ? 900 : 1700);
  }
  root.querySelectorAll("[data-a]").forEach(b => b.onclick = () => answer(b.dataset.a));
  document.addEventListener("keydown", e => {
    if (!S || $("play").hidden || !root.offsetParent || e.ctrlKey || e.metaKey || e.altKey) return;
    if (e.key === "d" || e.key === "D") answer("de");
    else if (e.key === "h" || e.key === "H") answer("het");
  });

  function finish() {
    S.done = true; clearInterval(S.timer);
    const score = S.answers.filter(a => a.ok).length, total = S.list.length, time_s = played(), day = today();
    saveLocal(progressKey(), null);
    const attempt = { test: LEVEL, day, score, total, time_s, finished_at: new Date().toISOString(),
                      answers: S.answers.map(a => ({ qid: a.w, chosen: a.chosen, correct: a.ok })) };
    history.unshift({ ...attempt, module: MODULE });
    api.saveAttempt(user.uid, MODULE, attempt).catch(e => $("resultText").insertAdjacentHTML("afterend", `<p class="saveerr">Sonuç kaydedilemedi (${esc(e.code || "hata")}).</p>`));
    const posted = savePlay(user, profile, { game: GAME, level: LEVEL, day, score, total, time_s }).catch(() => {});
    show("done");
    $("result").textContent = score === total ? "Hepsi doğru!" : score >= 8 ? "Çok iyi!" : score >= 5 ? "İyi gidiyor." : "Yarın daha iyi olacak!";
    $("resultText").textContent = `${score}/${total} doğru · süre ${fmt(time_s)}`;
    $("list").innerHTML = S.list.map((q, k) => `<li class="${S.answers[k].ok ? "" : "no"}"><span><b>${q.art}</b> ${esc(q.w)}</span><span class="small" style="margin:0">${esc(q.tr)}</span></li>`).join("");
    drawStats($("stats2"), history);
    posted.then(() => { resetRanking($("rank2")); drawRanking($("rank2"), { game: GAME, levels: { dag: "" }, user }); });
  }

  if (location.hostname === "localhost") (window.__ogGames ||= {}).dehet = () => S && { list: S.list };
  drawSetup();
}
