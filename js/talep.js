// Wish box: adult members ask for a word, idiom, pattern or topic they would like on the site.
// Saved in Firestore "talepler" (see firestore.rules: an adult creates and reads only their own, the admin reads all).
// Up to 2 screenshots per wish: shrunk in the browser to a JPEG data URL and stored in the same document,
// so no separate file storage is needed (a Firestore document may hold up to 1 MiB).
import { db, esc, isAdmin, isPreview } from "./core.js";
import { collection, addDoc, getDocs, query, where, serverTimestamp } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-firestore.js";

export const TALEP_SOORT = { kelime: "Kelime", deyim: "Deyim", kalip: "Konuşma kalıbı", konu: "Konu", diger: "Diğer" };
export const TALEP_MAX = 4000;          // characters of text
const SHOT_MAX_PX = 1280;               // longest side of a screenshot after shrinking
const SHOT_MAX_CHARS = 380000;          // ~280 KB per screenshot, two of them stay well under the 1 MiB document limit

// Shrink one image file to a JPEG data URL under SHOT_MAX_CHARS (lower quality / size step by step if needed)
async function shrink(file) {
  const img = await createImageBitmap(file);
  let scale = Math.min(1, SHOT_MAX_PX / Math.max(img.width, img.height));
  for (let tries = 0; tries < 6; tries++) {
    const c = document.createElement("canvas");
    c.width = Math.round(img.width * scale); c.height = Math.round(img.height * scale);
    c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
    for (const q of [0.8, 0.65, 0.5]) {
      const url = c.toDataURL("image/jpeg", q);
      if (url.length <= SHOT_MAX_CHARS) return url;
    }
    scale *= 0.75;                       // still too big: make it smaller and try again
  }
  throw new Error("Görüntü çok büyük");
}

const when = t => { const d = t?.toDate ? t.toDate() : new Date(t); return isNaN(d) ? "" : d.toLocaleDateString("tr-TR", { day: "numeric", month: "long" }); };

// Puts the box into `el`. page = where it was sent from (shown to the admin), soort = default kind.
export async function mountTalep(el, { user, profile, page, soort = "kelime" }) {
  if (!el) return;
  if (!(isAdmin(profile) || profile?.type === "adult")) { el.remove(); return; }   // adults only; children ask via a parent
  const shots = [];
  el.innerHTML = `<section class="panel" id="talep">
    <span class="eyebrow">İstek kutusu</span>
    <h3 style="margin:4px 0 4px">Sitede görmek istediğin bir şey var mı?</h3>
    <p class="muted" style="margin:0 0 10px;max-width:64ch">Bir kelime, deyim, konuşma kalıbı ya da konu. Nerede gördüğünü, örnek cümleleri, neyi anlamadığını rahatça yaz; ekran görüntüsü de ekleyebilirsin (en fazla 2).</p>
    <div class="row" style="gap:8px;flex-wrap:wrap;margin-bottom:8px">${Object.entries(TALEP_SOORT).map(([k, v]) =>
      `<label class="chip" style="cursor:pointer"><input type="radio" name="t-soort" value="${k}" ${k === soort ? "checked" : ""}> ${v}</label>`).join("")}</div>
    <textarea id="t-tekst" class="typed" rows="5" maxlength="${TALEP_MAX}" placeholder="Örnek: WhatsApp'ta “Je kunt altijd bij ons terecht” gördüm. terecht burada ne demek? Başka nasıl kullanılıyor?"></textarea>
    <div class="row" style="justify-content:space-between;gap:8px;flex-wrap:wrap;margin-top:6px">
      <label class="btn" style="cursor:pointer">📎 Ekran görüntüsü ekle<input type="file" id="t-file" accept="image/*" multiple hidden></label>
      <span class="muted num" id="t-count" style="font-size:13px">0 / ${TALEP_MAX}</span></div>
    <div id="t-shots" class="row" style="gap:8px;flex-wrap:wrap;margin-top:8px"></div>
    <div class="row" style="margin-top:10px;gap:10px"><button class="btn primary" id="t-send">Gönder</button><span id="t-msg"></span></div>
    <div id="t-mine" style="margin-top:14px"></div></section>`;
  const $ = id => el.querySelector("#" + id);
  const msg = (t, ok) => $("t-msg").innerHTML = `<span class="${ok ? "ok-msg" : "err-msg"}">${esc(t)}</span>`;
  const drawShots = () => $("t-shots").innerHTML = shots.map((s, i) =>
    `<span style="position:relative;display:inline-block"><img src="${s}" alt="ekran görüntüsü ${i + 1}" style="height:90px;border-radius:8px;border:1px solid var(--line)">
     <button class="btn" data-del="${i}" style="position:absolute;top:2px;right:2px;padding:0 6px" aria-label="Görüntüyü kaldır">×</button></span>`).join("");
  $("t-tekst").addEventListener("input", e => $("t-count").textContent = `${e.target.value.length} / ${TALEP_MAX}`);
  $("t-file").addEventListener("change", async e => {
    for (const f of [...e.target.files]) {
      if (shots.length >= 2) { msg("En fazla 2 ekran görüntüsü."); break; }
      try { shots.push(await shrink(f)); } catch (err) { msg("Görüntü eklenemedi: " + err.message); }
    }
    e.target.value = ""; drawShots();
  });
  $("t-shots").addEventListener("click", e => { const b = e.target.closest("[data-del]"); if (b) { shots.splice(+b.dataset.del, 1); drawShots(); } });

  // The user's own wishes with their status, newest first
  async function drawMine() {
    try {
      const snap = await getDocs(query(collection(db, "talepler"), where("uid", "==", user.uid)));
      const rows = snap.docs.map(d => d.data()).sort((a, b) => String(b.created_at?.seconds ?? b.created_at).localeCompare(String(a.created_at?.seconds ?? a.created_at), undefined, { numeric: true }));
      $("t-mine").innerHTML = rows.length ? `<span class="eyebrow">İsteklerin</span>${rows.slice(0, 8).map(r => `<div class="wrow" style="cursor:default">
        <span><b>${esc(TALEP_SOORT[r.soort] || r.soort)}</b> <span class="muted">· ${esc(when(r.created_at))}</span><br><span style="font-size:14px">${esc(r.tekst.slice(0, 140))}${r.tekst.length > 140 ? "…" : ""}</span></span>
        <span class="chip ${r.status === "yapildi" ? "ok" : ""}">${r.status === "yapildi" ? "eklendi" : "bekliyor"}</span></div>`).join("")}` : "";
    } catch { $("t-mine").innerHTML = ""; }   // rules not published yet: just show nothing
  }

  $("t-send").addEventListener("click", async () => {
    const tekst = $("t-tekst").value.trim();
    if (tekst.length < 2) return msg("Önce ne istediğini yaz.");
    if (isPreview()) return msg("Görünüm modunda gönderilmez.");
    $("t-send").disabled = true;
    const data = { uid: user.uid, name: profile?.name || "", soort: el.querySelector("[name=t-soort]:checked")?.value || soort,
      tekst: tekst.slice(0, TALEP_MAX), pagina: page, status: "yeni", created_at: serverTimestamp() };
    shots.forEach((s, i) => data["ss" + (i + 1)] = s);
    try {
      await addDoc(collection(db, "talepler"), data);
      $("t-tekst").value = ""; $("t-count").textContent = `0 / ${TALEP_MAX}`; shots.length = 0; drawShots();
      msg("Teşekkürler, isteğin bize ulaştı!", true); drawMine();
    } catch (e) { msg("Gönderilemedi: " + (e.code || e.message)); }
    $("t-send").disabled = false;
  });
  drawMine();
}
