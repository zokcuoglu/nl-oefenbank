// Rekenen, school topics: what Dutch primary schools teach in groep 5-6 and groep 7-8.
// Merged into kids/rekenen-vragen.js (same lists), so the page shows them as part of Rekenen & meetkunde.
//
// Where the choice of topics comes from: the SLO "tussendoelen rekenen-wiskunde" per groep and the four
// domains of the referentiekader that the doorstroomtoets in groep 8 measures (getallen, verhoudingen,
// meten en meetkunde, verbanden). Groep 5-6: handig rekenen tot 1000, delen (met rest), klok en tijd, geld,
// meten, eenvoudige breuken, afronden en schatten, grote getallen. Groep 7-8: breuken-kommagetallen-procenten,
// procenten, kommagetallen, verhoudingen, gemiddelde, snelheid, rekenen met letters.
// We do not know which method the school uses, so the wording follows the general goals, not one book.
import { ri, pick, shuffle, Q, svg, T, eur, dec, MC, pickOne } from "./vragen-basis.js?v=3";

export const S_TOPICS = [
  { id: "handig", nl: "Handig rekenen tot 1000", tr: "1000'e kadar akıldan hesap", sub_nl: "aanvullen, compenseren, verdubbelen", sub_tr: "tamamlama, yuvarlayıp düzeltme, iki katı", open: true, band: "5-6", school: true },
  { id: "delen", nl: "Delen", tr: "Bölme", sub_nl: "eerlijk verdelen, ook met rest", sub_tr: "eşit paylaştırma, kalanlı bölme", open: true, band: "5-6", school: true },
  { id: "tijd", nl: "Klok en tijd", tr: "Saat ve zaman", sub_nl: "minuten, uren, hoe lang duurt het", sub_tr: "dakika, saat, ne kadar sürer", open: true, band: "5-6", school: true },
  { id: "geld", nl: "Geld", tr: "Para", sub_nl: "betalen en wisselgeld", sub_tr: "ödeme ve para üstü", open: true, band: "5-6", school: true },
  { id: "meten", nl: "Meten", tr: "Ölçme", sub_nl: "meter, kilo, liter omrekenen", sub_tr: "metre, kilo, litre çevirme", open: true, band: "5-6", school: true },
  { id: "breuken", nl: "Breuken", tr: "Kesirler", sub_nl: "de helft, een kwart, drie kwart", sub_tr: "yarım, çeyrek, dörtte üç", open: true, band: "5-6", school: true },
  { id: "afronden", nl: "Afronden en schatten", tr: "Yuvarlama ve tahmin", sub_nl: "ongeveer hoeveel?", sub_tr: "yaklaşık kaç?", open: true, band: "5-6", school: true },
  { id: "grotegetallen", nl: "Grote getallen", tr: "Büyük sayılar", sub_nl: "duizendtallen, honderdtallen, tientallen", sub_tr: "binlikler, yüzlükler, onluklar", open: true, band: "5-6", school: true },
  { id: "breukproc", nl: "Breuken, kommagetallen en procenten", tr: "Kesir, ondalık sayı ve yüzde", sub_nl: "½ = 0,5 = 50%", sub_tr: "½ = 0,5 = %50", open: false, band: "7-8", school: true },
  { id: "procenten", nl: "Procenten", tr: "Yüzdeler", sub_nl: "korting, btw, hoeveel procent", sub_tr: "indirim, KDV, yüzde kaç", open: false, band: "7-8", school: true },
  { id: "kommagetallen", nl: "Kommagetallen", tr: "Ondalık sayılar", sub_nl: "rekenen met 0,5 en 2,75", sub_tr: "0,5 ve 2,75 ile hesap", open: false, band: "7-8", school: true },
  { id: "verhoudingen", nl: "Verhoudingen", tr: "Oran ve orantı", sub_nl: "recept, mengen, prijs per stuk", sub_tr: "tarif, karışım, tane fiyatı", open: false, band: "7-8", school: true },
  { id: "gemiddelde", nl: "Gemiddelde", tr: "Ortalama", sub_nl: "alles optellen en eerlijk verdelen", sub_tr: "hepsini topla, eşit paylaştır", open: false, band: "7-8", school: true },
  { id: "snelheid", nl: "Snelheid", tr: "Hız", sub_nl: "kilometer per uur", sub_tr: "saatte kilometre", open: false, band: "7-8", school: true },
  { id: "letters", nl: "Rekenen met letters", tr: "Harfli ifadeler", sub_nl: "welk getal is x?", sub_tr: "x hangi sayı?", open: false, band: "7-8", school: true }
];

// ---------------------------------------------------------------- helpers
const clock = m => `${Math.floor(m / 60) % 24}:${String(m % 60).padStart(2, "0")}`;       // minutes since midnight -> "14:05"
// A circle cut into n equal slices with k of them coloured: what a fraction looks like
const pie = (n, k) => { const cx = 110, cy = 65, r = 54; let out = `<circle class="room" cx="${cx}" cy="${cy}" r="${r}"/>`;
  const pt = i => { const a = -Math.PI / 2 + 2 * Math.PI * i / n; return [cx + r * Math.cos(a), cy + r * Math.sin(a)]; };
  for (let i = 0; i < k; i++) { const [x1, y1] = pt(i), [x2, y2] = pt(i + 1); out += `<path class="shape" d="M${cx},${cy} L${x1.toFixed(1)},${y1.toFixed(1)} A${r},${r} 0 0 1 ${x2.toFixed(1)},${y2.toFixed(1)} Z"/>`; }
  for (let i = 0; i < n; i++) { const [x, y] = pt(i); out += `<line x1="${cx}" y1="${cy}" x2="${x.toFixed(1)}" y2="${y.toFixed(1)}"/>`; }
  return svg(out); };
const money = (nl, tr, v, ex_nl, ex_tr) => Q(nl, tr, v, "euro", ex_nl, ex_tr, { show: eur(v) + " euro" });
const decQ = (nl, tr, v, unit, ex_nl, ex_tr) => Q(nl, tr, v, unit, ex_nl, ex_tr, { show: (dec(v) + " " + unit).trim() });

export const S_GEN = {};

// ----- Handig rekenen tot 1000
S_GEN.handig = [
  [
    () => { const a = ri(11, 89); return Q(`Hoeveel moet je bij ${a} optellen om 100 te krijgen?`, `${a} sayısına kaç eklersen 100 olur?`, 100 - a, "",
      `Vul aan: ${a} → ${Math.ceil(a / 10) * 10} → 100. Samen ${100 - a}.`, `Tamamla: ${a} → ${Math.ceil(a / 10) * 10} → 100. Toplam ${100 - a}.`); },
    () => { const a = ri(12, 60) * 10, b = ri(11, 39) * 10; return Q(`Hoeveel is ${a} + ${b}?`, `${a} + ${b} kaç eder?`, a + b, "",
      `Reken met tientallen: ${a / 10} + ${b / 10} = ${(a + b) / 10}, dus ${a + b}.`, `Onluklarla hesapla: ${a / 10} + ${b / 10} = ${(a + b) / 10}, yani ${a + b}.`); },
    () => { const a = ri(2, 9) * 100; return Q(`Hoeveel is 1000 − ${a}?`, `1000 − ${a} kaç eder?`, 1000 - a, "",
      `10 honderdtallen − ${a / 100} honderdtallen = ${10 - a / 100} honderdtallen.`, `10 yüzlük − ${a / 100} yüzlük = ${10 - a / 100} yüzlük.`); },
    () => { const a = ri(12, 45) * 10; return Q(`Wat is het dubbele van ${a}?`, `${a} sayısının iki katı kaçtır?`, 2 * a, "", `${a} + ${a} = ${2 * a}.`, `${a} + ${a} = ${2 * a}.`); }
  ],
  [
    () => { const a = ri(2, 6) * 100 - 1, b = ri(111, 389); return Q(`Reken handig uit: ${a} + ${b}`, `Kolay yoldan hesapla: ${a} + ${b}`, a + b, "",
      `Maak er ${a + 1} + ${b} van: ${a + 1 + b}. Dan 1 eraf: ${a + b}.`, `Önce ${a + 1} + ${b} = ${a + 1 + b}. Sonra 1 çıkar: ${a + b}.`); },
    () => { const b = ri(1, 4) * 100 - 2, a = b + ri(120, 480); return Q(`Reken handig uit: ${a} − ${b}`, `Kolay yoldan hesapla: ${a} − ${b}`, a - b, "",
      `Haal er eerst ${b + 2} af: ${a - b - 2}. Je haalde 2 te veel weg, dus 2 erbij: ${a - b}.`, `Önce ${b + 2} çıkar: ${a - b - 2}. 2 fazla çıkardın, 2 ekle: ${a - b}.`); },
    () => { const b = ri(201, 780), d = ri(4, 28), a = b + d; return Q(`Reken uit door aan te vullen: ${a} − ${b}`, `Tamamlayarak hesapla: ${a} − ${b}`, d, "",
      `De getallen liggen dicht bij elkaar. Tel vanaf ${b} door tot ${a}: dat is ${d}.`, `Sayılar birbirine yakın. ${b}'den ${a}'e kadar say: ${d} eder.`); },
    () => { const a = ri(11, 49) * 20; return Q(`Wat is de helft van ${a}?`, `${a} sayısının yarısı kaçtır?`, a / 2, "", `${a / 2} + ${a / 2} = ${a}.`, `${a / 2} + ${a / 2} = ${a}.`); }
  ],
  [
    () => { const t = ri(150, 320), g = ri(40, t - 60); return Q(`Een boek heeft ${t} bladzijden. Je hebt er al ${g} gelezen. Hoeveel bladzijden moet je nog lezen?`, `Bir kitap ${t} sayfa. ${g} sayfasını okudun. Kaç sayfa daha okuman gerekiyor?`, t - g, "",
      `${t} − ${g} = ${t - g}.`, `${t} − ${g} = ${t - g}.`); },
    () => { const a = ri(120, 380), b = ri(110, 290), c = ri(101, 199); return Q(`In drie bussen zitten ${a}, ${b} en ${c} supporters. Hoeveel supporters zijn dat samen?`, `Üç otobüste ${a}, ${b} ve ${c} taraftar var. Toplam kaç taraftar eder?`, a + b + c, "",
      `${a} + ${b} = ${a + b}. ${a + b} + ${c} = ${a + b + c}.`, `${a} + ${b} = ${a + b}. ${a + b} + ${c} = ${a + b + c}.`); },
    () => { const s = ri(60, 90) * 10, a = ri(101, 299), b = ri(101, s - a - 50); return Q(`In een zaal passen ${s} mensen. Er zitten al ${a} mensen en er komen er nog ${b} bij. Hoeveel plaatsen zijn er dan nog vrij?`, `Bir salona ${s} kişi sığıyor. İçeride ${a} kişi var, ${b} kişi daha geliyor. Kaç yer boş kalır?`, s - a - b, "",
      `${a} + ${b} = ${a + b}. ${s} − ${a + b} = ${s - a - b}.`, `${a} + ${b} = ${a + b}. ${s} − ${a + b} = ${s - a - b}.`); }
  ]
];

// ----- Delen
S_GEN.delen = [
  [
    () => { const a = ri(3, 9), b = ri(2, 10); return Q(`Hoeveel is ${a * b} : ${a}?`, `${a * b} : ${a} kaç eder?`, b, "", `${b} × ${a} = ${a * b}, dus ${a * b} : ${a} = ${b}.`, `${b} × ${a} = ${a * b}, yani ${a * b} : ${a} = ${b}.`); },
    () => { const a = ri(3, 8), b = ri(3, 9); return Q(`Je verdeelt ${a * b} knikkers eerlijk over ${a} kinderen. Hoeveel krijgt elk kind?`, `${a * b} bilyeyi ${a} çocuğa eşit paylaştırıyorsun. Her çocuğa kaç bilye düşer?`, b, "", `${a * b} : ${a} = ${b}.`, `${a * b} : ${a} = ${b}.`); },
    () => { const a = ri(2, 9), b = ri(2, 9); return Q(`Hoeveel is ${a * b * 10} : ${a}?`, `${a * b * 10} : ${a} kaç eder?`, b * 10, "", `${a * b} : ${a} = ${b}, dus ${a * b * 10} : ${a} = ${b * 10}.`, `${a * b} : ${a} = ${b}, yani ${a * b * 10} : ${a} = ${b * 10}.`); }
  ],
  [
    () => { const a = ri(3, 9), b = ri(2, 9), r = ri(1, a - 1); return Q(`${a * b + r} : ${a}. Hoeveel is de <b>rest</b>?`, `${a * b + r} : ${a}. <b>Kalan</b> kaçtır?`, r, "",
      `${b} × ${a} = ${a * b}. ${a * b + r} − ${a * b} = ${r}. De rest is ${r}.`, `${b} × ${a} = ${a * b}. ${a * b + r} − ${a * b} = ${r}. Kalan ${r}.`); },
    () => { const a = ri(3, 9), b = ri(2, 9), r = ri(1, a - 1); return Q(`Hoeveel <b>hele</b> keren past ${a} in ${a * b + r}?`, `${a}, ${a * b + r} sayısının içinde kaç <b>tam</b> kez vardır?`, b, "",
      `${b} × ${a} = ${a * b} past, ${b + 1} × ${a} = ${a * (b + 1)} is te veel. Dus ${b} keer (rest ${r}).`, `${b} × ${a} = ${a * b} sığar, ${b + 1} × ${a} = ${a * (b + 1)} fazla gelir. Yani ${b} kez (kalan ${r}).`); },
    () => { const a = pick([4, 5, 6, 8]), k = pick([10, 20, 25]); return Q(`Reken handig uit: ${a * k - a} : ${a}  (tip: ${a * k} : ${a} = ${k})`, `Kolay yoldan hesapla: ${a * k - a} : ${a}  (ipucu: ${a * k} : ${a} = ${k})`, k - 1, "",
      `${a * k - a} is één groepje van ${a} minder dan ${a * k}. Dus ${k} − 1 = ${k - 1}.`, `${a * k - a}, ${a * k}'den bir ${a}'lik grup eksiktir. Yani ${k} − 1 = ${k - 1}.`); }
  ],
  [
    () => { const a = pick([4, 5, 6, 8]), b = ri(4, 9), r = ri(1, a - 1); return Q(`${a * b + r} kinderen gaan op schoolreis. In één busje passen ${a} kinderen. Hoeveel busjes zijn er nodig?`, `${a * b + r} çocuk okul gezisine gidiyor. Bir minibüse ${a} çocuk sığıyor. Kaç minibüs gerekir?`, b + 1, "",
      `${b} busjes zijn vol (${a * b} kinderen). Voor de laatste ${r} is nog een busje nodig: ${b + 1}.`, `${b} minibüs dolar (${a * b} çocuk). Kalan ${r} çocuk için bir minibüs daha gerekir: ${b + 1}.`); },
    () => { const a = pick([5, 6, 7, 11]), b = ri(3, 8), r = ri(1, a - 1); return Q(`Er zijn ${a * b + r} kinderen. Ze maken teams van ${a}. Hoeveel <b>volle</b> teams kunnen ze maken?`, `${a * b + r} çocuk var. ${a} kişilik takımlar kuruyorlar. Kaç <b>tam</b> takım kurulabilir?`, b, "",
      `${b} × ${a} = ${a * b}. Er blijven ${r} kinderen over. ${b} volle teams.`, `${b} × ${a} = ${a * b}. ${r} çocuk artar. ${b} tam takım.`); },
    () => { const a = ri(3, 6), b = ri(4, 9), r = ri(1, a - 1); return Q(`Je verdeelt ${a * b + r} stickers eerlijk over ${a} vrienden. Hoeveel stickers blijven er over?`, `${a * b + r} çıkartmayı ${a} arkadaşa eşit paylaştırıyorsun. Kaç çıkartma artar?`, r, "",
      `Elk krijgt ${b}: dat zijn ${a * b} stickers. Over: ${r}.`, `Her biri ${b} alır: ${a * b} çıkartma eder. Artan: ${r}.`); }
  ]
];

// ----- Klok en tijd
const endTime = (nl, tr, start, dur, ex_nl, ex_tr) => {
  const right = clock(start + dur), wrong = [...new Set([dur + 10, dur - 10, dur + 60, dur - 15, dur + 5].map(d => clock(start + d)))].filter(x => x !== right).slice(0, 3);
  return Q(nl, tr, right, "", ex_nl, ex_tr, pickOne(right, wrong));
};
S_GEN.tijd = [
  [
    () => { const h = ri(2, 6); return Q(`Hoeveel minuten zijn ${h} uur?`, `${h} saat kaç dakikadır?`, 60 * h, "minuten", `1 uur = 60 minuten. ${h} × 60 = ${60 * h}.`, `1 saat = 60 dakika. ${h} × 60 = ${60 * h}.`); },
    () => { const [nl, tr, m] = pick([["een kwartier", "çeyrek saat", 15], ["een half uur", "yarım saat", 30], ["drie kwartier", "üç çeyrek saat", 45], ["anderhalf uur", "bir buçuk saat", 90]]); return Q(`Hoeveel minuten is ${nl}?`, `${tr.charAt(0).toUpperCase() + tr.slice(1)} kaç dakikadır?`, m, "minuten", `Een uur is 60 minuten, een kwartier is 15 minuten.`, `Bir saat 60 dakika, çeyrek saat 15 dakikadır.`); },
    () => { const h = ri(2, 11), kind = pick(["kwart over", "half", "kwart voor"]);
      const right = kind === "kwart over" ? `${h}:15` : kind === "half" ? `${h - 1}:30` : `${h - 1}:45`;
      const wrong = shuffle([`${h}:15`, `${h}:30`, `${h}:45`, `${h - 1}:15`, `${h - 1}:30`, `${h - 1}:45`].filter(x => x !== right)).slice(0, 3);
      return Q(`Het is 's ochtends <b>${kind} ${h}</b>. Hoe staat dat op een digitale klok?`, `Sabah, saat Hollandaca söylenişiyle <b>"${kind} ${h}"</b>. Dijital saatte nasıl yazar?`, right, "",
        kind === "half" ? `"Half ${h}" is een half uur vóór ${h} uur: ${right}.` : kind === "kwart voor" ? `"Kwart voor ${h}" is 15 minuten vóór ${h} uur: ${right}.` : `"Kwart over ${h}" is 15 minuten na ${h} uur: ${right}.`,
        kind === "half" ? `"Half ${h}", saat ${h} olmadan yarım saat öncesidir: ${right}.` : kind === "kwart voor" ? `"Kwart voor ${h}", saat ${h} olmadan 15 dakika öncesidir: ${right}.` : `"Kwart over ${h}", saat ${h} olduktan 15 dakika sonrasıdır: ${right}.`, pickOne(right, wrong)); }
  ],
  [
    () => { const s = ri(8, 17) * 60 + pick([0, 15, 30, 45]), d = pick([20, 25, 35, 40, 50, 55, 70, 80]); return Q(`Het is ${clock(s)}. Hoeveel minuten duurt het tot ${clock(s + d)}?`, `Saat şu an ${clock(s)}. Saatin ${clock(s + d)} olmasına kaç dakika var?`, d, "minuten",
      `Tel door tot het hele uur en dan verder: samen ${d} minuten.`, `Önce tam saate, sonra devamını say: toplam ${d} dakika.`); },
    () => { const s = ri(8, 18) * 60 + pick([0, 10, 15, 30, 45, 50]), d = pick([25, 35, 45, 50, 75, 90]); return endTime(`Het is ${clock(s)}. Hoe laat is het ${d} minuten later?`, `Saat ${clock(s)}. ${d} dakika sonra saat kaç olur?`, s, d,
      `${clock(s)} + ${d} minuten = ${clock(s + d)}.`, `${clock(s)} + ${d} dakika = ${clock(s + d)}.`); },
    () => { const d = ri(2, 6); return Q(`Hoeveel uren zitten er in ${d} dagen?`, `${d} gün kaç saattir?`, 24 * d, "uur", `1 dag = 24 uur. ${d} × 24 = ${24 * d}.`, `1 gün = 24 saat. ${d} × 24 = ${24 * d}.`); }
  ],
  [
    () => { const s = ri(13, 19) * 60 + pick([0, 15, 30, 45]), d = pick([85, 95, 100, 105, 110, 125]); return endTime(`Een film begint om ${clock(s)} en duurt ${d} minuten. Hoe laat is de film afgelopen?`, `Bir filmin başlama saati ${clock(s)}. Film ${d} dakika sürüyor. Film saat kaçta biter?`, s, d,
      `${d} minuten = ${Math.floor(d / 60)} uur en ${d % 60} minuten. ${clock(s)} → ${clock(s + d)}.`, `${d} dakika = ${Math.floor(d / 60)} saat ${d % 60} dakika. ${clock(s)} → ${clock(s + d)}.`); },
    () => { const s = ri(10, 19) * 60 + pick([0, 30, 45]); return endTime(`Een voetbalwedstrijd begint om ${clock(s)}. Er zijn twee helften van 45 minuten en een pauze van 15 minuten. Hoe laat is de wedstrijd afgelopen?`, `Bir futbol maçının başlama saati ${clock(s)}. 45'er dakikalık iki devre ve 15 dakikalık bir ara var. Maç saat kaçta biter?`, s, 105,
      `45 + 15 + 45 = 105 minuten = 1 uur en 45 minuten. ${clock(s)} → ${clock(s + 105)}.`, `45 + 15 + 45 = 105 dakika = 1 saat 45 dakika. ${clock(s)} → ${clock(s + 105)}.`); },
    () => { const s = ri(7, 9) * 60 + pick([5, 20, 35, 50]), d = pick([35, 45, 55, 65, 75]); return Q(`De trein vertrekt om ${clock(s)} en komt aan om ${clock(s + d)}. Hoeveel minuten duurt de reis?`, `Trenin kalkış saati ${clock(s)}, varış saati ${clock(s + d)}. Yolculuk kaç dakika sürer?`, d, "minuten",
      `Van ${clock(s)} tot ${clock(s + d)} is ${d} minuten.`, `${clock(s)} ile ${clock(s + d)} arası ${d} dakika.`); }
  ]
];

// ----- Geld (amounts in steps of 5 cent)
const cents = (a, b) => ri(a / 5, b / 5) * 5 / 100;
S_GEN.geld = [
  [
    () => { const a = cents(120, 480), b = cents(50, 350), v = Math.round((a + b) * 100) / 100; return money(`Een broodje kost €${eur(a)} en een flesje sap €${eur(b)}. Hoeveel betaal je samen?`, `Bir sandviç ${eur(a)} euro, bir şişe meyve suyu ${eur(b)} euro. Toplam ne kadar ödersin?`, v,
      `€${eur(a)} + €${eur(b)} = €${eur(v)}.`, `${eur(a)} + ${eur(b)} = ${eur(v)} euro.`); },
    () => { const e = ri(1, 4), c = pick([20, 50]), n = ri(2, 4), v = Math.round((e * 2 + n * c / 100) * 100) / 100; return money(`Je hebt ${e} munten van 2 euro en ${n} munten van ${c} cent. Hoeveel euro heb je?`, `${e} tane 2 euroluk ve ${n} tane ${c} sentlik madeni paran var. Kaç euron var?`, v,
      `${e} × 2 = ${e * 2} euro. ${n} × ${c} cent = ${n * c} cent. Samen €${eur(v)}.`, `${e} × 2 = ${e * 2} euro. ${n} × ${c} sent = ${n * c} sent. Toplam ${eur(v)} euro.`); },
    () => { const e = ri(2, 9); return Q(`Hoeveel cent is ${e} euro?`, `${e} euro kaç senttir?`, 100 * e, "cent", `1 euro = 100 cent. ${e} × 100 = ${100 * e}.`, `1 euro = 100 sent. ${e} × 100 = ${100 * e}.`); }
  ],
  [
    () => { const p = cents(120, 880), bill = p < 5 ? 5 : 10, v = Math.round((bill - p) * 100) / 100; return money(`Je koopt iets van €${eur(p)} en betaalt met een briefje van ${bill} euro. Hoeveel krijg je terug?`, `${eur(p)} euroluk bir şey alıyorsun ve ${bill} euroluk banknotla ödüyorsun. Kaç euro para üstü alırsın?`, v,
      `Vul aan van €${eur(p)} tot €${bill}: €${eur(v)}.`, `${eur(p)} eurodan ${bill} euroya tamamla: ${eur(v)} euro.`); },
    () => { const p = cents(1050, 1850), v = Math.round((20 - p) * 100) / 100; return money(`Een spel kost €${eur(p)}. Je betaalt met 20 euro. Hoeveel krijg je terug?`, `Bir oyun ${eur(p)} euro. 20 euroyla ödüyorsun. Kaç euro para üstü alırsın?`, v,
      `20 − ${eur(p)} = ${eur(v)}.`, `20 − ${eur(p)} = ${eur(v)}.`); },
    () => { const n = ri(3, 6), p = pick([0.5, 1.5, 2.5, 0.75, 1.25]), v = Math.round(n * p * 100) / 100; return money(`Eén ijsje kost €${eur(p)}. Hoeveel kosten ${n} ijsjes?`, `Bir dondurma ${eur(p)} euro. ${n} dondurma ne kadar tutar?`, v,
      `${n} × €${eur(p)} = €${eur(v)}.`, `${n} × ${eur(p)} = ${eur(v)} euro.`); }
  ],
  [
    () => { const n = ri(2, 4), p = cents(150, 400), tot = Math.round(n * p * 100) / 100, bill = tot >= 10 ? 20 : 10, v = Math.round((bill - tot) * 100) / 100; return money(`Je koopt ${n} schriften van €${eur(p)} per stuk en betaalt met ${bill} euro. Hoeveel krijg je terug?`, `Tanesi ${eur(p)} euro olan ${n} defter alıyorsun ve ${bill} euroyla ödüyorsun. Kaç euro para üstü alırsın?`, v,
      `${n} × €${eur(p)} = €${eur(tot)}. ${bill} − ${eur(tot)} = ${eur(v)}.`, `${n} × ${eur(p)} = ${eur(tot)} euro. ${bill} − ${eur(tot)} = ${eur(v)}.`); },
    () => { const w = pick([2, 3, 4, 5]), goal = w * ri(6, 15); return Q(`Je krijgt elke week €${w} zakgeld. Je wilt een bal van €${goal} kopen. Hoeveel weken moet je sparen?`, `Her hafta ${w} euro harçlık alıyorsun. ${goal} euroluk bir top almak istiyorsun. Kaç hafta para biriktirmen gerekir?`, goal / w, "weken",
      `${goal} : ${w} = ${goal / w} weken.`, `${goal} : ${w} = ${goal / w} hafta.`); },
    () => { const have = ri(11, 15), a = cents(350, 600), b = cents(250, 450), v = Math.round((have - a - b) * 100) / 100; return money(`Je hebt €${have}. Je koopt een tijdschrift van €${eur(a)} en een zak snoep van €${eur(b)}. Hoeveel geld heb je over?`, `${have} euron var. ${eur(a)} euroluk bir dergi ve ${eur(b)} euroluk bir paket şeker alıyorsun. Kaç euron kalır?`, v,
      `€${eur(a)} + €${eur(b)} = €${eur(Math.round((a + b) * 100) / 100)}. ${have} − ${eur(Math.round((a + b) * 100) / 100)} = ${eur(v)}.`, `${eur(a)} + ${eur(b)} = ${eur(Math.round((a + b) * 100) / 100)} euro. ${have} − ${eur(Math.round((a + b) * 100) / 100)} = ${eur(v)}.`); }
  ]
];

// ----- Meten: big unit -> small unit and back. [big nl, big tr, small nl, small tr, factor]
const UNITS = [["meter", "metre", "centimeter", "santimetre", 100], ["kilometer", "kilometre", "meter", "metre", 1000], ["kilogram", "kilogram", "gram", "gram", 1000], ["liter", "litre", "milliliter", "mililitre", 1000], ["centimeter", "santimetre", "millimeter", "milimetre", 10]];
S_GEN.meten = [
  [
    () => { const [bn, bt, sn, st, f] = pick(UNITS), a = ri(2, 9); return Q(`Hoeveel ${sn} is ${a} ${bn}?`, `${a} ${bt} kaç ${st} eder?`, a * f, sn, `1 ${bn} = ${f} ${sn}. ${a} × ${f} = ${a * f}.`, `1 ${bt} = ${f} ${st}. ${a} × ${f} = ${a * f}.`); },
    () => { const [bn, bt, sn, st, f] = pick(UNITS), a = ri(2, 9); return Q(`Hoeveel ${bn} is ${a * f} ${sn}?`, `${a * f} ${st} kaç ${bt} eder?`, a, bn, `${f} ${sn} = 1 ${bn}. ${a * f} : ${f} = ${a}.`, `${f} ${st} = 1 ${bt}. ${a * f} : ${f} = ${a}.`); },
    MC("Waarmee meet je hoe zwaar iets is?", "Bir şeyin ne kadar ağır olduğu neyle ölçülür?", ["kilogram", "kilogram"], [["meter", "metre"], ["liter", "litre"], ["minuten", "dakika"]],
      "Gewicht meet je in gram en kilogram, lengte in meter, inhoud in liter.", "Ağırlık gram ve kilogramla, uzunluk metreyle, hacim litreyle ölçülür.")
  ],
  [
    () => { const m = ri(1, 4), c = ri(1, 19) * 5; return Q(`Hoeveel centimeter is ${m} meter en ${c} centimeter?`, `${m} metre ${c} santimetre kaç santimetredir?`, 100 * m + c, "centimeter", `${m} m = ${100 * m} cm. ${100 * m} + ${c} = ${100 * m + c}.`, `${m} m = ${100 * m} cm. ${100 * m} + ${c} = ${100 * m + c}.`); },
    () => { const [nl, tr, v, sn, st, bn, bt] = pick([["een halve", "yarım", 500, "milliliter", "mililitre", "liter", "litre"], ["anderhalve", "bir buçuk", 1500, "milliliter", "mililitre", "liter", "litre"], ["een halve", "yarım", 500, "gram", "gram", "kilo", "kilo"], ["anderhalve", "bir buçuk", 1500, "meter", "metre", "kilometer", "kilometre"], ["een kwart", "çeyrek", 250, "gram", "gram", "kilo", "kilo"]]);
      return Q(`Hoeveel ${sn} is ${nl} ${bn}?`, `${tr.charAt(0).toUpperCase() + tr.slice(1)} ${bt} kaç ${st} eder?`, v, sn, `1 ${bn} = 1000 ${sn}, dus ${nl} ${bn} = ${v} ${sn}.`, `1 ${bt} = 1000 ${st}, yani ${tr} ${bt} = ${v} ${st}.`); },
    () => { const k = ri(1, 5), g = ri(1, 9) * 100; return Q(`Hoeveel gram is ${k} kilo en ${g} gram?`, `${k} kilo ${g} gram kaç gramdır?`, 1000 * k + g, "gram", `${k} kg = ${1000 * k} g. Samen ${1000 * k + g} g.`, `${k} kg = ${1000 * k} g. Toplam ${1000 * k + g} g.`); }
  ],
  [
    () => { const l = ri(1, 3), g = pick([200, 250, 500]); return Q(`In een fles zit ${l} liter limonade. In één glas gaat ${g} milliliter. Hoeveel glazen kun je vullen?`, `Bir şişede ${l} litre limonata var. Bir bardak ${g} mililitre alıyor. Kaç bardak doldurabilirsin?`, l * 1000 / g, "glazen",
      `${l} liter = ${l * 1000} ml. ${l * 1000} : ${g} = ${l * 1000 / g}.`, `${l} litre = ${l * 1000} ml. ${l * 1000} : ${g} = ${l * 1000 / g}.`); },
    () => { const n = pick([5, 10]), r = pick([200, 400, 600]); return Q(`Je loopt ${n} rondjes om een veld. Eén rondje is ${r} meter. Hoeveel <b>kilometer</b> loop je?`, `Bir sahanın etrafında ${n} tur koşuyorsun. Bir tur ${r} metre. Kaç <b>kilometre</b> koşarsın?`, n * r / 1000, "kilometer",
      `${n} × ${r} = ${n * r} meter = ${n * r / 1000} kilometer.`, `${n} × ${r} = ${n * r} metre = ${n * r / 1000} kilometre.`); },
    () => { const n = ri(3, 8), g = pick([250, 500]); const tot = n * g; return Q(`Een pak rijst weegt ${g} gram. Hoeveel <b>gram</b> wegen ${n} pakken samen?`, `Bir paket pirinç ${g} gram. ${n} paket toplam kaç <b>gram</b> eder?`, tot, "gram",
      `${n} × ${g} = ${tot} gram${tot % 1000 === 0 ? ` = ${tot / 1000} kilo` : ""}.`, `${n} × ${g} = ${tot} gram${tot % 1000 === 0 ? ` = ${tot / 1000} kilo` : ""}.`); }
  ]
];

// ----- Breuken (groep 5-6): a part of a whole
S_GEN.breuken = [
  [
    () => { const n = ri(4, 30) * 2; return Q(`Wat is de helft van ${n}?`, `${n} sayısının yarısı kaçtır?`, n / 2, "", `${n} : 2 = ${n / 2}.`, `${n} : 2 = ${n / 2}.`); },
    () => { const n = ri(2, 15) * 4; return Q(`Wat is een kwart (¼) van ${n}?`, `${n} sayısının çeyreği (¼) kaçtır?`, n / 4, "", `Een kwart is delen door 4: ${n} : 4 = ${n / 4}.`, `Çeyrek, 4'e bölmek demektir: ${n} : 4 = ${n / 4}.`); },
    () => { const n = pick([3, 4, 6, 8]), k = ri(1, n - 1); return Q(`De cirkel is in ${n} gelijke stukken verdeeld. Hoeveel stukken zijn gekleurd?`, `Daire ${n} eşit parçaya bölünmüş. Kaç parça boyalı?`, k, "",
      `${k} van de ${n} stukken zijn gekleurd. Dat schrijf je als ${k}/${n}.`, `${n} parçanın ${k} tanesi boyalı. Bu ${k}/${n} diye yazılır.`, { fig: pie(n, k) }); }
  ],
  [
    () => { const d = pick([3, 4, 5]), k = ri(2, d - 1), n = d * ri(2, 9); return Q(`Wat is ${k}/${d} van ${n}?`, `${n} sayısının ${k}/${d} kadarı kaçtır?`, n / d * k, "",
      `Eerst 1/${d}: ${n} : ${d} = ${n / d}. Dan keer ${k}: ${n / d * k}.`, `Önce 1/${d}: ${n} : ${d} = ${n / d}. Sonra ${k} ile çarp: ${n / d * k}.`); },
    () => { const [a, b] = pick([["1/2", "1/4"], ["1/3", "1/6"], ["3/4", "1/2"], ["1/2", "1/3"], ["2/3", "1/3"], ["1/4", "1/8"]]); return Q(`Welke breuk is het <b>grootst</b>?`, `Hangi kesir daha <b>büyüktür</b>?`, a, "",
      `Denk aan een pizza: bij ${a} krijg je een groter stuk dan bij ${b}.`, `Pizzayı düşün: ${a} ile ${b}'den daha büyük bir parça alırsın.`, pickOne(a, [b])); },
    () => { const n = ri(2, 5); return Q(`Hoeveel kwarten (¼) zitten er in ${n} hele pizza's?`, `${n} bütün pizzada kaç çeyrek (¼) vardır?`, 4 * n, "", `In één hele zitten 4 kwarten. ${n} × 4 = ${4 * n}.`, `Bir bütünde 4 çeyrek var. ${n} × 4 = ${4 * n}.`); }
  ],
  [
    () => { const n = pick([6, 8, 12]), k = ri(2, n - 2); return Q(`Een pizza is in ${n} gelijke punten gesneden. Je eet er ${k} op. Hoeveel punten zijn er nog over?`, `Bir pizza ${n} eşit dilime kesilmiş. ${k} dilim yiyorsun. Kaç dilim kalır?`, n - k, "",
      `${n} − ${k} = ${n - k}. Er is nog ${n - k}/${n} van de pizza.`, `${n} − ${k} = ${n - k}. Pizzanın ${n - k}/${n}'i kaldı.`, { fig: pie(n, k) }); },
    () => { const d = pick([3, 4]), n = d * ri(5, 8); return Q(`In een klas zitten ${n} kinderen. 1/${d} van de kinderen komt met de fiets. Hoeveel kinderen komen met de fiets?`, `Bir sınıfta ${n} çocuk var. Çocukların 1/${d} kadarı okula bisikletle geliyor. Kaç çocuk bisikletle geliyor?`, n / d, "",
      `${n} : ${d} = ${n / d}.`, `${n} : ${d} = ${n / d}.`); },
    () => { const n = 4 * ri(3, 10); return Q(`Je hebt ${n} euro. Je geeft drie kwart (¾) uit. Hoeveel euro geef je uit?`, `${n} euron var. Dörtte üçünü (¾) harcıyorsun. Kaç euro harcarsın?`, n / 4 * 3, "euro",
      `Een kwart is ${n / 4}. Drie kwart is 3 × ${n / 4} = ${n / 4 * 3}.`, `Çeyreği ${n / 4}. Dörtte üçü 3 × ${n / 4} = ${n / 4 * 3}.`); }
  ]
];

// ----- Afronden en schatten (numbers never end on 5 / 50, so there is no doubt which way to round)
const not5 = () => pick([1, 2, 3, 4, 6, 7, 8, 9]);
S_GEN.afronden = [
  [
    () => { const n = ri(1, 9) * 10 + not5(); const r = Math.round(n / 10) * 10; return Q(`Rond ${n} af op een tiental.`, `${n} sayısını en yakın onluğa yuvarla.`, r, "", `${n} ligt het dichtst bij ${r}.`, `${n}, ${r}'e daha yakındır.`); },
    () => { const n = ri(11, 98) * 10 + not5(); const r = Math.round(n / 10) * 10; return Q(`Rond ${n} af op een tiental.`, `${n} sayısını en yakın onluğa yuvarla.`, r, "", `Kijk naar het laatste cijfer: ${n % 10}. ${n % 10 < 5 ? "Minder dan 5: naar beneden" : "5 of meer: naar boven"}. ${r}.`, `Son rakama bak: ${n % 10}. ${n % 10 < 5 ? "5'ten küçük: aşağı" : "5 ya da büyük: yukarı"}. ${r}.`); }
  ],
  [
    () => { const n = ri(1, 9) * 100 + not5() * 10 + ri(0, 9); const r = Math.round(n / 100) * 100; return Q(`Rond ${n} af op een honderdtal.`, `${n} sayısını en yakın yüzlüğe yuvarla.`, r, "", `Kijk naar de tientallen: ${Math.floor(n / 10) % 10}. ${n} ligt het dichtst bij ${r}.`, `Onlar basamağına bak: ${Math.floor(n / 10) % 10}. ${n}, ${r}'e daha yakındır.`); },
    () => { const n = ri(1, 9) * 1000 + not5() * 100 + ri(0, 99); const r = Math.round(n / 1000) * 1000; return Q(`Rond ${n} af op een duizendtal.`, `${n} sayısını en yakın binliğe yuvarla.`, r, "", `Kijk naar de honderdtallen: ${Math.floor(n / 100) % 10}. ${n} ligt het dichtst bij ${r}.`, `Yüzler basamağına bak: ${Math.floor(n / 100) % 10}. ${n}, ${r}'e daha yakındır.`); },
    () => { const a = ri(2, 6) * 100 + pick([-3, -2, 2, 3, 4]), b = ri(1, 3) * 100 + pick([-4, -2, 1, 3]); const r = Math.round(a / 100) * 100 + Math.round(b / 100) * 100;
      return Q(`Schat het antwoord: ${a} + ${b} is ongeveer …`, `Tahmin et: ${a} + ${b} yaklaşık kaç eder?`, String(r), "", `${a} is ongeveer ${Math.round(a / 100) * 100}, ${b} is ongeveer ${Math.round(b / 100) * 100}. Samen ongeveer ${r}.`, `${a} yaklaşık ${Math.round(a / 100) * 100}, ${b} yaklaşık ${Math.round(b / 100) * 100}. Toplam yaklaşık ${r}.`, pickOne(r, [r + 100, r - 100, r + 200])); }
  ],
  [
    () => { const ps = [ri(2, 4) - 0.01, ri(1, 3) - 0.05, ri(3, 5) - 0.02, ri(1, 2) - 0.01].map(x => Math.round(x * 100) / 100); const r = ps.reduce((s, x) => s + Math.round(x), 0);
      return Q(`Je koopt vier dingen: €${ps.map(eur).join(", €")}. Ongeveer hoeveel euro is dat samen?`, `Dört şey alıyorsun: ${ps.map(eur).join(" euro, ")} euro. Toplam yaklaşık kaç euro eder?`, r, "euro",
        `Rond elke prijs af op hele euro's: ${ps.map(x => Math.round(x)).join(" + ")} = ${r}.`, `Her fiyatı tam euroya yuvarla: ${ps.map(x => Math.round(x)).join(" + ")} = ${r}.`); },
    () => { const n = ri(21, 48) * 1000 + not5() * 100 + ri(0, 99); const r = Math.round(n / 1000) * 1000; return Q(`In een stadion zitten ${n.toLocaleString("nl-NL")} toeschouwers. De krant schrijft: "ongeveer … duizend toeschouwers". Welk getal hoort daar?`, `Bir stadyumda ${n.toLocaleString("nl-NL")} seyirci var. Gazete "yaklaşık … bin seyirci" diye yazıyor. Boşluğa hangi sayı gelir?`, r / 1000, "",
      `${n.toLocaleString("nl-NL")} afgerond op een duizendtal is ${r.toLocaleString("nl-NL")}: ${r / 1000} duizend.`, `${n.toLocaleString("nl-NL")}, en yakın binliğe yuvarlanınca ${r.toLocaleString("nl-NL")} olur: ${r / 1000} bin.`); },
    () => { const p = ri(2, 8) * 10 - 1, n = ri(3, 6); return Q(`Eén kaartje kost €${p}. Ongeveer hoeveel euro kosten ${n} kaartjes? Reken met een rond getal.`, `Bir bilet ${p} euro. ${n} bilet yaklaşık kaç euro tutar? Yuvarlak sayıyla hesapla.`, (p + 1) * n, "euro",
      `€${p} is ongeveer €${p + 1}. ${n} × ${p + 1} = ${(p + 1) * n}.`, `${p} euro yaklaşık ${p + 1} euro. ${n} × ${p + 1} = ${(p + 1) * n}.`); }
  ]
];

// ----- Grote getallen: place value
S_GEN.grotegetallen = [
  [
    () => { const d = [ri(1, 9), ri(0, 9), ri(1, 9), ri(1, 9)]; const n = d[0] * 1000 + d[1] * 100 + d[2] * 10 + d[3]; return Q(`Welk getal is dit? ${d[0]} duizendtallen, ${d[1]} honderdtallen, ${d[2]} tientallen en ${d[3]} eenheden.`, `Bu hangi sayı? ${d[0]} binlik, ${d[1]} yüzlük, ${d[2]} onluk ve ${d[3]} birlik.`, n, "",
      `${d[0] * 1000} + ${d[1] * 100} + ${d[2] * 10} + ${d[3]} = ${n}.`, `${d[0] * 1000} + ${d[1] * 100} + ${d[2] * 10} + ${d[3]} = ${n}.`); },
    () => { const n = ri(12, 98) * 100 + ri(11, 89), s = pick([10, 100, 1000]); return Q(`Welk getal is ${s} meer dan ${n}?`, `${n} sayısından ${s} fazla olan sayı hangisidir?`, n + s, "", `${n} + ${s} = ${n + s}.`, `${n} + ${s} = ${n + s}.`); },
    () => { const a = ri(1001, 9998); let b = a + pick([-900, -90, -9, 9, 90, 900]); return Q(`Welk getal is het <b>grootst</b>?`, `Hangi sayı daha <b>büyüktür</b>?`, String(Math.max(a, b)), "", `Vergelijk van links naar rechts, cijfer voor cijfer.`, `Soldan sağa, basamak basamak karşılaştır.`, pickOne(Math.max(a, b), [Math.min(a, b)])); }
  ],
  [
    () => { const pos = pick([1, 2, 3, 4]), dgt = ri(1, 9); const ds = [ri(1, 9), ri(0, 9), ri(0, 9), ri(0, 9), ri(0, 9)].map(x => x === dgt ? (x + 1) % 10 || 1 : x); ds[4 - pos] = dgt; const n = Number(ds.join("")); const val = dgt * 10 ** pos;
      return Q(`Hoeveel is het cijfer ${dgt} waard in het getal ${n.toLocaleString("nl-NL")}?`, `${n.toLocaleString("nl-NL")} sayısında ${dgt} rakamının değeri kaçtır?`, val, "",
        `De ${dgt} staat op de plaats van de ${["", "tientallen", "honderdtallen", "duizendtallen", "tienduizendtallen"][pos]}: ${val}.`, `${dgt} rakamı ${["", "onlar", "yüzler", "binler", "on binler"][pos]} basamağında: ${val}.`); },
    () => { const a = ri(2, 9) * 1000, b = a + pick([1000, 2000]); return Q(`Welk getal ligt precies in het midden tussen ${a} en ${b}?`, `${a} ile ${b}'in tam ortasındaki sayı hangisidir?`, (a + b) / 2, "", `Het verschil is ${b - a}. De helft is ${(b - a) / 2}. ${a} + ${(b - a) / 2} = ${(a + b) / 2}.`, `Fark ${b - a}. Yarısı ${(b - a) / 2}. ${a} + ${(b - a) / 2} = ${(a + b) / 2}.`); },
    () => { const n = ri(21, 97) * 1000, s = pick([100, 1000, 10000]); return Q(`Welk getal is ${s.toLocaleString("nl-NL")} minder dan ${n.toLocaleString("nl-NL")}?`, `${n.toLocaleString("nl-NL")} sayısından ${s.toLocaleString("nl-NL")} eksik olan sayı hangisidir?`, n - s, "", `${n} − ${s} = ${n - s}.`, `${n} − ${s} = ${n - s}.`); }
  ],
  [
    () => { const a = ri(12, 45) * 1000, b = ri(2, 9) * 1000 + ri(1, 9) * 100; return Q(`In een stadion passen ${a.toLocaleString("nl-NL")} mensen. Er zijn ${b.toLocaleString("nl-NL")} plaatsen leeg. Hoeveel mensen zijn er?`, `Bir stadyuma ${a.toLocaleString("nl-NL")} kişi sığıyor. ${b.toLocaleString("nl-NL")} yer boş. Stadyumda kaç kişi var?`, a - b, "",
      `${a} − ${b} = ${a - b}.`, `${a} − ${b} = ${a - b}.`); },
    () => { const p = ri(3, 9) * 100, n = pick([10, 20, 100]); return Q(`Een school koopt ${n} tablets van €${p} per stuk. Hoeveel euro kost dat samen?`, `Bir okul, tanesi ${p} euro olan ${n} tablet alıyor. Toplam kaç euro tutar?`, p * n, "euro", `${n} × ${p} = ${p * n}.`, `${n} × ${p} = ${p * n}.`); },
    () => { const a = ri(11, 39) * 1000 + ri(1, 9) * 100, b = ri(11, 39) * 1000 + ri(1, 9) * 100; return Q(`Stad A heeft ${a.toLocaleString("nl-NL")} inwoners en stad B ${b.toLocaleString("nl-NL")}. Hoeveel inwoners hebben ze samen?`, `A şehrinin ${a.toLocaleString("nl-NL")}, B şehrinin ${b.toLocaleString("nl-NL")} nüfusu var. İkisinin toplam nüfusu kaçtır?`, a + b, "", `${a} + ${b} = ${a + b}.`, `${a} + ${b} = ${a + b}.`); }
  ]
];

// ================================================================ groep 7-8

// ----- Breuken, kommagetallen en procenten: the same number written three ways. [breuk, komma, procent]
const SAME = [["1/2", 0.5, 50], ["1/4", 0.25, 25], ["3/4", 0.75, 75], ["1/5", 0.2, 20], ["1/10", 0.1, 10], ["2/5", 0.4, 40], ["3/10", 0.3, 30], ["4/5", 0.8, 80]];
S_GEN.breukproc = [
  [
    () => { const [b, k, p] = pick(SAME); return Q(`Hoeveel procent is ${b}?`, `${b} yüzde kaçtır?`, p, "%", `${b} = ${dec(k)} = ${p}%.`, `${b} = ${dec(k)} = %${p}.`); },
    () => { const [b, k, p] = pick(SAME); return decQ(`Schrijf ${b} als kommagetal.`, `${b} kesrini ondalık sayı olarak yaz.`, k, "", `${b} = ${dec(k)} (= ${p}%).`, `${b} = ${dec(k)} (= %${p}).`); },
    () => { const [b, k, p] = pick(SAME); const wrong = shuffle(SAME.filter(x => x[0] !== b)).slice(0, 3).map(x => x[0]); return Q(`Welke breuk is hetzelfde als ${p}%?`, `%${p} hangi kesirle aynıdır?`, b, "", `${p}% = ${p}/100 = ${b}.`, `%${p} = ${p}/100 = ${b}.`, pickOne(b, wrong)); }
  ],
  [
    () => { const d = pick([3, 4, 5, 8]), k = ri(2, d - 1), n = d * ri(3, 12); return Q(`Hoeveel is ${k}/${d} van ${n}?`, `${n} sayısının ${k}/${d} kadarı kaçtır?`, n / d * k, "", `${n} : ${d} = ${n / d}. ${n / d} × ${k} = ${n / d * k}.`, `${n} : ${d} = ${n / d}. ${n / d} × ${k} = ${n / d * k}.`); },
    () => { const d = pick([5, 7, 9, 11]), a = ri(1, d - 3), b = ri(1, d - a - 1); return Q(`Hoeveel is ${a}/${d} + ${b}/${d}?`, `${a}/${d} + ${b}/${d} kaç eder?`, `${a + b}/${d}`, "", `De noemers zijn gelijk: tel alleen de tellers op. ${a} + ${b} = ${a + b}, dus ${a + b}/${d}.`, `Paydalar eşit: sadece payları topla. ${a} + ${b} = ${a + b}, yani ${a + b}/${d}.`, pickOne(`${a + b}/${d}`, [`${a + b}/${2 * d}`, `${a * b}/${d}`, `${a + b + 1}/${d}`])); },
    () => { const [s, k, f] = pick([["1/2", 2, "2/4"], ["1/3", 2, "2/6"], ["2/3", 2, "4/6"], ["3/4", 2, "6/8"], ["1/2", 5, "5/10"], ["2/5", 2, "4/10"]]); const wrong = shuffle(["1/2", "1/3", "2/3", "3/4", "2/5", "1/4"].filter(x => x !== s)).slice(0, 3); return Q(`Vereenvoudig de breuk ${f}.`, `${f} kesrini sadeleştir.`, s, "", `Deel teller en noemer door ${k}: ${s}.`, `Payı ve paydayı ${k}'e böl: ${s}.`, pickOne(s, wrong)); }
  ],
  [
    () => { const [p, b, step] = pick([[10, "1/10", 10], [20, "1/5", 5], [25, "1/4", 4], [50, "1/2", 2], [75, "3/4", 4]]), n = step * ri(4, 12) * (step < 5 ? 5 : 2); const v = n * p / 100;
      return Q(`${p}% van de ${n} leerlingen van een school speelt voetbal. Hoeveel leerlingen zijn dat?`, `Bir okuldaki ${n} öğrencinin yüzde ${p} kadarı futbol oynuyor. Bu kaç öğrenci eder?`, v, "", `${p}% = ${b}. ${b} van ${n} = ${v}.`, `%${p} = ${b}. ${n} sayısının ${b} kadarı = ${v}.`); },
    () => { const d = pick([4, 5, 10]), k = ri(1, d - 1), n = d * ri(2, 8); const p = 100 * k / d; return Q(`Van de ${n} penalty's gaan er ${n / d * k} in het doel. Hoeveel procent is dat?`, `${n} penaltının ${n / d * k} tanesi gol oluyor. Bu yüzde kaç eder?`, p, "%", `${n / d * k} van ${n} = ${k}/${d} = ${p}%.`, `${n} içinden ${n / d * k} = ${k}/${d} = %${p}.`); },
    () => { const a = ri(2, 9), b = pick([0.25, 0.5, 0.75]); return decQ(`Een fles van ${a} liter is voor ${b === 0.5 ? "de helft" : b === 0.25 ? "een kwart" : "drie kwart"} gevuld. Hoeveel liter zit erin? Schrijf het als kommagetal.`, `${a} litrelik bir şişenin ${b === 0.5 ? "yarısı" : b === 0.25 ? "çeyreği" : "dörtte üçü"} dolu. İçinde kaç litre var? Ondalık sayı olarak yaz.`, a * b, "liter", `${a} × ${dec(b)} = ${dec(a * b)}.`, `${a} × ${dec(b)} = ${dec(a * b)}.`); }
  ]
];

// ----- Procenten
S_GEN.procenten = [
  [
    () => { const n = ri(2, 40) * 10; return Q(`Hoeveel is 10% van ${n}?`, `${n} sayısının %10'u kaçtır?`, n / 10, "", `10% is delen door 10: ${n} : 10 = ${n / 10}.`, `%10, 10'a bölmek demektir: ${n} : 10 = ${n / 10}.`); },
    () => { const n = ri(3, 40) * 4, p = pick([50, 25]); return Q(`Hoeveel is ${p}% van ${n}?`, `${n} sayısının yüzde ${p} kadarı kaçtır?`, n * p / 100, "", `${p}% is ${p === 50 ? "de helft" : "een kwart"}: ${n} : ${p === 50 ? 2 : 4} = ${n * p / 100}.`, `%${p}, ${p === 50 ? "yarısı" : "çeyreği"} demektir: ${n} : ${p === 50 ? 2 : 4} = ${n * p / 100}.`); },
    () => { const n = ri(2, 20) * 100; return Q(`Hoeveel is 1% van ${n}?`, `${n} sayısının %1'i kaçtır?`, n / 100, "", `1% is delen door 100: ${n / 100}.`, `%1, 100'e bölmek demektir: ${n / 100}.`); }
  ],
  [
    () => { const n = ri(2, 20) * 10, p = pick([20, 30, 40, 60, 70]); return Q(`Hoeveel is ${p}% van ${n}?`, `${n} sayısının %${p} kadarı kaçtır?`, n * p / 100, "", `10% = ${n / 10}. ${p}% = ${p / 10} × ${n / 10} = ${n * p / 100}.`, `%10 = ${n / 10}. %${p} = ${p / 10} × ${n / 10} = ${n * p / 100}.`); },
    () => { const n = ri(2, 12) * 10, p = pick([10, 20, 25, 50]); const v = n - n * p / 100; return Q(`Een jas kost €${n}. Je krijgt ${p}% korting. Hoeveel betaal je?`, `Bir mont ${n} euro. %${p} indirim var. Kaç euro ödersin?`, v, "euro", `Korting: ${p}% van ${n} = ${n * p / 100}. ${n} − ${n * p / 100} = ${v}.`, `İndirim: ${n} euronun yüzde ${p} kadarı = ${n * p / 100}. ${n} − ${n * p / 100} = ${v}.`, { show: eur(v) + " euro" }); },
    () => { const t = pick([20, 25, 50]), p = pick([20, 40, 60, 80]), good = t * p / 100; return Q(`Je hebt ${good} van de ${t} vragen goed. Hoeveel procent is dat?`, `${t} sorunun ${good} tanesini doğru yaptın. Bu yüzde kaç eder?`, p, "%", `${good} van ${t} is hetzelfde als ${good * 100 / t} van 100: ${p}%.`, `${t} içinden ${good}, 100 içinden ${good * 100 / t} demektir: %${p}.`); }
  ],
  [
    () => { const n = ri(1, 9) * 100; return Q(`Een fiets kost €${n} zonder btw. Er komt 21% btw bij. Hoeveel euro btw is dat?`, `Bir bisiklet KDV'siz ${n} euro. Üzerine %21 KDV ekleniyor. KDV kaç euro eder?`, n * 21 / 100, "euro", `1% van ${n} = ${n / 100}. 21 × ${n / 100} = ${n * 21 / 100}.`, `${n} euronun %1'i = ${n / 100}. 21 × ${n / 100} = ${n * 21 / 100}.`); },
    () => { const n = ri(2, 9) * 100, p = pick([2, 3, 4, 5]); return Q(`Je zet €${n} op een spaarrekening. Je krijgt ${p}% rente per jaar. Hoeveel euro heb je na één jaar?`, `${n} euroyu bir birikim hesabına koyuyorsun. Yılda %${p} faiz alıyorsun. Bir yıl sonra kaç euron olur?`, n + n * p / 100, "euro", `Rente: ${p}% van ${n} = ${n * p / 100}. Samen ${n + n * p / 100}.`, `Faiz: ${n} euronun yüzde ${p} kadarı = ${n * p / 100}. Toplam ${n + n * p / 100}.`); },
    () => { const p = pick([20, 25, 50]), now = ri(2, 9) * (100 - p) / 5 * 1; const old = now * 100 / (100 - p); return Q(`Na ${p}% korting kost een spel €${now}. Hoeveel kostte het spel vóór de korting?`, `%${p} indirimden sonra bir oyun ${now} euro. Oyun indirimden önce kaç euroydu?`, old, "euro", `€${now} is ${100 - p}% van de oude prijs. Oude prijs = ${now} : ${100 - p} × 100 = ${old}.`, `${now} euro, eski fiyatın yüzde ${100 - p} kadarıdır. Eski fiyat = ${now} : ${100 - p} × 100 = ${old}.`, { show: eur(old) + " euro" }); }
  ]
];

// ----- Kommagetallen (worked in hundredths, so 0,1 + 0,2 really is 0,3)
const h2 = x => Math.round(x * 100) / 100;
S_GEN.kommagetallen = [
  [
    () => { const a = ri(1, 9) / 10, b = ri(1, 9) / 10; return decQ(`Hoeveel is ${dec(a)} + ${dec(b)}?`, `${dec(a)} + ${dec(b)} kaç eder?`, h2(a + b), "", `${Math.round(a * 10)} tienden + ${Math.round(b * 10)} tienden = ${Math.round((a + b) * 10)} tienden = ${dec(h2(a + b))}.`, `${Math.round(a * 10)} onda + ${Math.round(b * 10)} onda = ${Math.round((a + b) * 10)} onda = ${dec(h2(a + b))}.`); },
    () => { const a = ri(11, 99) / 10; return decQ(`Hoeveel is ${dec(a)} × 10?`, `${dec(a)} × 10 kaç eder?`, h2(a * 10), "", `Bij keer 10 schuift de komma één plaats naar rechts: ${dec(h2(a * 10))}.`, `10 ile çarpınca virgül bir basamak sağa kayar: ${dec(h2(a * 10))}.`); },
    () => { const a = h2(ri(1, 9) + ri(1, 9) / 10), b = h2(a + pick([-0.3, -0.2, 0.2, 0.4])); const hi = Math.max(a, b), lo = Math.min(a, b); return Q(`Welk getal is het <b>grootst</b>?`, `Hangi sayı daha <b>büyüktür</b>?`, dec(hi), "", `Vergelijk eerst de helen, dan de tienden.`, `Önce tam kısımları, sonra onda birleri karşılaştır.`, pickOne(dec(hi), [dec(lo)])); }
  ],
  [
    () => { const b = ri(11, 49) / 10, a = h2(b + ri(11, 49) / 10); return decQ(`Hoeveel is ${dec(a)} − ${dec(b)}?`, `${dec(a)} − ${dec(b)} kaç eder?`, h2(a - b), "", `Reken in tienden: ${Math.round(a * 10)} − ${Math.round(b * 10)} = ${Math.round((a - b) * 10)}, dus ${dec(h2(a - b))}.`, `Onda birlerle hesapla: ${Math.round(a * 10)} − ${Math.round(b * 10)} = ${Math.round((a - b) * 10)}, yani ${dec(h2(a - b))}.`); },
    () => { const a = pick([0.5, 1.5, 2.5, 0.25, 1.25, 0.75]), n = ri(2, 8); return decQ(`Hoeveel is ${n} × ${dec(a)}?`, `${n} × ${dec(a)} kaç eder?`, h2(a * n), "", `${n} × ${dec(a)} = ${dec(h2(a * n))}.`, `${n} × ${dec(a)} = ${dec(h2(a * n))}.`); },
    () => { const a = ri(2, 9), b = ri(11, 99) / 100; return decQ(`Hoeveel is ${a} + ${dec(b)}?`, `${a} + ${dec(b)} kaç eder?`, h2(a + b), "", `${a} helen en ${Math.round(b * 100)} honderdsten: ${dec(h2(a + b))}.`, `${a} tam ve ${Math.round(b * 100)} yüzde: ${dec(h2(a + b))}.`); }
  ],
  [
    () => { const a = ri(12, 48) / 10, b = ri(12, 48) / 10; return decQ(`Je fietst ${dec(a)} km naar school en daarna ${dec(b)} km naar de sporthal. Hoeveel km fiets je samen?`, `Okula ${dec(a)} km, sonra spor salonuna ${dec(b)} km bisiklet sürüyorsun. Toplam kaç km sürersin?`, h2(a + b), "km", `${dec(a)} + ${dec(b)} = ${dec(h2(a + b))}.`, `${dec(a)} + ${dec(b)} = ${dec(h2(a + b))}.`); },
    () => { const p = pick([1.25, 2.5, 0.75, 1.5]), n = ri(3, 8); return decQ(`Een pak sap bevat ${dec(p)} liter. Hoeveel liter is er in ${n} pakken?`, `Bir kutu meyve suyunda ${dec(p)} litre var. ${n} kutuda kaç litre olur?`, h2(p * n), "liter", `${n} × ${dec(p)} = ${dec(h2(p * n))}.`, `${n} × ${dec(p)} = ${dec(h2(p * n))}.`); },
    () => { const a = ri(131, 159) / 100, b = h2(a + ri(3, 15) / 100); return decQ(`Sem is ${dec(a)} m lang, zijn zus is ${dec(b)} m. Hoeveel <b>meter</b> is zijn zus langer?`, `Sem ${dec(a)} m boyunda, ablası ${dec(b)} m. Ablası kaç <b>metre</b> daha uzun?`, h2(b - a), "m", `${dec(b)} − ${dec(a)} = ${dec(h2(b - a))} m (${Math.round((b - a) * 100)} cm).`, `${dec(b)} − ${dec(a)} = ${dec(h2(b - a))} m (${Math.round((b - a) * 100)} cm).`); }
  ]
];

// ----- Verhoudingen
S_GEN.verhoudingen = [
  [
    () => { const a = pick([2, 3, 4]), k = ri(2, 4), g = ri(2, 6) * 50; return Q(`Een recept voor ${a} personen heeft ${g} gram meel nodig. Hoeveel gram meel is nodig voor ${a * k} personen?`, `${a} kişilik bir tarifte ${g} gram un gerekiyor. ${a * k} kişi için kaç gram un gerekir?`, g * k, "gram", `${a * k} personen is ${k} keer zo veel. ${k} × ${g} = ${g * k}.`, `${a * k} kişi, ${k} katı demek. ${k} × ${g} = ${g * k}.`); },
    () => { const n = ri(2, 6), p = ri(2, 9), m = n * ri(2, 4); return Q(`${n} flessen kosten samen €${n * p}. Hoeveel kosten ${m} flessen?`, `${n} şişe toplam ${n * p} euro. ${m} şişe kaç euro tutar?`, m * p, "euro", `Eén fles kost ${n * p} : ${n} = €${p}. ${m} × ${p} = ${m * p}.`, `Bir şişe ${n * p} : ${n} = ${p} euro. ${m} × ${p} = ${m * p}.`); },
    () => { const p = ri(2, 9), n = ri(3, 8); return Q(`${n} kaartjes kosten samen €${n * p}. Hoeveel kost één kaartje?`, `${n} bilet toplam ${n * p} euro. Bir bilet kaç euro?`, p, "euro", `${n * p} : ${n} = ${p}.`, `${n * p} : ${n} = ${p}.`); }
  ],
  [
    () => { const n = ri(2, 5), m = n + ri(1, 4), p = ri(2, 6); return Q(`${n} kilo appels kost €${n * p}. Hoeveel kost ${m} kilo?`, `${n} kilo elma ${n * p} euro. ${m} kilo kaç euro tutar?`, m * p, "euro", `1 kilo kost €${p}. ${m} kilo: ${m * p}.`, `1 kilo ${p} euro. ${m} kilo: ${m * p}.`); },
    () => { const a = pick([1, 2, 3]), b = a + pick([1, 2, 3]), k = ri(2, 7); return Q(`In een klas is de verhouding jongens : meisjes gelijk aan ${a} : ${b}. Er zijn ${a * k} jongens. Hoeveel meisjes zijn er?`, `Bir sınıfta erkek : kız oranı ${a} : ${b}. Sınıfta ${a * k} erkek var. Kaç kız var?`, b * k, "", `${a * k} : ${a} = ${k}. ${k} × ${b} = ${b * k}.`, `${a * k} : ${a} = ${k}. ${k} × ${b} = ${b * k}.`); },
    () => { const a = pick([1, 2]), b = pick([3, 4, 5]), k = ri(2, 6); return Q(`Limonade maak je van siroop en water in de verhouding ${a} : ${b}. Je gebruikt ${a * k} bekers siroop. Hoeveel bekers limonade krijg je <b>in totaal</b>?`, `Limonata, şurup ve su ${a} : ${b} oranında karıştırılarak yapılıyor. ${a * k} bardak şurup kullanıyorsun. <b>Toplam</b> kaç bardak limonata olur?`, (a + b) * k, "", `Water: ${b * k} bekers. Samen ${a * k} + ${b * k} = ${(a + b) * k}.`, `Su: ${b * k} bardak. Toplam ${a * k} + ${b * k} = ${(a + b) * k}.`); }
  ],
  [
    () => { const t = pick([3, 4, 5]), d = ri(2, 6), u = t * ri(2, 4); return Q(`Een kraan vult ${t * d} liter in ${t} minuten. Hoeveel liter vult de kraan in ${u} minuten?`, `Bir musluk ${t} dakikada ${t * d} litre dolduruyor. ${u} dakikada kaç litre doldurur?`, d * u, "liter", `Per minuut: ${t * d} : ${t} = ${d} liter. ${u} × ${d} = ${d * u}.`, `Dakikada: ${t * d} : ${t} = ${d} litre. ${u} × ${d} = ${d * u}.`); },
    () => { const p = ri(2, 5), n1 = ri(2, 4), n2 = n1 + ri(1, 3), extra = ri(1, n2 - 1);
      // one pack costs exactly p per bar, the other a bit more; which of the two is called A changes each time
      const cheap = { n: n1, price: p * n1 }, dear = { n: n2, price: p * n2 + extra }, aCheap = ri(0, 1) === 1, A = aCheap ? cheap : dear, B = aCheap ? dear : cheap, ans = aCheap ? "A" : "B";
      return Q(`Pak A: ${A.n} repen voor €${A.price}. Pak B: ${B.n} repen voor €${B.price}. Bij welk pak is één reep het goedkoopst?`, `A paketi: ${A.n} çikolata ${A.price} euro. B paketi: ${B.n} çikolata ${B.price} euro. Hangi pakette bir çikolata daha ucuz?`, ans, "",
        `Pak ${ans}: ${cheap.price} : ${cheap.n} = €${p} per reep. Bij het andere pak is het meer dan €${p}.`, `${ans} paketi: ${cheap.price} : ${cheap.n} = tanesi ${p} euro. Diğer pakette ${p} eurodan fazla.`, { opts: [{ v: "A", nl: "pak A", tr: "A paketi" }, { v: "B", nl: "pak B", tr: "B paketi" }] }); },
    () => { const a = ri(2, 4), b = ri(1, 3), tot = (a + b) * ri(3, 8); return Q(`Twee broers verdelen €${tot} in de verhouding ${a} : ${b}. Hoeveel euro krijgt de broer met het grootste deel?`, `İki kardeş ${tot} euroyu ${a} : ${b} oranında paylaşıyor. Büyük payı alan kardeş kaç euro alır?`, tot / (a + b) * Math.max(a, b), "euro", `${a} + ${b} = ${a + b} delen. Eén deel = ${tot / (a + b)}. Grootste deel: ${Math.max(a, b)} × ${tot / (a + b)} = ${tot / (a + b) * Math.max(a, b)}.`, `${a} + ${b} = ${a + b} pay. Bir pay = ${tot / (a + b)}. Büyük pay: ${Math.max(a, b)} × ${tot / (a + b)} = ${tot / (a + b) * Math.max(a, b)}.`); }
  ]
];

// ----- Gemiddelde (numbers are built so the average is whole)
const withMean = (n, lo, hi) => { const m = ri(lo, hi); const xs = Array.from({ length: n - 1 }, () => m + ri(-Math.min(3, m - 1), 3)); xs.push(m * n - xs.reduce((s, x) => s + x, 0)); return xs[n - 1] > 0 ? [shuffle(xs), m] : withMean(n, lo, hi); };
S_GEN.gemiddelde = [
  [
    () => { const [xs, m] = withMean(3, 4, 12); return Q(`Wat is het gemiddelde van ${xs.join(", ")}?`, `${xs.join(", ")} sayılarının ortalaması kaçtır?`, m, "", `Samen ${m * 3}. ${m * 3} : 3 = ${m}.`, `Toplam ${m * 3}. ${m * 3} : 3 = ${m}.`); },
    () => { const m = ri(5, 15), d = ri(1, 4); return Q(`Wat is het gemiddelde van ${m - d} en ${m + d}?`, `${m - d} ve ${m + d} sayılarının ortalaması kaçtır?`, m, "", `Samen ${2 * m}. ${2 * m} : 2 = ${m}. Het ligt precies in het midden.`, `Toplam ${2 * m}. ${2 * m} : 2 = ${m}. Tam ortadaki sayı.`); }
  ],
  [
    () => { const [xs, m] = withMean(4, 5, 12); return Q(`Wat is het gemiddelde van ${xs.join(", ")}?`, `${xs.join(", ")} sayılarının ortalaması kaçtır?`, m, "", `Samen ${m * 4}. ${m * 4} : 4 = ${m}.`, `Toplam ${m * 4}. ${m * 4} : 4 = ${m}.`); },
    () => { const [xs, m] = withMean(5, 6, 9); return Q(`Je haalt deze cijfers: ${xs.join(", ")}. Wat is je gemiddelde?`, `Şu notları alıyorsun: ${xs.join(", ")}. Ortalaman kaçtır?`, m, "", `Samen ${m * 5}. ${m * 5} : 5 = ${m}.`, `Toplam ${m * 5}. ${m * 5} : 5 = ${m}.`); },
    () => { const [xs, m] = withMean(4, 6, 9); const last = xs[3]; return Q(`Je hebt drie cijfers: ${xs.slice(0, 3).join(", ")}. Welk cijfer moet je voor de vierde toets halen om gemiddeld een ${m} te staan?`, `Üç notun var: ${xs.slice(0, 3).join(", ")}. Ortalamanın ${m} olması için dördüncü sınavdan kaç alman gerekir?`, last, "", `Voor gemiddeld ${m} heb je samen 4 × ${m} = ${4 * m} nodig. Je hebt ${4 * m - last}. Nog nodig: ${last}.`, `Ortalama ${m} için toplam 4 × ${m} = ${4 * m} gerekir. Elinde ${4 * m - last} var. Gereken: ${last}.`); }
  ],
  [
    () => { const [xs, m] = withMean(5, 2, 4); return Q(`Een voetbalteam scoort in vijf wedstrijden ${xs.join(", ")} doelpunten. Hoeveel doelpunten is dat gemiddeld per wedstrijd?`, `Bir futbol takımı beş maçta ${xs.join(", ")} gol atıyor. Maç başına ortalama kaç gol eder?`, m, "", `Samen ${m * 5} doelpunten. ${m * 5} : 5 = ${m}.`, `Toplam ${m * 5} gol. ${m * 5} : 5 = ${m}.`); },
    () => { const m = ri(12, 30), n = ri(4, 7); return Q(`Een klas van ${n} groepjes verzamelt gemiddeld ${m} flessen per groepje. Hoeveel flessen zijn er in totaal verzameld?`, `${n} gruptan oluşan bir sınıf, grup başına ortalama ${m} şişe topluyor. Toplam kaç şişe toplanmıştır?`, m * n, "", `Totaal = gemiddelde × aantal = ${m} × ${n} = ${m * n}.`, `Toplam = ortalama × sayı = ${m} × ${n} = ${m * n}.`); },
    () => { const [xs, m] = withMean(4, 14, 22); return Q(`De temperatuur op vier dagen is ${xs.join(", ")} graden. Wat is de gemiddelde temperatuur?`, `Dört günün sıcaklığı ${xs.join(", ")} derece. Ortalama sıcaklık kaç derecedir?`, m, "graden", `Samen ${m * 4}. ${m * 4} : 4 = ${m}.`, `Toplam ${m * 4}. ${m * 4} : 4 = ${m}.`); }
  ]
];

// ----- Snelheid
S_GEN.snelheid = [
  [
    () => { const v = pick([12, 15, 18, 20]), t = ri(2, 4); return Q(`Je fietst ${v} km per uur. Hoeveel km fiets je in ${t} uur?`, `Saatte ${v} km hızla bisiklet sürüyorsun. ${t} saatte kaç km gidersin?`, v * t, "km", `${t} × ${v} = ${v * t}.`, `${t} × ${v} = ${v * t}.`); },
    () => { const v = pick([80, 90, 100, 120]), t = ri(2, 4); return Q(`Een auto rijdt ${v} km per uur. Hoe ver komt hij in ${t} uur?`, `Bir araba saatte ${v} km gidiyor. ${t} saatte ne kadar yol alır?`, v * t, "km", `${t} × ${v} = ${v * t}.`, `${t} × ${v} = ${v * t}.`); }
  ],
  [
    () => { const v = pick([4, 5, 12, 15, 60, 80]), t = ri(2, 5); return Q(`Je legt ${v * t} km af in ${t} uur. Wat is je snelheid?`, `${t} saatte ${v * t} km yol alıyorsun. Hızın kaçtır?`, v, "km per uur", `Snelheid = afstand : tijd = ${v * t} : ${t} = ${v}.`, `Hız = yol : zaman = ${v * t} : ${t} = ${v}.`); },
    () => { const v = pick([15, 20, 60, 90]), t = ri(2, 5); return Q(`Je moet ${v * t} km rijden en gaat ${v} km per uur. Hoeveel uur doe je erover?`, `${v * t} km gitmen gerekiyor ve saatte ${v} km gidiyorsun. Yolculuk kaç saat sürer?`, t, "uur", `Tijd = afstand : snelheid = ${v * t} : ${v} = ${t}.`, `Zaman = yol : hız = ${v * t} : ${v} = ${t}.`); },
    () => { const v = pick([12, 16, 18, 20, 80, 100]); return Q(`Je gaat ${v} km per uur. Hoeveel km leg je af in een half uur?`, `Saatte ${v} km gidiyorsun. Yarım saatte kaç km yol alırsın?`, v / 2, "km", `Een half uur is de helft: ${v} : 2 = ${v / 2}.`, `Yarım saat, yarısı demektir: ${v} : 2 = ${v / 2}.`); }
  ],
  [
    () => { const v = pick([12, 18]), m = pick([10, 20, 40]); return Q(`Je fietst ${v} km per uur. Hoeveel km fiets je in ${m} minuten?`, `Saatte ${v} km hızla bisiklet sürüyorsun. ${m} dakikada kaç km gidersin?`, v * m / 60, "km", `In 10 minuten fiets je ${v} : 6 = ${v / 6} km. In ${m} minuten: ${m / 10} × ${v / 6} = ${v * m / 60} km.`, `10 dakikada ${v} : 6 = ${v / 6} km gidersin. ${m} dakikada: ${m / 10} × ${v / 6} = ${v * m / 60} km.`); },
    () => { const v = pick([5, 6]), d = v * ri(2, 3), s = ri(8, 10) * 60 + pick([0, 15, 30]); const right = clock(s + d / v * 60); return Q(`Je vertrekt om ${clock(s)} en wandelt ${d} km met ${v} km per uur. Hoe laat kom je aan?`, `Yola çıkış saatin ${clock(s)}. Saatte ${v} km hızla ${d} km yürüyorsun. Saat kaçta varırsın?`, right, "", `${d} : ${v} = ${d / v} uur. ${clock(s)} + ${d / v} uur = ${right}.`, `${d} : ${v} = ${d / v} saat. ${clock(s)} + ${d / v} saat = ${right}.`, pickOne(right, [clock(s + d / v * 60 + 30), clock(s + d / v * 60 - 60), clock(s + d / v * 60 + 60)])); },
    () => { const v1 = pick([60, 80]), t1 = ri(1, 2), v2 = pick([100, 120]), t2 = ri(1, 2); return Q(`Een auto rijdt eerst ${t1} uur met ${v1} km per uur en daarna ${t2} uur met ${v2} km per uur. Hoeveel km rijdt de auto in totaal?`, `Bir araba önce ${t1} saat boyunca saatte ${v1} km, sonra ${t2} saat boyunca saatte ${v2} km gidiyor. Toplam kaç km yol alır?`, v1 * t1 + v2 * t2, "km", `${t1} × ${v1} = ${v1 * t1}. ${t2} × ${v2} = ${v2 * t2}. Samen ${v1 * t1 + v2 * t2}.`, `${t1} × ${v1} = ${v1 * t1}. ${t2} × ${v2} = ${v2 * t2}. Toplam ${v1 * t1 + v2 * t2}.`); }
  ]
];

// ----- Rekenen met letters
S_GEN.letters = [
  [
    () => { const x = ri(2, 20), a = ri(3, 15); return Q(`x + ${a} = ${x + a}. Welk getal is x?`, `x + ${a} = ${x + a}. x hangi sayıdır?`, x, "", `${x + a} − ${a} = ${x}.`, `${x + a} − ${a} = ${x}.`); },
    () => { const x = ri(5, 25), a = ri(2, x - 1); return Q(`x − ${a} = ${x - a}. Welk getal is x?`, `x − ${a} = ${x - a}. x hangi sayıdır?`, x, "", `${x - a} + ${a} = ${x}.`, `${x - a} + ${a} = ${x}.`); },
    () => { const a = ri(2, 9), b = ri(2, 9); return Q(`a = ${a} en b = ${b}. Hoeveel is a + b?`, `a = ${a} ve b = ${b}. a + b kaç eder?`, a + b, "", `${a} + ${b} = ${a + b}.`, `${a} + ${b} = ${a + b}.`); }
  ],
  [
    () => { const x = ri(2, 12), a = ri(2, 9); return Q(`${a} × x = ${a * x}. Welk getal is x?`, `${a} × x = ${a * x}. x hangi sayıdır?`, x, "", `${a * x} : ${a} = ${x}.`, `${a * x} : ${a} = ${x}.`); },
    () => { const x = ri(2, 10), a = ri(2, 5), b = ri(1, 9); return Q(`${a} × x + ${b} = ${a * x + b}. Welk getal is x?`, `${a} × x + ${b} = ${a * x + b}. x hangi sayıdır?`, x, "", `Eerst ${b} eraf: ${a * x}. Dan delen door ${a}: ${x}.`, `Önce ${b} çıkar: ${a * x}. Sonra ${a}'e böl: ${x}.`); },
    () => { const x = ri(2, 9), a = ri(2, 6); return Q(`x = ${x}. Hoeveel is ${a} × x + x?`, `x = ${x}. ${a} × x + x kaç eder?`, (a + 1) * x, "", `${a} × ${x} = ${a * x}. ${a * x} + ${x} = ${(a + 1) * x}.`, `${a} × ${x} = ${a * x}. ${a * x} + ${x} = ${(a + 1) * x}.`); }
  ],
  [
    () => { const x = ri(3, 12), a = ri(2, 4), b = ri(2, 9); return Q(`Ik neem een getal in gedachten. Ik doe het keer ${a} en tel er ${b} bij op. Het antwoord is ${a * x + b}. Welk getal had ik in gedachten?`, `Aklımdan bir sayı tutuyorum. ${a} ile çarpıp ${b} ekliyorum. Sonuç ${a * x + b}. Aklımdaki sayı kaçtı?`, x, "", `Ga terug: ${a * x + b} − ${b} = ${a * x}. ${a * x} : ${a} = ${x}.`, `Geriye git: ${a * x + b} − ${b} = ${a * x}. ${a * x} : ${a} = ${x}.`); },
    () => { const p = ri(2, 6), n = ri(3, 9), f = ri(2, 5); return Q(`Een taxi kost €${f} starttarief en €${p} per kilometer. De rit kost €${f + p * n}. Hoeveel kilometer was de rit?`, `Bir taksi ${f} euro açılış ücreti ve kilometre başına ${p} euro alıyor. Yolculuk ${f + p * n} euro tutuyor. Yolculuk kaç kilometreydi?`, n, "km", `${f + p * n} − ${f} = ${p * n}. ${p * n} : ${p} = ${n}.`, `${f + p * n} − ${f} = ${p * n}. ${p * n} : ${p} = ${n}.`); },
    () => { const x = ri(4, 15), d = ri(2, 8); return Q(`Twee broers zijn samen ${2 * x + d} jaar. De oudste is ${d} jaar ouder dan de jongste. Hoe oud is de <b>jongste</b>?`, `İki kardeşin yaşları toplamı ${2 * x + d}. Büyük olan küçüğünden ${d} yaş büyük. <b>Küçük</b> kardeş kaç yaşında?`, x, "jaar", `Haal het verschil eraf: ${2 * x + d} − ${d} = ${2 * x}. De helft is ${x}.`, `Farkı çıkar: ${2 * x + d} − ${d} = ${2 * x}. Yarısı ${x}.`); }
  ]
];

// ---------------------------------------------------------------- theory
export const S_THEORY = {
  handig: [
    { nl: "<b>Aanvullen</b>: liggen twee getallen dicht bij elkaar, tel dan door van het kleine naar het grote. 403 − 398: van 398 naar 400 is 2, naar 403 is nog 3. Antwoord 5.<br><b>Compenseren</b>: maak er een rond getal van en herstel het daarna. 299 + 146 = 300 + 146 − 1 = 445.<br><b>Verdubbelen en halveren</b>: het dubbele van 240 is 480, de helft van 360 is 180.",
      tr: "<b>Tamamlama</b>: iki sayı birbirine yakınsa küçükten büyüğe doğru say. 403 − 398: 398'den 400'e 2, 403'e 3 daha. Cevap 5.<br><b>Yuvarlayıp düzeltme</b>: sayıyı yuvarla, sonra düzelt. 299 + 146 = 300 + 146 − 1 = 445.<br><b>İki katı ve yarısı</b>: 240'ın iki katı 480, 360'ın yarısı 180." },
    { eg: true, nl: "<b>In de winkel</b>: iets kost €1,98 en je betaalt met €5. De kassa vult aan: 2 cent naar €2, dan €3 naar €5. Je krijgt €3,02 terug. Zo rekent bijna iedereen wisselgeld uit: niet aftrekken maar aanvullen.",
      tr: "<b>Markette</b>: bir şey 1,98 euro ve 5 euroyla ödüyorsun. Kasiyer tamamlar: 2 sent ile 2 euro, sonra 3 euro ile 5 euro. 3,02 euro para üstü alırsın. Para üstünü hemen herkes böyle hesaplar: çıkararak değil, tamamlayarak." }
  ],
  delen: [
    { nl: "<b>Delen</b> is eerlijk verdelen. 24 : 6 = 4, want 4 × 6 = 24. Delen is het omgekeerde van vermenigvuldigen: ken je de tafels, dan kun je delen.<br><b>Rest</b>: soms blijft er iets over. 23 : 4 = 5 rest 3, want 5 × 4 = 20 en 23 − 20 = 3.",
      tr: "<b>Bölme</b>, eşit paylaştırmaktır. 24 : 6 = 4, çünkü 4 × 6 = 24. Bölme, çarpmanın tersidir: çarpım tablosunu biliyorsan bölebilirsin.<br><b>Kalan</b>: bazen bir şeyler artar. 23 : 4 = 5 kalan 3, çünkü 5 × 4 = 20 ve 23 − 20 = 3." },
    { eg: true, nl: "<b>Let op de vraag</b>: 23 kinderen gaan in auto's van 4. Er zijn 5 auto's vol, maar 3 kinderen moeten ook mee: je hebt <b>6</b> auto's nodig. Maak je teams van 4, dan zijn er maar <b>5</b> volle teams. Dezelfde som, een ander antwoord: het ligt aan wat er met de rest gebeurt.",
      tr: "<b>Soruya dikkat</b>: 23 çocuk 4 kişilik arabalara binecek. 5 araba dolar ama kalan 3 çocuk da gidecek: <b>6</b> araba gerekir. 4 kişilik takım kuruyorsan sadece <b>5</b> tam takım olur. İşlem aynı, cevap farklı: kalana ne olduğuna bağlı." }
  ],
  tijd: [
    { nl: "1 uur = 60 minuten. Een kwartier = 15 minuten, een half uur = 30 minuten.<br><b>Let op in het Nederlands</b>: <b>half 4</b> is 3:30, een half uur <b>vóór</b> vier. Kwart over 3 = 3:15, kwart voor 4 = 3:45.<br>Na 12 uur 's middags telt de digitale klok door: 1 uur 's middags is 13:00, 8 uur 's avonds is 20:00.",
      tr: "1 saat = 60 dakika. Çeyrek saat = 15 dakika, yarım saat = 30 dakika.<br><b>Hollandacada dikkat</b>: <b>half 4</b>, 3:30 demektir; dörtten yarım saat <b>önce</b>. Türkçedeki 'üç buçuk' Hollandacada 'half vier'dir. Kwart over 3 = 3:15, kwart voor 4 = 3:45.<br>Öğlen 12'den sonra dijital saat saymaya devam eder: öğleden sonra 1, 13:00'tür; akşam 8, 20:00'dir." },
    { eg: true, nl: "<b>Voetbal</b>: twee helften van 45 minuten en 15 minuten pauze is samen 105 minuten: 1 uur en 3 kwartier. Begint de wedstrijd om 14:30, dan is hij om 16:15 afgelopen.",
      tr: "<b>Futbol</b>: 45'er dakikalık iki devre ve 15 dakika ara, toplam 105 dakika eder: 1 saat 45 dakika. Maç 14:30'da başlarsa 16:15'te biter." }
  ],
  geld: [
    { nl: "1 euro = 100 cent. €2,50 is 2 euro en 50 cent.<br><b>Wisselgeld</b> reken je uit door aan te vullen: iets kost €3,60 en je betaalt met €5. Van €3,60 naar €4 is 40 cent, van €4 naar €5 is €1. Terug: €1,40.",
      tr: "1 euro = 100 sent. 2,50 euro, 2 euro 50 sent demektir.<br><b>Para üstü</b> tamamlayarak hesaplanır: bir şey 3,60 euro ve 5 euroyla ödüyorsun. 3,60'tan 4 euroya 40 sent, 4'ten 5 euroya 1 euro. Para üstü: 1,40 euro." },
    { eg: true, nl: "<b>Sparen</b>: wil je iets van €36 kopen en krijg je €4 zakgeld per week, dan moet je 36 : 4 = 9 weken sparen. Zo zie je meteen of iets haalbaar is.",
      tr: "<b>Para biriktirmek</b>: 36 euroluk bir şey almak istiyorsan ve haftada 4 euro harçlık alıyorsan 36 : 4 = 9 hafta biriktirmen gerekir. Böylece bir şeyin mümkün olup olmadığını hemen görürsün." }
  ],
  meten: [
    { nl: "<b>Lengte</b>: 1 km = 1000 m, 1 m = 100 cm, 1 cm = 10 mm.<br><b>Gewicht</b>: 1 kg = 1000 g.<br><b>Inhoud</b>: 1 liter = 1000 ml.<br>Van groot naar klein: <b>keer</b>. Van klein naar groot: <b>delen</b>.",
      tr: "<b>Uzunluk</b>: 1 km = 1000 m, 1 m = 100 cm, 1 cm = 10 mm.<br><b>Ağırlık</b>: 1 kg = 1000 g.<br><b>Hacim</b>: 1 litre = 1000 ml.<br>Büyük birimden küçüğe: <b>çarp</b>. Küçükten büyüğe: <b>böl</b>." },
    { eg: true, nl: "<b>Om te onthouden</b>: een deur is ongeveer 2 meter hoog. Een pak suiker weegt 1 kilo. In een pak melk zit 1 liter. Een rondje om de atletiekbaan is 400 meter, dus 2,5 rondje is 1 kilometer.",
      tr: "<b>Akılda tutmak için</b>: bir kapı yaklaşık 2 metre yüksekliğindedir. Bir paket şeker 1 kilodur. Bir kutu sütte 1 litre vardır. Atletizm pistinde bir tur 400 metredir, yani 2,5 tur 1 kilometre eder." }
  ],
  breuken: [
    { fig: pie(4, 3), nl: "Een <b>breuk</b> is een deel van een geheel. Het onderste getal (de <b>noemer</b>) zegt in hoeveel gelijke stukken je verdeelt. Het bovenste (de <b>teller</b>) zegt hoeveel stukken je neemt.<br>¾: verdeel in 4 stukken en neem er 3.<br>¾ van 20: eerst 20 : 4 = 5, dan 3 × 5 = 15.",
      tr: "<b>Kesir</b>, bir bütünün parçasıdır. Alttaki sayı (<b>payda</b>) bütünün kaç eşit parçaya bölündüğünü söyler. Üstteki sayı (<b>pay</b>) kaç parça alındığını söyler.<br>¾: 4 parçaya böl, 3'ünü al.<br>20'nin ¾'ü: önce 20 : 4 = 5, sonra 3 × 5 = 15." },
    { eg: true, nl: "<b>Pizza</b>: hoe meer mensen meedelen, hoe kleiner jouw stuk. Daarom is ¼ kleiner dan ½, ook al is 4 meer dan 2.<br><b>Klok</b>: een kwartier is ¼ van een uur, een half uur is ½.",
      tr: "<b>Pizza</b>: ne kadar çok kişi paylaşırsa senin dilimin o kadar küçülür. Bu yüzden, 4 sayısı 2'den büyük olsa da ¼, ½'den küçüktür.<br><b>Saat</b>: çeyrek saat, bir saatin ¼'üdür; yarım saat ½'sidir." }
  ],
  afronden: [
    { nl: "<b>Afronden</b>: zoek het ronde getal dat het dichtst bij ligt. Kijk naar het cijfer rechts van de plaats waarop je afrondt: 0 tot en met 4 → naar beneden, 5 tot en met 9 → naar boven.<br>347 op tientallen: 350. 347 op honderdtallen: 300.<br><b>Schatten</b>: rond eerst af, reken dan. 398 + 203 is ongeveer 400 + 200 = 600.",
      tr: "<b>Yuvarlama</b>: en yakın yuvarlak sayıyı bul. Yuvarladığın basamağın sağındaki rakama bak: 0-4 ise aşağı, 5-9 ise yukarı.<br>347 onluğa: 350. 347 yüzlüğe: 300.<br><b>Tahmin</b>: önce yuvarla, sonra hesapla. 398 + 203 yaklaşık 400 + 200 = 600." },
    { eg: true, nl: "<b>Bij de kassa</b>: €1,99 + €2,95 + €3,98. Reken met 2 + 3 + 4 = ongeveer 9 euro. Zo weet je vóór het afrekenen of je genoeg geld bij je hebt.<br><b>Nieuws</b>: 'ongeveer 40.000 toeschouwers' betekent niet precies 40.000. Het echte getal was misschien 39.612.",
      tr: "<b>Kasada</b>: 1,99 + 2,95 + 3,98 euro. 2 + 3 + 4 = yaklaşık 9 euro diye hesapla. Böylece ödemeden önce paranın yetip yetmeyeceğini bilirsin.<br><b>Haberler</b>: 'yaklaşık 40.000 seyirci' tam 40.000 demek değildir. Gerçek sayı belki 39.612'ydi." }
  ],
  grotegetallen: [
    { nl: "Elk cijfer heeft een <b>plaats</b>, en de plaats bepaalt de waarde. In 46.218:<br>4 = 40.000 (tienduizendtallen), 6 = 6000 (duizendtallen), 2 = 200 (honderdtallen), 1 = 10 (tientallen), 8 = 8 (eenheden).<br>In Nederland staat er een <b>punt</b> tussen de duizendtallen en de honderdtallen: 46.218.",
      tr: "Her rakamın bir <b>basamağı</b> vardır ve değeri basamağına göre değişir. 46.218 sayısında:<br>4 = 40.000 (on binler), 6 = 6000 (binler), 2 = 200 (yüzler), 1 = 10 (onlar), 8 = 8 (birler).<br>Hollanda'da binler ile yüzler arasına <b>nokta</b> konur: 46.218." },
    { eg: true, nl: "<b>Stadion</b>: in de Johan Cruijff ArenA passen ruim 55.000 mensen. Leiderdorp heeft ongeveer 27.000 inwoners: het hele dorp past er twee keer in.",
      tr: "<b>Stadyum</b>: Johan Cruijff ArenA'ya 55.000'den fazla kişi sığar. Leiderdorp'un nüfusu yaklaşık 27.000'dir: bütün kasaba stadyuma iki kez sığar." }
  ],
  breukproc: [
    { nl: "Eén getal, drie schrijfwijzen:<br>½ = 0,5 = 50% &nbsp; ¼ = 0,25 = 25% &nbsp; ¾ = 0,75 = 75%<br>⅕ = 0,2 = 20% &nbsp; 1/10 = 0,1 = 10%<br><b>Procent</b> betekent 'per honderd': 25% = 25/100.<br><b>Gelijknamige breuken optellen</b>: de noemer blijft gelijk, je telt de tellers op. 2/7 + 3/7 = 5/7.",
      tr: "Bir sayı, üç yazılış:<br>½ = 0,5 = %50 &nbsp; ¼ = 0,25 = %25 &nbsp; ¾ = 0,75 = %75<br>⅕ = 0,2 = %20 &nbsp; 1/10 = 0,1 = %10<br><b>Yüzde</b>, 'yüzde kaç' demektir: %25 = 25/100.<br><b>Paydası eşit kesirleri toplama</b>: payda aynı kalır, paylar toplanır. 2/7 + 3/7 = 5/7." },
    { eg: true, nl: "<b>Batterij</b>: staat je telefoon op 50%, dan is hij half vol. Op 25% is er nog een kwart over.<br><b>Voetbal</b>: een keeper stopt 3 van de 4 penalty's: ¾, dus 75%.",
      tr: "<b>Pil</b>: telefonun %50 gösteriyorsa yarı doludur. %25'te çeyreği kalmıştır.<br><b>Futbol</b>: bir kaleci 4 penaltının 3'ünü kurtarıyor: ¾, yani %75." }
  ],
  procenten: [
    { nl: "<b>1%</b> = delen door 100. <b>10%</b> = delen door 10. <b>50%</b> = de helft. <b>25%</b> = een kwart.<br>Andere procenten bouw je daarmee: 30% van 80 = 3 × 8 = 24.<br><b>Korting</b>: reken eerst de korting uit en haal die van de prijs af. 20% korting op €50: korting €10, je betaalt €40.",
      tr: "<b>%1</b> = 100'e böl. <b>%10</b> = 10'a böl. <b>%50</b> = yarısı. <b>%25</b> = çeyreği.<br>Diğer yüzdeleri bunlarla kurarsın: 80'in %30'u = 3 × 8 = 24.<br><b>İndirim</b>: önce indirimi hesapla, sonra fiyattan çıkar. 50 euroda %20 indirim: indirim 10 euro, 40 euro ödersin." },
    { eg: true, nl: "<b>Btw</b>: op de meeste dingen in Nederland zit 21% btw. Kost iets €100 zonder btw, dan betaal je €121.<br><b>Uitverkoop</b>: '50% korting' is de helft van de prijs. 'Tweede artikel gratis' is hetzelfde als 50% korting als je er twee koopt.",
      tr: "<b>KDV</b>: Hollanda'da çoğu üründe %21 KDV vardır. Bir şey KDV'siz 100 euroysa 121 euro ödersin.<br><b>İndirim sezonu</b>: '%50 indirim', fiyatın yarısıdır. 'İkincisi bedava' da, iki tane alırsan %50 indirimle aynı şeydir." }
  ],
  kommagetallen: [
    { nl: "Na de komma komen <b>tienden</b> en <b>honderdsten</b>. 2,75 = 2 helen, 7 tienden en 5 honderdsten.<br>Optellen en aftrekken: zet de komma's onder elkaar. 1,5 + 0,25 = 1,75.<br>Keer 10: de komma schuift één plaats naar rechts. 3,4 × 10 = 34.",
      tr: "Virgülden sonra <b>onda birler</b> ve <b>yüzde birler</b> gelir. 2,75 = 2 tam, 7 onda bir ve 5 yüzde bir.<br>Toplama ve çıkarma: virgülleri alt alta getir. 1,5 + 0,25 = 1,75.<br>10 ile çarpma: virgül bir basamak sağa kayar. 3,4 × 10 = 34." },
    { eg: true, nl: "<b>Geld</b> is een kommagetal: €2,75 is 2 euro en 75 cent.<br><b>Lengte</b>: ben je 1,38 m, dan ben je 1 meter en 38 centimeter.<br><b>Sport</b>: op de 100 meter gaat het om honderdsten van een seconde: 9,58 tegen 9,63.",
      tr: "<b>Para</b> bir ondalık sayıdır: 2,75 euro, 2 euro 75 sent demektir.<br><b>Boy</b>: 1,38 m boyundaysan 1 metre 38 santimetresin.<br><b>Spor</b>: 100 metre koşusunda saniyenin yüzde birleri önemlidir: 9,58'e karşı 9,63." }
  ],
  verhoudingen: [
    { nl: "Een <b>verhouding</b> zegt hoe twee hoeveelheden bij elkaar horen. Wordt de ene 2 keer zo groot, dan de andere ook.<br><b>Verhoudingstabel</b>: 3 flessen kosten €6 → 1 fles kost €2 → 7 flessen kosten €14. Ga via 1.<br>1 : 4 betekent: bij elk deel van het ene horen 4 delen van het andere.",
      tr: "<b>Oran</b>, iki miktarın birbirine nasıl bağlı olduğunu söyler. Biri 2 katına çıkarsa diğeri de çıkar.<br><b>Oran tablosu</b>: 3 şişe 6 euro → 1 şişe 2 euro → 7 şişe 14 euro. 1 tanesi üzerinden git.<br>1 : 4 şu demek: birinden 1 ölçüye karşılık diğerinden 4 ölçü." },
    { eg: true, nl: "<b>Koken</b>: een recept is voor 4 personen en jullie zijn met 8. Alles keer 2.<br><b>Supermarkt</b>: op het prijskaartje staat vaak ook de prijs per kilo of per liter. Daarmee vergelijk je een groot en een klein pak eerlijk.",
      tr: "<b>Yemek</b>: tarif 4 kişilik, siz 8 kişisiniz. Her şeyin 2 katı.<br><b>Market</b>: fiyat etiketinde çoğu zaman kilo ya da litre fiyatı da yazar. Büyük paketle küçük paket böyle adil karşılaştırılır." }
  ],
  gemiddelde: [
    { nl: "<b>Gemiddelde</b>: tel alles op en deel door het aantal.<br>Cijfers 6, 8 en 7: samen 21, gedeeld door 3 = 7.<br>Je kunt het zien als eerlijk verdelen: wie te veel heeft, geeft aan wie te weinig heeft, tot iedereen evenveel heeft.",
      tr: "<b>Ortalama</b>: hepsini topla, sayısına böl.<br>Notlar 6, 8 ve 7: toplam 21, 3'e bölünce 7.<br>Eşit paylaştırmak gibi düşünebilirsin: fazlası olan, azı olana verir; herkes eşitlenir." },
    { eg: true, nl: "<b>Rapport</b>: je gemiddelde cijfer is alle cijfers samen gedeeld door het aantal toetsen. Eén slecht cijfer kun je dus goedmaken.<br><b>Voetbal</b>: een spits met 20 doelpunten in 10 wedstrijden scoort gemiddeld 2 per wedstrijd, ook al scoorde hij soms niets.",
      tr: "<b>Karne</b>: ortalaman, bütün notların toplamının sınav sayısına bölümüdür. Yani bir kötü notu telafi edebilirsin.<br><b>Futbol</b>: 10 maçta 20 gol atan bir forvet, bazı maçlarda hiç atmasa da maç başına ortalama 2 gol atmıştır." }
  ],
  snelheid: [
    { nl: "<b>Snelheid</b> zegt hoeveel kilometer je in één uur aflegt: km per uur.<br><b>Afstand = snelheid × tijd</b><br><b>Snelheid = afstand : tijd</b><br><b>Tijd = afstand : snelheid</b><br>Voorbeeld: 15 km per uur, 2 uur lang → 30 km.",
      tr: "<b>Hız</b>, bir saatte kaç kilometre yol aldığını söyler: saatte km.<br><b>Yol = hız × zaman</b><br><b>Hız = yol : zaman</b><br><b>Zaman = yol : hız</b><br>Örnek: saatte 15 km, 2 saat boyunca → 30 km." },
    { eg: true, nl: "<b>Om te vergelijken</b>: wandelen gaat ongeveer 5 km per uur, fietsen 15, een auto op de snelweg 100. Loop je in een kwartier naar school, dan woon je ruim 1 km van school.",
      tr: "<b>Karşılaştırmak için</b>: yürüyüş saatte yaklaşık 5 km, bisiklet 15, otoyolda araba 100 km hızla gider. Okula 15 dakikada yürüyorsan okuldan 1 km'den biraz uzakta oturuyorsun." }
  ],
  letters: [
    { nl: "Een <b>letter</b> staat voor een getal dat je nog niet kent. x + 5 = 12: welk getal plus 5 is 12? x = 7.<br><b>Terugrekenen</b>: doe alles in omgekeerde volgorde. 3 × x + 2 = 17 → eerst 2 eraf (15), dan delen door 3: x = 5.",
      tr: "<b>Harf</b>, henüz bilmediğin bir sayının yerini tutar. x + 5 = 12: hangi sayıya 5 eklersen 12 olur? x = 7.<br><b>Geriye doğru hesap</b>: her şeyi ters sırayla yap. 3 × x + 2 = 17 → önce 2 çıkar (15), sonra 3'e böl: x = 5." },
    { eg: true, nl: "<b>Raadsel</b>: 'Ik heb een getal in gedachten. Keer 2, plus 3 is 11.' Dat is 2 × x + 3 = 11. Ga terug: 11 − 3 = 8, 8 : 2 = 4.<br><b>Taxi</b>: starttarief plus een bedrag per kilometer. Weet je de prijs, dan reken je terug hoeveel kilometer het was.",
      tr: "<b>Bilmece</b>: 'Aklımdan bir sayı tuttum. 2 ile çarpıp 3 ekleyince 11 oluyor.' Bu 2 × x + 3 = 11 demek. Geriye git: 11 − 3 = 8, 8 : 2 = 4.<br><b>Taksi</b>: açılış ücreti artı kilometre başına ücret. Tutarı biliyorsan kaç kilometre gidildiğini geriye doğru hesaplarsın." }
  ]
};

export const S_WORDS = {
  handig: [["optellen", "toplamak"], ["aftrekken", "çıkarmak"], ["aanvullen", "tamamlamak"], ["het dubbele", "iki katı"], ["de helft", "yarısı"], ["tiental", "onluk"], ["honderdtal", "yüzlük"]],
  delen: [["delen", "bölmek"], ["eerlijk verdelen", "eşit paylaştırmak"], ["rest", "kalan"], ["tafel", "çarpım tablosu"], ["vermenigvuldigen", "çarpmak"]],
  tijd: [["uur", "saat"], ["minuut", "dakika"], ["kwartier", "çeyrek saat"], ["half vier", "üç buçuk"], ["kwart over", "çeyrek geçiyor"], ["kwart voor", "çeyrek var"], ["duren", "sürmek"]],
  geld: [["geld", "para"], ["betalen", "ödemek"], ["wisselgeld", "para üstü"], ["sparen", "biriktirmek"], ["zakgeld", "harçlık"], ["prijs", "fiyat"], ["munt", "madeni para"], ["briefje", "banknot"]],
  meten: [["meten", "ölçmek"], ["lengte", "uzunluk"], ["gewicht", "ağırlık"], ["inhoud", "hacim"], ["omrekenen", "birim çevirmek"], ["wegen", "tartmak"]],
  breuken: [["breuk", "kesir"], ["teller", "pay"], ["noemer", "payda"], ["de helft", "yarım"], ["een kwart", "çeyrek"], ["drie kwart", "dörtte üç"], ["het geheel", "bütün"]],
  afronden: [["afronden", "yuvarlamak"], ["schatten", "tahmin etmek"], ["ongeveer", "yaklaşık"], ["tiental", "onluk"], ["honderdtal", "yüzlük"], ["duizendtal", "binlik"]],
  grotegetallen: [["cijfer", "rakam"], ["getal", "sayı"], ["eenheden", "birler"], ["tientallen", "onlar"], ["honderdtallen", "yüzler"], ["duizendtallen", "binler"], ["inwoners", "nüfus"]],
  breukproc: [["breuk", "kesir"], ["kommagetal", "ondalık sayı"], ["procent", "yüzde"], ["teller", "pay"], ["noemer", "payda"], ["vereenvoudigen", "sadeleştirmek"]],
  procenten: [["procent", "yüzde"], ["korting", "indirim"], ["btw", "KDV"], ["rente", "faiz"], ["uitverkoop", "indirim sezonu"]],
  kommagetallen: [["komma", "virgül"], ["tienden", "onda birler"], ["honderdsten", "yüzde birler"], ["helen", "tam kısım"]],
  verhoudingen: [["verhouding", "oran"], ["verhoudingstabel", "oran tablosu"], ["recept", "tarif"], ["mengen", "karıştırmak"], ["per stuk", "tanesi"]],
  gemiddelde: [["gemiddelde", "ortalama"], ["optellen", "toplamak"], ["delen", "bölmek"], ["cijfer", "not"], ["totaal", "toplam"]],
  snelheid: [["snelheid", "hız"], ["afstand", "yol / mesafe"], ["tijd", "zaman"], ["kilometer per uur", "saatte kilometre"]],
  letters: [["letter", "harf"], ["onbekende", "bilinmeyen"], ["terugrekenen", "geriye doğru hesaplamak"], ["vergelijking", "denklem"]]
};
