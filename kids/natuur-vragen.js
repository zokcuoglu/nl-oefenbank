// Natuur & techniek: light, mass and density, floating and sinking, atoms.
// Same shape as kids/rekenen-vragen.js (TOPICS, THEORY, WORDS, makeQuestion, isCorrect), so kids/rekenen.html
// can show either subject (?vak=natuur).
//
// Why most questions here are fixed: these topics are about understanding ("why does a ship float?"), not about
// sums, so each question is written by hand with one right and a few wrong answers. Only the parts with a
// calculation (density, volume, counting atoms) draw fresh numbers.
import { ri, pick, shuffle, Q, svg, T, maker, isCorrect } from "./rekenen-vragen.js?v=2";
export { isCorrect };

// All topics start hidden; the admin opens them on the admin page (tab İçerik).
export const TOPICS = [
  { id: "licht", nl: "Licht", tr: "Işık (optik)", sub_nl: "schaduw, spiegel, regenboog", sub_tr: "gölge, ayna, gökkuşağı", open: false },
  { id: "massa", nl: "Massa, gewicht en dichtheid", tr: "Kütle, ağırlık ve özkütle", sub_nl: "hoe zwaar, en hoe zwaar voor zijn grootte", sub_tr: "ne kadar ağır, boyuna göre ne kadar ağır", open: false },
  { id: "drijven", nl: "Drijven en zinken", tr: "Yüzme ve batma", sub_nl: "de opwaartse kracht van water", sub_tr: "suyun kaldırma kuvveti", open: false },
  { id: "atoom", nl: "Atomen en moleculen", tr: "Atomlar ve moleküller", sub_nl: "waar alles van gemaakt is", sub_tr: "her şey neyden yapılmış", open: false }
];

// A hand-written multiple-choice question: the first answer is the right one; the page shuffles nothing itself,
// so the options are shuffled here each time the question is drawn.
// right / each wrong = [Dutch, Turkish]
const MC = (nl, tr, right, wrong, ex_nl, ex_tr, extra = {}) => () => {
  const opts = shuffle([right, ...wrong].map(([n, t], i) => ({ v: "o" + i, nl: n, tr: t })));
  return Q(nl, tr, "o0", "", ex_nl, ex_tr, { opts, ...extra });
};
const FLOAT = [{ v: "drijft", nl: "het drijft", tr: "yüzer" }, { v: "zinkt", nl: "het zinkt", tr: "batar" }];

// ---------------------------------------------------------------- figures
const fig = {
  // a ray hits a mirror and leaves at the same angle
  mirror: (a) => svg(`<line x1="20" y1="110" x2="200" y2="110" style="stroke-width:4"/><line class="dash" x1="110" y1="110" x2="110" y2="20"/>
    <line x1="40" y1="30" x2="110" y2="110"/><line x1="110" y1="110" x2="180" y2="30"/>${T(84, 52, a)}${T(136, 52, "?")}${T(110, 126, "spiegel")}`),
  // measuring cup: the water level rises when a stone goes in
  cup: (a, b) => svg(`<polyline class="room" points="40,15 40,110 100,110 100,15"/><rect class="shape" x="40" y="60" width="60" height="50"/>${T(70, 126, a + " ml")}
    <polyline class="room" points="130,15 130,110 190,110 190,15"/><rect class="shape" x="130" y="40" width="60" height="70"/><circle cx="160" cy="97" r="10"/>${T(160, 126, b + " ml")}`),
  atom: () => svg(`<circle class="room" cx="110" cy="65" r="52"/><circle class="room" cx="110" cy="65" r="30"/><circle class="shape" cx="110" cy="65" r="17"/>
    <circle cx="140" cy="65" r="4"/><circle cx="110" cy="13" r="4"/><circle cx="73" cy="102" r="4"/>${T(110, 69, "kern")}${T(176, 30, "elektron")}`)
};

const GEN = {};

// ----- Licht
GEN.licht = [
  [
    MC("Hoe beweegt licht door de lucht?", "Işık havada nasıl ilerler?", ["in een rechte lijn", "düz bir çizgide"], [["in een kromme lijn", "eğri bir çizgide"], ["in een zigzag", "zikzak çizerek"], ["in rondjes", "daireler çizerek"]],
      "Licht gaat rechtdoor. Daarom kun je niet om een hoek kijken.", "Işık dümdüz gider. Bu yüzden köşenin arkasını göremezsin."),
    MC("Wat geeft <b>zelf</b> licht?", "Hangisi <b>kendisi</b> ışık verir?", ["de zon", "Güneş"], [["de maan", "Ay"], ["een spiegel", "ayna"], ["een raam", "pencere"]],
      "De zon is een lichtbron. De maan geeft zelf geen licht: ze kaatst het licht van de zon terug.", "Güneş bir ışık kaynağıdır. Ay kendisi ışık vermez: Güneş'in ışığını yansıtır."),
    MC("Wanneer ontstaat er een schaduw?", "Gölge ne zaman oluşur?", ["als iets het licht tegenhoudt", "bir şey ışığı engellediğinde"], [["als het licht heel fel is", "ışık çok parlak olduğunda"], ["als het licht door glas gaat", "ışık camdan geçtiğinde"], ["als het regent", "yağmur yağdığında"]],
      "Licht gaat rechtdoor en kan niet door jou heen. Achter jou blijft het donker: dat is je schaduw.", "Işık düz gider ve senin içinden geçemez. Arkanda karanlık kalır: bu senin gölgendir."),
    MC("Wat doet een spiegel met licht?", "Ayna ışığa ne yapar?", ["hij kaatst het terug", "geri yansıtır"], [["hij slokt het op", "yutar"], ["hij laat het door", "içinden geçirir"], ["hij maakt het warmer", "ısıtır"]],
      "Een spiegel weerkaatst bijna al het licht. Daardoor zie je jezelf.", "Ayna ışığın neredeyse hepsini yansıtır. Bu yüzden kendini görürsün."),
    MC("Door welk materiaal gaat licht goed heen?", "Işık hangi maddenin içinden rahatça geçer?", ["glas", "cam"], [["hout", "tahta"], ["karton", "karton"], ["ijzer", "demir"]],
      "Glas is doorzichtig. Hout, karton en ijzer houden het licht tegen.", "Cam saydamdır. Tahta, karton ve demir ışığı engeller.")
  ],
  [
    MC("Midden op de dag staat de zon hoog aan de hemel. Hoe is je schaduw dan?", "Öğle vakti Güneş gökyüzünde yüksektedir. O zaman gölgen nasıl olur?", ["kort", "kısa"], [["lang", "uzun"], ["er is geen licht", "ışık yoktur"], ["net zo lang als 's avonds", "akşamki kadar uzun"]],
      "Hoe hoger de zon, hoe korter de schaduw. 's Ochtends en 's avonds staat de zon laag en is je schaduw lang.", "Güneş ne kadar yüksekse gölge o kadar kısadır. Sabah ve akşam Güneş alçaktadır, gölgen uzun olur."),
    MC("Een rietje in een glas water lijkt geknikt. Hoe komt dat?", "Su dolu bardaktaki pipet kırılmış gibi görünür. Neden?", ["het licht verandert van richting als het van water naar lucht gaat", "ışık sudan havaya geçerken yön değiştirir"], [["het rietje is echt krom geworden", "pipet gerçekten eğilmiştir"], ["het water is te koud", "su çok soğuktur"], ["het glas is een spiegel", "bardak bir aynadır"]],
      "Dat heet breking: bij de overgang tussen water en lucht buigt het licht een beetje af.", "Buna kırılma denir: ışık su ile hava arasında geçerken biraz yön değiştirir."),
    MC("Hoe ontstaat een regenboog?", "Gökkuşağı nasıl oluşur?", ["regendruppels splitsen het zonlicht in kleuren", "yağmur damlaları güneş ışığını renklere ayırır"], [["de wolken zijn gekleurd", "bulutlar renklidir"], ["de zon verandert van kleur", "Güneş renk değiştirir"], ["de regen is gekleurd", "yağmur renklidir"]],
      "Wit zonlicht bestaat uit alle kleuren samen. In een druppel breekt het licht en gaan de kleuren uit elkaar.", "Beyaz güneş ışığı bütün renklerin birleşimidir. Damlanın içinde ışık kırılır ve renkler birbirinden ayrılır."),
    MC("Je staat voor de spiegel en steekt je <b>rechterhand</b> op. Welke hand lijkt je spiegelbeeld op te steken?", "Aynanın karşısında <b>sağ elini</b> kaldırıyorsun. Aynadaki görüntün hangi elini kaldırıyor gibi görünür?", ["de linkerhand", "sol elini"], [["de rechterhand", "sağ elini"], ["allebei de handen", "iki elini de"], ["geen hand", "hiçbirini"]],
      "Een spiegel wisselt links en rechts om.", "Ayna sağ ile solu yer değiştirir."),
    () => Q("Hoeveel kleuren noemen we meestal in de regenboog?", "Gökkuşağında genellikle kaç renk sayarız?", 7, "",
      "Rood, oranje, geel, groen, blauw, indigo en violet: 7 kleuren.", "Kırmızı, turuncu, sarı, yeşil, mavi, lacivert ve mor: 7 renk.")
  ],
  [
    () => { const a = ri(2, 9); return Q(`Licht legt in 1 seconde ongeveer 300.000 km af. Hoeveel km legt het af in ${a} seconden?`, `Işık 1 saniyede yaklaşık 300.000 km yol alır. ${a} saniyede kaç km yol alır?`, 300000 * a, "km",
      `${a} × 300.000 = ${(300 * a).toLocaleString("nl-NL")}.000 km.`, `${a} × 300.000 = ${(300 * a).toLocaleString("nl-NL")}.000 km.`); },
    () => { const a = ri(1, 9); return Q(`Je staat ${a} m voor een spiegel. Je spiegelbeeld lijkt even ver <b>achter</b> de spiegel te staan. Hoeveel meter zit er tussen jou en je spiegelbeeld?`, `Aynanın ${a} m önünde duruyorsun. Görüntün aynanın aynı uzaklıkta <b>arkasında</b> gibi görünür. Seninle görüntün arasında kaç metre var?`, 2 * a, "m",
      `${a} m tot de spiegel en ${a} m erachter: ${2 * a} m.`, `Aynaya kadar ${a} m, arkasında ${a} m: ${2 * a} m.`); },
    () => { const a = ri(4, 16) * 5; return Q(`Een lichtstraal valt op een spiegel. De hoek aan de ene kant is ${a}°. Hoe groot is de hoek waarmee de straal terugkaatst?`, `Bir ışık ışını aynaya çarpıyor. Bir taraftaki açı ${a}°. Işın kaç derecelik açıyla yansır?`, a, "graden",
      `Licht kaatst terug onder dezelfde hoek: ${a}°.`, `Işık aynı açıyla yansır: ${a}°.`, { fig: fig.mirror(a + "°") }); },
    MC("Bij onweer zie je eerst de bliksem en hoor je pas daarna de donder. Hoe komt dat?", "Fırtınada önce şimşeği görürsün, gök gürültüsünü sonra duyarsın. Neden?", ["licht is veel sneller dan geluid", "ışık sesten çok daha hızlıdır"], [["geluid is sneller dan licht", "ses ışıktan hızlıdır"], ["de donder begint later", "gök gürültüsü daha geç başlar"], ["je ogen zijn sneller dan je oren", "gözlerin kulaklarından hızlıdır"]],
      "Bliksem en donder ontstaan tegelijk. Het licht is er bijna meteen, het geluid doet er seconden over.", "Şimşek ve gök gürültüsü aynı anda oluşur. Işık neredeyse hemen ulaşır, ses ise saniyeler sonra gelir."),
    () => { const a = ri(2, 6); return Q(`Het geluid van de donder gaat ongeveer 340 m per seconde. Je hoort de donder ${a} seconden na de bliksem. Hoeveel meter is het onweer ongeveer bij je vandaan?`, `Gök gürültüsünün sesi saniyede yaklaşık 340 m yol alır. Gök gürültüsünü şimşekten ${a} saniye sonra duyuyorsun. Fırtına yaklaşık kaç metre uzakta?`, 340 * a, "m",
      `${a} × 340 = ${340 * a} m.`, `${a} × 340 = ${340 * a} m.`); }
  ]
];

// ----- Massa, gewicht en dichtheid
GEN.massa = [
  [
    MC("In welke eenheid meet je massa?", "Kütle hangi birimle ölçülür?", ["kilogram", "kilogram"], [["meter", "metre"], ["liter", "litre"], ["graden", "derece"]],
      "Massa meet je in gram en kilogram.", "Kütle gram ve kilogramla ölçülür."),
    () => { const a = ri(2, 9); return Q(`Hoeveel gram is ${a} kg?`, `${a} kg kaç gramdır?`, 1000 * a, "gram", `1 kg = 1000 gram, dus ${a} kg = ${1000 * a} gram.`, `1 kg = 1000 gram, yani ${a} kg = ${1000 * a} gram.`); },
    MC("Wat is zwaarder: 1 kg veren of 1 kg ijzer?", "Hangisi daha ağır: 1 kg tüy mü, 1 kg demir mi?", ["ze zijn even zwaar", "ikisi aynı"], [["1 kg ijzer", "1 kg demir"], ["1 kg veren", "1 kg tüy"]],
      "Allebei 1 kg. De veren nemen wel veel meer ruimte in.", "İkisi de 1 kg. Ama tüyler çok daha fazla yer kaplar."),
    MC("Welke kracht trekt alles naar de aarde toe?", "Her şeyi Dünya'ya doğru çeken kuvvet hangisidir?", ["de zwaartekracht", "yer çekimi"], [["de wind", "rüzgâr"], ["de opwaartse kracht", "kaldırma kuvveti"], ["magnetisme", "manyetizma"]],
      "De zwaartekracht trekt aan alles. Hoe hard ze aan jou trekt, noemen we je gewicht.", "Yer çekimi her şeyi çeker. Seni ne kadar kuvvetle çektiğine ağırlığın denir."),
    MC("Een astronaut gaat naar de maan. Wat gebeurt er met zijn <b>massa</b>?", "Bir astronot Ay'a gidiyor. <b>Kütlesine</b> ne olur?", ["die blijft hetzelfde", "aynı kalır"], [["die wordt kleiner", "azalır"], ["die wordt groter", "artar"], ["die wordt nul", "sıfır olur"]],
      "Massa is hoeveel stof er is; dat verandert niet. Zijn gewicht wordt wel kleiner, want de maan trekt minder hard.", "Kütle, madde miktarıdır; değişmez. Ağırlığı ise azalır, çünkü Ay daha az çeker.")
  ],
  [
    () => { const d = ri(2, 9), v = ri(2, 10); return Q(`Een blokje heeft een massa van ${d * v} gram en een volume van ${v} cm³. Wat is de dichtheid?`, `Bir bloğun kütlesi ${d * v} gram, hacmi ${v} cm³. Özkütlesi kaçtır?`, d, "g/cm³",
      `Dichtheid = massa ÷ volume = ${d * v} ÷ ${v} = ${d} g/cm³.`, `Özkütle = kütle ÷ hacim = ${d * v} ÷ ${v} = ${d} g/cm³.`); },
    () => { const d = ri(2, 9), v = ri(2, 10); return Q(`Een stof heeft een dichtheid van ${d} g/cm³. Hoeveel gram is een blokje van ${v} cm³?`, `Bir maddenin özkütlesi ${d} g/cm³. Hacmi ${v} cm³ olan bir blok kaç gramdır?`, d * v, "gram",
      `Massa = dichtheid × volume = ${d} × ${v} = ${d * v} gram.`, `Kütle = özkütle × hacim = ${d} × ${v} = ${d * v} gram.`); },
    MC("Twee blokken zijn precies even groot. Het ene is van ijzer, het andere van hout. Welk blok heeft de meeste massa?", "İki blok tam aynı büyüklükte. Biri demirden, diğeri tahtadan. Hangisinin kütlesi daha fazla?", ["het blok van ijzer", "demir blok"], [["het blok van hout", "tahta blok"], ["ze zijn even zwaar", "ikisi aynı"]],
      "IJzer heeft een grotere dichtheid: in dezelfde ruimte zit meer massa.", "Demirin özkütlesi daha büyüktür: aynı hacimde daha çok kütle vardır."),
    () => { const a = ri(2, 12); return Q(`Op de maan weegt alles ongeveer 6 keer zo weinig als op aarde. Een steen weegt op aarde ${6 * a} kg op de weegschaal. Wat geeft dezelfde weegschaal op de maan aan?`, `Ay'da her şey Dünya'dakinin yaklaşık 6'da biri kadar ağırlıktadır. Bir taş Dünya'da tartıda ${6 * a} kg geliyor. Aynı tartı Ay'da kaç kg gösterir?`, a, "kg",
      `${6 * a} ÷ 6 = ${a}. De massa van de steen is niet veranderd, de maan trekt alleen minder hard.`, `${6 * a} ÷ 6 = ${a}. Taşın kütlesi değişmedi, sadece Ay daha az çekiyor.`); }
  ],
  [
    () => { const l = ri(2, 5), b = ri(2, 4), h = ri(1, 3), d = ri(2, 8); const v = l * b * h; return Q(`Een blok is ${l} cm lang, ${b} cm breed en ${h} cm hoog. Het heeft een massa van ${v * d} gram. Wat is de dichtheid?`, `Bir blok ${l} cm uzunluğunda, ${b} cm genişliğinde ve ${h} cm yüksekliğinde. Kütlesi ${v * d} gram. Özkütlesi kaçtır?`, d, "g/cm³",
      `Volume = ${l} × ${b} × ${h} = ${v} cm³. Dichtheid = ${v * d} ÷ ${v} = ${d} g/cm³.`, `Hacim = ${l} × ${b} × ${h} = ${v} cm³. Özkütle = ${v * d} ÷ ${v} = ${d} g/cm³.`); },
    () => { const d = ri(2, 9), v = ri(3, 12); return Q(`Een steen heeft een massa van ${d * v} gram. De dichtheid is ${d} g/cm³. Wat is het volume van de steen?`, `Bir taşın kütlesi ${d * v} gram. Özkütlesi ${d} g/cm³. Taşın hacmi kaç cm³?`, v, "cm³",
      `Volume = massa ÷ dichtheid = ${d * v} ÷ ${d} = ${v} cm³.`, `Hacim = kütle ÷ özkütle = ${d * v} ÷ ${d} = ${v} cm³.`); },
    () => { const a = ri(2, 20); return Q(`1 liter water heeft een massa van 1 kg. Een emmer is gevuld met ${a} liter water. De lege emmer is 1 kg. Hoeveel kg is de volle emmer?`, `1 litre suyun kütlesi 1 kg'dır. Bir kovada ${a} litre su var. Boş kova 1 kg. Dolu kova kaç kg'dır?`, a + 1, "kg",
      `${a} liter water = ${a} kg. Met de emmer erbij: ${a + 1} kg.`, `${a} litre su = ${a} kg. Kovayla birlikte: ${a + 1} kg.`); },
    () => { const d1 = ri(2, 4), d2 = d1 + ri(1, 4), v = ri(2, 6); return Q(`Twee blokjes zijn elk ${v} cm³. Blokje A heeft een dichtheid van ${d1} g/cm³, blokje B van ${d2} g/cm³. Hoeveel gram is blokje B zwaarder dan blokje A?`, `İki bloğun her biri ${v} cm³. A bloğunun özkütlesi ${d1} g/cm³, B bloğununki ${d2} g/cm³. B bloğu A'dan kaç gram daha ağırdır?`, (d2 - d1) * v, "gram",
      `A: ${d1} × ${v} = ${d1 * v} g. B: ${d2} × ${v} = ${d2 * v} g. Verschil: ${(d2 - d1) * v} g.`, `A: ${d1} × ${v} = ${d1 * v} g. B: ${d2} × ${v} = ${d2 * v} g. Fark: ${(d2 - d1) * v} g.`); }
  ]
];

// ----- Drijven en zinken
const THINGS = [["een blokje hout", "tahta bir blok", "drijft"], ["een kurk", "bir mantar tıpa", "drijft"], ["een ijsblokje", "bir buz küpü", "drijft"], ["een lege plastic fles met de dop erop", "kapağı kapalı boş bir plastik şişe", "drijft"],
  ["een steen", "bir taş", "zinkt"], ["een ijzeren spijker", "demir bir çivi", "zinkt"], ["een muntje", "bir madeni para", "zinkt"], ["een glazen knikker", "cam bir bilye", "zinkt"]];
GEN.drijven = [
  [
    () => { const [nl, tr, v] = pick(THINGS); return Q(`Je legt ${nl} in een bak water. Wat gebeurt er?`, `Bir su kabına ${tr} koyuyorsun. Ne olur?`, v, "",
      v === "drijft" ? "Het is lichter dan evenveel water, dus het blijft drijven." : "Het is zwaarder dan evenveel water, dus het zinkt.",
      v === "drijft" ? "Aynı hacimdeki sudan daha hafiftir, bu yüzden yüzer." : "Aynı hacimdeki sudan daha ağırdır, bu yüzden batar.", { opts: FLOAT }); },
    MC("Hoe heet de kracht waarmee water een voorwerp omhoog duwt?", "Suyun bir cismi yukarı doğru ittiği kuvvete ne denir?", ["de opwaartse kracht", "kaldırma kuvveti"], [["de zwaartekracht", "yer çekimi"], ["de wrijving", "sürtünme"], ["de windkracht", "rüzgâr kuvveti"]],
      "Water duwt omhoog tegen alles wat erin ligt. Daardoor voel je je lichter in het zwembad.", "Su, içindeki her şeyi yukarı iter. Bu yüzden havuzda kendini daha hafif hissedersin."),
    MC("Een voorwerp heeft een <b>kleinere</b> dichtheid dan water. Wat doet het in water?", "Bir cismin özkütlesi suyunkinden <b>küçük</b>. Suda ne yapar?", ["het drijft", "yüzer"], [["het zinkt", "batar"], ["het lost op", "erir (çözünür)"], ["het wordt warm", "ısınır"]],
      "Kleinere dichtheid dan water: drijven. Grotere dichtheid: zinken.", "Özkütlesi sudan küçükse yüzer, büyükse batar.")
  ],
  [
    () => { const [txt, v] = pick([["0,5", "drijft"], ["0,8", "drijft"], ["0,9", "drijft"], ["2", "zinkt"], ["3", "zinkt"], ["8", "zinkt"]]); return Q(`Water heeft een dichtheid van 1 g/cm³. Een blokje heeft een dichtheid van ${txt} g/cm³. Wat doet het blokje in water?`, `Suyun özkütlesi 1 g/cm³. Bir bloğun özkütlesi ${txt} g/cm³. Blok suda ne yapar?`, v, "",
      `${txt} is ${v === "drijft" ? "kleiner" : "groter"} dan 1, dus het blokje ${v}.`, `${txt}, 1'den ${v === "drijft" ? "küçük" : "büyük"}, yani blok ${v === "drijft" ? "yüzer" : "batar"}.`, { opts: FLOAT }); },
    MC("Een schip is van ijzer en toch drijft het. Hoe kan dat?", "Gemi demirden yapılmıştır ama yine de yüzer. Nasıl olur?", ["het schip is hol: ijzer en lucht samen zijn lichter dan evenveel water", "geminin içi boş: demir ve hava birlikte, aynı hacimdeki sudan hafiftir"], [["ijzer drijft altijd", "demir her zaman yüzer"], ["de motor houdt het schip omhoog", "motor gemiyi yukarıda tutar"], ["zeewater is heel dik", "deniz suyu çok koyudur"]],
      "Een massief blok ijzer zinkt. Een schip is een holle vorm met veel lucht erin; alles samen heeft een kleinere dichtheid dan water.", "İçi dolu demir blok batar. Gemi ise içinde çok hava olan boş bir şekildir; hepsinin birlikte özkütlesi sudan küçüktür."),
    MC("Een bolletje klei zinkt. Je maakt van dezelfde klei een bakje en legt het op het water. Het drijft. Wat is er veranderd?", "Oyun hamurundan bir top batıyor. Aynı hamurdan bir kayık yapıp suya koyuyorsun. Yüzüyor. Ne değişti?", ["het volume is groter geworden, de massa is gelijk gebleven", "hacim büyüdü, kütle aynı kaldı"], [["de massa is kleiner geworden", "kütle azaldı"], ["de klei is een andere stof geworden", "hamur başka bir maddeye dönüştü"], ["het water is zwaarder geworden", "su ağırlaştı"]],
      "Het bakje neemt met de lucht erin veel meer ruimte in. Zelfde massa ÷ groter volume = kleinere dichtheid. Zo drijft ook een schip van ijzer.", "Kayık, içindeki havayla birlikte çok daha fazla yer kaplar. Aynı kütle ÷ daha büyük hacim = daha küçük özkütle. Demirden gemi de böyle yüzer."),
    MC("Een schip krijgt een groot gat en loopt vol water. Waarom zinkt het dan?", "Bir gemide büyük bir delik açılıyor ve gemi suyla doluyor. Neden batar?", ["de lucht in het schip wordt vervangen door water, dus het schip wordt zwaarder", "geminin içindeki havanın yerini su alır, gemi ağırlaşır"], [["het ijzer wordt zwaarder als het nat is", "demir ıslanınca ağırlaşır"], ["het water in de zee wordt lichter", "denizdeki su hafifler"], ["de motor stopt", "motor durur"]],
      "Met lucht erin is het schip als geheel lichter dan evenveel water. Zit er water in plaats van lucht, dan blijft alleen het zware ijzer over.", "İçinde hava varken gemi, bütün olarak aynı hacimdeki sudan hafiftir. Havanın yerine su dolunca geriye sadece ağır demir kalır."),
    MC("In de zee blijf je makkelijker drijven dan in het zwembad. Waarom?", "Denizde havuza göre daha kolay yüzersin. Neden?", ["zout water heeft een grotere dichtheid", "tuzlu suyun özkütlesi daha büyüktür"], [["de zee is dieper", "deniz daha derindir"], ["de zee is kouder", "deniz daha soğuktur"], ["in zee zijn golven", "denizde dalga vardır"]],
      "Door het zout is zeewater zwaarder dan zoet water. Het duwt je daardoor harder omhoog.", "Tuz yüzünden deniz suyu tatlı sudan ağırdır. Bu yüzden seni daha kuvvetli yukarı iter."),
    () => { const a = ri(3, 8) * 10, s = ri(1, 6) * 5; return Q(`In een maatbeker zit ${a} ml water. Je legt er een steen in en het water stijgt tot ${a + s} ml. Wat is het volume van de steen? (1 ml = 1 cm³)`, `Bir ölçü kabında ${a} ml su var. İçine bir taş koyuyorsun ve su ${a + s} ml'ye yükseliyor. Taşın hacmi kaç cm³? (1 ml = 1 cm³)`, s, "cm³",
      `De steen duwt zijn eigen volume aan water opzij: ${a + s} − ${a} = ${s} cm³.`, `Taş kendi hacmi kadar suyu iter: ${a + s} − ${a} = ${s} cm³.`, { fig: fig.cup(a, a + s) }); }
  ],
  [
    () => { const v = ri(4, 10) * 10, floats = ri(0, 1) === 1, m = floats ? v - ri(1, 3) * 10 : v + ri(1, 5) * 10; return Q(`Een blokje heeft een massa van ${m} gram en een volume van ${v} cm³. Evenveel water (${v} cm³) is ${v} gram. Wat doet het blokje in water?`, `Bir bloğun kütlesi ${m} gram, hacmi ${v} cm³. Aynı hacimdeki su (${v} cm³) ${v} gramdır. Blok suda ne yapar?`, floats ? "drijft" : "zinkt", "",
      `${m} gram is ${floats ? "minder" : "meer"} dan ${v} gram, dus het blokje ${floats ? "drijft" : "zinkt"}.`, `${m} gram, ${v} gramdan ${floats ? "az" : "fazla"}, yani blok ${floats ? "yüzer" : "batar"}.`, { opts: FLOAT }); },
    () => { const s = ri(2, 6) * 5, d = ri(2, 5), a = ri(3, 8) * 10; return Q(`Een steen heeft een massa van ${s * d} gram. In een maatbeker stijgt het water van ${a} ml naar ${a + s} ml als je de steen erin legt. Wat is de dichtheid van de steen?`, `Bir taşın kütlesi ${s * d} gram. Taşı ölçü kabına koyunca su ${a} ml'den ${a + s} ml'ye yükseliyor. Taşın özkütlesi kaçtır?`, d, "g/cm³",
      `Volume = ${a + s} − ${a} = ${s} cm³. Dichtheid = ${s * d} ÷ ${s} = ${d} g/cm³.`, `Hacim = ${a + s} − ${a} = ${s} cm³. Özkütle = ${s * d} ÷ ${s} = ${d} g/cm³.`, { fig: fig.cup(a, a + s) }); },
    () => { const a = ri(2, 9); return Q(`Van een ijsberg zitten ongeveer 9 van de 10 delen onder water. Een ijsberg is van onder tot boven ${10 * a} m hoog. Hoeveel meter zit er ongeveer onder water?`, `Bir buzdağının yaklaşık 10 parçasından 9'u suyun altındadır. Bir buzdağı alttan üste ${10 * a} m yüksekliğinde. Yaklaşık kaç metresi suyun altında?`, 9 * a, "m",
      `Eén deel is ${10 * a} ÷ 10 = ${a} m. Negen delen: ${9 * a} m.`, `Bir parça ${10 * a} ÷ 10 = ${a} m. Dokuz parça: ${9 * a} m.`); },
    () => { const V = ri(4, 9) * 100, floats = ri(0, 1) === 1, m = floats ? V - ri(1, 3) * 100 : V + ri(1, 4) * 100;
      return Q(`Een dichte stalen bak met lucht erin heeft een massa van ${m} kg. De hele bak neemt ${V} liter ruimte in. ${V} liter water is ${V} kg. Wat doet de bak in water?`, `İçi hava dolu, kapalı çelik bir kabın kütlesi ${m} kg. Kabın tamamı ${V} litre yer kaplıyor. ${V} litre su ${V} kg eder. Kap suda ne yapar?`, floats ? "drijft" : "zinkt", "",
        `De bak (${m} kg) is ${floats ? "lichter" : "zwaarder"} dan evenveel water (${V} kg), dus hij ${floats ? "drijft" : "zinkt"}. Het maakt niet uit dat hij van staal is: het hele volume telt.`, `Kap (${m} kg), aynı hacimdeki sudan (${V} kg) ${floats ? "hafif" : "ağır"}, yani ${floats ? "yüzer" : "batar"}. Çelikten olması önemli değil: bütün hacim sayılır.`, { opts: FLOAT }); },
    () => { const b = ri(3, 9) * 10, a = ri(1, 2) * 10 + ri(0, 1) * 5; return Q(`Een bootje van ${a} kg blijft drijven zolang boot en lading samen niet zwaarder zijn dan ${b} kg. Hoeveel kg lading mag er hoogstens in?`, `${a} kg'lık bir tekne, tekne ve yük birlikte ${b} kg'ı geçmediği sürece yüzüyor. Tekneye en fazla kaç kg yük konabilir?`, b - a, "kg",
      `${b} − ${a} = ${b - a} kg.`, `${b} − ${a} = ${b - a} kg.`); }
  ]
];

// ----- Atomen en moleculen
const PARTS = [["Welk deeltje heeft een <b>positieve</b> lading?", "Hangi parçacığın yükü <b>pozitiftir</b>?", 0, "Protonen zijn positief, elektronen negatief en neutronen hebben geen lading.", "Protonlar pozitif, elektronlar negatif, nötronlar ise yüksüzdür."],
  ["Welk deeltje heeft een <b>negatieve</b> lading?", "Hangi parçacığın yükü <b>negatiftir</b>?", 1, "Elektronen zijn negatief. Ze bewegen rond de kern.", "Elektronlar negatiftir. Çekirdeğin etrafında dolanırlar."],
  ["Welk deeltje heeft <b>geen</b> lading?", "Hangi parçacığın yükü <b>yoktur</b>?", 2, "Een neutron is neutraal: het heeft geen lading.", "Nötron nötrdür: yükü yoktur."]];
const PART_OPTS = [{ v: "p", nl: "het proton", tr: "proton" }, { v: "e", nl: "het elektron", tr: "elektron" }, { v: "n", nl: "het neutron", tr: "nötron" }];
// name, Turkish, protons
const ELEMENTS = [["waterstof", "hidrojen", 1], ["helium", "helyum", 2], ["koolstof", "karbon", 6], ["stikstof", "azot", 7], ["zuurstof", "oksijen", 8]];
// formula, Dutch name, Turkish name in the genitive ("suyun formülü"), atoms in one molecule
const MOLECULES = [["H₂O", "water", "Suyun", 3], ["CO₂", "koolstofdioxide", "Karbondioksitin", 3], ["O₂", "zuurstof", "Oksijenin", 2], ["CH₄", "methaan", "Metanın", 5], ["NH₃", "ammoniak", "Amonyağın", 4]];
GEN.atoom = [
  [
    MC("Alles om je heen is opgebouwd uit heel kleine deeltjes. Hoe heten die?", "Çevrendeki her şey çok küçük parçacıklardan oluşur. Bunlara ne denir?", ["atomen", "atom"], [["korrels", "tanecik"], ["cellen", "hücre"], ["druppels", "damla"]],
      "Alle stoffen bestaan uit atomen. Ze zijn zo klein dat je ze niet kunt zien.", "Bütün maddeler atomlardan oluşur. O kadar küçüktürler ki gözle görülmezler."),
    MC("Welke deeltjes zitten in de <b>kern</b> van een atoom?", "Atomun <b>çekirdeğinde</b> hangi parçacıklar bulunur?", ["protonen en neutronen", "protonlar ve nötronlar"], [["alleen elektronen", "sadece elektronlar"], ["protonen en elektronen", "protonlar ve elektronlar"], ["moleculen", "moleküller"]],
      "In de kern zitten protonen en neutronen. De elektronen bewegen eromheen.", "Çekirdekte protonlar ve nötronlar bulunur. Elektronlar çevresinde dolanır.", { fig: fig.atom() }),
    MC("Welke deeltjes bewegen <b>rond</b> de kern?", "Çekirdeğin <b>etrafında</b> hangi parçacıklar dolanır?", ["elektronen", "elektronlar"], [["protonen", "protonlar"], ["neutronen", "nötronlar"], ["atomen", "atomlar"]],
      "Elektronen zijn heel licht en bewegen rond de kern.", "Elektronlar çok hafiftir ve çekirdeğin etrafında dolanır.", { fig: fig.atom() }),
    () => { const [nl, tr, i, en, et] = pick(PARTS); return Q(nl, tr, PART_OPTS[i].v, "", en, et, { opts: PART_OPTS }); },
    MC("Wat is de formule van water?", "Suyun formülü nedir?", ["H₂O", "H₂O"], [["CO₂", "CO₂"], ["O₂", "O₂"], ["HO", "HO"]],
      "Een watermolecuul bestaat uit 2 waterstofatomen (H) en 1 zuurstofatoom (O).", "Bir su molekülü 2 hidrojen atomu (H) ve 1 oksijen atomundan (O) oluşur.")
  ],
  [
    () => { const [nl, tr, p] = pick(ELEMENTS.slice(1)); return Q(`Een atoom ${nl} heeft ${p} protonen. Het atoom is neutraal. Hoeveel elektronen heeft het?`, `Bir ${tr} atomunun ${p} protonu var. Atom nötr. Kaç elektronu vardır?`, p, "",
      `In een neutraal atoom zijn er evenveel elektronen als protonen: ${p}.`, `Nötr atomda elektron sayısı proton sayısına eşittir: ${p}.`); },
    () => { const [f, nl, tr, n] = pick(MOLECULES); return Q(`De formule van ${nl} is ${f}. Uit hoeveel atomen bestaat één molecuul?`, `${tr} formülü ${f}. Bir molekül kaç atomdan oluşur?`, n, "",
      `Tel de atomen: het kleine cijfer hoort bij de letter ervoor. Samen ${n} atomen.`, `Atomları say: küçük rakam, önündeki harfe aittir. Toplam ${n} atom.`); },
    () => { const [nl, tr, p] = pick(ELEMENTS); const opts = shuffle(ELEMENTS).slice(0, 4); if (!opts.some(o => o[2] === p)) opts[0] = [nl, tr, p];
      return Q(`Welk element heeft ${p} ${p === 1 ? "proton" : "protonen"} in de kern?`, `Çekirdeğinde ${p} proton bulunan element hangisidir?`, String(p), "",
        `Het aantal protonen bepaalt welk element het is. ${p} ${p === 1 ? "proton" : "protonen"}: ${nl}.`, `Proton sayısı, elementin hangisi olduğunu belirler. ${p} proton: ${tr}.`, { opts: shuffle(opts).map(o => ({ v: String(o[2]), nl: o[0], tr: o[1] })) }); },
    () => { const a = ri(2, 9); return Q(`Eén molecuul water (H₂O) heeft 2 waterstofatomen. Hoeveel waterstofatomen zitten er in ${a} moleculen water?`, `Bir su molekülünde (H₂O) 2 hidrojen atomu var. ${a} su molekülünde kaç hidrojen atomu vardır?`, 2 * a, "",
      `${a} × 2 = ${2 * a}.`, `${a} × 2 = ${2 * a}.`); }
  ],
  [
    () => { const p = ri(3, 12), n = p + ri(0, 3); return Q(`In de kern van een atoom zitten ${p} protonen en ${n} neutronen. Hoeveel deeltjes zitten er in de kern?`, `Bir atomun çekirdeğinde ${p} proton ve ${n} nötron var. Çekirdekte toplam kaç parçacık var?`, p + n, "",
      `${p} + ${n} = ${p + n}. Dit getal heet het massagetal.`, `${p} + ${n} = ${p + n}. Bu sayıya kütle numarası denir.`); },
    () => { const p = ri(3, 12), n = p + ri(0, 3); return Q(`De kern van een atoom heeft ${p + n} deeltjes. Daarvan zijn er ${p} protonen. Hoeveel neutronen heeft het atoom?`, `Bir atomun çekirdeğinde ${p + n} parçacık var. Bunların ${p} tanesi proton. Atomun kaç nötronu var?`, n, "",
      `${p + n} − ${p} = ${n} neutronen.`, `${p + n} − ${p} = ${n} nötron.`); },
    () => { const a = ri(2, 9); return Q(`Eén molecuul koolstofdioxide (CO₂) bestaat uit 1 koolstofatoom en 2 zuurstofatomen. Hoeveel atomen zitten er in totaal in ${a} moleculen CO₂?`, `Bir karbondioksit molekülü (CO₂) 1 karbon ve 2 oksijen atomundan oluşur. ${a} CO₂ molekülünde toplam kaç atom vardır?`, 3 * a, "",
      `Eén molecuul heeft 3 atomen. ${a} × 3 = ${3 * a}.`, `Bir molekülde 3 atom var. ${a} × 3 = ${3 * a}.`); },
    MC("Welke van deze is een <b>molecuul</b> (meerdere atomen aan elkaar)?", "Bunlardan hangisi bir <b>moleküldür</b> (birbirine bağlı birden çok atom)?", ["H₂O", "H₂O"], [["He", "He"], ["Fe", "Fe"], ["C", "C"]],
      "H₂O bestaat uit 3 atomen die aan elkaar vastzitten. He, Fe en C zijn losse atomen.", "H₂O birbirine bağlı 3 atomdan oluşur. He, Fe ve C tek atomdur.")
  ]
];

export const makeQuestion = maker(GEN);
export const kindsPerLevel = topicId => GEN[topicId].map(l => l.length);

// ---------------------------------------------------------------- theory
export const THEORY = {
  licht: [
    { nl: "<b>Licht</b> komt van een <b>lichtbron</b>: de zon, een lamp, een kaars. Het gaat in een <b>rechte lijn</b>.<br>Houdt iets het licht tegen, dan ontstaat erachter een <b>schaduw</b>. Staat de zon hoog, dan is je schaduw kort; staat ze laag, dan is hij lang.",
      tr: "<b>Işık</b> bir <b>ışık kaynağından</b> gelir: Güneş, lamba, mum. <b>Düz bir çizgide</b> ilerler.<br>Bir şey ışığı engellerse arkasında <b>gölge</b> oluşur. Güneş yüksekteyken gölgen kısa, alçaktayken uzun olur." },
    { fig: fig.mirror("40°"), nl: "<b>Weerkaatsing</b>: een spiegel kaatst licht terug onder dezelfde hoek als waarmee het aankomt. Je spiegelbeeld lijkt even ver achter de spiegel te staan als jij ervoor staat.",
      tr: "<b>Yansıma</b>: ayna ışığı, geldiği açıyla aynı açıda geri yansıtır. Aynadaki görüntün, sen aynanın ne kadar önündeysen o kadar arkasında gibi görünür." },
    { nl: "<b>Breking</b>: gaat licht van lucht naar water (of andersom), dan verandert het een beetje van richting. Daarom lijkt een rietje in water geknikt.<br><b>Regenboog</b>: wit zonlicht bestaat uit alle kleuren. Regendruppels halen die kleuren uit elkaar.",
      tr: "<b>Kırılma</b>: ışık havadan suya (ya da tersine) geçerken biraz yön değiştirir. Bu yüzden sudaki pipet kırık gibi görünür.<br><b>Gökkuşağı</b>: beyaz güneş ışığı bütün renklerden oluşur. Yağmur damlaları bu renkleri birbirinden ayırır." },
    { eg: true, nl: "<b>Ambulance</b>: voorop staat het woord in spiegelschrift. Zo lees je het gewoon in de spiegel van de auto die ervoor rijdt.<br><b>Zwembad</b>: het water lijkt minder diep dan het is. Dat komt door breking.<br><b>Zonnewijzer</b>: de schaduw van een stok draait mee met de zon en wijst zo de tijd aan.<br><b>Maan</b>: de maan is geen lamp. Je ziet alleen het stuk waar de zon op schijnt.",
      tr: "<b>Ambulans</b>: önündeki yazı ters (ayna yazısı) yazılır. Böylece öndeki arabanın aynasında düz okunur.<br><b>Havuz</b>: su olduğundan daha sığ görünür. Bunun nedeni kırılmadır.<br><b>Güneş saati</b>: bir çubuğun gölgesi Güneş'le birlikte döner ve saati gösterir.<br><b>Ay</b>: Ay bir lamba değildir. Sadece Güneş'in aydınlattığı kısmını görürsün." }
  ],
  massa: [
    { nl: "<b>Massa</b> is hoeveel stof er in iets zit. Je meet het in gram en kilogram. Je massa is overal hetzelfde, ook op de maan.<br><b>Gewicht</b> is hoe hard de zwaartekracht aan je trekt. Op de maan is die kracht ongeveer 6 keer zo klein, dus daar voel je je veel lichter.",
      tr: "<b>Kütle</b>, bir şeyin içindeki madde miktarıdır. Gram ve kilogramla ölçülür. Kütlen her yerde aynıdır, Ay'da da.<br><b>Ağırlık</b>, yer çekiminin seni ne kadar kuvvetle çektiğidir. Ay'da bu kuvvet yaklaşık 6'da biri kadardır, orada kendini çok daha hafif hissedersin." },
    { nl: "<b>Dichtheid</b> zegt hoe zwaar iets is voor zijn grootte.<br><b>Dichtheid = massa ÷ volume</b><br>Voorbeeld: een blokje van 40 gram en 5 cm³ heeft een dichtheid van 40 ÷ 5 = 8 g/cm³.<br>Water heeft een dichtheid van 1 g/cm³: 1 liter water is 1 kg.",
      tr: "<b>Özkütle</b>, bir şeyin boyuna göre ne kadar ağır olduğunu söyler.<br><b>Özkütle = kütle ÷ hacim</b><br>Örnek: 40 gram ve 5 cm³ olan bir bloğun özkütlesi 40 ÷ 5 = 8 g/cm³.<br>Suyun özkütlesi 1 g/cm³: 1 litre su 1 kg eder." },
    { eg: true, nl: "<b>Op de maan</b>: astronauten springen daar veel hoger dan op aarde. Hun massa is hetzelfde, maar de maan trekt 6 keer zo zwak aan hen.<br><b>Watten en ijzer</b>: een kilo watten vult een hele zak, een kilo ijzer past in je hand. Zelfde massa, heel ander volume: ijzer heeft een grote dichtheid.<br><b>Olie en water</b>: giet olie in een glas water en de olie blijft bovenop liggen. Olie heeft een kleinere dichtheid dan water.",
      tr: "<b>Ay'da</b>: astronotlar orada Dünya'dakinden çok daha yükseğe zıplar. Kütleleri aynıdır ama Ay onları 6 kat zayıf çeker.<br><b>Pamuk ve demir</b>: bir kilo pamuk koca bir torbayı doldurur, bir kilo demir avucuna sığar. Kütle aynı, hacim çok farklı: demirin özkütlesi büyüktür.<br><b>Yağ ve su</b>: bir bardak suya yağ dök, yağ üstte kalır. Yağın özkütlesi suyunkinden küçüktür." }
  ],
  drijven: [
    { nl: "Water duwt alles wat erin ligt omhoog. Die kracht heet de <b>opwaartse kracht</b>.<br><b>Regel</b>: is de dichtheid van een voorwerp <b>kleiner</b> dan die van water (1 g/cm³), dan <b>drijft</b> het. Is ze groter, dan <b>zinkt</b> het.",
      tr: "Su, içindeki her şeyi yukarı iter. Bu kuvvete <b>kaldırma kuvveti</b> denir.<br><b>Kural</b>: bir cismin özkütlesi suyunkinden (1 g/cm³) <b>küçükse yüzer</b>, büyükse <b>batar</b>." },
    { fig: fig.cup(60, 80), nl: "Een voorwerp duwt zijn eigen volume aan water opzij. Stijgt het water in een maatbeker van 60 naar 80 ml, dan is het voorwerp 20 cm³.<br><b>Schip</b>: massief ijzer zinkt, maar een schip is hol. IJzer en lucht samen zijn lichter dan evenveel water.",
      tr: "Bir cisim kendi hacmi kadar suyu iter. Ölçü kabında su 60 ml'den 80 ml'ye çıkarsa cismin hacmi 20 cm³'tür.<br><b>Gemi</b>: içi dolu demir batar ama geminin içi boştur. Demir ve hava birlikte, aynı hacimdeki sudan hafiftir." },
    { eg: true, nl: "<b>Waarom drijft een schip van ijzer?</b> Een ijzeren spijker zinkt meteen, maar een schip van duizenden tonnen ijzer drijft. Het geheim: het schip is een grote holle bak vol lucht. Voor het water telt het <b>hele</b> schip mee, met alle lucht erin. Het volume is daardoor enorm, terwijl de massa bijna alleen van het ijzer komt. Massa ÷ een heel groot volume = een kleine dichtheid. Het ijzer gedraagt zich dus alsof het licht is.<br><b>Proefje</b>: een bolletje klei zinkt. Maak van dezelfde klei een bakje: het drijft. Zelfde massa, groter volume.<br><b>Lek</b>: loopt een schip vol water, dan is de lucht weg en zinkt het. Zo ging het bij de Titanic.",
      tr: "<b>Demirden gemi neden yüzer?</b> Demir bir çivi hemen batar ama binlerce ton demirden yapılmış gemi yüzer. Sırrı şu: gemi, içi hava dolu kocaman boş bir kaptır. Su için geminin <b>tamamı</b> sayılır, içindeki bütün havayla birlikte. Böylece hacim çok büyük olur, kütle ise neredeyse sadece demirden gelir. Kütle ÷ çok büyük hacim = küçük özkütle. Yani demir, sanki hafifmiş gibi davranır.<br><b>Deney</b>: oyun hamurundan bir top yap, batar. Aynı hamurdan bir kayık yap: yüzer. Kütle aynı, hacim daha büyük.<br><b>Su alırsa</b>: geminin içine su dolarsa hava gider ve gemi batar. Titanik'te böyle oldu." },
    { eg: true, nl: "<b>Ei in zout water</b>: een ei zinkt in gewoon water. Roer er veel zout door en het ei gaat drijven. In de Dode Zee is het water zo zout dat je vanzelf blijft drijven.<br><b>Duikboot</b>: wil hij zakken, dan laat hij water in zijn tanks en wordt hij zwaarder. Wil hij stijgen, dan perst hij het water er met lucht weer uit.<br><b>Zwemvest</b>: veel lucht, weinig massa. Samen met het vest is jouw dichtheid kleiner dan die van water.",
      tr: "<b>Tuzlu suda yumurta</b>: yumurta normal suda batar. Suya bol tuz karıştır, yumurta yüzmeye başlar. Lut Gölü'nde su o kadar tuzludur ki kendiliğinden yüzersin.<br><b>Denizaltı</b>: dalmak isteyince tanklarına su alır ve ağırlaşır. Yükselmek isteyince suyu havayla dışarı iter.<br><b>Can yeleği</b>: çok hava, az kütle. Yelekle birlikte senin özkütlen suyunkinden küçük olur." }
  ],
  atoom: [
    { fig: fig.atom(), nl: "Alles is gemaakt van <b>atomen</b>. In het midden zit de <b>kern</b> met <b>protonen</b> (positief) en <b>neutronen</b> (geen lading). Rond de kern bewegen <b>elektronen</b> (negatief).<br>In een neutraal atoom zijn er evenveel elektronen als protonen.",
      tr: "Her şey <b>atomlardan</b> yapılmıştır. Ortada <b>çekirdek</b> vardır; içinde <b>protonlar</b> (pozitif) ve <b>nötronlar</b> (yüksüz) bulunur. Çekirdeğin etrafında <b>elektronlar</b> (negatif) dolanır.<br>Nötr bir atomda elektron sayısı proton sayısına eşittir." },
    { nl: "Het aantal protonen bepaalt welk <b>element</b> het is: 1 = waterstof (H), 2 = helium (He), 6 = koolstof (C), 8 = zuurstof (O).<br>Atomen die aan elkaar vastzitten vormen een <b>molecuul</b>. Water is H₂O: 2 waterstofatomen en 1 zuurstofatoom.",
      tr: "Proton sayısı, <b>elementin</b> hangisi olduğunu belirler: 1 = hidrojen (H), 2 = helyum (He), 6 = karbon (C), 8 = oksijen (O).<br>Birbirine bağlanan atomlar bir <b>molekül</b> oluşturur. Su H₂O'dur: 2 hidrojen atomu ve 1 oksijen atomu." },
    { eg: true, nl: "<b>Lego</b>: met een paar soorten blokjes bouw je een huis, een auto of een ruimteschip. Zo werkt de natuur ook: er zijn ruim honderd soorten atomen, en daarmee is alles gebouwd, ook jijzelf.<br><b>Hoe leeg is een atoom?</b> Stel dat een atoom zo groot was als een voetbalstadion. Dan was de kern een erwt op de middenstip. De rest is bijna helemaal leeg.<br><b>Hoe klein?</b> In één druppel water zitten meer moleculen dan er zandkorrels op een strand liggen.",
      tr: "<b>Lego</b>: birkaç çeşit parçayla ev, araba ya da uzay gemisi yaparsın. Doğa da böyle çalışır: yüzden biraz fazla çeşit atom vardır ve her şey, sen de dahil, bunlardan yapılmıştır.<br><b>Atom ne kadar boş?</b> Bir atom futbol stadyumu kadar büyük olsaydı çekirdek, orta noktadaki bir bezelye kadar olurdu. Geri kalanı neredeyse tamamen boştur.<br><b>Ne kadar küçük?</b> Bir damla suda, bir kumsaldaki kum tanelerinden daha fazla molekül vardır." }
  ]
};

export const WORDS = {
  licht: [["licht", "ışık"], ["lichtbron", "ışık kaynağı"], ["schaduw", "gölge"], ["spiegel", "ayna"], ["weerkaatsen", "yansımak"], ["breking", "kırılma"], ["regenboog", "gökkuşağı"], ["doorzichtig", "saydam"]],
  massa: [["massa", "kütle"], ["gewicht", "ağırlık"], ["zwaartekracht", "yer çekimi"], ["dichtheid", "özkütle"], ["volume (inhoud)", "hacim"], ["weegschaal", "tartı"]],
  drijven: [["drijven", "yüzmek"], ["zinken", "batmak"], ["opwaartse kracht", "kaldırma kuvveti"], ["dichtheid", "özkütle"], ["maatbeker", "ölçü kabı"], ["zout water", "tuzlu su"]],
  atoom: [["atoom", "atom"], ["kern", "çekirdek"], ["lading", "yük"], ["element", "element"], ["molecuul", "molekül"], ["waterstof", "hidrojen"], ["zuurstof", "oksijen"], ["koolstof", "karbon"]]
};
