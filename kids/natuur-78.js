// Natuur & techniek for groep 7-8: electricity, forces, sound, states of matter, the solar system.
// Merged into kids/natuur-vragen.js. All topics start hidden; the admin opens them (admin page, tab İçerik).
// These are the usual natuur & techniek themes of the upper years of Dutch primary school; the questions
// are written by hand, with fresh numbers only where something is calculated.
import { ri, pick, Q, svg, T, MC } from "./vragen-basis.js?v=3";

export const N_TOPICS = [
  { id: "elektriciteit", nl: "Elektriciteit", tr: "Elektrik", sub_nl: "stroomkring, geleider, schakelaar", sub_tr: "devre, iletken, anahtar", open: false, band: "7-8", school: true },
  { id: "magnetisme", nl: "Magnetisme", tr: "Manyetizma (mıknatıslar)", sub_nl: "aantrekken, afstoten, kompas", sub_tr: "çekme, itme, pusula", open: false, band: "7-8", school: true },
  { id: "krachten", nl: "Krachten en hefbomen", tr: "Kuvvetler ve kaldıraçlar", sub_nl: "duwen, trekken, wrijving, wip", sub_tr: "itme, çekme, sürtünme, tahterevalli", open: false, band: "7-8", school: true },
  { id: "geluid", nl: "Geluid", tr: "Ses", sub_nl: "trillingen, hoog en laag, echo", sub_tr: "titreşim, ince ve kalın ses, yankı", open: false, band: "7-8", school: true },
  { id: "fasen", nl: "Vast, vloeibaar en gas", tr: "Katı, sıvı ve gaz", sub_nl: "smelten, koken, verdampen", sub_tr: "erime, kaynama, buharlaşma", open: false, band: "7-8", school: true },
  { id: "zonnestelsel", nl: "Het zonnestelsel", tr: "Güneş sistemi", sub_nl: "zon, planeten, dag en nacht, seizoenen", sub_tr: "Güneş, gezegenler, gece gündüz, mevsimler", open: false, band: "7-8", school: true }
];

const fig = {
  // closed circuit: battery on the left, lamp on top
  circuit: () => svg(`<polyline class="room" points="40,30 180,30 180,105 40,105 40,30"/><circle class="shape" cx="110" cy="30" r="13"/>${T(110, 34, "✕")}
    <rect class="shape" x="30" y="55" width="20" height="26"/>${T(64, 72, "batterij", "start")}${T(110, 60, "lampje")}`),
  // bar magnet: north half filled, south half open, with dashed field lines from N to Z
  magnet: () => svg(`<path class="room dash" d="M80,52 C60,10 160,10 140,52"/><path class="room dash" d="M80,78 C60,120 160,120 140,78"/>
    <path class="room dash" d="M70,58 C20,30 20,100 70,72"/><path class="room dash" d="M150,58 C200,30 200,100 150,72"/>
    <rect class="shape" x="70" y="52" width="40" height="26"/><rect class="room" x="110" y="52" width="40" height="26"/>${T(90, 70, "N")}${T(130, 70, "Z")}`),
  // two magnets: same poles facing (push away) or different poles (pull together)
  poles: (same) => svg(`<rect class="shape" x="20" y="50" width="35" height="26"/><rect class="room" x="55" y="50" width="35" height="26"/>${T(37, 68, "N")}${T(72, 68, "Z")}
    <rect class="${same ? "room" : "shape"}" x="130" y="50" width="35" height="26"/><rect class="${same ? "shape" : "room"}" x="165" y="50" width="35" height="26"/>
    ${T(147, 68, same ? "Z" : "N")}${T(182, 68, same ? "N" : "Z")}${T(110, 40, same ? "← →" : "→ ←")}`),
  // seesaw with two loads
  wip: (l, r) => svg(`<line x1="25" y1="70" x2="195" y2="70" style="stroke-width:4"/><polygon class="shape" points="110,72 96,104 124,104"/>
    <rect class="shape" x="30" y="46" width="26" height="22"/><rect class="shape" x="164" y="46" width="26" height="22"/>${T(43, 40, l)}${T(177, 40, r)}`)
};

export const N_GEN = {};

// ----- Elektriciteit
const MATERIALS = [["koper", "bakır", true], ["ijzer", "demir", true], ["aluminium", "alüminyum", true], ["plastic", "plastik", false], ["hout", "tahta", false], ["rubber", "lastik", false], ["glas", "cam", false]];
N_GEN.elektriciteit = [
  [
    MC("Wanneer gaat een lampje in een stroomkring branden?", "Bir devredeki ampul ne zaman yanar?", ["als de kring helemaal gesloten is", "devre tamamen kapalıysa"], [["als er één draad aan de batterij zit", "pile tek bir kablo bağlıysa"], ["als de schakelaar open staat", "anahtar açıksa"], ["altijd", "her zaman"]],
      "Stroom loopt alleen rond in een gesloten kring: van de batterij door het lampje en weer terug.", "Akım sadece kapalı devrede dolaşır: pilden ampule, oradan tekrar pile.", { fig: fig.circuit() }),
    () => { const good = pick(MATERIALS.filter(m => m[2])), bad = MATERIALS.filter(m => !m[2]).sort(() => Math.random() - 0.5).slice(0, 3);
      return MC("Welk materiaal laat stroom goed door (een <b>geleider</b>)?", "Hangi madde elektriği iyi iletir (<b>iletken</b>)?", [good[0], good[1]], bad.map(b => [b[0], b[1]]),
        "Metalen geleiden stroom. Plastic, hout, rubber en glas houden stroom tegen: dat zijn isolatoren.", "Metaller elektriği iletir. Plastik, tahta, lastik ve cam iletmez: bunlar yalıtkandır.")(); },
    MC("Waarom zit er plastic om een stroomdraad?", "Elektrik kablosunun etrafında neden plastik vardır?", ["plastic houdt de stroom tegen, zodat je geen schok krijgt", "plastik akımı geçirmez, böylece çarpılmazsın"], [["plastic maakt de stroom sneller", "plastik akımı hızlandırır"], ["plastic geeft licht", "plastik ışık verir"], ["anders roest de draad", "yoksa kablo paslanır"]],
      "Plastic is een isolator. Het koper binnenin geleidt de stroom, het plastic eromheen beschermt jou.", "Plastik yalıtkandır. İçindeki bakır akımı iletir, dışındaki plastik seni korur."),
    MC("Wat doet een schakelaar?", "Anahtar (düğme) ne yapar?", ["hij opent of sluit de stroomkring", "devreyi açar ya da kapatır"], [["hij maakt stroom", "elektrik üretir"], ["hij bewaart stroom", "elektriği depolar"], ["hij maakt de lamp feller", "ampulü daha parlak yapar"]],
      "Zet je het licht uit, dan onderbreek je de kring en kan de stroom niet meer rond.", "Işığı kapattığında devreyi kesersin ve akım artık dolaşamaz."),
    MC("Je wrijft een ballon een tijdje over je haar en houdt hem dan tegen de muur. Wat gebeurt er?", "Bir balonu bir süre saçına sürtüp sonra duvara tutuyorsun. Ne olur?", ["de ballon blijft aan de muur plakken", "balon duvara yapışıp kalır"], [["de ballon knapt", "balon patlar"], ["de ballon wordt warm", "balon ısınır"], ["er gebeurt niets", "hiçbir şey olmaz"]],
      "Door het wrijven krijgt de ballon een elektrische lading. Die lading trekt aan de muur en aan je haren. Dat heet statische elektriciteit.", "Sürtünce balon elektrik yükü kazanır. Bu yük duvarı ve saçlarını çeker. Buna statik elektrik denir."),
    MC("Waar mag je <b>nooit</b> iets in steken?", "Hangisinin içine <b>asla</b> bir şey sokmamalısın?", ["in een stopcontact", "prize"], [["in een spaarpot", "kumbaraya"], ["in een etui", "kalem kutusuna"], ["in een zandbak", "kum havuzuna"]],
      "In het stopcontact zit 230 volt. Daar kun je een zware schok van krijgen. Een stekker is gemaakt om erin te gaan; een vork of een vinger niet.", "Prizde 230 volt vardır. Ağır bir elektrik çarpması yaşayabilirsin. Fiş prize takılmak için yapılmıştır; çatal ya da parmak değil.")
  ],
  [
    MC("Twee lampjes zitten achter elkaar in één kring (serie). Eén lampje gaat kapot. Wat gebeurt er met het andere?", "İki ampul aynı devrede art arda bağlı (seri). Biri bozuluyor. Diğerine ne olur?", ["het gaat ook uit", "o da söner"], [["het blijft branden", "yanmaya devam eder"], ["het gaat feller branden", "daha parlak yanar"], ["het gaat knipperen", "yanıp söner"]],
      "In serie is er maar één weg. Is die onderbroken, dan loopt er nergens meer stroom.", "Seri bağlantıda tek bir yol vardır. O yol kesilirse hiçbir yerden akım geçmez."),
    MC("Thuis zijn de lampen parallel geschakeld. Wat is daar het voordeel van?", "Evde lambalar paralel bağlıdır. Bunun faydası nedir?", ["gaat er één lamp kapot, dan blijven de andere branden", "bir lamba bozulursa diğerleri yanmaya devam eder"], [["je hebt geen stroom nodig", "elektriğe gerek kalmaz"], ["de lampen worden nooit warm", "lambalar hiç ısınmaz"], ["er is maar één draad nodig", "tek kablo yeter"]],
      "Bij parallel heeft elke lamp zijn eigen weg naar de stroombron.", "Paralel bağlantıda her lambanın kaynağa giden kendi yolu vardır."),
    () => { const n = ri(2, 4); return Q(`Eén batterij is 1,5 volt. Je zet ${n * 2} batterijen achter elkaar. Hoeveel volt is dat samen?`, `Bir pil 1,5 volttur. ${n * 2} pili art arda bağlıyorsun. Toplam kaç volt eder?`, n * 3, "volt", `${n * 2} × 1,5 = ${n * 3} volt.`, `${n * 2} × 1,5 = ${n * 3} volt.`); },
    MC("Waarom mag je een föhn niet gebruiken in bad?", "Banyoda küvetin içindeyken neden saç kurutma makinesi kullanılmaz?", ["water met zouten erin geleidt stroom, en jouw lichaam ook", "içinde tuz bulunan su elektriği iletir, senin vücudun da"], [["de föhn wordt dan te koud", "makine çok soğur"], ["water maakt de föhn zwaarder", "su makineyi ağırlaştırır"], ["het haar droogt dan niet", "saç kurumaz"]],
      "Kraanwater geleidt stroom. Valt een apparaat in het water, dan kan de stroom door jouw lichaam lopen. Dat is levensgevaarlijk.", "Musluk suyu elektriği iletir. Bir cihaz suya düşerse akım vücudundan geçebilir. Bu ölümcül tehlikelidir."),
    MC("Een batterij van 1,5 volt kun je gewoon vastpakken, het stopcontact niet. Waarom?", "1,5 voltluk bir pili rahatça tutabilirsin ama prize dokunamazsın. Neden?", ["het stopcontact heeft veel meer spanning (230 volt) en dat is gevaarlijk", "prizin gerilimi çok daha yüksektir (230 volt) ve bu tehlikelidir"], [["een batterij heeft geen stroom", "pilde elektrik yoktur"], ["het stopcontact is warmer", "priz daha sıcaktır"], ["batterijen zijn van plastic", "piller plastiktir"]],
      "Hoe hoger de spanning, hoe harder de stroom kan duwen. 1,5 volt voel je niet, 230 volt kan levensgevaarlijk zijn.", "Gerilim ne kadar yüksekse akım o kadar güçlü itilir. 1,5 voltu hissetmezsin, 230 volt ise hayati tehlike yaratabilir.")
  ],
  [
    () => { const w = pick([5, 10, 40, 60]), h = ri(2, 6); return Q(`Een lamp gebruikt ${w} watt. Hoeveel wattuur energie gebruikt hij als hij ${h} uur brandt?`, `Bir lamba ${w} watt harcıyor. ${h} saat yanarsa kaç watt-saat enerji harcar?`, w * h, "wattuur", `Energie = vermogen × tijd = ${w} × ${h} = ${w * h} wattuur.`, `Enerji = güç × zaman = ${w} × ${h} = ${w * h} watt-saat.`); },
    () => { const old = pick([40, 60, 75]), led = pick([5, 8, 10]), n = ri(3, 8); return Q(`Je vervangt ${n} oude lampen van ${old} watt door ledlampen van ${led} watt. Hoeveel watt gebruik je dan minder als alle lampen aan zijn?`, `${old} watt'lık ${n} eski ampulü ${led} watt'lık led ampullerle değiştiriyorsun. Bütün lambalar açıkken kaç watt daha az harcarsın?`, n * (old - led), "watt", `Per lamp ${old} − ${led} = ${old - led} watt minder. ${n} × ${old - led} = ${n * (old - led)}.`, `Lamba başına ${old} − ${led} = ${old - led} watt az. ${n} × ${old - led} = ${n * (old - led)}.`); },
    MC("Een zonnepaneel maakt stroom. Waar komt de energie vandaan?", "Güneş paneli elektrik üretir. Enerji nereden gelir?", ["uit het licht van de zon", "Güneş'in ışığından"], [["uit de wind", "rüzgârdan"], ["uit de warmte van het dak", "çatının ısısından"], ["uit een batterij in het paneel", "panelin içindeki pilden"]],
      "Een zonnepaneel zet zonlicht om in elektriciteit. Daarom levert het 's nachts niets.", "Güneş paneli güneş ışığını elektriğe çevirir. Bu yüzden gece hiç üretmez."),
    MC("Bij onweer zie je een bliksemflits. Wat is bliksem?", "Fırtınada şimşek çakar. Şimşek nedir?", ["een hele grote elektrische vonk", "çok büyük bir elektrik kıvılcımı"], [["vuur dat uit een wolk valt", "buluttan düşen ateş"], ["licht van de zon dat weerkaatst", "Güneş ışığının yansıması"], ["twee wolken die botsen", "iki bulutun çarpışması"]],
      "In een onweerswolk bouwt zich elektrische lading op. Wordt die te groot, dan springt er een vonk over: de bliksem.", "Fırtına bulutunda elektrik yükü birikir. Çok artınca bir kıvılcım atlar: şimşek."),
    () => { const n = ri(4, 12), k = ri(6, 14); return Q(`In een straat staan ${n} huizen. Op elk dak liggen ${k} zonnepanelen. Hoeveel zonnepanelen zijn er in de hele straat?`, `Bir sokakta ${n} ev var. Her evin çatısında ${k} güneş paneli var. Bütün sokakta kaç güneş paneli var?`, n * k, "",
      `${n} × ${k} = ${n * k}.`, `${n} × ${k} = ${n * k}.`); }
  ]
];

// ----- Magnetisme
// What a magnet attracts: iron and steel yes; aluminium, copper, plastic, wood, paper and glass no.
// (Euro coins are left out on purpose: some of them are attracted and some are not.)
const MAGNETIC = [["een paperclip", "ataş"], ["een ijzeren spijker", "demir çivi"], ["een schaar van staal", "çelik makas"], ["een punaise van staal", "çelik raptiye"]];
const NOT_MAGNETIC = [["een plastic lepel", "plastik kaşık"], ["een houten potlood", "tahta kalem"], ["een blikje van aluminium", "alüminyum kutu"], ["een gum", "silgi"], ["een glazen knikker", "cam bilye"], ["een koperen sleutel", "bakır anahtar"]];
N_GEN.magnetisme = [
  [
    () => { const r = pick(MAGNETIC), w = NOT_MAGNETIC.slice().sort(() => Math.random() - 0.5).slice(0, 3);
      return MC("Wat wordt door een magneet aangetrokken?", "Hangisi mıknatıs tarafından çekilir?", r, w,
        "Een magneet trekt ijzer en staal aan. Plastic, hout, glas en de meeste andere metalen (zoals aluminium en koper) niet.", "Mıknatıs demiri ve çeliği çeker. Plastik, tahta, cam ve diğer metallerin çoğu (alüminyum ve bakır gibi) çekilmez.")(); },
    MC("Je houdt twee <b>noordpolen</b> naar elkaar toe. Wat gebeurt er?", "İki mıknatısın <b>kuzey kutuplarını</b> birbirine yaklaştırıyorsun. Ne olur?", ["ze duwen elkaar weg", "birbirlerini iterler"], [["ze trekken elkaar aan", "birbirlerini çekerler"], ["er gebeurt niets", "hiçbir şey olmaz"], ["ze worden warm", "ısınırlar"]],
      "Gelijke polen stoten elkaar af: noord en noord, of zuid en zuid.", "Aynı kutuplar birbirini iter: kuzey ile kuzey ya da güney ile güney.", { fig: fig.poles(true) }),
    MC("Je houdt een noordpool en een zuidpool naar elkaar toe. Wat gebeurt er?", "Bir kuzey kutbunu bir güney kutbuna yaklaştırıyorsun. Ne olur?", ["ze trekken elkaar aan", "birbirlerini çekerler"], [["ze duwen elkaar weg", "birbirlerini iterler"], ["er gebeurt niets", "hiçbir şey olmaz"], ["de magneten breken", "mıknatıslar kırılır"]],
      "Ongelijke polen trekken elkaar aan: noord en zuid klikken tegen elkaar.", "Farklı kutuplar birbirini çeker: kuzey ile güney birbirine yapışır.", { fig: fig.poles(false) }),
    () => Q("Hoeveel polen heeft een magneet?", "Bir mıknatısın kaç kutbu vardır?", 2, "", "Een noordpool (N) en een zuidpool (Z).", "Bir kuzey kutbu (N) ve bir güney kutbu (Z; Türkçede S).", { fig: fig.magnet() })
  ],
  [
    MC("Een magneet houdt een tekening op de koelkast vast. Wat leert dat je?", "Bir mıknatıs buzdolabındaki resmi tutuyor. Bu sana ne öğretir?", ["de kracht van een magneet werkt door papier heen", "mıknatısın kuvveti kâğıdın içinden geçer"], [["papier is magnetisch", "kâğıt manyetiktir"], ["de koelkast is van plastic", "buzdolabı plastiktir"], ["de magneet is nat", "mıknatıs ıslaktır"]],
      "Het magneetveld gaat door papier, glas, water en zelfs je hand heen. De deur van de koelkast is van staal.", "Manyetik alan kâğıttan, camdan, sudan, hatta elinden bile geçer. Buzdolabının kapısı çeliktir."),
    MC("Je breekt een staafmagneet in twee stukken. Wat heb je dan?", "Bir çubuk mıknatısı ikiye kırıyorsun. Elinde ne olur?", ["twee kleinere magneten, elk met een noord- en een zuidpool", "her birinin kuzey ve güney kutbu olan iki küçük mıknatıs"], [["een losse noordpool en een losse zuidpool", "tek başına bir kuzey ve tek başına bir güney kutbu"], ["twee stukken ijzer zonder kracht", "kuvveti olmayan iki demir parçası"], ["één magneet en één stuk ijzer", "bir mıknatıs ve bir demir parçası"]],
      "Een magneet heeft altijd twee polen. Breek je hem, dan krijgt elk stuk weer een noord- en een zuidpool.", "Mıknatısın her zaman iki kutbu vardır. Kırarsan her parçanın yine bir kuzey ve bir güney kutbu olur."),
    MC("Waarom wijst een kompasnaald altijd naar het noorden?", "Pusula iğnesi neden hep kuzeyi gösterir?", ["de aarde is zelf een grote magneet", "Dünya'nın kendisi büyük bir mıknatıstır"], [["de zon trekt aan de naald", "Güneş iğneyi çeker"], ["de wind duwt de naald", "rüzgâr iğneyi iter"], ["het noorden is kouder", "kuzey daha soğuktur"]],
      "De kompasnaald is een klein magneetje. Het magneetveld van de aarde draait de naald naar het noorden.", "Pusula iğnesi küçük bir mıknatıstır. Dünya'nın manyetik alanı iğneyi kuzeye çevirir."),
    MC("Een elektromagneet houdt een stuk ijzer vast. Wat gebeurt er als je de stroom uitzet?", "Bir elektromıknatıs bir demir parçasını tutuyor. Elektriği kesersen ne olur?", ["het ijzer valt los, want zonder stroom is het geen magneet meer", "demir düşer, çünkü elektrik olmadan artık mıknatıs değildir"], [["het ijzer blijft altijd hangen", "demir hep asılı kalır"], ["het ijzer wordt zelf een magneet", "demirin kendisi mıknatıs olur"], ["de magneet wordt sterker", "mıknatıs güçlenir"]],
      "Een elektromagneet is alleen een magneet zolang er stroom door de draad loopt. Daarom kun je hem aan- en uitzetten.", "Elektromıknatıs, yalnızca telinden akım geçtiği sürece mıknatıstır. Bu yüzden açılıp kapatılabilir.")
  ],
  [
    () => { const n = ri(4, 12) * 10, a = ri(1, n / 10 - 1) * 10; return Q(`In een bak liggen ${n} lege blikjes. ${a} zijn van staal, de rest van aluminium. Een grote magneet haalt de stalen blikjes eruit. Hoeveel blikjes blijven er liggen?`, `Bir kutuda ${n} boş teneke var. ${a} tanesi çelik, geri kalanı alüminyum. Büyük bir mıknatıs çelik olanları çekip alıyor. Kaç teneke kalır?`, n - a, "",
      `De magneet pakt alleen het staal. Er blijven ${n} − ${a} = ${n - a} aluminium blikjes over.`, `Mıknatıs sadece çeliği çeker. Geriye ${n} − ${a} = ${n - a} alüminyum teneke kalır.`); },
    () => { const p = ri(2, 4), w = pick([20, 30, 40, 50]); return Q(`Proefje: je wikkelt draad om een spijker en sluit een batterij aan. Met 10 wikkelingen pakt de spijker ${p} paperclips op. In dit proefje pakt hij er bij elke 10 wikkelingen extra ${p} meer op. Hoeveel paperclips pakt hij op met ${w} wikkelingen?`, `Deney: bir çivinin etrafına tel sarıp bir pile bağlıyorsun. 10 sarımla çivi ${p} ataş kaldırıyor. Bu deneyde her 10 sarım fazlası ${p} ataş daha kaldırıyor. ${w} sarımla kaç ataş kaldırır?`, p * w / 10, "",
      `${w} wikkelingen is ${w / 10} keer 10. ${w / 10} × ${p} = ${p * w / 10}. Meer wikkelingen maken de elektromagneet sterker.`, `${w} sarım, 10'un ${w / 10} katıdır. ${w / 10} × ${p} = ${p * w / 10}. Sarım arttıkça elektromıknatıs güçlenir.`); },
    MC("Hoe maak je van een gewone ijzeren naald een kompasnaald?", "Sıradan bir demir iğneyi nasıl pusula iğnesine çevirirsin?", ["vaak met een magneet in dezelfde richting langs de naald strijken", "bir mıknatısı iğne boyunca hep aynı yönde defalarca sürtmek"], [["de naald in de vriezer leggen", "iğneyi dondurucuya koymak"], ["de naald heen en weer buigen", "iğneyi ileri geri bükmek"], ["de naald nat maken", "iğneyi ıslatmak"]],
      "Door het strijken wordt de naald zelf een magneetje. Leg je hem op een kurkje in een bak water, dan draait hij naar het noorden.", "Sürtünce iğnenin kendisi küçük bir mıknatıs olur. Su dolu bir kapta mantar tıpanın üstüne koyarsan kuzeye döner."),
    MC("Je kompas wijst recht vooruit: daar is het noorden. Je draait je helemaal om. Welke kant kijk je nu op?", "Pusulan tam önünü gösteriyor: kuzey orada. Tamamen arkanı dönüyorsun. Şimdi hangi yöne bakıyorsun?", ["het zuiden", "güney"], [["het noorden", "kuzey"], ["het oosten", "doğu"], ["het westen", "batı"]],
      "Tegenover het noorden ligt het zuiden. De naald wijst nog steeds naar het noorden, nu achter je.", "Kuzeyin tam tersi güneydir. İğne hâlâ kuzeyi gösterir, artık senin arkanda.")
  ]
];

// ----- Krachten en hefbomen
N_GEN.krachten = [
  [
    MC("Je schopt tegen een bal. Wat doet de kracht van je voet?", "Topa vuruyorsun. Ayağının kuvveti ne yapar?", ["ze brengt de bal in beweging", "topu harekete geçirir"], [["ze maakt de bal zwaarder", "topu ağırlaştırır"], ["ze maakt de bal kleiner", "topu küçültür"], ["niets", "hiçbir şey"]],
      "Een kracht kan iets in beweging brengen, afremmen, van richting veranderen of vervormen.", "Kuvvet bir cismi harekete geçirebilir, yavaşlatabilir, yönünü ya da şeklini değiştirebilir."),
    MC("Een bal rolt over het gras en stopt vanzelf. Welke kracht remt hem af?", "Top çimde yuvarlanıyor ve kendiliğinden duruyor. Onu hangi kuvvet yavaşlatır?", ["wrijving", "sürtünme"], [["zwaartekracht", "yer çekimi"], ["magnetisme", "manyetizma"], ["de opwaartse kracht", "kaldırma kuvveti"]],
      "Het gras schuurt langs de bal: dat is wrijving. Op ijs is er weinig wrijving en glijdt alles ver door.", "Çim topa sürtünür: buna sürtünme denir. Buzda sürtünme azdır, her şey uzağa kayar."),
    MC("Waarom valt een appel naar beneden en niet omhoog?", "Elma neden yukarı değil aşağı düşer?", ["de zwaartekracht van de aarde trekt eraan", "Dünya'nın yer çekimi onu çeker"], [["de lucht duwt hem omlaag", "hava onu aşağı iter"], ["de boom duwt hem weg", "ağaç onu iter"], ["appels zijn zwaarder dan lucht", "elma havadan ağırdır"]],
      "De aarde trekt alles naar zich toe. Die kracht heet zwaartekracht.", "Dünya her şeyi kendine çeker. Bu kuvvete yer çekimi denir."),
    MC("Waarmee meet je een kracht?", "Kuvvet neyle ölçülür?", ["met een krachtmeter (in newton)", "dinamometreyle (newton olarak)"], [["met een thermometer", "termometreyle"], ["met een liniaal", "cetvelle"], ["met een stopwatch", "kronometreyle"]],
      "Kracht meet je in newton. Een appel van 100 gram trekt met ongeveer 1 newton aan je hand.", "Kuvvet newton ile ölçülür. 100 gramlık bir elma eline yaklaşık 1 newton kuvvet uygular.")
  ],
  [
    MC("Op een wip zit een zwaar kind tegenover een licht kind. Hoe komt de wip toch in evenwicht?", "Tahterevallide ağır bir çocuk ile hafif bir çocuk karşılıklı oturuyor. Tahterevalli nasıl dengeye gelir?", ["het zware kind gaat dichter bij het midden zitten", "ağır çocuk ortaya daha yakın oturur"], [["het zware kind gaat verder naar achteren", "ağır çocuk daha geriye oturur"], ["het lichte kind gaat dichter bij het midden zitten", "hafif çocuk ortaya daha yakın oturur"], ["dat kan nooit", "bu hiç olmaz"]],
      "Bij een hefboom telt kracht × afstand tot het draaipunt. Wie ver van het midden zit, heeft meer effect.", "Kaldıraçta kuvvet × dönme noktasına uzaklık önemlidir. Ortadan uzakta oturanın etkisi daha büyük olur.", { fig: fig.wip("zwaar", "licht") }),
    () => { const a = ri(2, 4), w1 = ri(2, 5) * 10, k = pick([2, 3]); return Q(`Op een wip zit een kind van ${w1 * k} kg op ${a} meter van het midden. Aan de andere kant zit een kind van ${w1} kg. Op hoeveel meter van het midden moet dat kind zitten voor evenwicht?`, `Tahterevallide ${w1 * k} kg'lık bir çocuk ortadan ${a} metre uzakta oturuyor. Diğer tarafta ${w1} kg'lık bir çocuk var. Denge için bu çocuk ortadan kaç metre uzakta oturmalı?`, a * k, "m",
      `Gewicht × afstand moet gelijk zijn: ${w1 * k} × ${a} = ${w1 * k * a}. ${w1 * k * a} : ${w1} = ${a * k} m.`, `Ağırlık × uzaklık eşit olmalı: ${w1 * k} × ${a} = ${w1 * k * a}. ${w1 * k * a} : ${w1} = ${a * k} m.`); },
    MC("Waarom zit de klink van een deur ver van de scharnieren?", "Kapı kolu neden menteşelerden uzaktadır?", ["dan heb je minder kracht nodig om de deur te draaien", "böylece kapıyı çevirmek için daha az kuvvet gerekir"], [["dat ziet er mooier uit", "daha güzel görünür"], ["dan gaat de deur langzamer", "kapı daha yavaş açılır"], ["anders past de deur niet", "yoksa kapı yerine oturmaz"]],
      "Een deur is een hefboom. Duw eens vlak bij de scharnieren: dan is het veel zwaarder.", "Kapı bir kaldıraçtır. Menteşelerin hemen yanından itmeyi dene: çok daha zordur."),
    MC("Waarom hebben fietsbanden en schoenzolen ribbels?", "Bisiklet lastiklerinde ve ayakkabı tabanlarında neden tırtık vardır?", ["voor meer wrijving, zodat je niet wegglijdt", "sürtünmeyi artırmak için, böylece kaymazsın"], [["voor minder wrijving, zodat je sneller gaat", "sürtünmeyi azaltmak için, böylece hızlanırsın"], ["om ze lichter te maken", "hafifletmek için"], ["dat is alleen versiering", "sadece süs"]],
      "Wrijving is niet altijd lastig: zonder wrijving kun je niet remmen, sturen of lopen.", "Sürtünme her zaman kötü değildir: sürtünme olmadan fren yapamaz, dönemez, yürüyemezsin.")
  ],
  [
    () => { const m = ri(2, 9) * 10; return Q(`Op aarde trekt de zwaartekracht met ongeveer 10 newton aan elke kilogram. Met hoeveel newton trekt de aarde aan een kind van ${m} kg?`, `Dünya'da yer çekimi her kilograma yaklaşık 10 newton kuvvet uygular. Dünya ${m} kg'lık bir çocuğu kaç newton kuvvetle çeker?`, m * 10, "newton", `${m} × 10 = ${m * 10} newton.`, `${m} × 10 = ${m * 10} newton.`); },
    () => { const l = ri(2, 4), w = ri(2, 6) * 10, k = pick([2, 4, 5]); return Q(`Je tilt een steen van ${w * k} kg op met een lange stok als hefboom. De steen ligt op 1 meter van het draaipunt, jij duwt op ${k} meter. Met hoeveel kg kracht hoef je maar te duwen?`, `${w * k} kg'lık bir taşı, uzun bir sopayı kaldıraç yaparak kaldırıyorsun. Taş dönme noktasından 1 metre uzakta, sen ${k} metre uzaktan bastırıyorsun. Kaç kg'lık kuvvetle bastırman yeter?`, w, "kg",
      `${w * k} × 1 = ${w * k}. Jij duwt op ${k} meter: ${w * k} : ${k} = ${w} kg.`, `${w * k} × 1 = ${w * k}. Sen ${k} metreden bastırıyorsun: ${w * k} : ${k} = ${w} kg.`); },
    MC("Een parachutist valt eerst snel en met open parachute langzaam. Welke kracht remt hem af?", "Paraşütçü önce hızlı, paraşüt açılınca yavaş düşer. Onu hangi kuvvet yavaşlatır?", ["de luchtweerstand", "hava direnci"], [["de zwaartekracht", "yer çekimi"], ["magnetisme", "manyetizma"], ["de wind van opzij", "yandan esen rüzgâr"]],
      "De grote parachute moet veel lucht opzij duwen. Die lucht duwt terug: luchtweerstand.", "Büyük paraşüt çok havayı kenara itmek zorundadır. Hava da geri iter: hava direnci."),
    MC("Waarom buigt een wielrenner zich diep over het stuur?", "Bisiklet yarışçısı neden gidonun üzerine iyice eğilir?", ["zo vangt hij minder wind en is de luchtweerstand kleiner", "böylece daha az rüzgâr alır, hava direnci azalır"], [["zo wordt hij zwaarder", "böylece ağırlaşır"], ["zo ziet hij de weg beter", "yolu daha iyi görür"], ["zo is er meer wrijving met de weg", "yolla sürtünme artar"]],
      "Hoe kleiner je voorkant, hoe minder lucht je opzij hoeft te duwen.", "Ön yüzün ne kadar küçükse o kadar az havayı itmen gerekir.")
  ]
];

// ----- Geluid
N_GEN.geluid = [
  [
    MC("Hoe ontstaat geluid?", "Ses nasıl oluşur?", ["doordat iets trilt", "bir şeyin titreşmesiyle"], [["doordat iets warm wordt", "bir şeyin ısınmasıyla"], ["doordat licht weerkaatst", "ışığın yansımasıyla"], ["doordat lucht stilstaat", "havanın durmasıyla"]],
      "Een snaar, een trommelvel of je stembanden trillen. De lucht eromheen trilt mee en zo bereikt het geluid je oor.", "Bir tel, davul derisi ya da ses tellerin titreşir. Çevredeki hava da titreşir ve ses kulağına ulaşır."),
    MC("Kan geluid door de lege ruimte (zonder lucht) reizen?", "Ses boşlukta (havasız ortamda) yayılabilir mi?", ["nee, geluid heeft een stof nodig om doorheen te gaan", "hayır, sesin yayılması için bir madde gerekir"], [["ja, net als licht", "evet, ışık gibi"], ["ja, maar langzamer", "evet, ama daha yavaş"], ["alleen overdag", "sadece gündüz"]],
      "Geluid gaat door lucht, water of hout, maar niet door het niets. In de ruimte is het daarom doodstil.", "Ses havada, suda ya da tahtada yayılır ama boşlukta yayılmaz. Bu yüzden uzay tamamen sessizdir."),
    MC("Je spant een gitaarsnaar strakker aan. Wat gebeurt er met de toon?", "Gitar telini gerersen sese ne olur?", ["de toon wordt hoger", "ses incelir"], [["de toon wordt lager", "ses kalınlaşır"], ["de toon wordt zachter", "ses kısılır"], ["er verandert niets", "hiçbir şey değişmez"]],
      "Een strakke snaar trilt sneller. Sneller trillen geeft een hogere toon.", "Gergin tel daha hızlı titreşir. Hızlı titreşim daha ince ses verir.")
  ],
  [
    MC("Waarin gaat geluid het snelst?", "Ses hangisinde en hızlı yayılır?", ["in ijzer", "demirde"], [["in lucht", "havada"], ["in water", "suda"], ["overal even snel", "hepsinde aynı"]],
      "In lucht ongeveer 340 meter per seconde, in water ruim 4 keer zo snel, in ijzer nog veel sneller. Leg je oor op een rail en je hoort de trein eerder.", "Havada saniyede yaklaşık 340 metre, suda 4 kattan fazla, demirde çok daha hızlı. Kulağını raya dayarsan treni daha erken duyarsın."),
    MC("Wat is een echo?", "Yankı nedir?", ["geluid dat terugkaatst tegen een wand of berg", "bir duvara ya da dağa çarpıp geri dönen ses"], [["geluid dat steeds harder wordt", "gittikçe yükselen ses"], ["twee mensen die tegelijk roepen", "aynı anda bağıran iki kişi"], ["geluid onder water", "su altındaki ses"]],
      "Geluid kaatst terug, net als licht in een spiegel. Je hoort jezelf iets later nog een keer.", "Ses, aynadaki ışık gibi geri yansır. Kendi sesini biraz sonra bir daha duyarsın."),
    MC("Welk geluid heeft de hoogste toon?", "Hangisinin sesi en incedir?", ["een fluitje", "düdük"], [["een grote trom", "büyük davul"], ["een brommer", "motosiklet"], ["een scheepshoorn", "gemi düdüğü"]],
      "Kleine, dunne dingen trillen snel en klinken hoog. Grote dingen trillen langzaam en klinken laag.", "Küçük, ince şeyler hızlı titreşir ve ince ses verir. Büyük şeyler yavaş titreşir ve kalın ses verir."),
    () => { const t = ri(2, 8); return Q(`Geluid gaat in lucht ongeveer 340 meter per seconde. Je hoort de donder ${t} seconden na de bliksem. Hoe ver weg is het onweer?`, `Ses havada saniyede yaklaşık 340 metre yol alır. Gök gürültüsünü şimşekten ${t} saniye sonra duyuyorsun. Fırtına ne kadar uzakta?`, 340 * t, "m", `${t} × 340 = ${340 * t} meter.`, `${t} × 340 = ${340 * t} metre.`); }
  ],
  [
    () => { const t = pick([2, 4, 6]); return Q(`Je roept naar een bergwand en hoort de echo na ${t} seconden. Geluid gaat 340 meter per seconde. Hoe ver weg is de bergwand? (Het geluid gaat heen én terug.)`, `Bir kayalığa doğru bağırıyorsun ve yankıyı ${t} saniye sonra duyuyorsun. Ses saniyede 340 metre yol alır. Kayalık ne kadar uzakta? (Ses gidiyor ve geri dönüyor.)`, 170 * t, "m",
      `In ${t} seconden legt het geluid ${340 * t} m af. Dat is heen en terug, dus de wand staat op ${170 * t} m.`, `Ses ${t} saniyede ${340 * t} m yol alır. Bu gidiş dönüştür, yani kayalık ${170 * t} m uzakta.`); },
    MC("Hoe vindt een vleermuis in het donker zijn weg?", "Yarasa karanlıkta yolunu nasıl bulur?", ["hij maakt hoge geluiden en luistert naar de echo", "ince sesler çıkarır ve yankıyı dinler"], [["hij ziet warmte", "ısıyı görür"], ["hij ruikt de muren", "duvarların kokusunu alır"], ["hij onthoudt de weg", "yolu ezberler"]],
      "De echo vertelt hem waar een muur of een insect is. Schepen meten zo de diepte van de zee: sonar.", "Yankı ona duvarın ya da böceğin nerede olduğunu söyler. Gemiler denizin derinliğini böyle ölçer: sonar."),
    MC("Hoe hard geluid is, meet je in decibel. Welk geluid kan je oren beschadigen?", "Sesin şiddeti desibelle ölçülür. Hangi ses kulaklarına zarar verebilir?", ["heel harde muziek door een koptelefoon, lange tijd", "uzun süre kulaklıkla çok yüksek sesli müzik"], [["fluisteren", "fısıltı"], ["een gewoon gesprek", "normal bir konuşma"], ["regen op het raam", "cama vuran yağmur"]],
      "Boven ongeveer 80 decibel kan lang luisteren je gehoor beschadigen. Die schade gaat niet meer over.", "Yaklaşık 80 desibelin üzerinde uzun süre dinlemek işitmeye zarar verebilir. Bu hasar geri dönmez."),
    () => { const d = ri(2, 6) * 1500; return Q(`Een schip stuurt een geluidssignaal naar de zeebodem. In water gaat geluid 1500 meter per seconde. De zee is ${d / 2} meter diep. Na hoeveel seconden komt de echo terug?`, `Bir gemi deniz dibine ses sinyali gönderiyor. Ses suda saniyede 1500 metre yol alır. Deniz ${d / 2} metre derinliğinde. Yankı kaç saniye sonra geri döner?`, d / 1500, "seconden",
      `Heen en terug is ${d} meter. ${d} : 1500 = ${d / 1500} seconden.`, `Gidiş dönüş ${d} metre. ${d} : 1500 = ${d / 1500} saniye.`); }
  ]
];

// ----- Vast, vloeibaar en gas
N_GEN.fasen = [
  [
    MC("Water kan in drie vormen voorkomen. Welke?", "Su üç halde bulunabilir. Hangileri?", ["ijs, water en waterdamp", "buz, su ve su buharı"], [["ijs, sneeuw en hagel", "buz, kar ve dolu"], ["water, regen en mist", "su, yağmur ve sis"], ["warm, lauw en koud", "sıcak, ılık ve soğuk"]],
      "Vast (ijs), vloeibaar (water) en gas (waterdamp). Het is steeds dezelfde stof.", "Katı (buz), sıvı (su) ve gaz (su buharı). Hep aynı maddedir."),
    MC("Bij welke temperatuur bevriest water?", "Su kaç derecede donar?", ["0 graden", "0 derece"], [["10 graden", "10 derece"], ["100 graden", "100 derece"], ["−10 graden", "−10 derece"]],
      "Bij 0 °C wordt water ijs, en ijs smelt bij 0 °C weer tot water.", "0 °C'de su buza dönüşür, buz da 0 °C'de eriyip tekrar su olur."),
    MC("Bij welke temperatuur kookt water?", "Su kaç derecede kaynar?", ["100 graden", "100 derece"], [["50 graden", "50 derece"], ["0 graden", "0 derece"], ["1000 graden", "1000 derece"]],
      "Bij 100 °C kookt water en wordt het waterdamp.", "100 °C'de su kaynar ve su buharına dönüşür."),
    MC("Hoe heet het als een vaste stof vloeibaar wordt?", "Katı bir maddenin sıvı hale geçmesine ne denir?", ["smelten", "erime"], [["stollen", "donma"], ["verdampen", "buharlaşma"], ["condenseren", "yoğuşma"]],
      "IJs smelt tot water, chocola smelt in je hand.", "Buz eriyip su olur, çikolata elinde erir.")
  ],
  [
    MC("De was hangt buiten en wordt droog. Waar blijft het water?", "Çamaşır dışarıda asılı ve kuruyor. Su nereye gidiyor?", ["het verdampt en gaat als waterdamp de lucht in", "buharlaşır ve su buharı olarak havaya karışır"], [["het zakt in de stof", "kumaşın içine çekilir"], ["het verdwijnt helemaal", "tamamen yok olur"], ["het valt op de grond", "yere düşer"]],
      "Water verdampt ook zonder te koken, alleen langzamer. Wind en zon helpen.", "Su kaynamadan da buharlaşır, sadece daha yavaş. Rüzgâr ve güneş yardım eder."),
    MC("Na het douchen is de spiegel beslagen. Hoe komt dat?", "Duştan sonra ayna buğulanır. Neden?", ["waterdamp koelt af tegen de koude spiegel en wordt weer druppels", "su buharı soğuk aynada soğuyup tekrar damlaya dönüşür"], [["de spiegel zweet", "ayna terler"], ["er spat water tegen de spiegel", "aynaya su sıçrar"], ["de spiegel smelt een beetje", "ayna biraz erir"]],
      "Dat heet condenseren: gas wordt weer vloeistof. Zo ontstaan ook wolken en dauw.", "Buna yoğuşma denir: gaz tekrar sıvıya dönüşür. Bulutlar ve çiy de böyle oluşur."),
    MC("Je vult een glazen fles helemaal met water en legt hem in de vriezer. Wat kan er gebeuren?", "Cam bir şişeyi ağzına kadar suyla doldurup dondurucuya koyuyorsun. Ne olabilir?", ["de fles barst, want ijs neemt meer ruimte in dan water", "şişe çatlar, çünkü buz sudan daha fazla yer kaplar"], [["de fles wordt kleiner", "şişe küçülür"], ["het water verdwijnt", "su yok olur"], ["er gebeurt niets", "hiçbir şey olmaz"]],
      "Water zet uit als het bevriest. Daarom drijft ijs ook: het is lichter dan evenveel water.", "Su donarken genleşir. Buz bu yüzden yüzer de: aynı hacimdeki sudan hafiftir."),
    MC("In welke vorm zitten de deeltjes het dichtst op elkaar en bewegen ze het minst?", "Parçacıklar hangi halde birbirine en yakın durur ve en az hareket eder?", ["in een vaste stof", "katı halde"], [["in een vloeistof", "sıvı halde"], ["in een gas", "gaz halde"], ["overal hetzelfde", "hepsinde aynı"]],
      "In een vaste stof trillen de deeltjes op hun plaats. In een gas vliegen ze vrij rond.", "Katıda parçacıklar yerlerinde titreşir. Gazda serbestçe uçuşurlar.")
  ],
  [
    () => { const a = ri(3, 12), b = ri(4, 15); return Q(`Het is ${a} graden. In de nacht daalt de temperatuur ${a + b} graden. Hoeveel graden <b>onder nul</b> is het dan?`, `Hava ${a} derece. Gece sıcaklık ${a + b} derece düşüyor. Sıcaklık sıfırın <b>kaç derece altına</b> iner?`, b, "graden", `${a} − ${a + b} = −${b}. Dat is ${b} graden onder nul: het vriest.`, `${a} − ${a + b} = −${b}. Sıfırın ${b} derece altı: don var.`); },
    () => { const s = ri(15, 25), r = pick([5, 10, 15]), t = Math.ceil((100 - s) / r); const s2 = 100 - t * r; return Q(`Een pan water is ${s2} graden. Op het vuur wordt het water elke minuut ${r} graden warmer. Na hoeveel minuten kookt het?`, `Bir tenceredeki su ${s2} derece. Ocakta su her dakika ${r} derece ısınıyor. Kaç dakika sonra kaynar?`, t, "minuten", `Tot 100 graden is het nog ${100 - s2} graden. ${100 - s2} : ${r} = ${t} minuten.`, `100 dereceye ${100 - s2} derece var. ${100 - s2} : ${r} = ${t} dakika.`); },
    MC("Waarom strooit men in de winter zout op de weg?", "Kışın yollara neden tuz dökülür?", ["zout water bevriest pas bij een lagere temperatuur", "tuzlu su daha düşük sıcaklıkta donar"], [["zout maakt de weg warmer", "tuz yolu ısıtır"], ["zout maakt de weg ruwer", "tuz yolu pürüzlü yapar"], ["zout droogt het water op", "tuz suyu kurutur"]],
      "Gewoon water bevriest bij 0 °C. Met zout erin blijft het ook onder nul nog vloeibaar.", "Normal su 0 °C'de donar. İçinde tuz olunca sıfırın altında da sıvı kalır."),
    MC("Hoe ontstaat regen?", "Yağmur nasıl oluşur?", ["water verdampt, koelt hoog in de lucht af tot druppels en valt weer naar beneden", "su buharlaşır, yükseklerde soğuyup damlalara dönüşür ve tekrar yere düşer"], [["wolken zijn zakken vol water die openscheuren", "bulutlar su dolu torbalardır ve yırtılır"], ["de zee spat omhoog", "deniz yukarı sıçrar"], ["de wind blaast water uit de rivieren", "rüzgâr nehirlerden su üfler"]],
      "Dit is de waterkringloop: verdampen, condenseren tot wolken, regenen, en via rivieren terug naar zee.", "Bu su döngüsüdür: buharlaşma, bulut olarak yoğuşma, yağış ve nehirlerle tekrar denize dönüş.")
  ]
];

// ----- Het zonnestelsel
const PLANETS = ["Mercurius", "Venus", "Aarde", "Mars", "Jupiter", "Saturnus", "Uranus", "Neptunus"];
const PLANETS_TR = ["Merkür", "Venüs", "Dünya", "Mars", "Jüpiter", "Satürn", "Uranüs", "Neptün"];
N_GEN.zonnestelsel = [
  [
    () => Q("Hoeveel planeten heeft ons zonnestelsel?", "Güneş sistemimizde kaç gezegen vardır?", 8, "", `Acht: ${PLANETS.join(", ")}.`, `Sekiz: ${PLANETS_TR.join(", ")}.`),
    MC("Wat is de zon?", "Güneş nedir?", ["een ster", "bir yıldız"], [["een planeet", "bir gezegen"], ["een maan", "bir uydu"], ["een komeet", "bir kuyruklu yıldız"]],
      "De zon is een ster: een enorme bol heet gas die zelf licht geeft. Alle andere sterren zijn ook zonnen, maar veel verder weg.", "Güneş bir yıldızdır: kendi ışığını veren, sıcak gazdan oluşan dev bir küre. Diğer bütün yıldızlar da birer güneştir ama çok daha uzaktadır."),
    MC("Waardoor is het dag en nacht?", "Gece ve gündüz neden olur?", ["de aarde draait om haar eigen as", "Dünya kendi ekseni etrafında döner"], [["de zon draait om de aarde", "Güneş Dünya'nın etrafında döner"], ["de maan schuift voor de zon", "Ay Güneş'in önüne geçer"], ["de zon gaat 's nachts uit", "Güneş gece söner"]],
      "De aarde draait in 24 uur één keer rond. De kant die naar de zon is gekeerd heeft dag.", "Dünya 24 saatte bir kez döner. Güneş'e bakan tarafta gündüz olur."),
    () => { const i = ri(0, 6), others = PLANETS.map((p, k) => k).filter(k => k !== i + 1).sort(() => Math.random() - 0.5).slice(0, 3);
      return Q(`De planeten op volgorde vanaf de zon: ${PLANETS.slice(0, i + 1).join(", ")}, … Welke planeet komt daarna?`, `Gezegenler Güneş'ten uzaklık sırasıyla: ${PLANETS_TR.slice(0, i + 1).join(", ")}, … Sıradaki gezegen hangisi?`, PLANETS[i + 1], "", `De volgorde: ${PLANETS.join(", ")}.`, `Sıra: ${PLANETS_TR.join(", ")}.`,
        { opts: [i + 1, ...others].sort(() => Math.random() - 0.5).map(k => ({ v: PLANETS[k], nl: PLANETS[k], tr: PLANETS_TR[k] })) }); }
  ],
  [
    MC("Hoe lang doet de aarde over één rondje om de zon?", "Dünya'nın Güneş etrafında bir tur atması ne kadar sürer?", ["een jaar", "bir yıl"], [["een dag", "bir gün"], ["een maand", "bir ay"], ["een week", "bir hafta"]],
      "Eén rondje om de zon duurt ongeveer 365 dagen: een jaar.", "Güneş etrafında bir tur yaklaşık 365 gün sürer: bir yıl."),
    MC("Waardoor hebben we zomer en winter?", "Yaz ve kış neden olur?", ["de as van de aarde staat scheef", "Dünya'nın ekseni eğiktir"], [["in de zomer staat de aarde dichter bij de zon", "yazın Dünya Güneş'e daha yakındır"], ["de zon brandt in de zomer harder", "Güneş yazın daha güçlü yanar"], ["de wolken houden in de winter de warmte tegen", "bulutlar kışın ısıyı engeller"]],
      "Door de scheve as krijgt het noorden in juni meer en langer zonlicht dan in december. De afstand tot de zon is niet de oorzaak.", "Eğik eksen yüzünden kuzey yarım küre haziranda aralığa göre daha çok ve daha uzun süre güneş alır. Nedeni Güneş'e uzaklık değildir."),
    MC("Waarom zien we de maan soms rond en soms als een sikkel?", "Ay'ı neden bazen yuvarlak, bazen hilal şeklinde görürüz?", ["we zien steeds een ander deel van de verlichte helft", "aydınlık yarısının her seferinde farklı bir kısmını görürüz"], [["de maan wordt echt kleiner en groter", "Ay gerçekten küçülüp büyür"], ["de aarde staat ervoor", "Dünya önüne geçer"], ["wolken bedekken een stuk", "bulutlar bir kısmını örter"]],
      "De zon verlicht altijd de helft van de maan. De maan draait om de aarde, dus wij kijken er steeds anders tegenaan.", "Güneş her zaman Ay'ın yarısını aydınlatır. Ay Dünya'nın etrafında döndüğü için ona her seferinde farklı açıdan bakarız."),
    MC("Welke planeet is het grootst?", "En büyük gezegen hangisidir?", ["Jupiter", "Jüpiter"], [["Aarde", "Dünya"], ["Saturnus", "Satürn"], ["Mars", "Mars"]],
      "Jupiter is zo groot dat de aarde er meer dan duizend keer in past.", "Jüpiter o kadar büyüktür ki içine binden fazla Dünya sığar.")
  ],
  [
    () => { const n = ri(2, 9); return Q(`De aarde draait in 24 uur één keer om haar as. Hoeveel uur duurt het voordat ze ${n} keer is rondgedraaid?`, `Dünya kendi ekseni etrafında 24 saatte bir kez döner. ${n} kez dönmesi kaç saat sürer?`, 24 * n, "uur", `${n} × 24 = ${24 * n} uur (${n} dagen).`, `${n} × 24 = ${24 * n} saat (${n} gün).`); },
    () => { const m = ri(2, 6) * 6; return Q(`Op de maan weegt alles 6 keer zo weinig als op aarde. Een rugzak weegt op aarde ${m} kg op de weegschaal. Wat geeft de weegschaal op de maan aan?`, `Ay'da her şey Dünya'dakinin 6'da biri kadar ağırlıktadır. Bir sırt çantası Dünya'da tartıda ${m} kg geliyor. Tartı Ay'da kaç kg gösterir?`, m / 6, "kg", `${m} : 6 = ${m / 6}.`, `${m} : 6 = ${m / 6}.`); },
    () => { return Q(`Licht van de zon doet er ongeveer 8 minuten over om de aarde te bereiken. Mars staat verder weg: daar doet het licht ongeveer 13 minuten over. Hoeveel minuten langer is het licht onderweg naar Mars?`, `Güneş ışığının Dünya'ya ulaşması yaklaşık 8 dakika sürer. Mars daha uzaktadır: ışık oraya yaklaşık 13 dakikada ulaşır. Işık Mars'a kaç dakika daha geç ulaşır?`, 5, "minuten", "13 − 8 = 5 minuten.", "13 − 8 = 5 dakika."); },
    MC("Waarom valt de maan niet weg van de aarde?", "Ay neden Dünya'dan uzaklaşıp gitmez?", ["de zwaartekracht van de aarde houdt haar in een baan", "Dünya'nın yer çekimi onu yörüngede tutar"], [["de maan zit vast aan de aarde", "Ay Dünya'ya bağlıdır"], ["de zon duwt de maan terug", "Güneş Ay'ı geri iter"], ["de maan is te licht om te bewegen", "Ay hareket edemeyecek kadar hafiftir"]],
      "De maan beweegt snel opzij en wordt tegelijk naar de aarde getrokken. Samen geeft dat een baan rond de aarde.", "Ay hızla yana doğru hareket eder ve aynı anda Dünya'ya doğru çekilir. İkisi birlikte Dünya çevresinde bir yörünge oluşturur.")
  ]
];

export const N_THEORY = {
  elektriciteit: [
    { nl: "<b>Wat is stroom?</b> Denk aan een kring van kinderen die een bal doorgeven. De batterij is het kind dat de bal steeds weer een duw geeft. De draad is de weg. Het lampje gaat branden als de bal erlangs komt. Is de kring ergens open, dan stopt alles.<br>Stroom kun je niet zien, maar wel wat hij doet: licht, warmte, beweging en geluid.",
      tr: "<b>Elektrik akımı nedir?</b> Topu birbirine paslayan, halka olmuş çocukları düşün. Pil, topa durmadan itiş veren çocuktur. Kablo yoldur. Top ampulün yanından geçince ampul yanar. Halka bir yerden açılırsa her şey durur.<br>Akımı göremezsin ama yaptıklarını görürsün: ışık, ısı, hareket ve ses." },
    { fig: fig.circuit(), nl: "Stroom loopt alleen in een <b>gesloten stroomkring</b>: van de batterij, door de draad en het lampje, terug naar de batterij. Een <b>schakelaar</b> opent of sluit de kring.<br><b>Geleiders</b> laten stroom door (metalen zoals koper). <b>Isolatoren</b> houden stroom tegen (plastic, rubber, hout, glas).",
      tr: "Akım yalnızca <b>kapalı devrede</b> dolaşır: pilden kabloya ve ampule, oradan tekrar pile. <b>Anahtar</b> devreyi açar ya da kapatır.<br><b>İletkenler</b> akımı geçirir (bakır gibi metaller). <b>Yalıtkanlar</b> geçirmez (plastik, lastik, tahta, cam)." },
    { nl: "<b>Serie</b>: lampjes achter elkaar in één kring. Gaat er één kapot, dan gaan ze allemaal uit.<br><b>Parallel</b>: elk lampje heeft een eigen weg. Gaat er één kapot, dan blijft de rest branden. Zo is het thuis.",
      tr: "<b>Seri</b>: ampuller tek devrede art arda. Biri bozulursa hepsi söner.<br><b>Paralel</b>: her ampulün kendi yolu vardır. Biri bozulursa diğerleri yanar. Evde böyledir." },
    { eg: true, nl: "<b>Kerstlampjes</b>: bij oude slingers ging de hele slinger uit als één lampje stuk was. Die waren in serie geschakeld.<br><b>Stroomdraad</b>: het koper binnenin geleidt, het plastic eromheen beschermt jou.<br><b>Water en stroom</b>: nooit een apparaat gebruiken met natte handen of bij het bad. Water geleidt stroom, en jouw lichaam ook.",
      tr: "<b>Yılbaşı ışıkları</b>: eski süslerde bir ampul bozulunca bütün dizi sönerdi. Çünkü seri bağlıydılar.<br><b>Elektrik kablosu</b>: içindeki bakır iletir, dışındaki plastik seni korur.<br><b>Su ve elektrik</b>: ıslak elle ya da küvetin yanında asla cihaz kullanma. Su elektriği iletir, senin vücudun da." },
    { eg: true, nl: "<b>Ballonproefje</b>: wrijf een ballon over je haar. Je haren gaan rechtop staan en de ballon blijft aan de muur plakken. Dat is <b>statische elektriciteit</b>. Ook de kleine knetter als je je trui uittrekt is een piepkleine vonk. Bliksem is precies hetzelfde, alleen enorm groot.",
      tr: "<b>Balon deneyi</b>: bir balonu saçına sürt. Saçların dikilir ve balon duvara yapışır kalır. Bu <b>statik elektriktir</b>. Kazağını çıkarırken duyduğun çıtırtı da minicik bir kıvılcımdır. Şimşek de tamamen aynı şeydir, sadece dev boyutta." },
    { eg: true, nl: "<b>Waar komt de stroom thuis vandaan?</b> Uit een energiecentrale, een windmolen of zonnepanelen. Het reist door dikke kabels onder de grond naar jouw huis.<br><b>Batterij of stopcontact?</b> Een batterij heeft 1,5 volt: die kun je gewoon vastpakken. Het stopcontact heeft 230 volt: daar steek je nooit iets in behalve een stekker.",
      tr: "<b>Evdeki elektrik nereden gelir?</b> Bir elektrik santralinden, rüzgâr türbininden ya da güneş panellerinden. Toprağın altındaki kalın kablolarla evine kadar gelir.<br><b>Pil mi priz mi?</b> Pil 1,5 volttur: rahatça tutabilirsin. Priz 230 volttur: içine fişten başka asla bir şey sokulmaz." }
  ],
  magnetisme: [
    { fig: fig.magnet(), nl: "Een <b>magneet</b> trekt dingen van <b>ijzer</b> en <b>staal</b> aan: een paperclip, een spijker, de deur van de koelkast. Niet alles wat van metaal is: aluminium (blikjes) en koper niet. Plastic, hout, papier en glas ook niet.<br>Elke magneet heeft twee <b>polen</b>: een <b>noordpool (N)</b> en een <b>zuidpool (Z)</b>. Daar is de kracht het sterkst.",
      tr: "<b>Mıknatıs</b>, <b>demir</b> ve <b>çelikten</b> yapılmış şeyleri çeker: ataş, çivi, buzdolabının kapısı. Metal olan her şeyi değil: alüminyum (içecek kutuları) ve bakır çekilmez. Plastik, tahta, kâğıt ve cam da çekilmez.<br>Her mıknatısın iki <b>kutbu</b> vardır: <b>kuzey kutbu (N)</b> ve <b>güney kutbu</b> (Hollandacada Z, Türkçede S). Kuvvet en çok kutuplardadır." },
    { fig: fig.poles(true), nl: "<b>Gelijke polen stoten elkaar af</b>: noord tegen noord duwt weg.<br><b>Ongelijke polen trekken elkaar aan</b>: noord en zuid klikken vast.<br>Rond een magneet zit een onzichtbaar <b>magneetveld</b>. Het werkt door papier, glas en water heen, en hoe dichterbij, hoe sterker.",
      tr: "<b>Aynı kutuplar birbirini iter</b>: kuzey kuzeyi iter.<br><b>Farklı kutuplar birbirini çeker</b>: kuzey ile güney yapışır.<br>Mıknatısın etrafında görünmez bir <b>manyetik alan</b> vardır. Kâğıttan, camdan ve sudan geçer; ne kadar yakınsa o kadar güçlüdür." },
    { nl: "<b>De aarde is een grote magneet.</b> Daarom draait een kompasnaald (een klein magneetje) altijd naar het noorden.<br><b>Elektromagneet</b>: wikkel een draad om een spijker en sluit een batterij aan. Zolang er stroom loopt, is de spijker een magneet. Stroom uit: geen magneet meer. Meer wikkelingen maken hem sterker. Zo hangen <b>elektriciteit en magnetisme</b> samen.",
      tr: "<b>Dünya büyük bir mıknatıstır.</b> Bu yüzden pusula iğnesi (küçük bir mıknatıs) hep kuzeye döner.<br><b>Elektromıknatıs</b>: bir çivinin etrafına tel sar ve bir pile bağla. Akım geçtiği sürece çivi mıknatıstır. Akım kesilince artık mıknatıs değildir. Sarım arttıkça güçlenir. <b>Elektrik ile manyetizma</b> böyle birbirine bağlıdır." },
    { eg: true, nl: "<b>Om je heen</b>: koelkastmagneten, het deurtje van een keukenkastje dat dichtklikt, een magneetbord in de klas.<br><b>Schroothoop</b>: een kraan met een enorme elektromagneet tilt een hele auto op. Zet de kraanmachinist de stroom uit, dan valt de auto los.<br><b>Afval scheiden</b>: met een grote magneet haalt men stalen blikjes uit het afval; aluminium blijft liggen.<br><b>Luidspreker en koptelefoon</b>: daarin laat een magneet een vliesje trillen, en dat hoor je als geluid.",
      tr: "<b>Etrafında</b>: buzdolabı mıknatısları, kapanınca tık diye duran mutfak dolabı kapağı, sınıftaki mıknatıslı tahta.<br><b>Hurdalık</b>: dev bir elektromıknatısı olan vinç koca bir arabayı kaldırır. Vinç operatörü elektriği kesince araba düşer.<br><b>Çöp ayırma</b>: büyük bir mıknatısla çöpten çelik tenekeler ayıklanır; alüminyumlar yerinde kalır.<br><b>Hoparlör ve kulaklık</b>: içlerinde bir mıknatıs ince bir zarı titreştirir, sen bunu ses olarak duyarsın." },
    { eg: true, nl: "<b>Proefje: maak zelf een kompas.</b> Strijk een naald een paar keer met een magneet, steeds in dezelfde richting. Leg de naald op een plat kurkje in een bak water. De naald draait langzaam tot hij noord-zuid ligt.<br><b>Noorderlicht</b>: deeltjes van de zon worden door het magneetveld van de aarde naar de polen geleid. Daar laten ze de lucht gekleurd oplichten.",
      tr: "<b>Deney: kendi pusulanı yap.</b> Bir iğneyi bir mıknatısla, hep aynı yönde birkaç kez sürt. İğneyi su dolu bir kapta yassı bir mantar tıpanın üstüne koy. İğne yavaşça dönüp kuzey-güney yönünde durur.<br><b>Kuzey ışıkları</b>: Güneş'ten gelen parçacıklar Dünya'nın manyetik alanıyla kutuplara yönlendirilir. Orada havayı renkli renkli parlatırlar." }
  ],
  krachten: [
    { nl: "Een <b>kracht</b> is duwen of trekken. Een kracht kan iets in beweging brengen, afremmen, laten draaien of vervormen. Je meet kracht in <b>newton</b>.<br><b>Zwaartekracht</b> trekt alles naar de aarde. <b>Wrijving</b> remt alles af wat ergens langs schuurt. <b>Luchtweerstand</b> is wrijving met de lucht.",
      tr: "<b>Kuvvet</b>, itmek ya da çekmektir. Kuvvet bir cismi harekete geçirebilir, yavaşlatabilir, döndürebilir ya da şeklini değiştirebilir. Kuvvet <b>newton</b> ile ölçülür.<br><b>Yer çekimi</b> her şeyi Dünya'ya çeker. <b>Sürtünme</b>, bir yere sürtünen her şeyi yavaşlatır. <b>Hava direnci</b>, havayla sürtünmedir." },
    { fig: fig.wip("zwaar", "licht"), nl: "<b>Hefboom</b>: met een lange arm heb je weinig kracht nodig. Het gaat om <b>kracht × afstand tot het draaipunt</b>.<br>Op een wip is er evenwicht als gewicht × afstand aan beide kanten gelijk is. 40 kg op 1 meter houdt 20 kg op 2 meter in evenwicht.",
      tr: "<b>Kaldıraç</b>: uzun bir kolla az kuvvet yeter. Önemli olan <b>kuvvet × dönme noktasına uzaklıktır</b>.<br>Tahterevallide iki tarafta ağırlık × uzaklık eşitse denge olur. 1 metredeki 40 kg, 2 metredeki 20 kg'ı dengeler." },
    { eg: true, nl: "<b>Hefbomen om je heen</b>: een deurklink, een schaar, een flesopener, een kruiwagen, de trappers van je fiets. Probeer een deur open te duwen vlak bij de scharnieren: dat gaat veel zwaarder.<br><b>Voetbal</b>: op nat gras glijd je sneller uit: minder wrijving. Daarom hebben voetbalschoenen noppen.",
      tr: "<b>Çevrendeki kaldıraçlar</b>: kapı kolu, makas, şişe açacağı, el arabası, bisikletinin pedalları. Bir kapıyı menteşelerin hemen yanından itmeyi dene: çok daha zordur.<br><b>Futbol</b>: ıslak çimde daha kolay kayarsın: sürtünme azalır. Krampon bu yüzden dişlidir." }
  ],
  geluid: [
    { nl: "<b>Geluid</b> ontstaat doordat iets <b>trilt</b>. De lucht trilt mee en brengt het geluid naar je oor.<br>Snel trillen = <b>hoge</b> toon, langzaam trillen = <b>lage</b> toon. Grote trillingen = <b>hard</b>, kleine = zacht.<br>Geluid gaat in lucht ongeveer 340 meter per seconde. Het heeft een stof nodig: in de lege ruimte is het stil.",
      tr: "<b>Ses</b>, bir şeyin <b>titreşmesiyle</b> oluşur. Hava da titreşir ve sesi kulağına taşır.<br>Hızlı titreşim = <b>ince</b> ses, yavaş titreşim = <b>kalın</b> ses. Büyük titreşim = <b>yüksek</b> ses, küçük titreşim = alçak ses.<br>Ses havada saniyede yaklaşık 340 metre yol alır. Yayılması için madde gerekir: boşlukta ses yoktur." },
    { eg: true, nl: "<b>Voel het zelf</b>: leg je vingers op je keel en zeg 'aaa'. Je voelt je stembanden trillen.<br><b>Onweer</b>: tel de seconden tussen bliksem en donder. Elke 3 seconden is ongeveer 1 kilometer.<br><b>Echo</b>: roep in een tunnel of naar een bergwand en het geluid kaatst terug. Vleermuizen en schepen gebruiken dat om te 'zien'.",
      tr: "<b>Kendin hisset</b>: parmaklarını boğazına koy ve 'aaa' de. Ses tellerinin titrediğini hissedersin.<br><b>Fırtına</b>: şimşek ile gök gürültüsü arasındaki saniyeleri say. Her 3 saniye yaklaşık 1 kilometredir.<br><b>Yankı</b>: bir tünelde ya da kayalığa doğru bağır, ses geri döner. Yarasalar ve gemiler bunu 'görmek' için kullanır." }
  ],
  fasen: [
    { nl: "Stoffen kunnen <b>vast</b>, <b>vloeibaar</b> of <b>gas</b> zijn. Bij water: ijs, water, waterdamp.<br>vast → vloeibaar: <b>smelten</b> (0 °C) &nbsp; vloeibaar → vast: <b>stollen / bevriezen</b><br>vloeibaar → gas: <b>verdampen</b> (water kookt bij 100 °C) &nbsp; gas → vloeibaar: <b>condenseren</b><br>Het blijft dezelfde stof: alleen de deeltjes bewegen sneller of langzamer.",
      tr: "Maddeler <b>katı</b>, <b>sıvı</b> ya da <b>gaz</b> halde olabilir. Suda: buz, su, su buharı.<br>katı → sıvı: <b>erime</b> (0 °C) &nbsp; sıvı → katı: <b>donma</b><br>sıvı → gaz: <b>buharlaşma</b> (su 100 °C'de kaynar) &nbsp; gaz → sıvı: <b>yoğuşma</b><br>Madde aynı kalır: sadece parçacıklar daha hızlı ya da daha yavaş hareket eder." },
    { eg: true, nl: "<b>Beslagen spiegel</b>: na het douchen condenseert waterdamp op het koude glas.<br><b>De was</b> droogt doordat het water verdampt, ook zonder dat het kookt.<br><b>Strooizout</b>: zout water bevriest pas onder nul, daarom strooit men zout op gladde wegen.<br><b>Regen</b>: zeewater verdampt, wordt hoog in de lucht wolk en valt als regen terug. Dat is de waterkringloop.",
      tr: "<b>Buğulanan ayna</b>: duştan sonra su buharı soğuk camda yoğuşur.<br><b>Çamaşır</b>, su kaynamadan da buharlaştığı için kurur.<br><b>Yol tuzu</b>: tuzlu su ancak sıfırın altında donar, bu yüzden buzlu yollara tuz dökülür.<br><b>Yağmur</b>: deniz suyu buharlaşır, yükseklerde bulut olur ve yağmur olarak geri düşer. Bu su döngüsüdür." }
  ],
  zonnestelsel: [
    { nl: "De <b>zon</b> is een ster. Er draaien <b>8 planeten</b> omheen: Mercurius, Venus, Aarde, Mars, Jupiter, Saturnus, Uranus, Neptunus.<br><b>Dag en nacht</b>: de aarde draait in 24 uur om haar as.<br><b>Jaar</b>: de aarde draait in ongeveer 365 dagen om de zon.<br><b>Seizoenen</b>: de as van de aarde staat scheef. Niet de afstand tot de zon, maar de stand bepaalt of het zomer of winter is.",
      tr: "<b>Güneş</b> bir yıldızdır. Etrafında <b>8 gezegen</b> döner: Merkür, Venüs, Dünya, Mars, Jüpiter, Satürn, Uranüs, Neptün.<br><b>Gece ve gündüz</b>: Dünya 24 saatte kendi ekseni etrafında döner.<br><b>Yıl</b>: Dünya yaklaşık 365 günde Güneş'in etrafında döner.<br><b>Mevsimler</b>: Dünya'nın ekseni eğiktir. Yaz ya da kış olmasını Güneş'e uzaklık değil, bu eğiklik belirler." },
    { eg: true, nl: "<b>Hoe groot?</b> Stel dat de zon een voetbal is. Dan is de aarde een peperkorrel op ongeveer 25 meter afstand, en Jupiter een knikker op ruim 100 meter.<br><b>De maan</b> geeft zelf geen licht. Je ziet het stuk waar de zon op schijnt; daarom verandert de vorm elke nacht een beetje.<br><b>Zomer en winter</b>: in december is het in Nederland winter en in Australië zomer, op dezelfde dag.",
      tr: "<b>Ne kadar büyük?</b> Güneş bir futbol topu olsaydı Dünya yaklaşık 25 metre uzakta bir karabiber tanesi, Jüpiter de 100 metreden uzakta bir bilye olurdu.<br><b>Ay</b> kendi ışığını vermez. Güneş'in aydınlattığı kısmını görürsün; şekli bu yüzden her gece biraz değişir.<br><b>Yaz ve kış</b>: aralık ayında Hollanda'da kış, Avustralya'da yazdır; aynı gün." }
  ]
};

export const N_WORDS = {
  elektriciteit: [["stroom", "akım / elektrik"], ["stroomkring", "devre"], ["batterij", "pil"], ["draad", "kablo"], ["schakelaar", "anahtar"], ["geleider", "iletken"], ["isolator", "yalıtkan"], ["lampje", "ampul"], ["statische elektriciteit", "statik elektrik"], ["stopcontact", "priz"], ["stekker", "fiş"], ["spanning (volt)", "gerilim (volt)"]],
  magnetisme: [["magneet", "mıknatıs"], ["aantrekken", "çekmek"], ["afstoten", "itmek"], ["noordpool", "kuzey kutbu"], ["zuidpool", "güney kutbu"], ["magneetveld", "manyetik alan"], ["kompas", "pusula"], ["elektromagneet", "elektromıknatıs"], ["ijzer / staal", "demir / çelik"]],
  krachten: [["kracht", "kuvvet"], ["duwen", "itmek"], ["trekken", "çekmek"], ["wrijving", "sürtünme"], ["zwaartekracht", "yer çekimi"], ["hefboom", "kaldıraç"], ["wip", "tahterevalli"], ["evenwicht", "denge"], ["luchtweerstand", "hava direnci"]],
  geluid: [["geluid", "ses"], ["trillen", "titreşmek"], ["hoge toon", "ince ses"], ["lage toon", "kalın ses"], ["hard", "yüksek sesli"], ["zacht", "alçak sesli"], ["echo", "yankı"], ["snaar", "tel"]],
  fasen: [["vast", "katı"], ["vloeibaar", "sıvı"], ["gas", "gaz"], ["smelten", "erimek"], ["bevriezen", "donmak"], ["verdampen", "buharlaşmak"], ["condenseren", "yoğuşmak"], ["koken", "kaynamak"], ["waterdamp", "su buharı"]],
  zonnestelsel: [["zon", "Güneş"], ["ster", "yıldız"], ["planeet", "gezegen"], ["maan", "Ay"], ["aarde", "Dünya"], ["as", "eksen"], ["baan", "yörünge"], ["seizoen", "mevsim"]]
};
