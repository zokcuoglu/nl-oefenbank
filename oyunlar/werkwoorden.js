// Günün düzensiz fiilleri: 5 irregular verbs a day (the same for everybody).
// For each verb the player types the past tense ("Ik ___ gisteren") and picks heb/ben + types the participle.
// 2 points per verb: 1 for the past tense, 1 for auxiliary + participle together.
// Verbs: werkwoorden.json (next to this file). Where both hebben and zijn are right (lopen, rijden, vergeten…), both count.
import { shareText, trDate, squares } from "./share.js";
import { esc, fmt, today, pickDaily, loadLocal, saveLocal, dropOldProgress, savePlay, drawRanking, resetRanking, drawStats, injectCss, flash } from "./common.js";

const GAME = "werkwoorden", MODULE = "oyun-werkwoorden", LEVEL = "dag", COUNT = 5;
const CSS = `
.ww .verb{font-family:var(--og-font);font-weight:700;font-size:clamp(32px,8vw,46px);text-align:center;margin:10px 0 2px}
.ww .tr{text-align:center;color:var(--og-muted);margin-bottom:16px}
.ww .row{display:flex;flex-wrap:wrap;align-items:center;gap:8px;justify-content:center;margin:10px 0;font-size:19px}
.ww .row input{font:inherit;font-size:19px;width:7.5em;max-width:46vw;padding:8px 10px;border-radius:8px;border:2px solid var(--og-line);background:var(--og-card);color:var(--og-ink)}
.ww .row input:focus{outline:none;border-color:var(--og-accent)}
.ww .row input.right{border-color:var(--og-ok);background:var(--og-ok-soft)}
.ww .row input.wrong{border-color:var(--og-bad);background:var(--og-bad-soft)}
.ww .aux{display:inline-flex;gap:4px}
.ww .aux button{font:inherit;font-size:17px;padding:7px 12px;border-radius:8px;border:2px solid var(--og-line);background:var(--og-card);color:var(--og-ink);cursor:pointer}
.ww .aux button.on{border-color:var(--og-accent);background:var(--og-accent);color:var(--og-accent-ink)}
.ww .fix{text-align:center;min-height:1.6em;margin-top:6px;color:var(--og-bad);font-weight:600}
.ww .fix.ok{color:var(--og-ok)}
.ww .act{text-align:center;margin-top:12px}
.ww .dots{display:flex;gap:6px;justify-content:center;margin-top:14px}
.ww .dots i{width:12px;height:12px;border-radius:50%;background:var(--og-line)}
.ww .dots i.ok{background:var(--og-ok)}.ww .dots i.half{background:#d9a400}.ww .dots i.no{background:var(--og-bad)}
.ww .tbl{width:100%;border-collapse:collapse;margin-top:12px;font-size:15px}
.ww .tbl td,.ww .tbl th{padding:6px 8px;border-bottom:1px solid var(--og-line);text-align:left}
.ww .tbl td.no{color:var(--og-bad)}
.ww .tip{font-size:14px;color:var(--og-muted);margin-top:14px}
.ww .example{border:2px dashed var(--og-line);border-radius:12px;padding:12px 14px;margin:12px 0;display:grid;gap:6px}
.ww .example .hd{font-weight:700;font-family:var(--og-font)}
.ww .steps{margin:6px 0 0;padding-left:20px;display:grid;gap:4px}
.ww .lab{text-align:center;font-weight:700;font-size:14px;margin-top:14px;color:var(--og-ink)}
.ww .lab small{display:block;font-weight:400;color:var(--og-muted)}
.ww .rule{text-align:center;font-size:13.5px;color:var(--og-muted);margin-top:-2px}
.ww .full{text-align:center;margin-top:8px;font-size:15px;background:var(--og-sunk);border-radius:8px;padding:8px}`;

// Lower case, single spaces, no spaces at the ends: "  Liep " counts as "liep"
const norm = s => String(s || "").trim().toLowerCase().replace(/\s+/g, " ");
const auxWord = h => h === "zijn" ? "ben" : "heb";
// Right answer as text: "liep" / "heb gelopen" or "heb/ben gelopen"
const impText = v => v.imp.join(" / ");
const perfText = v => `${v.hulp.map(auxWord).join("/")} ${v.vd}`;

export async function mountWerkwoorden(root, { user, profile, api, shareUrl = location.href }) {
  // Result as squares, two per verb (past tense, perfectum): "Düzensiz fiiller · 5 Kasım · 8/10" + 🟩🟩 🟩🟥 … + link
  const textOf = att => {
    const pairs = [];
    for (let i = 0; i < att.answers.length; i += 2) pairs.push(squares(att.answers.slice(i, i + 2).map(a => a.correct)));
    return `Düzensiz fiiller · ${trDate(att.day)} · ${att.score}/${att.total}\n${pairs.join(" ")}\n${shareUrl}`;
  };
  injectCss(CSS, "og-ww-css");
  root.classList.add("og", "ww");
  root.innerHTML = `
    <section data-r="setup">
      <h2 class="ot">Günün düzensiz fiilleri</h2>
      <p class="sub">Her gün 5 düzensiz fiil (<i>onregelmatige werkwoorden</i>), herkes için aynı. Bu fiiller geçmiş zamanda
        kurala uymaz (<i>lopen</i> → <i>loopte</i> değil <b>liep</b>), o yüzden ezberlemek gerekir. Her fiil için iki şey soruluyor:</p>
      <div class="example">
        <div class="hd">Örnek: lopen · yürümek</div>
        <div>① <b>Verleden tijd</b> (geçmiş zaman): <i>Ik <b>liep</b> gisteren.</i> — Dün yürüdüm.</div>
        <div>② <b>Perfectum</b> (heb/ben + voltooid deelwoord): <i>Ik <b>heb gelopen</b>.</i> — Yürüdüm.</div>
        <ol class="steps">
          <li>Birinci kutuya geçmiş zamanı yaz: <b>liep</b></li>
          <li><b>heb</b> ya da <b>ben</b> butonuna bas</li>
          <li>İkinci kutuya voltooid deelwoord'u yaz: <b>gelopen</b> → Kontrol et</li>
        </ol>
      </div>
      <p class="sub">Her fiil 2 puan: 1 geçmiş zaman, 1 perfectum (heb/ben ve deelwoord birlikte doğruysa).</p>
      <p class="today" data-r="today" hidden></p>
      <button class="bt" data-r="share1" hidden>📤 Paylaş</button>
      <div style="margin-top:14px"><button class="bt pri" data-r="go">Başla</button></div>
      <div class="grid2"><div class="pan" data-r="stats"></div><div class="pan" data-r="rank"></div></div>
    </section>
    <section data-r="play" hidden>
      <div class="bar"><span class="pill" data-r="count"></span><span class="pill" data-r="clock">0:00</span></div>
      <div class="pan">
        <div class="verb" data-r="verb"></div>
        <div class="tr" data-r="tr"></div>
        <div class="lab">① Verleden tijd <small>geçmiş zaman</small></div>
        <div class="row">Ik <input data-r="imp" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="liep" aria-label="geçmiş zaman"> gisteren.</div>
        <div class="lab">② Perfectum <small>heb ya da ben seç + voltooid deelwoord yaz</small></div>
        <div class="row">Ik <span class="aux"><button data-aux="hebben">heb</button><button data-aux="zijn">ben</button></span>
          <input data-r="vd" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="gelopen" aria-label="voltooid deelwoord">.</div>
        <div class="rule">Çoğu fiil <b>heb</b> alır. Yer değiştirme (gaan, komen) ya da durum değişimi (worden, sterven) → <b>ben</b>.</div>
        <div class="fix" data-r="fix"></div>
        <div class="full" data-r="full" hidden></div>
        <div class="act"><button class="bt pri" data-r="check">Kontrol et</button></div>
        <div class="dots" data-r="dots"></div>
      </div>
    </section>
    <section data-r="done" hidden>
      <div class="pan">
        <div class="big" data-r="result"></div>
        <p class="sub" data-r="resultText"></p>
        <button class="bt" data-r="share2">📤 Paylaş</button>
        <table class="tbl"><thead><tr><th>Fiil</th><th>Verleden tijd<br><small>ik / wij</small></th><th>Perfectum</th></tr></thead><tbody data-r="list"></tbody></table>
        <p class="tip">İpucu: hareket bildiren fiiller (lopen, rijden, zwemmen…) bir yere gidiyorsan <b>zijn</b>, sadece hareketi anlatıyorsan <b>hebben</b> alır:
          <i>Ik ben naar school gelopen</i> / <i>Ik heb veel gelopen</i>.</p>
      </div>
      <div class="grid2"><div class="pan" data-r="stats2"></div><div class="pan" data-r="rank2"></div></div>
    </section>`;
  const $ = r => root.querySelector(`[data-r="${r}"]`);

  let verbs = [];
  try {
    verbs = (await fetch(new URL("./werkwoorden.json", import.meta.url), { cache: "no-cache" }).then(r => r.json())).werkwoorden;
  } catch { root.innerHTML = `<p class="notice">Fiiller yüklenemedi. Sayfayı yenile.</p>`; return; }

  let history = [];
  try { history = (await api.loadAttempts(user.uid, MODULE)).filter(h => h.day); } catch {}
  dropOldProgress(GAME);
  const progressKey = () => `${GAME}:progress:${today()}`;
  const playedToday = () => history.find(h => h.day === today());
  let S = null;

  function drawSetup() {
    const done = playedToday();
    $("today").hidden = !done;
    if (done) $("today").textContent = `Bugün ${done.score}/${done.total} puan aldın. Yarın yeni fiiller var!`;
    $("share1").hidden = !(done && done.answers?.length);
    $("share1").onclick = () => shareText($("share1"), textOf(done));
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
    S = { list: pickDaily(verbs, v => v.inf, COUNT, today(), GAME), answers: saved?.answers || [],
          elapsed: saved?.elapsed || 0, resumedAt: Date.now(), aux: null, checked: false };
    clearInterval(S.timer); S.timer = setInterval(tick, 500); tick();
    show("play");
    next();
  }
  const played = () => S.elapsed + Math.floor((Date.now() - S.resumedAt) / 1000);
  function tick() { $("clock").textContent = fmt(played()); }
  const saveProgress = () => S && !S.done && saveLocal(progressKey(), { answers: S.answers, elapsed: played() });

  function setAux(a) {
    if (!S || S.checked) return;
    S.aux = a;
    root.querySelectorAll("[data-aux]").forEach(b => b.classList.toggle("on", b.dataset.aux === a));
  }
  root.querySelectorAll("[data-aux]").forEach(b => b.onclick = () => { setAux(b.dataset.aux); $("vd").focus(); });

  function next() {
    const i = S.answers.length;
    if (i >= S.list.length) return finish();
    const v = S.list[i];
    S.aux = null; S.checked = false;
    $("count").textContent = `${i + 1} / ${S.list.length}`;
    $("verb").textContent = v.inf;
    $("tr").textContent = v.tr;
    for (const r of ["imp", "vd"]) { $(r).value = ""; $(r).className = ""; $(r).disabled = false; }
    root.querySelectorAll("[data-aux]").forEach(b => b.classList.remove("on"));
    $("fix").textContent = ""; $("fix").className = "fix"; $("full").hidden = true;
    $("check").textContent = "Kontrol et";
    $("dots").innerHTML = S.list.map((_, k) => {
      const a = S.answers[k]; if (!a) return "<i></i>";
      const p = (a.impOk ? 1 : 0) + (a.perfOk ? 1 : 0);
      return `<i class="${p === 2 ? "ok" : p === 1 ? "half" : "no"}"></i>`;
    }).join("");
    // Grey example in the boxes only for the very first verb
    $("imp").placeholder = i === 0 ? "liep" : ""; $("vd").placeholder = i === 0 ? "gelopen" : "";
    $("imp").focus();
  }

  function check() {
    if (!S || S.done) return;
    if (S.checked) return next();                         // second press = next verb
    const v = S.list[S.answers.length];
    const imp = norm($("imp").value), vd = norm($("vd").value);
    if (!imp || !vd || !S.aux) {                          // ask for all three parts first
      $("fix").className = "fix";
      $("fix").textContent = !imp ? "Geçmiş zamanı yaz." : !S.aux ? "heb mi, ben mi? Birini seç." : "Voltooid deelwoord'u yaz.";
      (!imp ? $("imp") : $("vd")).focus();
      return;
    }
    const impOk = v.imp.includes(imp);
    const perfOk = v.hulp.includes(S.aux) && vd === v.vd;
    S.checked = true;
    S.answers.push({ inf: v.inf, imp, aux: S.aux, vd, impOk, perfOk });
    $("imp").className = impOk ? "right" : "wrong";
    $("vd").className = perfOk ? "right" : "wrong";
    $("imp").disabled = $("vd").disabled = true;
    const fixes = [];
    if (!impOk) fixes.push(`Ik ${impText(v)} gisteren`);
    if (!perfOk) fixes.push(`Ik ${perfText(v)}`);
    $("fix").className = fixes.length ? "fix" : "fix ok";
    $("fix").textContent = fixes.length ? "Doğrusu: " + fixes.join(" · ") : v.hulp.length > 1 ? "Doğru! (heb ve ben ikisi de olur)" : "Doğru!";
    flash($("verb"), fixes.length ? "shake" : "pop");
    // The whole verb at once: present, past (singular / plural), perfectum
    $("full").hidden = false;
    $("full").innerHTML = `<b>${esc(v.inf)}</b> → ${esc(impText(v))}${v.impMv ? ` / ${esc(v.impMv)} (wij, jullie, zij)` : ""} → ${esc(perfText(v))}`;
    $("check").textContent = S.answers.length >= S.list.length ? "Sonucu gör" : "Sonraki fiil";
    $("check").focus();
    saveProgress();
  }
  $("check").onclick = check;
  // Enter: from the first box go to heb/ben + second box; from the second box check; after checking, next verb
  $("imp").addEventListener("keydown", e => { if (e.key === "Enter") { e.preventDefault(); $("vd").focus(); } });
  $("vd").addEventListener("keydown", e => { if (e.key === "Enter") { e.preventDefault(); check(); } });

  function finish() {
    S.done = true; clearInterval(S.timer);
    const score = S.answers.reduce((n, a) => n + (a.impOk ? 1 : 0) + (a.perfOk ? 1 : 0), 0);
    const total = S.list.length * 2, time_s = played(), day = today();
    saveLocal(progressKey(), null);
    const answers = S.answers.flatMap(a => [
      { qid: `${a.inf}:imp`, chosen: a.imp, correct: a.impOk },
      { qid: `${a.inf}:perf`, chosen: `${auxWord(a.aux)} ${a.vd}`, correct: a.perfOk }]);
    const attempt = { test: LEVEL, day, score, total, time_s, finished_at: new Date().toISOString(), answers };
    history.unshift({ ...attempt, module: MODULE });
    api.saveAttempt(user.uid, MODULE, attempt).catch(e => $("resultText").insertAdjacentHTML("afterend", `<p class="saveerr">Sonuç kaydedilemedi (${esc(e.code || "hata")}).</p>`));
    const posted = savePlay(user, profile, { game: GAME, level: LEVEL, day, score, total, time_s }).catch(() => {});
    show("done");
    $("share2").onclick = () => shareText($("share2"), textOf(attempt));
    $("result").textContent = score === total ? "Hepsi doğru!" : score >= 8 ? "Çok iyi!" : score >= 5 ? "İyi gidiyor." : "Yarın daha iyi olacak!";
    $("resultText").textContent = `${score}/${total} puan · süre ${fmt(time_s)}`;
    $("list").innerHTML = S.list.map((v, k) => {
      const a = S.answers[k];
      return `<tr><td><b>${esc(v.inf)}</b><br><span class="small" style="margin:0">${esc(v.tr)}</span></td>
        <td class="${a.impOk ? "" : "no"}">${esc(impText(v))}${v.impMv ? ` / ${esc(v.impMv)}` : ""}</td><td class="${a.perfOk ? "" : "no"}">${esc(perfText(v))}</td></tr>`;
    }).join("");
    drawStats($("stats2"), history);
    posted.then(() => { resetRanking($("rank2")); drawRanking($("rank2"), { game: GAME, levels: { dag: "" }, user }); });
  }

  if (location.hostname === "localhost") (window.__ogGames ||= {}).werkwoorden = () => S && { list: S.list };
  drawSetup();
}
