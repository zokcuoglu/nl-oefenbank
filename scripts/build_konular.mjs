// Writes data/rekenen-konular.json: the names of all topics of kids/rekenen.html (both subjects).
// The mailer (scripts/mailer.py) is Python and cannot read the JavaScript question files, so it uses this list
// for the weekly summary. Run after adding or renaming a topic:  node scripts/build_konular.mjs
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
// The pages import the files with "?v=3" (browser cache). Node cannot import that from disk, so copy them without it.
const tmp = mkdtempSync(join(tmpdir(), "konular-"));
for (const f of ["vragen-basis", "rekenen-school", "rekenen-vragen", "natuur-78", "natuur-vragen"])
  writeFileSync(join(tmp, f + ".mjs"), readFileSync(join(root, "kids", f + ".js"), "utf8").replace(/\.js\?v=\d+"/g, '.mjs"'));
const out = {};
for (const f of ["rekenen-vragen", "natuur-vragen"]) {
  const { TOPICS } = await import(pathToFileURL(join(tmp, f + ".mjs")).href);
  for (const t of TOPICS) out[t.id] = { nl: t.nl, tr: t.tr, band: t.band, school: !!t.school };
}
out.gemengd = { nl: "Gemengde toets", tr: "Karışık sınav" };
out.herhaal = { nl: "Herhalen", tr: "Günlük tekrar" };
writeFileSync(join(root, "data", "rekenen-konular.json"), JSON.stringify(out, null, 2) + "\n");
console.log(Object.keys(out).length, "topics written");
