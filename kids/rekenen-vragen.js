// Rekenen & meetkunde: topics, short theory and question generators.
// Used by kids/rekenen.html (the page) and admin.html (which topics are open).
//
// Why generators instead of a fixed list: the numbers are drawn at random, so a child can practise the
// same kind of question many times without learning the answers by heart.
// Every question exists in Dutch (school language) and Turkish (home language), so both sets of terms stick.
//
// Agreement on this page: pi = 3, so every answer is a whole number.
//
// A question is: { id, level, nl, tr, answer, unit, ex_nl, ex_tr, fig?, opts? }
//   level 1 = straight sum, 2 = the other way round, 3 = word problem
//   opts  = [{ v, nl, tr }] for a multiple-choice question; without opts the child types a number


// open: shown to students by default. The admin can change this per topic (Firestore settings/rekenen).
export const TOPICS = [
  { id: "meetkunde", nl: "Omtrek en oppervlakte", tr: "Çevre ve alan", sub_nl: "vierkant, rechthoek, cirkel", sub_tr: "kare, dikdörtgen, daire", open: true },
  { id: "som", nl: "Optellen van 1 tot n", tr: "1'den n'e kadar toplam", sub_nl: "1 + 2 + 3 + … slim uitrekenen", sub_tr: "1 + 2 + 3 + … akıllıca hesapla", open: true },
  { id: "machten", nl: "Machten en wortels", tr: "Üslü sayılar ve karekök", sub_nl: "5², 2³, √49", sub_tr: "5², 2³, √49", open: true },
  { id: "fibonacci", nl: "De rij van Fibonacci", tr: "Fibonacci dizisi", sub_nl: "een getallenrij uit de natuur", sub_tr: "doğadaki sayı dizisi", open: true },
  { id: "getallen", nl: "Kwadraat- en driehoeksgetallen", tr: "Kare sayılar ve üçgen sayılar", sub_nl: "patronen in getallen", sub_tr: "sayı örüntüleri", open: false },
  { id: "driehoek", nl: "Oppervlakte van een driehoek", tr: "Üçgenin alanı", sub_nl: "de helft van een rechthoek", sub_tr: "dikdörtgenin yarısı", open: false },
  { id: "samengesteld", nl: "Samengestelde figuren", tr: "Bileşik şekiller", sub_nl: "L-vorm: knip in rechthoeken", sub_tr: "L şekli: dikdörtgenlere böl", open: false },
  { id: "inhoud", nl: "Inhoud", tr: "Hacim", sub_nl: "kubus en doos", sub_tr: "küp ve kutu", open: false },
  { id: "priem", nl: "Priemgetallen en delers", tr: "Asal sayılar ve bölenler", sub_nl: "welke getallen passen erin?", sub_tr: "hangi sayılara bölünür?", open: false },
  { id: "hoeken", nl: "Hoeken", tr: "Açılar", sub_nl: "scherp, recht, stomp", sub_tr: "dar, dik, geniş", open: false },
  { id: "schaal", nl: "Schaal", tr: "Ölçek", sub_nl: "plattegrond en kaart", sub_tr: "kroki ve harita", open: false },
  { id: "negatief", nl: "Negatieve getallen", tr: "Negatif sayılar", sub_nl: "onder nul: thermometer", sub_tr: "sıfırın altı: termometre", open: false },
  { id: "natuurpatronen", nl: "Patronen in de natuur", tr: "Doğadaki örüntüler", sub_nl: "symmetrie, zeshoeken, vertakkingen", sub_tr: "simetri, altıgenler, dallanma", open: false }
];
// band = the school years a topic belongs to ("5-6" or "7-8"); school = true when it is ordinary school material
// (false = enrichment, things we do at home). The page groups the menu by these two.
const BAND78 = ["inhoud", "priem", "schaal", "negatief"];
TOPICS.forEach(t => { t.band = BAND78.includes(t.id) ? "7-8" : "5-6"; t.school = BAND78.includes(t.id); });
TOPICS.push(...S_TOPICS);

import { PI, ri, pick, shuffle, tri, isPrime, divisors, gcd, Q, num, svg, T, maker, isCorrect } from "./vragen-basis.js?v=3";
import { S_TOPICS, S_GEN, S_THEORY, S_WORDS } from "./rekenen-school.js?v=3";
export { PI, isCorrect };

// ---------------------------------------------------------------- figures (small inline SVG, colours from the page)
export const fig = {
  square: a => svg(`<rect class="shape" x="65" y="12" width="90" height="90"/>${T(110, 122, a)}${T(162, 62, a, "start")}`),
  rect: (a, b) => svg(`<rect class="shape" x="35" y="22" width="150" height="76"/>${T(110, 118, a)}${T(192, 64, b, "start")}`),
  circle: (label, diameter) => svg(`<circle class="shape" cx="110" cy="62" r="52"/><circle cx="110" cy="62" r="2.5"/>
    <line x1="${diameter ? 58 : 110}" y1="62" x2="162" y2="62"/>${T(diameter ? 110 : 136, 54, label)}`),
  // room (rectangle) with a round carpet in the middle
  carpet: (a, b, r) => svg(`<rect class="room" x="35" y="14" width="150" height="92"/><circle class="shape" cx="110" cy="60" r="34"/>
    <circle cx="110" cy="60" r="2.5"/><line x1="110" y1="60" x2="144" y2="60"/>${T(127, 53, r)}${T(110, 124, a)}${T(192, 64, b, "start")}`),
  // a x b rectangle drawn as unit squares, so the area can be counted: this is what "oppervlakte" means
  grid: (a, b, la, lb) => { const u = Math.min(170 / a, 96 / b), x0 = (220 - a * u) / 2 - 8, y0 = 8;
    let cells = ""; for (let i = 1; i < a; i++) cells += `<line class="cell" x1="${x0 + i * u}" y1="${y0}" x2="${x0 + i * u}" y2="${y0 + b * u}"/>`;
    for (let j = 1; j < b; j++) cells += `<line class="cell" x1="${x0}" y1="${y0 + j * u}" x2="${x0 + a * u}" y2="${y0 + j * u}"/>`;
    return svg(`<rect class="shape" x="${x0}" y="${y0}" width="${a * u}" height="${b * u}"/>${cells}${T(x0 + a * u / 2, y0 + b * u + 16, la)}${T(x0 + a * u + 6, y0 + b * u / 2 + 4, lb, "start")}`); },
  // squares with sides 1, 1, 2, 3, 5 fit together into one rectangle: the Fibonacci numbers as a picture
  fibsquares: () => svg(`<rect class="shape" x="30" y="10" width="100" height="100"/><rect class="shape" x="130" y="10" width="60" height="60"/>
    <rect class="shape" x="150" y="70" width="40" height="40"/><rect class="shape" x="130" y="70" width="20" height="20"/><rect class="shape" x="130" y="90" width="20" height="20"/>
    ${T(80, 65, 5)}${T(160, 45, 3)}${T(170, 95, 2)}${T(140, 84, 1)}${T(140, 104, 1)}`),
  triangle: (b, h) => svg(`<polygon class="shape" points="35,104 185,104 80,18"/><line class="dash" x1="80" y1="18" x2="80" y2="104"/>
    ${T(110, 122, b)}${T(88, 68, h, "start")}`),
  // L-shape made of a tall left part and a low right part
  lshape: (w1, h1, w2, h2) => svg(`<polygon class="shape" points="52,12 112,12 112,62 172,62 172,108 52,108"/><line class="dash" x1="112" y1="62" x2="112" y2="108"/>
    ${T(82, 124, w1)}${T(142, 124, w2)}${T(46, 64, h1, "end")}${T(178, 90, h2, "start")}`),
  box: (l, b, h) => svg(`<polygon class="shape" points="40,48 140,48 140,108 40,108"/><polygon class="shape" points="40,48 70,22 170,22 140,48"/>
    <polygon class="shape" points="140,48 170,22 170,82 140,108"/>${T(90, 124, l)}${T(162, 106, b, "start")}${T(176, 56, h, "start")}`)
};

// ---------------------------------------------------------------- question generators
// GEN[topic][level - 1] = list of functions; each returns one question with fresh numbers.
const GEN = {};

// ----- Omtrek en oppervlakte (vierkant, rechthoek, cirkel)
GEN.meetkunde = [
  [ // level 1: the sides are known
    () => { const a = ri(2, 12); return Q(`Een vierkant heeft zijden van ${a} cm. Wat is de <b>omtrek</b>?`, `Bir karenin kenarı ${a} cm. <b>Çevresi</b> kaç cm?`, 4 * a, "cm",
      `Omtrek vierkant = 4 × zijde = 4 × ${a} = ${4 * a} cm.`, `Karenin çevresi = 4 × kenar = 4 × ${a} = ${4 * a} cm.`, { fig: fig.square(`${a} cm`) }); },
    () => { const a = ri(2, 12); return Q(`Een vierkant heeft zijden van ${a} cm. Wat is de <b>oppervlakte</b>?`, `Bir karenin kenarı ${a} cm. <b>Alanı</b> kaç cm²?`, a * a, "cm²",
      `Oppervlakte vierkant = zijde × zijde = ${a} × ${a} = ${a * a} cm². Tel de hokjes: het zijn er ook ${a * a}.`, `Karenin alanı = kenar × kenar = ${a} × ${a} = ${a * a} cm². Şekildeki küçük kareleri sayarsan da ${a * a} çıkar.`, { fig: fig.grid(a, a, `${a} cm`, `${a} cm`) }); },
    () => { const b = ri(2, 8), a = b + ri(1, 6); return Q(`Een rechthoek is ${a} cm lang en ${b} cm breed. Wat is de <b>omtrek</b>?`, `Bir dikdörtgenin kenarları ${a} cm ve ${b} cm. <b>Çevresi</b> kaç cm?`, 2 * (a + b), "cm",
      `Omtrek rechthoek = 2 × (lengte + breedte) = 2 × (${a} + ${b}) = ${2 * (a + b)} cm.`, `Dikdörtgenin çevresi = 2 × (uzun + kısa) = 2 × (${a} + ${b}) = ${2 * (a + b)} cm.`, { fig: fig.rect(`${a} cm`, `${b} cm`) }); },
    () => { const b = ri(2, 8), a = b + ri(1, 6); return Q(`Een rechthoek is ${a} cm lang en ${b} cm breed. Wat is de <b>oppervlakte</b>?`, `Bir dikdörtgenin kenarları ${a} cm ve ${b} cm. <b>Alanı</b> kaç cm²?`, a * b, "cm²",
      `Oppervlakte rechthoek = lengte × breedte = ${a} × ${b} = ${a * b} cm². ${b} rijen van ${a} hokjes.`, `Dikdörtgenin alanı = uzun × kısa = ${a} × ${b} = ${a * b} cm². ${b} sıra, her sırada ${a} küçük kare.`, { fig: fig.grid(a, b, `${a} cm`, `${b} cm`) }); },
    () => { const r = ri(2, 15); return Q(`De straal van een cirkel is ${r} cm. Wat is de <b>diameter</b>?`, `Bir dairenin yarıçapı ${r} cm. <b>Çapı</b> kaç cm?`, 2 * r, "cm",
      `Diameter = 2 × straal = 2 × ${r} = ${2 * r} cm.`, `Çap = 2 × yarıçap = 2 × ${r} = ${2 * r} cm.`, { fig: fig.circle(`${r} cm`, false) }); },
    () => { const r = ri(2, 15); return Q(`De diameter van een cirkel is ${2 * r} cm. Wat is de <b>straal</b>?`, `Bir dairenin çapı ${2 * r} cm. <b>Yarıçapı</b> kaç cm?`, r, "cm",
      `Straal = diameter ÷ 2 = ${2 * r} ÷ 2 = ${r} cm.`, `Yarıçap = çap ÷ 2 = ${2 * r} ÷ 2 = ${r} cm.`, { fig: fig.circle(`${2 * r} cm`, true) }); },
    () => { const r = ri(1, 10); return Q(`De straal van een cirkel is ${r} cm. Wat is de <b>omtrek</b>? (π = 3)`, `Bir dairenin yarıçapı ${r} cm. <b>Çevresi</b> kaç cm? (π = 3)`, 2 * PI * r, "cm",
      `Diameter = ${2 * r} cm. Omtrek = π × diameter = ${2 * r}π = 3 × ${2 * r} = ${6 * r} cm.`, `Çap = ${2 * r} cm. Çevre = π × çap = ${2 * r}π = 3 × ${2 * r} = ${6 * r} cm.`, { fig: fig.circle(`${r} cm`, false) }); },
    () => { const r = ri(1, 10); return Q(`De straal van een cirkel is ${r} cm. Wat is de <b>oppervlakte</b>? (π = 3)`, `Bir dairenin yarıçapı ${r} cm. <b>Alanı</b> kaç cm²? (π = 3)`, PI * r * r, "cm²",
      `Oppervlakte = π × straal × straal = ${r * r}π = 3 × ${r * r} = ${3 * r * r} cm².`, `Alan = π × r × r = ${r * r}π = 3 × ${r * r} = ${3 * r * r} cm².`, { fig: fig.circle(`${r} cm`, false) }); }
  ],
  [ // level 2: the other way round
    () => { const a = ri(2, 12); return Q(`De oppervlakte van een vierkant is ${a * a} cm². Hoe lang is één <b>zijde</b>?`, `Bir karenin alanı ${a * a} cm². Bir <b>kenarı</b> kaç cm?`, a, "cm",
      `Welk getal keer zichzelf is ${a * a}? ${a} × ${a} = ${a * a}. De zijde is ${a} cm.`, `Hangi sayı × kendisi = ${a * a}? ${a} × ${a} = ${a * a}. Kenar ${a} cm.`); },
    () => { const a = ri(2, 15); return Q(`De omtrek van een vierkant is ${4 * a} cm. Hoe lang is één <b>zijde</b>?`, `Bir karenin çevresi ${4 * a} cm. Bir <b>kenarı</b> kaç cm?`, a, "cm",
      `Zijde = omtrek ÷ 4 = ${4 * a} ÷ 4 = ${a} cm.`, `Kenar = çevre ÷ 4 = ${4 * a} ÷ 4 = ${a} cm.`); },
    () => { const b = ri(2, 9), a = b + ri(1, 5); return Q(`De oppervlakte van een rechthoek is ${a * b} cm². De lengte is ${a} cm. Wat is de <b>breedte</b>?`, `Bir dikdörtgenin alanı ${a * b} cm², uzun kenarı ${a} cm. <b>Kısa kenarı</b> kaç cm?`, b, "cm",
      `Breedte = oppervlakte ÷ lengte = ${a * b} ÷ ${a} = ${b} cm.`, `Kısa kenar = alan ÷ uzun kenar = ${a * b} ÷ ${a} = ${b} cm.`); },
    () => { const b = ri(2, 9), a = b + ri(1, 6); return Q(`De omtrek van een rechthoek is ${2 * (a + b)} cm. Eén zijde is ${a} cm. Hoe lang is de <b>andere zijde</b>?`, `Bir dikdörtgenin çevresi ${2 * (a + b)} cm, bir kenarı ${a} cm. <b>Diğer kenarı</b> kaç cm?`, b, "cm",
      `${2 * (a + b)} ÷ 2 = ${a + b} (twee zijden samen). ${a + b} − ${a} = ${b} cm.`, `${2 * (a + b)} ÷ 2 = ${a + b} (iki kenarın toplamı). ${a + b} − ${a} = ${b} cm.`); },
    () => { const a = ri(3, 12); return Q(`De oppervlakte van een vierkant is ${a * a} cm². Wat is de <b>omtrek</b>?`, `Bir karenin alanı ${a * a} cm². <b>Çevresi</b> kaç cm?`, 4 * a, "cm",
      `Zijde = ${a} cm (${a} × ${a} = ${a * a}). Omtrek = 4 × ${a} = ${4 * a} cm.`, `Kenar = ${a} cm (${a} × ${a} = ${a * a}). Çevre = 4 × ${a} = ${4 * a} cm.`); },
    () => { const r = ri(2, 10); return Q(`De omtrek van een cirkel is ${6 * r} cm. Wat is de <b>straal</b>? (π = 3)`, `Bir dairenin çevresi ${6 * r} cm. <b>Yarıçapı</b> kaç cm? (π = 3)`, r, "cm",
      `Diameter = omtrek ÷ π = ${6 * r} ÷ 3 = ${2 * r} cm. Straal = ${2 * r} ÷ 2 = ${r} cm.`, `Çap = çevre ÷ π = ${6 * r} ÷ 3 = ${2 * r} cm. Yarıçap = ${2 * r} ÷ 2 = ${r} cm.`); },
    () => { const r = ri(2, 10); return Q(`De omtrek van een cirkel is ${2 * r}π cm. Wat is de <b>straal</b>?`, `Bir dairenin çevresi ${2 * r}π cm. <b>Yarıçapı</b> kaç cm?`, r, "cm",
      `Omtrek = π × diameter, dus de diameter is ${2 * r} cm. Straal = ${r} cm.`, `Çevre = π × çap, yani çap ${2 * r} cm. Yarıçap = ${r} cm.`); },
    () => { const r = ri(2, 10); return Q(`De oppervlakte van een cirkel is ${3 * r * r} cm². Wat is de <b>straal</b>? (π = 3)`, `Bir dairenin alanı ${3 * r * r} cm². <b>Yarıçapı</b> kaç cm? (π = 3)`, r, "cm",
      `${3 * r * r} ÷ 3 = ${r * r}. Welk getal keer zichzelf is ${r * r}? ${r}. Straal = ${r} cm.`, `${3 * r * r} ÷ 3 = ${r * r}. Hangi sayı × kendisi = ${r * r}? ${r}. Yarıçap = ${r} cm.`); },
    () => { const r = ri(2, 9); return Q(`De oppervlakte van een cirkel is ${r * r}π cm². Wat is de <b>diameter</b>?`, `Bir dairenin alanı ${r * r}π cm². <b>Çapı</b> kaç cm?`, 2 * r, "cm",
      `Straal × straal = ${r * r}, dus straal = ${r} cm. Diameter = 2 × ${r} = ${2 * r} cm.`, `r × r = ${r * r}, yani yarıçap ${r} cm. Çap = 2 × ${r} = ${2 * r} cm.`); },
    () => { const r = ri(2, 8); return Q(`De omtrek van een cirkel is ${6 * r} cm. Wat is de <b>oppervlakte</b>? (π = 3)`, `Bir dairenin çevresi ${6 * r} cm. <b>Alanı</b> kaç cm²? (π = 3)`, 3 * r * r, "cm²",
      `Diameter = ${6 * r} ÷ 3 = ${2 * r}, straal = ${r}. Oppervlakte = 3 × ${r} × ${r} = ${3 * r * r} cm².`, `Çap = ${6 * r} ÷ 3 = ${2 * r}, yarıçap = ${r}. Alan = 3 × ${r} × ${r} = ${3 * r * r} cm².`); }
  ],
  [ // level 3: word problems (field, room, decoration)
    () => { const b = ri(5, 20), a = b + ri(2, 15); return Q(`Een boer heeft een rechthoekig veld van ${a} m bij ${b} m. Hij zet een hek om het hele veld. Hoeveel meter hek heeft hij nodig?`, `Bir çiftçinin tarlası dikdörtgen: ${a} m ve ${b} m. Tarlanın etrafına çit çekecek. Kaç metre çit lazım?`, 2 * (a + b), "m",
      `Een hek eromheen is de omtrek: 2 × (${a} + ${b}) = ${2 * (a + b)} m.`, `Etrafını çevirmek = çevre: 2 × (${a} + ${b}) = ${2 * (a + b)} m.`); },
    () => { const b = ri(3, 5), a = b + ri(1, 3), p = pick([5, 10, 20]); return Q(`Een kamer is ${a} m bij ${b} m. Er komt tapijt op de hele vloer. Tapijt kost €${p} per m². Hoeveel euro kost het tapijt?`, `Bir oda ${a} m ve ${b} m. Bütün yere halı serilecek. Halının 1 m²'si ${p} euro. Halı kaç euro tutar?`, a * b * p, "euro",
      `Oppervlakte = ${a} × ${b} = ${a * b} m². Kosten = ${a * b} × ${p} = ${a * b * p} euro.`, `Alan = ${a} × ${b} = ${a * b} m². Tutar = ${a * b} × ${p} = ${a * b * p} euro.`); },
    () => { const a = ri(4, 12); return Q(`Een vierkante tuin heeft een omtrek van ${4 * a} m. In de hele tuin komt gras. Hoeveel m² gras is dat?`, `Kare bir bahçenin çevresi ${4 * a} m. Bütün bahçeye çim ekilecek. Kaç m² çim lazım?`, a * a, "m²",
      `Zijde = ${4 * a} ÷ 4 = ${a} m. Oppervlakte = ${a} × ${a} = ${a * a} m².`, `Kenar = ${4 * a} ÷ 4 = ${a} m. Alan = ${a} × ${a} = ${a * a} m².`); },
    () => { const d = ri(2, 9); return Q(`Een ronde tafel heeft een diameter van ${d} m. Om de rand komt een lint. Hoeveel meter lint is nodig? (π = 3)`, `Yuvarlak bir masanın çapı ${d} m. Kenarına şerit yapıştırılacak. Kaç metre şerit lazım? (π = 3)`, 3 * d, "m",
      `Om de rand = omtrek = π × diameter = 3 × ${d} = ${3 * d} m.`, `Kenarı = çevre = π × çap = 3 × ${d} = ${3 * d} m.`); },
    () => { const r = ri(1, 3), b = 2 * r + ri(1, 3), a = b + ri(1, 3); return Q(`Een woonkamer is ${a} m bij ${b} m. In het midden ligt een rond kleed met een straal van ${r} m. Hoeveel m² van de vloer blijft <b>vrij</b>? (π = 3)`, `Bir salon ${a} m ve ${b} m. Ortasına yarıçapı ${r} m olan yuvarlak bir halı konuyor. Yerin kaç m²'si <b>boş</b> kalır? (π = 3)`, a * b - 3 * r * r, "m²",
      `Kamer = ${a} × ${b} = ${a * b} m². Kleed = 3 × ${r} × ${r} = ${3 * r * r} m². Vrij = ${a * b} − ${3 * r * r} = ${a * b - 3 * r * r} m².`, `Salon = ${a} × ${b} = ${a * b} m². Halı = 3 × ${r} × ${r} = ${3 * r * r} m². Boş = ${a * b} − ${3 * r * r} = ${a * b - 3 * r * r} m².`, { fig: fig.carpet(`${a} m`, `${b} m`, `${r} m`) }); },
    () => { const r = ri(2, 10); return Q(`Uit een vierkant stuk karton van ${2 * r} cm bij ${2 * r} cm knip je de grootste cirkel die past. Hoeveel cm² karton blijft over? (π = 3)`, `Kenarı ${2 * r} cm olan kare bir kartondan, sığan en büyük daire kesiliyor. Geriye kaç cm² karton kalır? (π = 3)`, r * r, "cm²",
      `Vierkant = ${2 * r} × ${2 * r} = ${4 * r * r} cm². De cirkel heeft straal ${r}: 3 × ${r} × ${r} = ${3 * r * r} cm². Over = ${r * r} cm².`, `Kare = ${2 * r} × ${2 * r} = ${4 * r * r} cm². Dairenin yarıçapı ${r}: 3 × ${r} × ${r} = ${3 * r * r} cm². Kalan = ${r * r} cm².`); },
    () => { const b = ri(2, 4), a = b + ri(1, 4), s = ri(1, b - 1); return Q(`Een muur is ${a} m bij ${b} m. In de muur zit een vierkant raam met zijden van ${s} m. De muur wordt geverfd, het raam niet. Hoeveel m² wordt geverfd?`, `Bir duvar ${a} m ve ${b} m. Duvarda kenarı ${s} m olan kare bir pencere var. Duvar boyanacak, pencere boyanmayacak. Kaç m² boyanır?`, a * b - s * s, "m²",
      `Muur = ${a} × ${b} = ${a * b} m². Raam = ${s} × ${s} = ${s * s} m². Verven = ${a * b} − ${s * s} = ${a * b - s * s} m².`, `Duvar = ${a} × ${b} = ${a * b} m². Pencere = ${s} × ${s} = ${s * s} m². Boyanacak = ${a * b} − ${s * s} = ${a * b - s * s} m².`); },
    () => { const d = pick([40, 50, 60, 70]); return Q(`Een fietswiel heeft een diameter van ${d} cm. Het wiel draait 10 rondjes. Hoeveel <b>meter</b> rijdt de fiets? (π = 3)`, `Bir bisiklet tekerleğinin çapı ${d} cm. Tekerlek 10 tur dönüyor. Bisiklet kaç <b>metre</b> gider? (π = 3)`, 3 * d / 10, "m",
      `1 rondje = omtrek = 3 × ${d} = ${3 * d} cm. 10 rondjes = ${30 * d} cm = ${3 * d / 10} m.`, `1 tur = çevre = 3 × ${d} = ${3 * d} cm. 10 tur = ${30 * d} cm = ${3 * d / 10} m.`); },
    () => { const r = ri(2, 6); return Q(`Om een rond zwembad staat een hek van ${6 * r} m. Hoe groot is de <b>oppervlakte</b> van het zwembad? (π = 3)`, `Yuvarlak bir havuzun etrafındaki çit ${6 * r} m. Havuzun <b>alanı</b> kaç m²? (π = 3)`, 3 * r * r, "m²",
      `Omtrek ${6 * r} m, dus diameter ${2 * r} m en straal ${r} m. Oppervlakte = 3 × ${r} × ${r} = ${3 * r * r} m².`, `Çevre ${6 * r} m, yani çap ${2 * r} m, yarıçap ${r} m. Alan = 3 × ${r} × ${r} = ${3 * r * r} m².`); },
    () => { const b = ri(4, 7) * 10, a = b + ri(2, 5) * 10, n = ri(2, 5); return Q(`Een voetbalveld is ${a} m lang en ${b} m breed. De trainer laat het team ${n} rondjes om het veld lopen. Hoeveel meter lopen de spelers?`, `Bir futbol sahası ${a} m uzunluğunda ve ${b} m genişliğinde. Antrenör takıma sahanın etrafında ${n} tur koşturuyor. Oyuncular kaç metre koşar?`, n * 2 * (a + b), "m",
      `Eén rondje = omtrek = 2 × (${a} + ${b}) = ${2 * (a + b)} m. ${n} rondjes: ${n * 2 * (a + b)} m.`, `Bir tur = çevre = 2 × (${a} + ${b}) = ${2 * (a + b)} m. ${n} tur: ${n * 2 * (a + b)} m.`); },
    () => { const s2 = ri(1, 2), b = 2 * s2 + ri(1, 2), a = b + ri(2, 4); return Q(`Een kamer is ${a} m bij ${b} m. Er liggen twee vierkante kleden, elk met zijden van ${s2} m. Hoeveel m² van de vloer is niet bedekt?`, `Bir oda ${a} m ve ${b} m. Yerde, kenarı ${s2} m olan iki kare halı var. Zeminin kaç m²'si açıkta kalır?`, a * b - 2 * s2 * s2, "m²",
      `Kamer = ${a * b} m². Twee kleden = 2 × ${s2 * s2} = ${2 * s2 * s2} m². Niet bedekt: ${a * b - 2 * s2 * s2} m².`, `Oda = ${a * b} m². İki halı = 2 × ${s2 * s2} = ${2 * s2 * s2} m². Açıkta kalan: ${a * b - 2 * s2 * s2} m².`); },
    () => { const b = ri(2, 6), a = b + ri(1, 5); return Q(`Een tuin is ${a} m bij ${b} m. De buren hebben een tuin die 2 keer zo lang én 2 keer zo breed is. Hoeveel m² is de tuin van de buren?`, `Bir bahçe ${a} m ve ${b} m. Komşunun bahçesi hem 2 kat uzun hem 2 kat geniş. Komşunun bahçesi kaç m²?`, 4 * a * b, "m²",
      `${2 * a} × ${2 * b} = ${4 * a * b} m². Dat is 4 keer zo groot als ${a * b} m², niet 2 keer.`, `${2 * a} × ${2 * b} = ${4 * a * b} m². Bu, ${a * b} m²'nin 2 değil 4 katıdır.`); },
    () => { const r = ri(1, 5), n = ri(2, 4); return Q(`Een ronde pizza heeft een straal van ${r * 5} cm. Je bestelt ${n} pizza's. Hoeveel cm² pizza is dat samen? (π = 3)`, `Yuvarlak bir pizzanın yarıçapı ${r * 5} cm. ${n} pizza sipariş ediyorsun. Toplam kaç cm² pizza eder? (π = 3)`, n * 3 * 25 * r * r, "cm²",
      `Eén pizza: 3 × ${r * 5} × ${r * 5} = ${75 * r * r} cm². ${n} pizza's: ${n * 75 * r * r} cm².`, `Bir pizza: 3 × ${r * 5} × ${r * 5} = ${75 * r * r} cm². ${n} pizza: ${n * 75 * r * r} cm².`); }
  ]
];

// ----- Optellen van 1 tot n
GEN.som = [
  [
    () => { const n = ri(4, 10); return Q(`Hoeveel is 1 + 2 + 3 + … + ${n}?`, `1 + 2 + 3 + … + ${n} kaç eder?`, tri(n), "",
      `${n} × ${n + 1} ÷ 2 = ${n * (n + 1)} ÷ 2 = ${tri(n)}.`, `${n} × ${n + 1} ÷ 2 = ${n * (n + 1)} ÷ 2 = ${tri(n)}.`); },
    () => { const n = pick([6, 8, 10]); return Q(`Je telt 1 + 2 + … + ${n} op. Je maakt paren: 1 + ${n}, 2 + ${n - 1}, … Hoeveel is <b>elk paar</b> samen?`, `1 + 2 + … + ${n} topluyorsun. Çiftler yapıyorsun: 1 + ${n}, 2 + ${n - 1}, … <b>Her çift</b> kaç eder?`, n + 1, "",
      `1 + ${n} = ${n + 1}, 2 + ${n - 1} = ${n + 1}. Elk paar is ${n + 1}.`, `1 + ${n} = ${n + 1}, 2 + ${n - 1} = ${n + 1}. Her çift ${n + 1} eder.`); },
    () => { const n = pick([6, 8, 10, 12]); return Q(`Je telt 1 + 2 + … + ${n} op en maakt paren die samen ${n + 1} zijn. <b>Hoeveel paren</b> zijn er?`, `1 + 2 + … + ${n} toplarken toplamı ${n + 1} olan çiftler yapıyorsun. <b>Kaç çift</b> var?`, n / 2, "",
      `${n} getallen, steeds 2 per paar: ${n} ÷ 2 = ${n / 2} paren.`, `${n} sayı var, her çiftte 2 sayı: ${n} ÷ 2 = ${n / 2} çift.`); }
  ],
  [
    () => { const n = pick([12, 15, 20, 25, 30, 40, 50, 100]); return Q(`Hoeveel is 1 + 2 + 3 + … + ${n}?`, `1 + 2 + 3 + … + ${n} kaç eder?`, tri(n), "",
      `${n} × ${n + 1} ÷ 2 = ${tri(n)}.`, `${n} × ${n + 1} ÷ 2 = ${tri(n)}.`); },
    () => { const n = ri(4, 10); return Q(`Hoeveel is 2 + 4 + 6 + … + ${2 * n}? (de even getallen)`, `2 + 4 + 6 + … + ${2 * n} kaç eder? (çift sayılar)`, 2 * tri(n), "",
      `Dat is 2 × (1 + 2 + … + ${n}) = 2 × ${tri(n)} = ${2 * tri(n)}.`, `Bu, 2 × (1 + 2 + … + ${n}) = 2 × ${tri(n)} = ${2 * tri(n)}.`); },
    () => { const n = ri(3, 10); return Q(`Tel de eerste ${n} oneven getallen op: 1 + 3 + 5 + … + ${2 * n - 1}. Hoeveel is dat?`, `İlk ${n} tek sayıyı topla: 1 + 3 + 5 + … + ${2 * n - 1}. Kaç eder?`, n * n, "",
      `De som van de eerste ${n} oneven getallen is ${n} × ${n} = ${n * n}.`, `İlk ${n} tek sayının toplamı ${n} × ${n} = ${n * n} eder.`); },
    () => { const n = ri(5, 12); return Q(`1 + 2 + 3 + … + ? = ${tri(n)}. Tot welk getal is er geteld?`, `1 + 2 + 3 + … + ? = ${tri(n)}. Hangi sayıya kadar toplandı?`, n, "",
      `Probeer: ${n} × ${n + 1} ÷ 2 = ${tri(n)}. Het antwoord is ${n}.`, `Dene: ${n} × ${n + 1} ÷ 2 = ${tri(n)}. Cevap ${n}.`); }
  ],
  [
    () => { const n = ri(7, 30); return Q(`Je spaart. Op dag 1 doe je €1 in je spaarpot, op dag 2 €2, op dag 3 €3, en zo verder. Hoeveel euro heb je na ${n} dagen?`, `Para biriktiriyorsun. 1. gün kumbaraya 1 euro, 2. gün 2 euro, 3. gün 3 euro atıyorsun ve böyle devam ediyorsun. ${n} gün sonra kaç euron olur?`, tri(n), "euro",
      `1 + 2 + … + ${n} = ${n} × ${n + 1} ÷ 2 = ${tri(n)} euro.`, `1 + 2 + … + ${n} = ${n} × ${n + 1} ÷ 2 = ${tri(n)} euro.`); },
    () => { const n = ri(6, 15); return Q(`Je bouwt een toren van blikken. Bovenaan staat 1 blik, daaronder 2, daaronder 3. De toren heeft ${n} rijen. Hoeveel blikken zijn er?`, `Konserve kutularından kule yapıyorsun. En üstte 1 kutu, altında 2, onun altında 3 kutu var. Kule ${n} sıra. Toplam kaç kutu var?`, tri(n), "",
      `1 + 2 + … + ${n} = ${n} × ${n + 1} ÷ 2 = ${tri(n)} blikken.`, `1 + 2 + … + ${n} = ${n} × ${n + 1} ÷ 2 = ${tri(n)} kutu.`); },
    () => { const n = ri(5, 12); return Q(`Er zijn ${n} kinderen. Iedereen geeft iedereen één keer een hand. Hoeveel keer wordt er een hand gegeven?`, `${n} çocuk var. Herkes herkesle bir kez tokalaşıyor. Toplam kaç tokalaşma olur?`, tri(n - 1), "",
      `Het eerste kind geeft ${n - 1} handen, het volgende ${n - 2}, … Dat is 1 + 2 + … + ${n - 1} = ${tri(n - 1)}.`, `İlk çocuk ${n - 1} kişiyle, sonraki ${n - 2} kişiyle… Yani 1 + 2 + … + ${n - 1} = ${tri(n - 1)}.`); },
    () => { const n = ri(5, 10); return Q(`In een competitie zitten ${n} voetbalteams. Elk team speelt één keer tegen elk ander team. Hoeveel wedstrijden zijn er?`, `Bir ligde ${n} futbol takımı var. Her takım diğer her takımla bir kez oynuyor. Toplam kaç maç olur?`, tri(n - 1), "",
      `${n - 1} + ${n - 2} + … + 1 = ${n - 1} × ${n} ÷ 2 = ${tri(n - 1)} wedstrijden.`, `${n - 1} + ${n - 2} + … + 1 = ${n - 1} × ${n} ÷ 2 = ${tri(n - 1)} maç.`); },
    () => { const n = ri(6, 12); return Q(`Een klok slaat om 1 uur één keer, om 2 uur twee keer, en zo verder. Hoeveel slagen hoor je in totaal van 1 uur tot en met ${n} uur?`, `Bir saat 1'de bir kez, 2'de iki kez çalıyor ve böyle devam ediyor. Saat 1'den ${n}'e kadar (${n} dahil) toplam kaç kez çalar?`, tri(n), "",
      `1 + 2 + … + ${n} = ${n} × ${n + 1} ÷ 2 = ${tri(n)}.`, `1 + 2 + … + ${n} = ${n} × ${n + 1} ÷ 2 = ${tri(n)}.`); },
    () => { const n = ri(8, 20); return Q(`Boomstammen liggen op een stapel. De onderste rij heeft ${n} stammen, elke rij daarboven één minder, tot er bovenaan 1 ligt. Hoeveel stammen zijn er?`, `Kütükler üst üste dizilmiş. En alt sırada ${n} kütük var, her üst sırada bir eksik; en üstte 1 kütük var. Toplam kaç kütük var?`, tri(n), "",
      `${n} + ${n - 1} + … + 1 = ${n} × ${n + 1} ÷ 2 = ${tri(n)}.`, `${n} + ${n - 1} + … + 1 = ${n} × ${n + 1} ÷ 2 = ${tri(n)}.`); }
  ]
];

// ----- Machten en wortels
GEN.machten = [
  [
    () => { const a = ri(2, 12); return Q(`Hoeveel is ${a}²?`, `${a}² kaç eder?`, a * a, "", `${a}² = ${a} × ${a} = ${a * a}.`, `${a}² = ${a} × ${a} = ${a * a}.`); },
    () => { const a = ri(2, 5); return Q(`Hoeveel is ${a}³?`, `${a}³ kaç eder?`, a ** 3, "", `${a}³ = ${a} × ${a} × ${a} = ${a ** 3}.`, `${a}³ = ${a} × ${a} × ${a} = ${a ** 3}.`); },
    () => { const n = ri(2, 6); const sup = "²³⁴⁵⁶"[n - 2]; return Q(`Hoeveel is 2${sup}? (2 keer zichzelf, ${n} keer)`, `2${sup} kaç eder? (${n} tane 2'yi çarp)`, 2 ** n, "",
      `2${sup} = ${Array(n).fill(2).join(" × ")} = ${2 ** n}.`, `2${sup} = ${Array(n).fill(2).join(" × ")} = ${2 ** n}.`); },
    () => { const n = ri(2, 5); const sup = "²³⁴⁵"[n - 2]; return Q(`Hoeveel is 10${sup}?`, `10${sup} kaç eder?`, 10 ** n, "",
      `10${sup} is een 1 met ${n} nullen: ${10 ** n}.`, `10${sup}: 1'in yanına ${n} sıfır: ${10 ** n}.`); }
  ],
  [
    () => { const a = ri(2, 12); return Q(`Hoeveel is √${a * a}? (de wortel van ${a * a})`, `√${a * a} kaç eder? (${a * a} sayısının karekökü)`, a, "",
      `Welk getal keer zichzelf is ${a * a}? ${a} × ${a} = ${a * a}. Dus √${a * a} = ${a}.`, `Hangi sayı × kendisi = ${a * a}? ${a} × ${a} = ${a * a}. Yani √${a * a} = ${a}.`); },
    () => { const a = ri(3, 12); return Q(`?² = ${a * a}. Welk getal hoort op de plaats van het vraagteken?`, `?² = ${a * a}. Soru işaretinin yerine hangi sayı gelir?`, a, "",
      `${a} × ${a} = ${a * a}, dus het getal is ${a}.`, `${a} × ${a} = ${a * a}, yani sayı ${a}.`); },
    () => { const a = ri(2, 9), b = ri(2, 9); return Q(`Hoeveel is ${a}² + ${b}²?`, `${a}² + ${b}² kaç eder?`, a * a + b * b, "",
      `${a}² = ${a * a} en ${b}² = ${b * b}. Samen ${a * a + b * b}.`, `${a}² = ${a * a}, ${b}² = ${b * b}. Toplam ${a * a + b * b}.`); },
    () => { const b = ri(2, 8), a = b + ri(1, 4); return Q(`Hoeveel is ${a}² − ${b}²?`, `${a}² − ${b}² kaç eder?`, a * a - b * b, "",
      `${a}² = ${a * a} en ${b}² = ${b * b}. ${a * a} − ${b * b} = ${a * a - b * b}.`, `${a}² = ${a * a}, ${b}² = ${b * b}. ${a * a} − ${b * b} = ${a * a - b * b}.`); },
    () => { const a = ri(2, 10), b = ri(2, 10); return Q(`Hoeveel is √${a * a} + √${b * b}?`, `√${a * a} + √${b * b} kaç eder?`, a + b, "",
      `√${a * a} = ${a} en √${b * b} = ${b}. Samen ${a + b}.`, `√${a * a} = ${a}, √${b * b} = ${b}. Toplam ${a + b}.`); },
    () => { const n = ri(3, 6); return Q(`2 tot de macht ? is ${2 ** n}. Hoe vaak moet je 2 met zichzelf vermenigvuldigen?`, `2'nin kaçıncı kuvveti ${2 ** n} eder? (Kaç tane 2 çarpılır?)`, n, "",
      `${Array(n).fill(2).join(" × ")} = ${2 ** n}. Dat zijn ${n} tweeën.`, `${Array(n).fill(2).join(" × ")} = ${2 ** n}. ${n} tane 2 var.`); }
  ],
  [
    () => { const a = ri(4, 12); return Q(`Een vierkante tuin heeft een oppervlakte van ${a * a} m². Om de tuin komt een hek. Hoeveel meter hek is nodig?`, `Kare bir bahçenin alanı ${a * a} m². Etrafına çit çekilecek. Kaç metre çit lazım?`, 4 * a, "m",
      `Zijde = √${a * a} = ${a} m. Omtrek = 4 × ${a} = ${4 * a} m.`, `Kenar = √${a * a} = ${a} m. Çevre = 4 × ${a} = ${4 * a} m.`); },
    () => { const a = ri(2, 5); return Q(`Een grote kubus is gebouwd van kleine blokjes. Elke ribbe is ${a} blokjes lang. Hoeveel blokjes zijn er in totaal?`, `Büyük bir küp küçük küplerden yapılmış. Her kenarı ${a} küp uzunluğunda. Toplam kaç küçük küp var?`, a ** 3, "",
      `${a} × ${a} × ${a} = ${a}³ = ${a ** 3} blokjes.`, `${a} × ${a} × ${a} = ${a}³ = ${a ** 3} küp.`); },
    () => { const n = ri(3, 7); return Q(`Een bacterie deelt zich elke dag in tweeën. Op dag 1 zijn er 2, op dag 2 zijn er 4. Hoeveel zijn er op dag ${n}?`, `Bir bakteri her gün ikiye bölünüyor. 1. gün 2 tane, 2. gün 4 tane var. ${n}. gün kaç tane olur?`, 2 ** n, "",
      `Elke dag keer 2: ${Array(n).fill(2).join(" × ")} = ${2 ** n}.`, `Her gün 2 katı: ${Array(n).fill(2).join(" × ")} = ${2 ** n}.`); },
    () => { const a = ri(4, 10), b = ri(2, 9); return Q(`Op een vierkant terras liggen ${a} rijen van ${a} tegels. Er zijn ${b} tegels kapot. Hoeveel tegels zijn nog heel?`, `Kare bir terasta ${a} sıra var, her sırada ${a} karo. ${b} karo kırık. Kaç karo sağlam?`, a * a - b, "",
      `${a}² = ${a * a} tegels. ${a * a} − ${b} = ${a * a - b}.`, `${a}² = ${a * a} karo. ${a * a} − ${b} = ${a * a - b}.`); },
    () => { const a = ri(3, 9); return Q(`Je hebt ${a * a} vierkante tegels en legt er één groot vierkant van. Hoeveel tegels liggen er in <b>één rij</b>?`, `${a * a} kare karon var ve hepsiyle büyük bir kare yapıyorsun. <b>Bir sırada</b> kaç karo olur?`, a, "",
      `√${a * a} = ${a}. In elke rij liggen ${a} tegels.`, `√${a * a} = ${a}. Her sırada ${a} karo olur.`); },
    () => { const n = ri(4, 9); return Q(`Op het eerste vakje van een schaakbord ligt 1 graankorrel, op het tweede 2, op het derde 4: steeds het dubbele. Hoeveel korrels liggen er op vakje ${n}?`, `Satranç tahtasının ilk karesinde 1 buğday tanesi, ikincisinde 2, üçüncüsünde 4 var: hep iki katı. ${n}. karede kaç tane var?`, 2 ** (n - 1), "",
      `De rij: ${Array.from({ length: n }, (_, i) => 2 ** i).join(", ")}. Op vakje ${n}: ${2 ** (n - 1)}.`, `Dizi: ${Array.from({ length: n }, (_, i) => 2 ** i).join(", ")}. ${n}. karede: ${2 ** (n - 1)}.`); },
    () => { const a = ri(2, 9); return Q(`Een kubus heeft 6 vlakken. Elk vlak is een vierkant met zijden van ${a} cm. Je beplakt de hele kubus met papier. Hoeveel cm² papier heb je nodig?`, `Bir küpün 6 yüzü var. Her yüz, kenarı ${a} cm olan bir kare. Küpün tamamını kâğıtla kaplıyorsun. Kaç cm² kâğıt gerekir?`, 6 * a * a, "cm²",
      `Eén vlak: ${a}² = ${a * a} cm². Zes vlakken: 6 × ${a * a} = ${6 * a * a} cm².`, `Bir yüz: ${a}² = ${a * a} cm². Altı yüz: 6 × ${a * a} = ${6 * a * a} cm².`); }
  ]
];

// ----- Kwadraat- en driehoeksgetallen
GEN.getallen = [
  [
    () => { const n = ri(3, 10); return Q(`De kwadraatgetallen zijn 1, 4, 9, 16, … Wat is het ${n}e kwadraatgetal?`, `Kare sayılar: 1, 4, 9, 16, … ${n}. kare sayı kaçtır?`, n * n, "", `${n} × ${n} = ${n * n}.`, `${n} × ${n} = ${n * n}.`); },
    () => { const n = ri(4, 9); const row = [1, 2, 3, 4].map(i => (n - 4 + i) ** 2).join(", "); return Q(`Welk getal komt hierna? ${row}, …`, `Sıradaki sayı hangisi? ${row}, …`, (n + 1) ** 2, "",
      `Het zijn kwadraten. Het volgende is ${n + 1} × ${n + 1} = ${(n + 1) ** 2}.`, `Bunlar kare sayılar. Sıradaki ${n + 1} × ${n + 1} = ${(n + 1) ** 2}.`); },
    () => { const n = ri(4, 8); const row = [1, 2, 3, 4].map(i => tri(n - 4 + i)).join(", "); return Q(`Welk getal komt hierna? ${row}, …`, `Sıradaki sayı hangisi? ${row}, …`, tri(n + 1), "",
      `Er komt steeds één meer bij. Nu komt er ${n + 1} bij: ${tri(n)} + ${n + 1} = ${tri(n + 1)}.`, `Her seferinde bir fazlası ekleniyor. Şimdi ${n + 1} eklenir: ${tri(n)} + ${n + 1} = ${tri(n + 1)}.`); }
  ],
  [
    () => { const n = ri(5, 12); return Q(`De driehoeksgetallen zijn 1, 3, 6, 10, … Wat is het ${n}e driehoeksgetal?`, `Üçgen sayılar: 1, 3, 6, 10, … ${n}. üçgen sayı kaçtır?`, tri(n), "",
      `1 + 2 + … + ${n} = ${n} × ${n + 1} ÷ 2 = ${tri(n)}.`, `1 + 2 + … + ${n} = ${n} × ${n + 1} ÷ 2 = ${tri(n)}.`); },
    () => { const sq = pick([16, 25, 36, 49, 64, 81]); const wrong = shuffle([12, 18, 20, 30, 45, 50, 72, 90].filter(x => x !== sq)).slice(0, 3);
      return Q(`Welk getal is een <b>kwadraatgetal</b>?`, `Hangisi bir <b>kare sayıdır</b>?`, sq, "",
        `${Math.sqrt(sq)} × ${Math.sqrt(sq)} = ${sq}.`, `${Math.sqrt(sq)} × ${Math.sqrt(sq)} = ${sq}.`, { opts: shuffle([sq, ...wrong]).map(num) }); },
    () => { const n = ri(4, 12); return Q(`${n * n} is een kwadraatgetal. Hoeveel moet je erbij tellen om bij het <b>volgende</b> kwadraatgetal te komen?`, `${n * n} bir kare sayı. <b>Sonraki</b> kare sayıya ulaşmak için kaç eklemelisin?`, 2 * n + 1, "",
      `Het volgende is ${(n + 1) ** 2}. ${(n + 1) ** 2} − ${n * n} = ${2 * n + 1}.`, `Sonraki ${(n + 1) ** 2}. ${(n + 1) ** 2} − ${n * n} = ${2 * n + 1}.`); }
  ],
  [
    () => { const n = ri(4, 10); return Q(`Tel twee driehoeksgetallen naast elkaar op: ${tri(n - 1)} + ${tri(n)}. Hoeveel is dat?`, `Art arda gelen iki üçgen sayıyı topla: ${tri(n - 1)} + ${tri(n)}. Kaç eder?`, n * n, "",
      `${tri(n - 1)} + ${tri(n)} = ${n * n}. Dat is altijd een kwadraat: ${n} × ${n}.`, `${tri(n - 1)} + ${tri(n)} = ${n * n}. Sonuç hep bir kare sayı: ${n} × ${n}.`); },
    () => { const n = ri(4, 9); return Q(`Biljartballen liggen in een driehoek: 1 bal in de eerste rij, 2 in de tweede, en zo verder. Er zijn ${n} rijen. Hoeveel ballen zijn er?`, `Bilardo topları üçgen şeklinde dizilmiş: ilk sırada 1, ikinci sırada 2 top ve böyle devam ediyor. ${n} sıra var. Kaç top var?`, tri(n), "",
      `1 + 2 + … + ${n} = ${tri(n)}.`, `1 + 2 + … + ${n} = ${tri(n)}.`); },
    () => { const n = ri(5, 12); return Q(`In een zaal staan de stoelen in een vierkant: evenveel rijen als stoelen per rij. Er zijn ${n * n} stoelen. Hoeveel rijen zijn er?`, `Bir salonda sandalyeler kare şeklinde dizilmiş: sıra sayısı ile bir sıradaki sandalye sayısı aynı. ${n * n} sandalye var. Kaç sıra var?`, n, "",
      `${n} × ${n} = ${n * n}, dus ${n} rijen.`, `${n} × ${n} = ${n * n}, yani ${n} sıra.`); }
  ]
];

// ----- Oppervlakte van een driehoek
const triDims = () => { let b = ri(3, 12), h = ri(2, 10); if ((b * h) % 2) b++; return [b, h]; };   // keep the area whole
GEN.driehoek = [
  [
    () => { const [b, h] = triDims(); return Q(`Een driehoek heeft een basis van ${b} cm en een hoogte van ${h} cm. Wat is de oppervlakte?`, `Bir üçgenin tabanı ${b} cm, yüksekliği ${h} cm. Alanı kaç cm²?`, b * h / 2, "cm²",
      `Oppervlakte = basis × hoogte ÷ 2 = ${b} × ${h} ÷ 2 = ${b * h / 2} cm².`, `Alan = taban × yükseklik ÷ 2 = ${b} × ${h} ÷ 2 = ${b * h / 2} cm².`, { fig: fig.triangle(`${b} cm`, `${h} cm`) }); },
    () => { const [a, b] = triDims(); return Q(`Een rechthoek van ${a} cm bij ${b} cm wordt schuin doormidden geknipt. Je krijgt twee gelijke driehoeken. Wat is de oppervlakte van <b>één</b> driehoek?`, `${a} cm ve ${b} cm kenarlı bir dikdörtgen köşeden köşeye ikiye kesiliyor. İki eşit üçgen oluyor. <b>Bir</b> üçgenin alanı kaç cm²?`, a * b / 2, "cm²",
      `Rechthoek = ${a} × ${b} = ${a * b} cm². De helft is ${a * b / 2} cm².`, `Dikdörtgen = ${a} × ${b} = ${a * b} cm². Yarısı ${a * b / 2} cm².`); }
  ],
  [
    () => { const [b, h] = triDims(); return Q(`Een driehoek heeft een oppervlakte van ${b * h / 2} cm² en een basis van ${b} cm. Wat is de hoogte?`, `Bir üçgenin alanı ${b * h / 2} cm², tabanı ${b} cm. Yüksekliği kaç cm?`, h, "cm",
      `2 × ${b * h / 2} = ${b * h}. ${b * h} ÷ ${b} = ${h} cm.`, `2 × ${b * h / 2} = ${b * h}. ${b * h} ÷ ${b} = ${h} cm.`); },
    () => { const [b, h] = triDims(); return Q(`Een driehoek heeft een oppervlakte van ${b * h / 2} cm² en een hoogte van ${h} cm. Hoe lang is de basis?`, `Bir üçgenin alanı ${b * h / 2} cm², yüksekliği ${h} cm. Tabanı kaç cm?`, b, "cm",
      `2 × ${b * h / 2} = ${b * h}. ${b * h} ÷ ${h} = ${b} cm.`, `2 × ${b * h / 2} = ${b * h}. ${b * h} ÷ ${h} = ${b} cm.`); }
  ],
  [
    () => { const [b, h] = triDims(); const p = pick([2, 5, 10]); return Q(`Een zeil van een bootje is een driehoek met een basis van ${b} m en een hoogte van ${h} m. De stof kost €${p} per m². Hoeveel kost het zeil?`, `Bir teknenin yelkeni üçgen: tabanı ${b} m, yüksekliği ${h} m. Kumaşın 1 m²'si ${p} euro. Yelken kaç euro tutar?`, b * h / 2 * p, "euro",
      `Oppervlakte = ${b} × ${h} ÷ 2 = ${b * h / 2} m². Kosten = ${b * h / 2} × ${p} = ${b * h / 2 * p} euro.`, `Alan = ${b} × ${h} ÷ 2 = ${b * h / 2} m². Tutar = ${b * h / 2} × ${p} = ${b * h / 2 * p} euro.`); },
    () => { const [a, b] = triDims(); return Q(`Een rechthoekige tuin van ${a} m bij ${b} m wordt schuin in tweeën gedeeld. In de ene helft komen bloemen. Hoeveel m² bloemen is dat?`, `${a} m ve ${b} m kenarlı dikdörtgen bir bahçe köşeden köşeye ikiye bölünüyor. Bir yarısına çiçek ekiliyor. Kaç m² çiçek olur?`, a * b / 2, "m²",
      `${a} × ${b} = ${a * b} m². De helft: ${a * b / 2} m².`, `${a} × ${b} = ${a * b} m². Yarısı: ${a * b / 2} m².`); }
  ]
];

// ----- Samengestelde figuren (L-vorm). Left part w1 x h1 (tall), right part w2 x h2 (low).
const lDims = () => { const h2 = ri(2, 5), h1 = h2 + ri(1, 4), w1 = ri(2, 6), w2 = ri(2, 6); return [w1, h1, w2, h2]; };
const lFig = (w1, h1, w2, h2, u) => fig.lshape(`${w1} ${u}`, `${h1} ${u}`, `${w2} ${u}`, `${h2} ${u}`);
GEN.samengesteld = [
  [
    () => { const [w1, h1, w2, h2] = lDims(); return Q(`Deze L-vorm bestaat uit twee rechthoeken: ${w1} cm bij ${h1} cm en ${w2} cm bij ${h2} cm. Wat is de totale oppervlakte?`, `Bu L şekli iki dikdörtgenden oluşuyor: ${w1} cm × ${h1} cm ve ${w2} cm × ${h2} cm. Toplam alan kaç cm²?`, w1 * h1 + w2 * h2, "cm²",
      `${w1} × ${h1} = ${w1 * h1} en ${w2} × ${h2} = ${w2 * h2}. Samen ${w1 * h1 + w2 * h2} cm².`, `${w1} × ${h1} = ${w1 * h1}, ${w2} × ${h2} = ${w2 * h2}. Toplam ${w1 * h1 + w2 * h2} cm².`, { fig: lFig(w1, h1, w2, h2, "cm") }); }
  ],
  [
    () => { const [w1, h1, w2, h2] = lDims(); const W = w1 + w2; return Q(`Uit een rechthoek van ${W} cm bij ${h1} cm is een hoek van ${w2} cm bij ${h1 - h2} cm weggeknipt. Wat is de oppervlakte van de L-vorm die overblijft?`, `${W} cm × ${h1} cm bir dikdörtgenin köşesinden ${w2} cm × ${h1 - h2} cm bir parça kesilmiş. Kalan L şeklinin alanı kaç cm²?`, W * h1 - w2 * (h1 - h2), "cm²",
      `Groot: ${W} × ${h1} = ${W * h1}. Weg: ${w2} × ${h1 - h2} = ${w2 * (h1 - h2)}. Over: ${W * h1 - w2 * (h1 - h2)} cm².`, `Büyük: ${W} × ${h1} = ${W * h1}. Kesilen: ${w2} × ${h1 - h2} = ${w2 * (h1 - h2)}. Kalan: ${W * h1 - w2 * (h1 - h2)} cm².`); },
    () => { const [w1, h1, w2, h2] = lDims(); return Q(`Wat is de <b>omtrek</b> van deze L-vorm? De hele onderkant is ${w1 + w2} cm en de hele linkerkant is ${h1} cm.`, `Bu L şeklinin <b>çevresi</b> kaç cm? Alt kenarın tamamı ${w1 + w2} cm, sol kenarın tamamı ${h1} cm.`, 2 * (w1 + w2 + h1), "cm",
      `De omtrek van een L-vorm is even lang als die van de hele rechthoek: 2 × (${w1 + w2} + ${h1}) = ${2 * (w1 + w2 + h1)} cm.`, `L şeklinin çevresi, tam dikdörtgenin çevresiyle aynıdır: 2 × (${w1 + w2} + ${h1}) = ${2 * (w1 + w2 + h1)} cm.`, { fig: lFig(w1, h1, w2, h2, "cm") }); }
  ],
  [
    () => { const [w1, h1, w2, h2] = lDims(); const p = pick([5, 10]); const A = w1 * h1 + w2 * h2; return Q(`Een kamer heeft een L-vorm: een deel van ${w1} m bij ${h1} m en een deel van ${w2} m bij ${h2} m. Een nieuwe vloer kost €${p} per m². Hoeveel kost de vloer?`, `Bir oda L şeklinde: bir bölümü ${w1} m × ${h1} m, diğer bölümü ${w2} m × ${h2} m. Yeni zemin 1 m² için ${p} euro. Zemin kaç euro tutar?`, A * p, "euro",
      `${w1 * h1} + ${w2 * h2} = ${A} m². ${A} × ${p} = ${A * p} euro.`, `${w1 * h1} + ${w2 * h2} = ${A} m². ${A} × ${p} = ${A * p} euro.`, { fig: lFig(w1, h1, w2, h2, "m") }); },
    () => { const b = ri(6, 10), a = b + ri(2, 6), d = ri(2, 4), c = d + ri(1, 2); return Q(`Een tuin is ${a} m bij ${b} m. In de tuin ligt een rechthoekig zwembad van ${c} m bij ${d} m. De rest is gras. Hoeveel m² gras is er?`, `Bir bahçe ${a} m × ${b} m. Bahçede ${c} m × ${d} m dikdörtgen bir havuz var. Geri kalan çim. Kaç m² çim var?`, a * b - c * d, "m²",
      `Tuin = ${a * b} m². Zwembad = ${c * d} m². Gras = ${a * b - c * d} m².`, `Bahçe = ${a * b} m². Havuz = ${c * d} m². Çim = ${a * b - c * d} m².`); }
  ]
];

// ----- Inhoud
GEN.inhoud = [
  [
    () => { const a = ri(2, 5); return Q(`Een kubus heeft ribben van ${a} cm. Wat is de inhoud?`, `Bir küpün kenarı ${a} cm. Hacmi kaç cm³?`, a ** 3, "cm³",
      `Inhoud = ${a} × ${a} × ${a} = ${a ** 3} cm³.`, `Hacim = ${a} × ${a} × ${a} = ${a ** 3} cm³.`); },
    () => { const l = ri(3, 8), b = ri(2, 5), h = ri(2, 5); return Q(`Een doos is ${l} cm lang, ${b} cm breed en ${h} cm hoog. Wat is de inhoud?`, `Bir kutunun uzunluğu ${l} cm, genişliği ${b} cm, yüksekliği ${h} cm. Hacmi kaç cm³?`, l * b * h, "cm³",
      `Inhoud = lengte × breedte × hoogte = ${l} × ${b} × ${h} = ${l * b * h} cm³.`, `Hacim = uzunluk × genişlik × yükseklik = ${l} × ${b} × ${h} = ${l * b * h} cm³.`, { fig: fig.box(`${l} cm`, `${b} cm`, `${h} cm`) }); }
  ],
  [
    () => { const a = ri(2, 6); return Q(`De inhoud van een kubus is ${a ** 3} cm³. Hoe lang is één ribbe?`, `Bir küpün hacmi ${a ** 3} cm³. Bir kenarı kaç cm?`, a, "cm",
      `${a} × ${a} × ${a} = ${a ** 3}. De ribbe is ${a} cm.`, `${a} × ${a} × ${a} = ${a ** 3}. Kenar ${a} cm.`); },
    () => { const l = ri(3, 8), b = ri(2, 5), h = ri(2, 6); return Q(`Een doos heeft een inhoud van ${l * b * h} cm³. De doos is ${l} cm lang en ${b} cm breed. Hoe hoog is de doos?`, `Bir kutunun hacmi ${l * b * h} cm³. Uzunluğu ${l} cm, genişliği ${b} cm. Yüksekliği kaç cm?`, h, "cm",
      `${l} × ${b} = ${l * b}. ${l * b * h} ÷ ${l * b} = ${h} cm.`, `${l} × ${b} = ${l * b}. ${l * b * h} ÷ ${l * b} = ${h} cm.`); }
  ],
  [
    () => { const l = ri(4, 8), b = ri(2, 4), h = ri(2, 5); return Q(`Een aquarium is ${l} dm lang, ${b} dm breed en ${h} dm hoog. 1 dm³ is 1 liter. Hoeveel liter water past erin?`, `Bir akvaryumun uzunluğu ${l} dm, genişliği ${b} dm, yüksekliği ${h} dm. 1 dm³ = 1 litre. İçine kaç litre su sığar?`, l * b * h, "liter",
      `${l} × ${b} × ${h} = ${l * b * h} dm³ = ${l * b * h} liter.`, `${l} × ${b} × ${h} = ${l * b * h} dm³ = ${l * b * h} litre.`); },
    () => { const l = ri(3, 6), b = ri(2, 4), h = ri(2, 4), n = ri(2, 5); return Q(`In een doos passen ${l} blokjes in de lengte, ${b} in de breedte en ${h} in de hoogte. Hoeveel blokjes passen er in ${n} zulke dozen?`, `Bir kutuya uzunlamasına ${l}, enine ${b}, yukarı doğru ${h} küp sığıyor. Böyle ${n} kutuya toplam kaç küp sığar?`, l * b * h * n, "",
      `Eén doos: ${l} × ${b} × ${h} = ${l * b * h}. ${n} dozen: ${l * b * h * n}.`, `Bir kutu: ${l} × ${b} × ${h} = ${l * b * h}. ${n} kutu: ${l * b * h * n}.`); }
  ]
];

// ----- Priemgetallen en delers
const PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47];
const COMPOSITE = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 27, 28, 33, 35, 39, 45, 49];
GEN.priem = [
  [
    () => { const p = pick(PRIMES), w = shuffle(COMPOSITE).slice(0, 3); return Q(`Welk getal is een <b>priemgetal</b>?`, `Hangisi bir <b>asal sayıdır</b>?`, p, "",
      `${p} kun je alleen delen door 1 en door ${p}.`, `${p} sadece 1'e ve ${p}'e bölünür.`, { opts: shuffle([p, ...w]).map(num) }); },
    () => { const n = pick([6, 8, 9, 10, 12, 14, 15, 16, 18, 20]); const d = divisors(n); return Q(`Hoeveel delers heeft ${n}? (Tel 1 en ${n} ook mee.)`, `${n} sayısının kaç böleni var? (1'i ve ${n}'i de say.)`, d.length, "",
      `De delers van ${n}: ${d.join(", ")}. Dat zijn er ${d.length}.`, `${n} sayısının bölenleri: ${d.join(", ")}. ${d.length} tane.`); }
  ],
  [
    () => { const c = pick(COMPOSITE.filter(x => x % 2)), w = shuffle(PRIMES.filter(x => x > 2)).slice(0, 3); const d = divisors(c)[1]; return Q(`Welk getal is <b>geen</b> priemgetal?`, `Hangisi asal sayı <b>değildir</b>?`, c, "",
      `${c} = ${d} × ${c / d}, dus geen priemgetal.`, `${c} = ${d} × ${c / d}, yani asal değil.`, { opts: shuffle([c, ...w]).map(num) }); },
    () => { const [a, b] = pick([[1, 10], [10, 20], [20, 30], [30, 40], [1, 20], [40, 50]]); const ps = PRIMES.filter(p => p > a && p < b); return Q(`Hoeveel priemgetallen liggen er tussen ${a} en ${b}?`, `${a} ile ${b} arasında kaç asal sayı var?`, ps.length, "",
      `${ps.join(", ")}: dat zijn er ${ps.length}.`, `${ps.join(", ")}: ${ps.length} tane.`); },
    () => { const n = pick(COMPOSITE.filter(x => x > 8)); const d = divisors(n); return Q(`Wat is de grootste deler van ${n}, behalve ${n} zelf?`, `${n} sayısının, kendisi hariç en büyük böleni kaçtır?`, d[d.length - 2], "",
      `De delers van ${n}: ${d.join(", ")}. De grootste na ${n} is ${d[d.length - 2]}.`, `${n} sayısının bölenleri: ${d.join(", ")}. ${n}'den sonraki en büyüğü ${d[d.length - 2]}.`); }
  ],
  [
    () => { const g = pick([2, 3, 4, 5, 6]), [x, y] = pick([[2, 3], [3, 4], [2, 5], [3, 5], [4, 5]]); const a = g * x, b = g * y; return Q(`Je hebt ${a} rode en ${b} blauwe ballonnen. Je maakt zo veel mogelijk <b>gelijke</b> trossen en gebruikt alle ballonnen. Hoeveel trossen maak je?`, `${a} kırmızı ve ${b} mavi balonun var. Bütün balonları kullanarak olabildiğince çok sayıda <b>eşit</b> demet yapıyorsun. Kaç demet olur?`, gcd(a, b), "",
      `Het grootste getal dat in ${a} en in ${b} past is ${gcd(a, b)}. Elke tros: ${x} rode en ${y} blauwe.`, `Hem ${a}'i hem ${b}'i bölen en büyük sayı ${gcd(a, b)}. Her demette ${x} kırmızı, ${y} mavi.`); },
    () => { const n = pick([12, 16, 18, 20, 24, 30]); const d = divisors(n); return Q(`Je hebt ${n} snoepjes en doet ze in zakjes met in elk zakje evenveel. Op hoeveel manieren kan dat? (Ook 1 zakje en ${n} zakjes tellen mee.)`, `${n} şekerin var; her torbada eşit sayıda olacak şekilde torbalara koyuyorsun. Bu kaç farklı şekilde yapılabilir? (1 torba ve ${n} torba da sayılır.)`, d.length, "",
      `Het aantal zakjes moet een deler van ${n} zijn: ${d.join(", ")}. Dat zijn ${d.length} manieren.`, `Torba sayısı ${n}'in böleni olmalı: ${d.join(", ")}. ${d.length} farklı şekil.`); }
  ]
];

// ----- Hoeken
const ANGLE_OPTS = [{ v: "scherp", nl: "scherpe hoek", tr: "dar açı" }, { v: "recht", nl: "rechte hoek", tr: "dik açı" }, { v: "stomp", nl: "stompe hoek", tr: "geniş açı" }];
GEN.hoeken = [
  [
    () => { const g = pick([20, 35, 45, 60, 80, 90, 90, 100, 120, 135, 150, 170]); const v = g < 90 ? "scherp" : g === 90 ? "recht" : "stomp"; return Q(`Een hoek is ${g} graden. Wat voor hoek is dat?`, `Bir açı ${g} derece. Bu nasıl bir açıdır?`, v, "",
      `Kleiner dan 90° is scherp, precies 90° is recht, groter dan 90° is stomp.`, `90°'den küçük dar, tam 90° dik, 90°'den büyük geniş açıdır.`, { opts: ANGLE_OPTS }); },
    () => { const n = ri(1, 4); return Q(`Een kwart draai is 90 graden. Hoeveel graden draai je bij ${n} kwart ${n === 1 ? "draai" : "draaien"}?`, `Çeyrek dönüş 90 derecedir. ${n} çeyrek dönüş kaç derece eder?`, 90 * n, "graden",
      `${n} × 90 = ${90 * n} graden.`, `${n} × 90 = ${90 * n} derece.`); }
  ],
  [
    () => { const a = ri(4, 14) * 5; return Q(`Een rechte hoek (90°) is in twee stukken verdeeld. Het ene stuk is ${a}°. Hoe groot is het andere stuk?`, `Bir dik açı (90°) iki parçaya bölünmüş. Bir parça ${a}°. Diğer parça kaç derece?`, 90 - a, "graden",
      `90 − ${a} = ${90 - a} graden.`, `90 − ${a} = ${90 - a} derece.`); },
    () => { const a = ri(6, 14) * 5, b = ri(6, 14) * 5; return Q(`Twee hoeken van een driehoek zijn ${a}° en ${b}°. Hoe groot is de derde hoek? (Samen altijd 180°.)`, `Bir üçgenin iki açısı ${a}° ve ${b}°. Üçüncü açı kaç derece? (Toplam hep 180°.)`, 180 - a - b, "graden",
      `180 − ${a} − ${b} = ${180 - a - b} graden.`, `180 − ${a} − ${b} = ${180 - a - b} derece.`); }
  ],
  [
    () => { const h = ri(1, 6); return Q(`Het is precies ${h} uur. Hoe groot is de hoek tussen de grote en de kleine wijzer? (Tussen twee cijfers op de klok zit 30°.)`, `Saat tam ${h}. Akrep ile yelkovan arasındaki açı kaç derece? (Saatte iki rakam arası 30°.)`, 30 * h, "graden",
      `${h} × 30 = ${30 * h} graden.`, `${h} × 30 = ${30 * h} derece.`); },
    () => { const a = ri(14, 20) * 5, b = ri(14, 20) * 5, c = ri(14, 20) * 5; return Q(`Drie hoeken van een vierhoek zijn ${a}°, ${b}° en ${c}°. Hoe groot is de vierde hoek? (Samen altijd 360°.)`, `Bir dörtgenin üç açısı ${a}°, ${b}° ve ${c}°. Dördüncü açı kaç derece? (Toplam hep 360°.)`, 360 - a - b - c, "graden",
      `360 − ${a} − ${b} − ${c} = ${360 - a - b - c} graden.`, `360 − ${a} − ${b} − ${c} = ${360 - a - b - c} derece.`); }
  ]
];

// ----- Schaal
GEN.schaal = [
  [
    () => { const a = ri(2, 12); return Q(`Een plattegrond heeft schaal 1 : 100. Een muur is op de tekening ${a} cm. Hoe lang is de muur in het echt, in <b>meters</b>?`, `Bir krokinin ölçeği 1 : 100. Bir duvar çizimde ${a} cm. Gerçekte kaç <b>metre</b>?`, a, "m",
      `1 cm op de tekening is 100 cm = 1 m in het echt. ${a} cm is dus ${a} m.`, `Çizimdeki 1 cm gerçekte 100 cm = 1 m. Yani ${a} cm = ${a} m.`); },
    () => { const a = ri(2, 9), s = pick([10, 20, 50]); return Q(`Een tekening heeft schaal 1 : ${s}. Een lijn is ${a} cm op de tekening. Hoeveel <b>cm</b> is dat in het echt?`, `Bir çizimin ölçeği 1 : ${s}. Bir çizgi çizimde ${a} cm. Gerçekte kaç <b>cm</b>?`, a * s, "cm",
      `${a} × ${s} = ${a * s} cm.`, `${a} × ${s} = ${a * s} cm.`); }
  ],
  [
    () => { const a = ri(3, 15); return Q(`Een kamer is in het echt ${a} m lang. Je tekent de kamer op schaal 1 : 100. Hoeveel cm wordt dat op je tekening?`, `Bir oda gerçekte ${a} m uzunluğunda. Odayı 1 : 100 ölçeğiyle çiziyorsun. Çizimde kaç cm olur?`, a, "cm",
      `${a} m = ${a * 100} cm. ${a * 100} ÷ 100 = ${a} cm.`, `${a} m = ${a * 100} cm. ${a * 100} ÷ 100 = ${a} cm.`); },
    () => { const a = ri(1, 8) * 2; return Q(`Een tekening heeft schaal 1 : 50. Een kast is op de tekening ${a} cm breed. Hoe breed is de kast in het echt, in <b>meters</b>?`, `Bir çizimin ölçeği 1 : 50. Bir dolap çizimde ${a} cm genişliğinde. Gerçekte kaç <b>metre</b>?`, a / 2, "m",
      `${a} × 50 = ${a * 50} cm = ${a / 2} m.`, `${a} × 50 = ${a * 50} cm = ${a / 2} m.`); }
  ],
  [
    () => { const a = ri(3, 8), b = ri(2, 6); return Q(`Op een plattegrond met schaal 1 : 100 is een kamer ${a} cm bij ${b} cm. Wat is de oppervlakte van de kamer in het echt, in m²?`, `Ölçeği 1 : 100 olan bir krokide bir oda ${a} cm × ${b} cm. Odanın gerçek alanı kaç m²?`, a * b, "m²",
      `In het echt: ${a} m bij ${b} m. Oppervlakte = ${a} × ${b} = ${a * b} m².`, `Gerçekte: ${a} m × ${b} m. Alan = ${a} × ${b} = ${a * b} m².`); },
    () => { const k = pick([2, 5, 10]), a = ri(3, 9); return Q(`Op een kaart is 1 cm in het echt ${k} km. Van huis naar het stadion is ${a} cm op de kaart. Hoeveel km is het <b>heen en terug</b>?`, `Bir haritada 1 cm gerçekte ${k} km. Evden stadyuma haritada ${a} cm. <b>Gidiş dönüş</b> kaç km?`, 2 * a * k, "km",
      `Heen: ${a} × ${k} = ${a * k} km. Heen en terug: ${2 * a * k} km.`, `Gidiş: ${a} × ${k} = ${a * k} km. Gidiş dönüş: ${2 * a * k} km.`); }
  ]
];

// ----- Negatieve getallen
GEN.negatief = [
  [
    () => { const a = ri(1, 8), b = a + ri(1, 8); return Q(`Het is ${a} graden. Het wordt ${b} graden kouder. Hoe koud is het dan?`, `Hava ${a} derece. ${b} derece soğuyor. Hava kaç derece olur?`, a - b, "graden",
      `${a} − ${b} = ${a - b}. Het is ${b - a} graden onder nul.`, `${a} − ${b} = ${a - b}. Sıfırın altında ${b - a} derece.`); },
    () => { const a = ri(2, 10), b = ri(1, 15); return Q(`Hoeveel is −${a} + ${b}?`, `−${a} + ${b} kaç eder?`, b - a, "",
      `Begin bij −${a} en ga ${b} stappen omhoog: ${b - a}.`, `−${a}'den başla, ${b} adım yukarı çık: ${b - a}.`); }
  ],
  [
    () => { const a = ri(1, 12), b = ri(1, 15); return Q(`In de nacht is het −${a} graden, in de middag ${b} graden. Hoeveel graden is het <b>verschil</b>?`, `Gece hava −${a} derece, öğlen ${b} derece. Aradaki <b>fark</b> kaç derece?`, a + b, "graden",
      `Van −${a} naar 0 is ${a}, van 0 naar ${b} is ${b}. Samen ${a + b}.`, `−${a}'den 0'a ${a}, 0'dan ${b}'e ${b}. Toplam ${a + b}.`); },
    () => { const a = ri(1, 10), b = ri(1, 10); return Q(`Hoeveel is −${a} − ${b}?`, `−${a} − ${b} kaç eder?`, -a - b, "",
      `Begin bij −${a} en ga nog ${b} stappen omlaag: −${a + b}.`, `−${a}'den başla, ${b} adım daha aşağı in: −${a + b}.`); }
  ],
  [
    () => { const a = ri(1, 5), n = a + ri(1, 3); return Q(`Je staat in de lift op verdieping ${a}. De lift gaat ${n} verdiepingen naar beneden. Op welke verdieping ben je nu? (De begane grond is 0.)`, `Asansörde ${a}. kattasın. Asansör ${n} kat aşağı iniyor. Şimdi kaçıncı kattasın? (Zemin kat 0.)`, a - n, "",
      `${a} − ${n} = ${a - n}. Dat is ${n - a} ${n - a === 1 ? "verdieping" : "verdiepingen"} onder de grond.`, `${a} − ${n} = ${a - n}. Yerin ${n - a} kat altı.`); },
    () => { const a = ri(2, 9), b = ri(3, 12), c = ri(2, 9); return Q(`Om 7 uur is het −${a} graden. Tot de middag wordt het ${b} graden warmer. In de avond wordt het weer ${c} graden kouder. Hoeveel graden is het in de avond?`, `Saat 7'de hava −${a} derece. Öğlene kadar ${b} derece ısınıyor. Akşam yine ${c} derece soğuyor. Akşam hava kaç derece?`, -a + b - c, "graden",
      `−${a} + ${b} = ${b - a}. ${b - a} − ${c} = ${-a + b - c}.`, `−${a} + ${b} = ${b - a}. ${b - a} − ${c} = ${-a + b - c}.`); }
  ]
];

// ----- De rij van Fibonacci: 1, 1, 2, 3, 5, 8, ... (each number is the sum of the two before it)
const FIB = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233];     // FIB[n] = n-th Fibonacci number
GEN.fibonacci = [
  [
    () => { const n = ri(5, 10); const row = FIB.slice(n - 3, n + 1).join(", "); return Q(`Dit is een stuk van de rij van Fibonacci: ${row}, … Welk getal komt hierna?`, `Bu, Fibonacci dizisinin bir parçası: ${row}, … Sıradaki sayı hangisi?`, FIB[n + 1], "",
      `Tel de laatste twee op: ${FIB[n - 1]} + ${FIB[n]} = ${FIB[n + 1]}.`, `Son iki sayıyı topla: ${FIB[n - 1]} + ${FIB[n]} = ${FIB[n + 1]}.`); },
    () => { const n = ri(5, 9); return Q(`De rij van Fibonacci begint zo: 1, 1, 2, 3, 5, … Wat is het ${n}e getal van de rij?`, `Fibonacci dizisi şöyle başlar: 1, 1, 2, 3, 5, … Dizinin ${n}. sayısı kaçtır?`, FIB[n], "",
      `De rij: ${FIB.slice(1, n + 1).join(", ")}. Het ${n}e getal is ${FIB[n]}.`, `Dizi: ${FIB.slice(1, n + 1).join(", ")}. ${n}. sayı ${FIB[n]}.`); },
    () => { const n = ri(4, 10); return Q(`In de rij van Fibonacci staan ${FIB[n]} en ${FIB[n + 1]} naast elkaar. Welk getal komt daarna?`, `Fibonacci dizisinde ${FIB[n]} ve ${FIB[n + 1]} yan yana. Sonraki sayı kaçtır?`, FIB[n + 2], "",
      `${FIB[n]} + ${FIB[n + 1]} = ${FIB[n + 2]}.`, `${FIB[n]} + ${FIB[n + 1]} = ${FIB[n + 2]}.`); }
  ],
  [
    () => { const n = ri(5, 10); return Q(`Welk getal ontbreekt in de rij van Fibonacci? ${FIB[n - 1]}, ${FIB[n]}, ?, ${FIB[n + 2]}`, `Fibonacci dizisinde eksik sayı hangisi? ${FIB[n - 1]}, ${FIB[n]}, ?, ${FIB[n + 2]}`, FIB[n + 1], "",
      `${FIB[n - 1]} + ${FIB[n]} = ${FIB[n + 1]}. Controle: ${FIB[n]} + ${FIB[n + 1]} = ${FIB[n + 2]}.`, `${FIB[n - 1]} + ${FIB[n]} = ${FIB[n + 1]}. Kontrol: ${FIB[n]} + ${FIB[n + 1]} = ${FIB[n + 2]}.`); },
    () => { const n = ri(5, 10); return Q(`Welk getal staat vooraan? ?, ${FIB[n]}, ${FIB[n + 1]} (rij van Fibonacci)`, `En baştaki sayı hangisi? ?, ${FIB[n]}, ${FIB[n + 1]} (Fibonacci dizisi)`, FIB[n - 1], "",
      `Ga terug: ${FIB[n + 1]} − ${FIB[n]} = ${FIB[n - 1]}.`, `Geriye git: ${FIB[n + 1]} − ${FIB[n]} = ${FIB[n - 1]}.`); },
    () => { const a = ri(2, 5), b = ri(2, 6); const r = [a, b]; while (r.length < 6) r.push(r[r.length - 1] + r[r.length - 2]);
      return Q(`Een rij begint met ${a} en ${b}. Daarna geldt de regel van Fibonacci: tel de laatste twee getallen op. Wat is het <b>6e</b> getal?`, `Bir dizi ${a} ve ${b} ile başlıyor. Sonra Fibonacci kuralı geçerli: son iki sayıyı topla. <b>6.</b> sayı kaçtır?`, r[5], "",
        `De rij: ${r.join(", ")}.`, `Dizi: ${r.join(", ")}.`); },
    () => { const n = ri(5, 9); return Q(`Tel de eerste ${n} getallen van de rij van Fibonacci op: ${FIB.slice(1, n + 1).join(" + ")}. Hoeveel is dat?`, `Fibonacci dizisinin ilk ${n} sayısını topla: ${FIB.slice(1, n + 1).join(" + ")}. Kaç eder?`, FIB[n + 2] - 1, "",
      `Samen ${FIB[n + 2] - 1}. Dat is altijd 1 minder dan het getal twee plaatsen verder (${FIB[n + 2]}).`, `Toplam ${FIB[n + 2] - 1}. Bu hep, iki sıra sonraki sayıdan (${FIB[n + 2]}) 1 eksiktir.`); }
  ],
  [
    () => { const n = ri(4, 9); return Q(`Een paar konijnen krijgt vanaf de tweede maand elke maand een nieuw paar jongen. Het aantal paren groeit zo: 1, 1, 2, 3, 5, … Hoeveel paren zijn er in maand ${n}?`, `Bir çift tavşan, ikinci aydan itibaren her ay yeni bir çift yavru yapıyor. Çift sayısı şöyle artıyor: 1, 1, 2, 3, 5, … ${n}. ayda kaç çift tavşan olur?`, FIB[n], "",
      `Dat is de rij van Fibonacci: ${FIB.slice(1, n + 1).join(", ")}. In maand ${n}: ${FIB[n]} paren.`, `Bu Fibonacci dizisi: ${FIB.slice(1, n + 1).join(", ")}. ${n}. ayda ${FIB[n]} çift.`); },
    () => { const n = ri(3, 7); return Q(`Je loopt een trap op met ${n} treden. Je neemt steeds 1 trede of 2 treden tegelijk. Op hoeveel manieren kun je boven komen? (Tip: bij 1 trede 1 manier, bij 2 treden 2 manieren, daarna de regel van Fibonacci.)`, `${n} basamaklı bir merdiveni çıkıyorsun. Her adımda 1 ya da 2 basamak çıkıyorsun. Yukarı kaç farklı şekilde çıkabilirsin? (İpucu: 1 basamakta 1 yol, 2 basamakta 2 yol, sonra Fibonacci kuralı.)`, FIB[n + 1], "",
      `Aantal manieren per trap: ${FIB.slice(2, n + 2).join(", ")}. Bij ${n} treden: ${FIB[n + 1]}.`, `Basamak sayısına göre yol sayısı: ${FIB.slice(2, n + 2).join(", ")}. ${n} basamakta: ${FIB[n + 1]}.`); },
    () => { const f = pick([5, 8, 13, 21, 34]), w = shuffle([4, 6, 7, 9, 10, 12, 15, 20].filter(x => x !== f)).slice(0, 3); return Q(`Veel bloemen hebben een aantal bloemblaadjes dat in de rij van Fibonacci staat. Welk aantal staat in die rij?`, `Birçok çiçeğin taç yaprağı sayısı Fibonacci dizisinde yer alır. Hangi sayı bu dizidedir?`, f, "",
      `De rij: 1, 1, 2, 3, 5, 8, 13, 21, 34, … ${f} staat erin.`, `Dizi: 1, 1, 2, 3, 5, 8, 13, 21, 34, … ${f} bu dizide.`, { opts: shuffle([f, ...w]).map(num) }); },
    () => { const n = ri(5, 8); return Q(`Op een dennenappel tel je ${FIB[n]} spiralen naar links. Het aantal spiralen naar rechts is het <b>volgende</b> Fibonacci-getal. Hoeveel spiralen naar rechts zijn er?`, `Bir çam kozalağında sola doğru ${FIB[n]} spiral sayıyorsun. Sağa doğru spiral sayısı <b>sonraki</b> Fibonacci sayısı. Sağa doğru kaç spiral var?`, FIB[n + 1], "",
      `Na ${FIB[n]} komt ${FIB[n - 1]} + ${FIB[n]} = ${FIB[n + 1]}.`, `${FIB[n]}'den sonra ${FIB[n - 1]} + ${FIB[n]} = ${FIB[n + 1]} gelir.`); },
    () => { const n = ri(3, 8); return Q(`Een mannetjesbij heeft 1 ouder, 2 grootouders en 3 overgrootouders. Dat gaat verder volgens de rij van Fibonacci: 1, 2, 3, 5, … Hoeveel voorouders heeft hij ${n} generaties terug?`, `Bir erkek arının 1 ebeveyni, 2 büyük ebeveyni ve 3 büyük büyük ebeveyni vardır. Bu, Fibonacci dizisine göre devam eder: 1, 2, 3, 5, … ${n} nesil geride kaç atası vardır?`, FIB[n + 1], "",
      `De rij: ${FIB.slice(2, n + 2).join(", ")}. ${n} generaties terug: ${FIB[n + 1]}.`, `Dizi: ${FIB.slice(2, n + 2).join(", ")}. ${n} nesil geride: ${FIB[n + 1]}.`); }
  ]
];

// ----- Patronen in de natuur: symmetrie, zeshoeken, vertakkingen
const SYM = [["een vierkant", "bir karenin", 4], ["een rechthoek", "bir dikdörtgenin", 2], ["een gelijkzijdige driehoek", "bir eşkenar üçgenin", 3],
  ["de letter A", "A harfinin", 1], ["de letter H", "H harfinin", 2], ["een vlinder", "bir kelebeğin", 1], ["een sneeuwvlok", "bir kar tanesinin", 6], ["een regelmatige zeshoek", "bir düzgün altıgenin", 6]];
GEN.natuurpatronen = [
  [
    () => { const [nl, tr, n] = pick(SYM); return Q(`Hoeveel symmetrieassen (vouwlijnen) heeft ${nl}?`, `${tr.charAt(0).toUpperCase() + tr.slice(1)} kaç simetri ekseni (katlama çizgisi) vardır?`, n, "",
      `Je kunt ${nl} op ${n} ${n === 1 ? "manier" : "manieren"} zo dubbelvouwen dat de helften precies op elkaar passen.`, `Bu şekil, iki yarısı tam üst üste gelecek şekilde ${n} farklı yerden katlanabilir.`); },
    () => { const a = ri(2, 9); return Q(`Een cel van een honingraat is een zeshoek. Alle zijden zijn ${a} mm. Wat is de omtrek van één cel?`, `Bal peteğinin bir gözü altıgendir. Bütün kenarları ${a} mm. Bir gözün çevresi kaç mm?`, 6 * a, "mm",
      `Een zeshoek heeft 6 zijden: 6 × ${a} = ${6 * a} mm.`, `Altıgenin 6 kenarı var: 6 × ${a} = ${6 * a} mm.`); },
    () => { const a = ri(3, 12); return Q(`Een vlinder is symmetrisch. Op de linkervleugel zitten ${a} stippen. Hoeveel stippen heeft de vlinder in totaal?`, `Kelebek simetriktir. Sol kanadında ${a} benek var. Kelebekte toplam kaç benek var?`, 2 * a, "",
      `Rechts zitten er evenveel: 2 × ${a} = ${2 * a}.`, `Sağ kanatta da aynı sayıda var: 2 × ${a} = ${2 * a}.`); }
  ],
  [
    () => { const k = ri(2, 8); return Q(`Een sneeuwvlok heeft 6 armen. Elke arm heeft ${k} kleine takjes. Hoeveel takjes heeft de sneeuwvlok?`, `Bir kar tanesinin 6 kolu var. Her kolda ${k} küçük dal var. Kar tanesinde toplam kaç dal var?`, 6 * k, "",
      `6 × ${k} = ${6 * k}.`, `6 × ${k} = ${6 * k}.`); },
    () => { const n = ri(3, 6); return Q(`Een tak splitst zich in 2 takken. Elke nieuwe tak splitst zich weer in 2. Hoeveel uiteinden zijn er na ${n} keer splitsen?`, `Bir dal 2 dala ayrılıyor. Her yeni dal yine 2'ye ayrılıyor. ${n} kez ayrıldıktan sonra kaç uç olur?`, 2 ** n, "",
      `Elke keer verdubbelt het: ${Array.from({ length: n }, (_, i) => 2 ** (i + 1)).join(", ")}.`, `Her seferinde iki katına çıkar: ${Array.from({ length: n }, (_, i) => 2 ** (i + 1)).join(", ")}.`); },
    () => { const n = ri(3, 9); return Q(`Je tekent ${n} losse zeshoeken. Hoeveel zijden teken je in totaal?`, `Birbirine değmeyen ${n} altıgen çiziyorsun. Toplam kaç kenar çizersin?`, 6 * n, "",
      `${n} × 6 = ${6 * n}.`, `${n} × 6 = ${6 * n}.`); }
  ],
  [
    () => { const a = ri(4, 9), b = ri(3, 8); return Q(`Een varenblad heeft ${a} zijblaadjes. Elk zijblaadje lijkt op het hele blad en heeft zelf ${b} nog kleinere blaadjes. Hoeveel van die kleinste blaadjes zijn er?`, `Bir eğrelti otu yaprağının ${a} yan yaprağı var. Her yan yaprak bütün yaprağa benziyor ve kendisinin de ${b} daha küçük yaprağı var. En küçük yapraklardan toplam kaç tane var?`, a * b, "",
      `${a} × ${b} = ${a * b}. Het kleine lijkt op het grote: dat heet een fractal.`, `${a} × ${b} = ${a * b}. Küçük parça büyüğe benziyor: buna fraktal denir.`); },
    () => { const r = ri(3, 6), m = ri(5, 10), d = ri(2, 5); return Q(`Bijen bouwen elke dag ${r} rijen van ${m} cellen. Hoeveel cellen hebben ze na ${d} dagen?`, `Arılar her gün ${r} sıra, her sırada ${m} göz yapıyor. ${d} gün sonra kaç göz olur?`, r * m * d, "",
      `Per dag ${r} × ${m} = ${r * m}. Na ${d} dagen: ${r * m * d}.`, `Günde ${r} × ${m} = ${r * m}. ${d} gün sonra: ${r * m * d}.`); },
    () => { const k = ri(2, 6), n = ri(3, 7); return Q(`Een zeester heeft 5 armen. Op elke arm zitten ${k} rijen van ${n} zuignapjes. Hoeveel zuignapjes heeft de zeester?`, `Bir deniz yıldızının 5 kolu var. Her kolda ${k} sıra, her sırada ${n} vantuz var. Deniz yıldızında kaç vantuz var?`, 5 * k * n, "",
      `Per arm ${k} × ${n} = ${k * n}. 5 armen: ${5 * k * n}.`, `Bir kolda ${k} × ${n} = ${k * n}. 5 kolda: ${5 * k * n}.`); }
  ]
];

// School topics (kids/rekenen-school.js) are added to the same lists, so the page sees one subject
Object.assign(GEN, S_GEN);
export const makeQuestion = maker(GEN);
export const kindsPerLevel = topicId => GEN[topicId].map(l => l.length);

// ---------------------------------------------------------------- theory (short, with the figure next to it)
// Each topic: a list of blocks { nl, tr, fig? }. Kept short: a rule, then one worked example.
export const THEORY = {
  meetkunde: [
    { fig: fig.grid(6, 4, "6 cm", "4 cm"), nl: "<b>Wat is oppervlakte?</b> Verdeel de figuur in hokjes van 1 cm bij 1 cm. Elk hokje is <b>1 cm²</b>.<br>Deze rechthoek van 6 cm bij 4 cm heeft 4 rijen van 6 hokjes: 6 × 4 = <b>24 hokjes</b>. De oppervlakte is dus 24 cm².<br>Oppervlakte = hoeveel hokjes van 1 bij 1 erin passen.",
      tr: "<b>Alan nedir?</b> Şekli 1 cm × 1 cm küçük karelere böl. Her küçük kare <b>1 cm²</b> eder.<br>6 cm × 4 cm olan bu dikdörtgende 4 sıra var, her sırada 6 kare: 6 × 4 = <b>24 kare</b>. Yani alan 24 cm².<br>Alan = içine kaç tane 1×1 kare sığdığı." },
    { fig: fig.square("a"), nl: "<b>Vierkant</b>: alle vier zijden zijn even lang (a).<br><b>Omtrek = 4 × a</b><br><b>Oppervlakte = a × a</b><br>Voorbeeld: a = 5 cm → omtrek 20 cm, oppervlakte 25 cm².",
      tr: "<b>Kare</b>: dört kenarı da eşit (a).<br><b>Çevre = 4 × a</b><br><b>Alan = a × a</b><br>Örnek: a = 5 cm → çevre 20 cm, alan 25 cm²." },
    { fig: fig.rect("lengte (a)", "b"), nl: "<b>Rechthoek</b>: lengte a en breedte b.<br><b>Omtrek = 2 × (a + b)</b><br><b>Oppervlakte = a × b</b><br>Andersom: oppervlakte ÷ lengte = breedte.",
      tr: "<b>Dikdörtgen</b>: uzun kenar a, kısa kenar b.<br><b>Çevre = 2 × (a + b)</b><br><b>Alan = a × b</b><br>Tersi: alan ÷ uzun kenar = kısa kenar." },
    { fig: fig.circle("straal", false), nl: "<b>Cirkel</b>: de <b>straal</b> loopt van het midden naar de rand. De <b>diameter</b> loopt van rand tot rand door het midden.<br><b>Diameter = 2 × straal</b><br><b>Omtrek = π × diameter</b><br><b>Oppervlakte = π × straal × straal</b><br>π (pi) is ongeveer 3,14. Hier rekenen we met <b>π = 3</b>.",
      tr: "<b>Daire</b>: <b>yarıçap</b> merkezden kenara gider. <b>Çap</b> bir kenardan diğerine, merkezden geçer.<br><b>Çap = 2 × yarıçap</b><br><b>Çevre = π × çap</b><br><b>Alan = π × r × r</b><br>π (pi) yaklaşık 3,14. Burada <b>π = 3</b> alıyoruz." },
    { nl: "<b>Onthoud</b>: omtrek = eromheen lopen (hek, lint). Oppervlakte = bedekken (tapijt, verf).<br>Wat blijft vrij? Grote figuur − kleine figuur.",
      tr: "<b>Aklında kalsın</b>: çevre = etrafında yürümek (çit, şerit). Alan = içini kaplamak (halı, boya).<br>Boş kalan yer = büyük şekil − küçük şekil." },
    { eg: true, nl: "<b>Voetbalveld</b>: de witte lijn eromheen is de <b>omtrek</b>, al het gras is de <b>oppervlakte</b>. Een veld van 100 m bij 60 m: een rondje langs de lijn is 320 m, en er ligt 6000 m² gras.<br><b>Pizza</b>: de korst is de omtrek, de hele pizza met kaas is de oppervlakte.<br><b>Proefje met π</b>: leg een touwtje om een blik of beker en meet het. Meet daarna hoe breed het blik is. Het touwtje is ongeveer 3 keer zo lang. Dat geldt voor elke cirkel, groot of klein: dat getal is π.",
      tr: "<b>Futbol sahası</b>: etrafındaki beyaz çizgi <b>çevre</b>, bütün çim <b>alan</b>. 100 m × 60 m bir sahada çizgi boyunca bir tur 320 m eder, sahada 6000 m² çim vardır.<br><b>Pizza</b>: kenarındaki kabuk çevre, peynirli bütün pizza alan.<br><b>π deneyi</b>: bir konserve kutusunun ya da bardağın etrafına ip sar ve ölç. Sonra kutunun genişliğini ölç. İp yaklaşık 3 kat uzundur. Bu, büyük küçük her dairede böyledir: bu sayı π'dir." }
  ],
  som: [
    { nl: "Hoe tel je snel <b>1 + 2 + 3 + … + 10</b> op?<br>Maak paren: 1 + 10 = 11, 2 + 9 = 11, 3 + 8 = 11, 4 + 7 = 11, 5 + 6 = 11.<br>Dat zijn <b>5 paren van 11</b>: 5 × 11 = <b>55</b>.",
      tr: "<b>1 + 2 + 3 + … + 10</b> hızlıca nasıl toplanır?<br>Çiftler yap: 1 + 10 = 11, 2 + 9 = 11, 3 + 8 = 11, 4 + 7 = 11, 5 + 6 = 11.<br><b>11 eden 5 çift</b> var: 5 × 11 = <b>55</b>." },
    { nl: "<b>Regel</b>: 1 + 2 + … + n = <b>n × (n + 1) ÷ 2</b><br>Voorbeeld: tot 7 → 7 × 8 ÷ 2 = 56 ÷ 2 = 28.<br>Voorbeeld: tot 100 → 100 × 101 ÷ 2 = 5050.",
      tr: "<b>Kural</b>: 1 + 2 + … + n = <b>n × (n + 1) ÷ 2</b><br>Örnek: 7'ye kadar → 7 × 8 ÷ 2 = 56 ÷ 2 = 28.<br>Örnek: 100'e kadar → 100 × 101 ÷ 2 = 5050." },
    { nl: "Handig om te weten: de eerste n <b>oneven</b> getallen samen zijn n × n. Voorbeeld: 1 + 3 + 5 = 9 = 3 × 3.",
      tr: "Bilmesi güzel: ilk n <b>tek</b> sayının toplamı n × n eder. Örnek: 1 + 3 + 5 = 9 = 3 × 3." },
    { eg: true, nl: "<b>Het verhaal van Gauss</b>: men vertelt dat de wiskundige Gauss als schooljongen alle getallen van 1 tot 100 moest optellen. De meester dacht dat de klas daar lang mee bezig zou zijn. Gauss zag de paren (1 + 100, 2 + 99, …) en had het antwoord bijna meteen: 5050.<br><b>Voetbal</b>: in de Eredivisie spelen 18 clubs. Speelt elke club één keer tegen elke andere, dan zijn dat 17 + 16 + … + 1 = 153 wedstrijden.",
      tr: "<b>Gauss'un hikâyesi</b>: anlatılana göre matematikçi Gauss küçük bir öğrenciyken 1'den 100'e kadar bütün sayıları toplaması istenmiş. Öğretmen sınıfın uzun süre uğraşacağını düşünmüş. Gauss çiftleri görmüş (1 + 100, 2 + 99, …) ve cevabı hemen bulmuş: 5050.<br><b>Futbol</b>: Eredivisie'de 18 kulüp var. Her kulüp diğer her kulüple bir kez oynarsa 17 + 16 + … + 1 = 153 maç olur." }
  ],
  machten: [
    { nl: "<b>Macht</b>: het kleine getal zegt hoe vaak je het grote getal met zichzelf vermenigvuldigt.<br>5² = 5 × 5 = 25 (je zegt: vijf <b>kwadraat</b>)<br>2³ = 2 × 2 × 2 = 8 (twee tot de derde)",
      tr: "<b>Üslü sayı</b>: küçük sayı, büyük sayının kaç kez kendisiyle çarpılacağını söyler.<br>5² = 5 × 5 = 25 (beşin <b>karesi</b>)<br>2³ = 2 × 2 × 2 = 8 (ikinin küpü)" },
    { nl: "<b>Wortel</b> (√) is het omgekeerde van kwadraat.<br>√49 = 7, want 7 × 7 = 49.<br>Vraag jezelf: welk getal keer zichzelf geeft dit?",
      tr: "<b>Karekök</b> (√), karenin tersidir.<br>√49 = 7, çünkü 7 × 7 = 49.<br>Kendine sor: hangi sayı × kendisi bunu verir?" },
    { fig: fig.square("a"), nl: "Een vierkant met zijde a heeft oppervlakte a². Ken je de oppervlakte, dan is de zijde de wortel: oppervlakte 36 → zijde √36 = 6.",
      tr: "Kenarı a olan karenin alanı a² olur. Alanı biliyorsan kenar kareköktür: alan 36 → kenar √36 = 6." },
    { eg: true, nl: "<b>Papier vouwen</b>: vouw een blad dubbel en je hebt 2 lagen. Nog een keer: 4. Nog een keer: 8. Na 10 keer vouwen zouden het 2¹⁰ = 1024 lagen zijn. Daarom lukt het bijna niemand om een blad vaker dan 7 keer dubbel te vouwen.<br><b>Schaakbord</b>: 8 rijen van 8 vakjes, dus 8² = 64 vakjes.<br><b>Vierkante kamer</b>: weet je dat de vloer 25 m² is, dan is elke muur √25 = 5 m lang.",
      tr: "<b>Kâğıt katlama</b>: bir kâğıdı ikiye katla, 2 kat olur. Bir daha: 4. Bir daha: 8. 10 kez katlasan 2¹⁰ = 1024 kat olurdu. Bu yüzden bir kâğıdı 7 kereden fazla katlamayı neredeyse kimse başaramaz.<br><b>Satranç tahtası</b>: 8 sıra, her sırada 8 kare, yani 8² = 64 kare.<br><b>Kare oda</b>: zeminin 25 m² olduğunu biliyorsan her duvar √25 = 5 m uzunluğundadır." }
  ],
  fibonacci: [
    { fig: fig.fibsquares(), nl: "De <b>rij van Fibonacci</b>: 1, 1, 2, 3, 5, 8, 13, 21, 34, …<br><b>Regel</b>: tel de laatste twee getallen op, dan heb je het volgende. 5 + 8 = 13, 8 + 13 = 21.<br>Vierkanten met zijden 1, 1, 2, 3 en 5 passen precies aan elkaar. Trek je daar een boog doorheen, dan krijg je een spiraal.",
      tr: "<b>Fibonacci dizisi</b>: 1, 1, 2, 3, 5, 8, 13, 21, 34, …<br><b>Kural</b>: son iki sayıyı topla, sıradaki sayıyı bulursun. 5 + 8 = 13, 8 + 13 = 21.<br>Kenarları 1, 1, 2, 3 ve 5 olan kareler birbirine tam oturur. İçlerinden bir yay çizersen spiral çıkar." },
    { nl: "<b>In de natuur</b> kom je deze getallen vaak tegen:<br>· bloemblaadjes: veel bloemen hebben er 3, 5, 8, 13 of 21<br>· dennenappel en zonnebloem: de spiralen naar links en naar rechts zijn vaak twee Fibonacci-getallen naast elkaar (8 en 13, of 21 en 34)<br>· een slakkenhuis groeit in een spiraal die op die van de vierkanten lijkt<br>Het klopt niet bij elke bloem, maar wel opvallend vaak.",
      tr: "<b>Doğada</b> bu sayılara sık rastlanır:<br>· taç yapraklar: birçok çiçekte 3, 5, 8, 13 ya da 21 tane olur<br>· çam kozalağı ve ayçiçeği: sola ve sağa dönen spirallerin sayısı çoğu zaman art arda iki Fibonacci sayısıdır (8 ve 13 ya da 21 ve 34)<br>· salyangoz kabuğu, karelerdeki spirale benzeyen bir spiralle büyür<br>Her çiçekte tutmaz ama şaşırtıcı derecede sık tutar." },
    { eg: true, nl: "<b>Zelf kijken</b>: tel de spiralen op een ananas of een dennenappel. Je vindt bijna altijd 8 en 13, of 13 en 21. Tel de blaadjes van een madeliefje of een andere bloem en kijk of het getal in de rij staat.",
      tr: "<b>Kendin bak</b>: bir ananasın ya da çam kozalağının spirallerini say. Neredeyse hep 8 ve 13 ya da 13 ve 21 bulursun. Bir papatyanın ya da başka bir çiçeğin yapraklarını say ve sayının dizide olup olmadığına bak." }
  ],
  natuurpatronen: [
    { nl: "<b>Symmetrie</b>: de ene helft is het spiegelbeeld van de andere. De vouwlijn heet <b>symmetrieas</b>. Een vlinder heeft er 1, een sneeuwvlok 6.<br><b>Zeshoeken</b>: bijen bouwen cellen met 6 zijden. Zeshoeken passen zonder gaten aan elkaar en er is weinig was voor nodig.<br><b>Vertakkingen</b>: bij een varen of een boom lijkt het kleine stuk op het grote. Zo'n patroon heet een <b>fractal</b>.",
      tr: "<b>Simetri</b>: bir yarı, diğer yarının ayna görüntüsüdür. Katlama çizgisine <b>simetri ekseni</b> denir. Kelebekte 1, kar tanesinde 6 tane vardır.<br><b>Altıgenler</b>: arılar 6 kenarlı gözler yapar. Altıgenler arada boşluk kalmadan birbirine oturur ve az balmumu harcanır.<br><b>Dallanma</b>: eğrelti otunda ya da ağaçta küçük parça büyüğe benzer. Böyle örüntüye <b>fraktal</b> denir." },
    { eg: true, nl: "<b>Zelf kijken</b>: snijd een appel dwars door (niet van steel naar onder, maar opzij): in het midden zie je een ster met 5 punten. Bekijk een blad van een varen of een stuk romanesco: elk klein stukje lijkt op het geheel. En een voetbal is gemaakt van vijfhoeken en zeshoeken die precies aan elkaar passen.",
      tr: "<b>Kendin bak</b>: bir elmayı enine kes (saptan aşağı değil, yandan): ortada 5 köşeli bir yıldız görürsün. Bir eğrelti otu yaprağına ya da romanesco brokoliye bak: her küçük parça bütüne benzer. Futbol topu da birbirine tam oturan beşgen ve altıgenlerden yapılmıştır." }
  ],
  getallen: [
    { nl: "<b>Kwadraatgetallen</b>: 1, 4, 9, 16, 25, … (1×1, 2×2, 3×3, …). Je kunt er een vierkant van leggen.<br><b>Driehoeksgetallen</b>: 1, 3, 6, 10, 15, … (1, 1+2, 1+2+3, …). Je kunt er een driehoek van leggen.",
      tr: "<b>Kare sayılar</b>: 1, 4, 9, 16, 25, … (1×1, 2×2, 3×3, …). Bunlarla kare dizilir.<br><b>Üçgen sayılar</b>: 1, 3, 6, 10, 15, … (1, 1+2, 1+2+3, …). Bunlarla üçgen dizilir." },
    { nl: "Het n-de driehoeksgetal = n × (n + 1) ÷ 2. Twee driehoeksgetallen naast elkaar zijn samen een kwadraat: 6 + 10 = 16.",
      tr: "n. üçgen sayı = n × (n + 1) ÷ 2. Art arda iki üçgen sayının toplamı bir kare sayıdır: 6 + 10 = 16." },
    { eg: true, nl: "<b>Bowlen</b>: de 10 kegels staan in een driehoek: 1 + 2 + 3 + 4 = 10, een driehoeksgetal.<br><b>Schaakbord</b>: 8 × 8 = 64 vakjes, een kwadraatgetal. Een doos met 6 rijen van 6 eieren: 36.",
      tr: "<b>Bowling</b>: 10 kuka üçgen şeklinde dizilir: 1 + 2 + 3 + 4 = 10, bir üçgen sayı.<br><b>Satranç tahtası</b>: 8 × 8 = 64 kare, bir kare sayı. 6 sıra, her sırada 6 yumurta olan bir koli: 36." }
  ],
  driehoek: [
    { fig: fig.triangle("basis", "hoogte"), nl: "Een driehoek is de <b>helft van een rechthoek</b>.<br><b>Oppervlakte = basis × hoogte ÷ 2</b><br>Voorbeeld: basis 6 cm, hoogte 4 cm → 6 × 4 ÷ 2 = 12 cm².",
      tr: "Üçgen, bir <b>dikdörtgenin yarısıdır</b>.<br><b>Alan = taban × yükseklik ÷ 2</b><br>Örnek: taban 6 cm, yükseklik 4 cm → 6 × 4 ÷ 2 = 12 cm²." },
    { eg: true, nl: "<b>Boterham</b>: snijd een vierkante boterham schuin door. Je hebt twee driehoeken die precies even groot zijn: elk de helft van de boterham. Zo werkt de regel ook: eerst de hele rechthoek uitrekenen, dan door 2 delen.",
      tr: "<b>Tost ekmeği</b>: kare bir dilim ekmeği köşeden köşeye kes. Tam aynı büyüklükte iki üçgen olur: her biri ekmeğin yarısı. Kural da böyle çalışır: önce bütün dikdörtgeni hesapla, sonra 2'ye böl." }
  ],
  samengesteld: [
    { fig: fig.lshape("", "", "", ""), nl: "Een L-vorm knip je in <b>twee rechthoeken</b>. Reken van elk de oppervlakte uit en tel ze op.<br>Of: neem de grote rechthoek en haal het stuk dat ontbreekt eraf.",
      tr: "L şeklini <b>iki dikdörtgene</b> böl. Her birinin alanını bul ve topla.<br>Ya da: büyük dikdörtgeni al, eksik parçayı çıkar." },
    { eg: true, nl: "<b>Je eigen huis</b>: bijna geen kamer is een nette rechthoek. Er zit een hoek uit voor de trap, of er is een stuk aangebouwd. Wie een vloer koopt, verdeelt de plattegrond in rechthoeken, rekent elk stuk uit en telt alles op.",
      tr: "<b>Kendi evin</b>: neredeyse hiçbir oda düzgün bir dikdörtgen değildir. Merdiven için bir köşe eksiktir ya da bir bölüm sonradan eklenmiştir. Zemin kaplaması alan kişi krokiyi dikdörtgenlere böler, her parçayı hesaplar ve hepsini toplar." }
  ],
  inhoud: [
    { fig: fig.box("lengte", "breedte", "hoogte"), nl: "<b>Inhoud</b> = hoeveel erin past.<br><b>Doos: lengte × breedte × hoogte</b><br><b>Kubus: ribbe × ribbe × ribbe</b> (ribbe³)<br>1 dm³ = 1 liter.",
      tr: "<b>Hacim</b> = içine ne kadar sığdığı.<br><b>Kutu: uzunluk × genişlik × yükseklik</b><br><b>Küp: kenar × kenar × kenar</b> (kenar³)<br>1 dm³ = 1 litre." },
    { eg: true, nl: "<b>Pak melk</b>: in een pak zit 1 liter. Een kubus van 10 cm bij 10 cm bij 10 cm is ook precies 1 liter: 10 × 10 × 10 = 1000 cm³.<br><b>Verhuisdoos</b>: twee keer zo lang, zo breed én zo hoog? Dan past er niet 2 keer, maar 2 × 2 × 2 = 8 keer zo veel in.",
      tr: "<b>Süt kutusu</b>: bir kutuda 1 litre süt var. 10 cm × 10 cm × 10 cm bir küp de tam 1 litredir: 10 × 10 × 10 = 1000 cm³.<br><b>Taşınma kolisi</b>: boyu, eni ve yüksekliği iki katı olan bir koliye 2 kat değil, 2 × 2 × 2 = 8 kat fazla eşya sığar." }
  ],
  priem: [
    { nl: "Een <b>deler</b> van een getal past er precies in. De delers van 12: 1, 2, 3, 4, 6, 12.<br>Een <b>priemgetal</b> heeft precies twee delers: 1 en zichzelf. Voorbeelden: 2, 3, 5, 7, 11, 13.<br>1 is geen priemgetal.",
      tr: "Bir sayının <b>böleni</b> o sayıyı tam böler. 12'nin bölenleri: 1, 2, 3, 4, 6, 12.<br><b>Asal sayının</b> tam iki böleni vardır: 1 ve kendisi. Örnekler: 2, 3, 5, 7, 11, 13.<br>1 asal sayı değildir." },
    { eg: true, nl: "<b>Koekjes verdelen</b>: 12 koekjes kun je eerlijk verdelen over 2, 3, 4 of 6 kinderen. Met 13 koekjes lukt dat nooit: 13 is een priemgetal.<br><b>Cicaden</b>: in Amerika leven insecten die maar eens in de 13 of 17 jaar uit de grond komen. Allebei priemgetallen.",
      tr: "<b>Kurabiye paylaşmak</b>: 12 kurabiye 2, 3, 4 ya da 6 çocuğa eşit paylaştırılabilir. 13 kurabiyeyle bu hiç olmaz: 13 bir asal sayıdır.<br><b>Ağustos böcekleri</b>: Amerika'da yalnızca 13 ya da 17 yılda bir topraktan çıkan böcekler yaşar. İkisi de asal sayı." }
  ],
  hoeken: [
    { nl: "Een hoek meet je in <b>graden</b> (°).<br><b>Scherpe hoek</b>: kleiner dan 90°. <b>Rechte hoek</b>: precies 90°. <b>Stompe hoek</b>: groter dan 90°.<br>De hoeken van een driehoek zijn samen 180°, van een vierhoek 360°.",
      tr: "Açı <b>derece</b> (°) ile ölçülür.<br><b>Dar açı</b>: 90°'den küçük. <b>Dik açı</b>: tam 90°. <b>Geniş açı</b>: 90°'den büyük.<br>Üçgenin açıları toplamı 180°, dörtgenin 360°." },
    { eg: true, nl: "<b>Kijk om je heen</b>: om 3 uur maken de wijzers van de klok een rechte hoek. Een pizzapunt is een scherpe hoek. Een laptop die ver open staat maakt een stompe hoek. Een skater die een '360' doet, draait één keer helemaal rond.",
      tr: "<b>Etrafına bak</b>: saat 3'te akrep ile yelkovan dik açı yapar. Bir pizza dilimi dar açıdır. Çok açılmış bir dizüstü bilgisayar geniş açı yapar. '360' yapan bir kaykaycı tam bir tur döner." }
  ],
  schaal: [
    { nl: "<b>Schaal 1 : 100</b> betekent: 1 cm op de tekening is 100 cm (1 m) in het echt.<br>Van tekening naar echt: <b>keer</b>. Van echt naar tekening: <b>delen</b>.",
      tr: "<b>Ölçek 1 : 100</b> şu demek: çizimdeki 1 cm gerçekte 100 cm (1 m).<br>Çizimden gerçeğe: <b>çarp</b>. Gerçekten çizime: <b>böl</b>." },
    { eg: true, nl: "<b>Madurodam</b> in Den Haag is gebouwd op schaal 1 : 25. Een toren die in het echt 100 m hoog is, is daar 4 m. Een mens van 1,75 m zou er 7 cm zijn.<br><b>Speelgoedauto</b>: op de doos staat vaak 1 : 64. De echte auto is 64 keer zo lang.",
      tr: "Lahey'deki <b>Madurodam</b> 1 : 25 ölçeğiyle yapılmıştır. Gerçekte 100 m olan bir kule orada 4 m'dir. 1,75 m boyundaki bir insan orada 7 cm olurdu.<br><b>Oyuncak araba</b>: kutusunda çoğu zaman 1 : 64 yazar. Gerçek araba 64 kat uzundur." }
  ],
  negatief: [
    { nl: "Getallen <b>onder nul</b> hebben een min: −1, −2, −3, … Denk aan een thermometer.<br>Kouder = omlaag, warmer = omhoog.<br>Voorbeeld: 3 − 5 = −2. En −2 + 6 = 4.",
      tr: "<b>Sıfırın altındaki</b> sayıların önünde eksi var: −1, −2, −3, … Termometreyi düşün.<br>Soğumak = aşağı, ısınmak = yukarı.<br>Örnek: 3 − 5 = −2. Ve −2 + 6 = 4." },
    { eg: true, nl: "<b>Parkeergarage</b>: de verdiepingen onder de grond heten −1 en −2.<br><b>Nederland</b>: een groot deel van het land ligt lager dan de zee. Het laagste punt ligt bijna 7 meter onder zeeniveau: ongeveer −7 m.<br><b>Vriezer</b>: daar is het ongeveer −18 graden.",
      tr: "<b>Otopark</b>: yerin altındaki katlara −1 ve −2 denir.<br><b>Hollanda</b>: ülkenin büyük bir bölümü deniz seviyesinden alçaktadır. En alçak nokta deniz seviyesinin neredeyse 7 metre altındadır: yaklaşık −7 m.<br><b>Dondurucu</b>: içi yaklaşık −18 derecedir." }
  ]
};

// Word list per topic: Dutch = Turkish (shown under the theory)
export const WORDS = {
  meetkunde: [["oppervlakte", "alan"], ["omtrek", "çevre"], ["zijde", "kenar"], ["lengte", "uzunluk"], ["breedte", "genişlik"], ["straal", "yarıçap"], ["diameter (middellijn)", "çap"], ["vierkant", "kare"], ["rechthoek", "dikdörtgen"], ["cirkel", "daire"]],
  som: [["optellen", "toplamak"], ["de som", "toplam"], ["paar", "çift"], ["even getal", "çift sayı"], ["oneven getal", "tek sayı"]],
  machten: [["macht", "üs / kuvvet"], ["kwadraat", "kare"], ["wortel", "karekök"], ["vermenigvuldigen", "çarpmak"]],
  fibonacci: [["rij", "dizi"], ["regel", "kural"], ["optellen", "toplamak"], ["bloemblaadje", "taç yaprak"], ["dennenappel", "çam kozalağı"], ["zonnebloem", "ayçiçeği"], ["spiraal", "spiral"]],
  natuurpatronen: [["symmetrie", "simetri"], ["symmetrieas", "simetri ekseni"], ["spiegelbeeld", "ayna görüntüsü"], ["zeshoek", "altıgen"], ["honingraat", "bal peteği"], ["sneeuwvlok", "kar tanesi"], ["varen", "eğrelti otu"]],
  getallen: [["kwadraatgetal", "kare sayı"], ["driehoeksgetal", "üçgen sayı"], ["rij", "sıra / dizi"], ["patroon", "örüntü"]],
  driehoek: [["driehoek", "üçgen"], ["basis", "taban"], ["hoogte", "yükseklik"], ["de helft", "yarısı"]],
  samengesteld: [["samengestelde figuur", "bileşik şekil"], ["knippen", "kesmek"], ["optellen", "toplamak"], ["aftrekken", "çıkarmak"]],
  inhoud: [["inhoud", "hacim"], ["kubus", "küp"], ["ribbe", "kenar (ayrıt)"], ["doos", "kutu"], ["hoogte", "yükseklik"]],
  priem: [["priemgetal", "asal sayı"], ["deler", "bölen"], ["delen", "bölmek"]],
  hoeken: [["hoek", "açı"], ["graden", "derece"], ["scherpe hoek", "dar açı"], ["rechte hoek", "dik açı"], ["stompe hoek", "geniş açı"]],
  schaal: [["schaal", "ölçek"], ["plattegrond", "kroki"], ["kaart", "harita"], ["in het echt", "gerçekte"]],
  negatief: [["negatief getal", "negatif sayı"], ["onder nul", "sıfırın altı"], ["graden", "derece"], ["verschil", "fark"]]
};
Object.assign(THEORY, S_THEORY);
Object.assign(WORDS, S_WORDS);
