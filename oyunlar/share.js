// "Paylaş" for the daily games: result as coloured squares plus a link to the game.
// Phone: the share menu (WhatsApp etc.); computer: copied to the clipboard.
// Own file (not in common.js), so a browser with an older cached common.js still loads the games.

// "5 Kasım" for 2026-11-05
export const trDate = day => new Date(day + "T12:00:00Z").toLocaleDateString("tr-TR", { day: "numeric", month: "long", timeZone: "UTC" });
// 🟩 right, 🟥 wrong
export const squares = oks => oks.map(ok => ok ? "🟩" : "🟥").join("");

export async function shareText(btn, text) {
  if (navigator.share && matchMedia("(pointer: coarse)").matches) {
    try { await navigator.share({ text }); return; } catch (e) { if (e.name === "AbortError") return; }
  }
  try { await navigator.clipboard.writeText(text); }
  catch {   // older browsers: copy through a hidden text box
    const ta = Object.assign(document.createElement("textarea"), { value: text }); document.body.append(ta); ta.select();
    try { document.execCommand("copy"); } catch {} ta.remove();
  }
  const old = btn.textContent; btn.textContent = "Kopyalandı ✓"; setTimeout(() => btn.textContent = old, 2000);
}
