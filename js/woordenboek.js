// Dutch-Dutch dictionary panel for the Lezen pages.
// Why: in the real exam you may use a Dutch-Dutch dictionary (Van Dale NT2), but no Turkish. So this panel
// shows Dutch only: article, word type, definition and example, from data/woordenboek.json (built from the
// single word source). Type a word, or double-click a word in the text.
// Usage: import { mountWoordenboek } from "../js/woordenboek.js"; const wb = mountWoordenboek("../data/woordenboek.json");
//        wb.show(true|false) to show or hide the button (e.g. only while reading a text).

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const VOWELS = "aeiou";

// Possible dictionary keys for a word as it appears in a text: "lessen" -> les, "werkte" -> werken,
// "gekregen" -> krijgen (irregular forms come from the f map). Only keys that exist in E are kept.
function candidates(word, E, F) {
  const w = word.toLowerCase().replace(/^[^a-zà-ÿ]+|[^a-zà-ÿ]+$/g, "");
  const out = [w, F[w]];
  const stems = [w];                                                       // the word itself may be a stem (betaal, geef)
  if (/^ge.{3,}[dt]$/.test(w)) stems.push(w.slice(2, -1));               // gewerkt -> werk
  if (/^ge.{3,}en$/.test(w)) out.push(w.slice(2));                        // gelopen -> lopen (if regular)
  // Separable verbs: opgezegd -> opzeggen, opgenomen -> opnemen (prefix + "ge" + participle)
  for (let i = 2; i <= 5; i++) if (w.slice(i, i + 2) === "ge" && w.length > i + 4) {
    const pre = w.slice(0, i), rest = w.slice(i + 2);
    if (F["ge" + rest]) out.push(pre + F["ge" + rest]);
    if (/[dt]$/.test(rest)) stems.push(pre + rest.slice(0, -1));
    if (/en$/.test(rest)) out.push(pre + rest);
  }
  for (const suf of ["eren", "ste", "ten", "den", "ere", "er", "te", "de", "en", "es", "e", "s", "'s", "t", "st"])
    if (w.endsWith(suf) && w.length - suf.length >= 2) stems.push(w.slice(0, -suf.length));
  for (const s of stems) {
    const v = new Set([s]);
    if (/z$/.test(s)) v.add(s.slice(0, -1) + "s");                        // huizen -> huis
    if (/v$/.test(s)) v.add(s.slice(0, -1) + "f");                        // brieven -> brief
    if (s.length > 2 && s.at(-1) === s.at(-2) && !VOWELS.includes(s.at(-1))) v.add(s.slice(0, -1)); // lessen -> les
    const open = s.match(/^(.*[^aeiou])([aeou])([^aeiou])$/);
    if (open) v.add(open[1] + open[2] + open[2] + open[3]);              // buren -> buur, afspraken -> afspraak
    for (const x of v) {
      out.push(x, x + "en", x + "n");
      const fv = x.replace(/f$/, "v").replace(/s$/, "z");                 // blijf -> blijven, lees -> lezen
      if (fv !== x) { out.push(fv + "en"); const m2 = fv.match(/^(.*)([aeou])\2([vz])$/); if (m2) out.push(m2[1] + m2[2] + m2[3] + "en"); }
      // werk -> werken; maak -> maken (long vowel written double in the stem, single before -en)
      const m = x.match(/^(.*)([aeou])\2([^aeiou])$/);
      if (m) out.push(m[1] + m[2] + m[3] + "en");
      // zet -> zetten (short vowel: consonant doubles before -en)
      if (/[^aeiou][aeiou][^aeiouwy]$/.test(x)) out.push(x + x.at(-1) + "en");
    }
  }
  return [...new Set(out.filter(k => k && E[k]))];
}

export function mountWoordenboek(url) {
  let E = null, F = {}, loading = null;
  const load = () => loading ||= fetch(url, { cache: "no-cache" }).then(r => r.json()).then(d => { E = d.e; F = d.f; }).catch(() => { E = {}; });

  const css = document.createElement("style");
  css.textContent = `
  .wb-btn{position:fixed;right:16px;bottom:16px;z-index:50;border:1px solid var(--line);background:var(--surface);border-radius:999px;padding:10px 16px;font-weight:600;box-shadow:0 2px 10px rgba(0,0,0,.12);cursor:pointer}
  .wb-panel{position:fixed;right:16px;bottom:68px;z-index:50;width:min(380px,calc(100vw - 32px));max-height:min(70vh,560px);display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--line);border-radius:12px;box-shadow:0 6px 24px rgba(0,0,0,.18)}
  .wb-panel header{display:flex;gap:8px;align-items:center;padding:10px 12px;border-bottom:1px solid var(--line)}
  .wb-panel input{flex:1;font-size:16px;padding:7px 10px;border:1px solid var(--line);border-radius:8px;background:var(--ground);color:inherit}
  .wb-panel .wb-out{overflow:auto;padding:10px 14px;font-size:15px;line-height:1.5}
  .wb-panel .wb-e{padding:8px 0;border-bottom:1px solid var(--line)} .wb-panel .wb-e:last-child{border:0}
  .wb-panel .wb-h{font-weight:700} .wb-panel .wb-s{font-size:13px;color:var(--muted);font-style:italic}
  .wb-panel .wb-vb{color:var(--muted);font-style:italic}
  .wb-panel .x{border:0;background:none;font-size:20px;cursor:pointer;color:var(--muted)}`;
  document.head.append(css);

  const btn = Object.assign(document.createElement("button"), { className: "wb-btn", type: "button", textContent: "📖 Woordenboek" });
  const panel = Object.assign(document.createElement("div"), { className: "wb-panel", hidden: true });
  panel.innerHTML = `<header><input type="search" lang="nl" placeholder="Zoek een woord…" autocomplete="off" spellcheck="false">
    <button class="x" type="button" aria-label="Sluiten">×</button></header>
    <div class="wb-out" lang="nl"><p class="muted" style="margin:0;font-size:14px">Bir kelime yaz ya da metinde kelimeye çift tıkla. Sınavdaki gibi sadece Hollandaca açıklama gösterilir.</p></div>`;
  btn.hidden = true;
  document.body.append(panel, btn);
  const input = panel.querySelector("input"), out = panel.querySelector(".wb-out");

  async function lookup(word) {
    await load();
    word = word.trim();
    if (!word) return;
    const keys = candidates(word, E, F);
    if (!keys.length) { out.innerHTML = `<p style="margin:0"><b>${esc(word)}</b> — niet gevonden.</p><p class="muted" style="margin:6px 0 0;font-size:14px">Bu kelime sözlüğümüzde yok. Cümlenin geri kalanından anlamı tahmin etmeye çalış.</p>`; return; }
    const seen = new Set(), items = keys.flatMap(k => E[k]).filter(i => !seen.has(i.nl) && seen.add(i.nl)).slice(0, 8);
    out.innerHTML = items.map(i => `<div class="wb-e"><span class="wb-h">${esc(i.nl)}</span> <span class="wb-s">${esc(i.soort)}${i.lw ? ` · ${esc(i.lw)}` : ""}</span>
      ${i.def ? `<div>${esc(i.def)}</div>` : ""}${i.vb ? `<div class="wb-vb">${esc(i.vb)}</div>` : ""}</div>`).join("");
  }
  const open = (word = "") => { panel.hidden = false; load(); if (word) { input.value = word; lookup(word); } input.focus(); };

  btn.addEventListener("click", () => panel.hidden ? open() : (panel.hidden = true));
  panel.querySelector(".x").addEventListener("click", () => { panel.hidden = true; });
  let t; input.addEventListener("input", () => { clearTimeout(t); t = setTimeout(() => lookup(input.value), 250); });
  // Double-click a word in a Dutch text -> look it up
  document.addEventListener("dblclick", e => {
    if (btn.hidden || !e.target.closest('[lang="nl"]') || e.target.closest(".wb-panel")) return;
    const w = String(getSelection() || "").trim();
    if (w && !/\s/.test(w)) open(w);
  });
  return { show(on) { btn.hidden = !on; if (!on) panel.hidden = true; }, lookup: open, candidates: w => candidates(w, E || {}, F) };
}
