"""Item 5: Een wolf, wat nu? (Vragen van kinderen)
Written only from the transcript the user provided. The transcript is automatic speech recognition:
obvious mistakes are read as 'de Veluwe' (not 'de Vel') and 'wandelen' (not 'bandelen').
The child's name is not clear in the transcript, so it is not used.
"""

ITEM = {
    "id": "wolf",
    "nr": 5,
    "titel": "Een wolf, wat nu?",
    "bron": "Vragen van kinderen",
    "video_url": "https://www.youtube.com/watch?v=LWcRrDyoQCg",
    "afbeelding_url": "https://i.ytimg.com/vi/LWcRrDyoQCg/hqdefault.jpg",
    "niveau_video": "B1",
    "niveau_uitleg": "Çocuklar için bir program, ama doğal ve hızlı bir konuşma var: 'nou', 'eh', 'hartstikke', 'wegwezen' gibi günlük dil ve yarım cümleler. Tavsiyeler basit (A2), konuşmanın kendisi B1.",

    # A0: absolute beginner – very short present-tense sentences, only the most common words
    "a0": """Dit is een <strong>wolf</strong>. Een wolf woont in het <strong>bos</strong>.

Een wolf kan <strong>bijten</strong>.

Zie je een wolf? Ren niet weg! Blijf staan. Kijk boos. Zeg: 'Weg!'

Loop met een groep.""",
    "gloss_a0": "de wolf = kurt • wonen = yaşamak • het bos = orman • bijten = ısırmak • zien = görmek • wegrennen = kaçmak • blijven staan = olduğu yerde durmak • kijken = bakmak • boos = kızgın • weg! = git! • lopen = yürümek • de groep = grup",

    "a1": """Een kind wandelt graag in het <strong>bos</strong>. Het kind vraagt: 'Wat moet ik doen als ik een <strong>wolf</strong> zie?'

In Nederland wonen weer wolven. Ze wonen in een groep.

Expert Diederik geeft tips. Ren niet weg! Dan rent de wolf achter je aan. Een wolf kan <strong>bijten</strong>.

Blijf staan. Kijk de wolf boos aan. Doe een klein stapje terug. Zeg hard: '<strong>Wegwezen</strong>!'

Wandel liever met een groep. Dat vindt een wolf niet leuk.""",
    "gloss_a1": "wandelen = yürüyüş yapmak • het bos = orman • de wolf = kurt • wegrennen = kaçmak • achter je aan = peşinden • bijten = ısırmak • blijven staan = olduğu yerde durmak • boos = kızgın • het stapje = küçük adım • wegwezen! = defol!, git buradan!",

    "a2": """Een kind wandelt graag in het bos en vraagt: 'Wat moet ik doen als ik een wolf <strong>tegenkom</strong>?'

Wolven waren 150 jaar weg uit Nederland. Maar sinds 2015 leven ze weer in onze natuur. Wolven leven in een familiegroep: een <strong>roedel</strong>. Op de Veluwe wonen al zeven roedels. Je kunt dus echt een wolf tegenkomen.

Collega Ties speelt de wolf, met een masker op. Wat doe je? Veel mensen willen <strong>wegrennen</strong>, maar dat is juist fout. Een jonge wolf is <strong>nieuwsgierig</strong>. Hij rent dan achter je aan, net als een hond achter een stok.

Expert Diederik zegt: blijf staan en kijk de wolf boos aan. Doe ondertussen een stapje achteruit. Werkt dat niet? Maak jezelf groot, roep '<strong>Wegwezen</strong>!' en sla met een stok op de grond.

Wandelen in het bos is <strong>hartstikke</strong> leuk. Maar ga in een groep en hou je hond aan de lijn.""",
    "gloss_a2": "tegenkomen = karşılaşmak • de natuur = doğa • de roedel = (kurt) sürüsü • het masker = maske • wegrennen = koşarak kaçmak • juist = tam da, aksine • nieuwsgierig = meraklı • de stok = sopa • ondertussen = bu arada • achteruit = geriye • hartstikke = çok (günlük dil) • aan de lijn = tasmalı",

    "b1": """'Ik loop heel graag in het bos, maar wat moet ik doen als ik een wolf tegenkom?' Met die vraag gaan we naar de Veluwe.

Wolven zijn ongeveer 150 jaar weg geweest uit Nederland, maar sinds 2015 lopen ze weer rond in onze natuur. De wolf is het grootste <strong>roofdier</strong> dat we hier hebben. Wolven leven in een familiegroep, die we een roedel noemen. Omdat wetenschappers verwachten dat er steeds meer roedels komen, is <strong>de kans</strong> best <strong>aanwezig</strong> dat je er een keer een tegenkomt. Alleen al op de Veluwe leven zeven roedels.

Om te oefenen speelt collega Ties de wolf. Wie een wolf ziet, wil misschien het liefst wegrennen. Maar dat moet je juist niet doen, want dan gaat de wolf achter je aan, net als een spelende hond achter een stok. En een wolf is wel gevaarlijk: hij kan bijten.

Wat moet je dan wel doen? Volgens expert Diederik moet je blijven staan en de wolf boos aankijken. Ondertussen doe je een stapje achteruit. Zo laat je zien: ik <strong>hou je in de gaten</strong>, maar ga weg. Werkt dat niet, maak jezelf dan groot en sla met een stok op de grond.

Het belangrijkste is dat wolven leren dat mensen niet leuk zijn, zodat ze <strong>op afstand blijven</strong>.""",
    "gloss_b1": "rondlopen = dolaşmak • het roofdier = yırtıcı hayvan • de wetenschapper = bilim insanı • verwachten = beklemek • de kans is aanwezig = ihtimal var • alleen al = sadece … bile • oefenen = alıştırma yapmak • het liefst = en çok tercih ederek • aankijken = -e bakmak • iemand in de gaten houden = gözünü birinin üzerinden ayırmamak • op afstand blijven = uzak durmak",

    "b2": """Lange tijd was de wolf uit Nederland verdwenen, maar sinds 2015 <strong>struint</strong> het grootste roofdier van ons land weer door de natuur. Op de Veluwe leven inmiddels zeven roedels, en wetenschappers verwachten dat het er meer worden. Wie graag wandelt, vraagt zich dan ook terecht af: wat doe je als je <strong>oog in oog</strong> staat met een wolf?

In deze aflevering speelt collega Ties, verstopt achter een overtuigend masker, voor wolf. De eerste reflex – <strong>het hazenpad kiezen</strong> – blijkt precies verkeerd. Een jonge, nieuwsgierige wolf ziet een rennend mens namelijk als een spelletje, zoals een hond die achter een weggegooide stok aan rent. En ook al is het spel voor de wolf, hij kan wel degelijk bijten.

Expert Diederik adviseert daarom <strong>voet bij stuk te houden</strong>: blijf staan, kijk de wolf met een boze, <strong>dreigende</strong> blik aan en zet ondertussen langzaam een stap achteruit. Een dreigend gezicht vindt een wolf allesbehalve prettig. Helpt dat niet, maak jezelf dan zo groot mogelijk, roep 'wegwezen!' en sla met een stok op de grond.

Daarnaast raadt hij aan om in een groep te wandelen en de hond kort aan de lijn te houden. Uiteindelijk draait het erom dat wolven leren dat mensen niet interessant zijn en dat ze afstand houden.""",
    "gloss_b2": "struinen = gezinmek, dolaşmak • terecht = haklı olarak • oog in oog staan met = burun buruna gelmek • voor wolf spelen = kurt rolü yapmak • overtuigend = inandırıcı • het hazenpad kiezen = tabanları yağlamak, kaçmak • wel degelijk = gerçekten de • voet bij stuk houden = geri adım atmamak • dreigend = tehditkâr • allesbehalve = hiç de … değil • aanraden = tavsiye etmek • het draait erom dat = asıl mesele şu ki",

    "c1": """Ruim anderhalve eeuw was de wolf uit het Nederlandse landschap verdwenen; sinds 2015 is hij terug, en dat roept bij menig wandelaar de vraag op hoe je je gedraagt bij een onverwachte ontmoeting. Gezien het groeiende aantal roedels – op de Veluwe alleen al zeven – is dat geen theoretische kwestie.

Voor de demonstratie wordt collega Ties ingezet: geen <strong>wolf in schaapskleren</strong>, maar eerder een schaap in wolfskleren, en volgens de makers nauwelijks van echt te <strong>onderscheiden</strong>. De les die volgt, druist in tegen ieders instinct. Wegrennen is uit den boze: een vluchtend mens wekt bij een jonge, nieuwsgierige wolf juist de lust om erachteraan te gaan, zoals een weggeworpen stok een hond in beweging zet.

Het devies luidt daarom: blijf staan, <strong>geef geen krimp</strong> en kijk het dier strak en dreigend aan, terwijl je <strong>behoedzaam</strong> achteruit stapt. Volgens expert Diederik heeft een wolf een hekel aan zo'n dreigende blik en <strong>druipt</strong> hij vanzelf <strong>af</strong>. Blijft hij toch, dan is het zaak <strong>hem de stuipen op het lijf te jagen</strong>: maak jezelf groot, roep luidkeels 'wegwezen' en sla met een stok op de grond.

Op de langere termijn gaat het om iets fundamentelers: wolven moeten leren dat mensen oninteressant zijn, zodat ze uit zichzelf afstand bewaren.""",
    "gloss_c1": "anderhalve eeuw = bir buçuk asır • menig = birçok • gezien = göz önüne alındığında • een wolf in schaapskleren = kuzu postuna bürünmüş kurt • onderscheiden = ayırt etmek • indruisen tegen = -e ters düşmek • uit den boze zijn = kesinlikle yasak/yanlış olmak • het devies luidt = parola şu, kural şu • geen krimp geven = kılını kıpırdatmamak, yılmamak • behoedzaam = temkinli • afdruipen = sessizce sıvışmak • het is zaak = önemli olan … • iemand de stuipen op het lijf jagen = ödünü koparmak • luidkeels = avazı çıktığı kadar",

    "uitdrukkingen": [
        {"nl": "wegwezen!", "niveau": "A2", "tr": "git buradan!, defol!",
         "uitleg": "Günlük dilde sert ama kısa bir 'git!' komutu. Videoda kurdu kovmak için bağırılıyor. 'Ik ben weg' / 'wegwezen hier' = hadi gidelim, gibi de kullanılır.",
         "voorbeeld": "Wegwezen, jij! Dit is mijn plek.", "voorbeeld_tr": "Git buradan! Burası benim yerim."},
        {"nl": "hartstikke (leuk, goed …)", "niveau": "A2", "tr": "çok, son derece (günlük dil)",
         "uitleg": "'Heel' anlamında güçlendirici. Konuşma dilinde çok yaygın: hartstikke leuk, hartstikke druk, hartstikke bedankt.",
         "voorbeeld": "Bedankt voor je hulp, hartstikke lief!", "voorbeeld_tr": "Yardımın için teşekkürler, çok tatlısın!"},
        {"nl": "de kans is aanwezig", "niveau": "B1", "tr": "ihtimal var, olabilir",
         "uitleg": "'Er is een kans' demenin biraz daha resmî hali. Videoda: 'De kans is dus best aanwezig dat je een keer een wolf tegenkomt.'",
         "voorbeeld": "De kans is aanwezig dat het morgen sneeuwt.", "voorbeeld_tr": "Yarın kar yağma ihtimali var."},
        {"nl": "iemand in de gaten houden", "niveau": "B1", "tr": "birini gözden kaçırmamak, gözü üstünde olmak",
         "uitleg": "Birini ya da bir şeyi dikkatle izlemek. Videoda kurda söylenen mesaj: 'Ik hou je in de gaten, maar je moet wel wegwezen.'",
         "voorbeeld": "Kun jij de kinderen even in de gaten houden?", "voorbeeld_tr": "Çocuklara biraz göz kulak olabilir misin?"},
        {"nl": "op afstand blijven", "niveau": "B1", "tr": "uzak durmak, mesafeyi korumak",
         "uitleg": "Fiziksel olarak ya da mecazi anlamda birine çok yaklaşmamak. 'Afstand houden' da aynı anlamda.",
         "voorbeeld": "Blijf op afstand van de hond van de buren.", "voorbeeld_tr": "Komşunun köpeğinden uzak dur."},
        {"nl": "het hazenpad kiezen", "niveau": "B2", "tr": "tabanları yağlamak, kaçıp gitmek",
         "uitleg": "Tavşan gibi hızla kaçmak. Videodaki ana mesaj: kurt görünce tam da bunu yapmamalısın!",
         "voorbeeld": "Toen de politie kwam, koos de dief het hazenpad.", "voorbeeld_tr": "Polis gelince hırsız tabanları yağladı."},
        {"nl": "voet bij stuk houden", "niveau": "B2", "tr": "geri adım atmamak, direnmek",
         "uitleg": "Baskıya rağmen fikrini ya da yerini değiştirmemek. Kurt karşısında da hem mecazi hem gerçek anlamda: olduğun yerde kal.",
         "voorbeeld": "Ondanks alle kritiek hield de minister voet bij stuk.", "voorbeeld_tr": "Tüm eleştirilere rağmen bakan geri adım atmadı."},
        {"nl": "een wolf in schaapskleren", "niveau": "C1", "tr": "kuzu postuna bürünmüş kurt",
         "uitleg": "Zararsız görünen ama aslında tehlikeli olan kişi. C1 metninde ters çevriliyor: Ties maskeli olduğu için 'kurt kılığında bir koyun'.",
         "voorbeeld": "Pas op met die verkoper: het is een wolf in schaapskleren.", "voorbeeld_tr": "O satıcıya dikkat et: kuzu postuna bürünmüş bir kurt."},
        {"nl": "geen krimp geven", "niveau": "C1", "tr": "kılını kıpırdatmamak, yılmamak",
         "uitleg": "Zor bir durumda bile korku ya da acı göstermemek, pes etmemek.",
         "voorbeeld": "De keeper gaf geen krimp, ook niet na de harde botsing.", "voorbeeld_tr": "Kaleci sert çarpışmadan sonra bile yılmadı."},
        {"nl": "iemand de stuipen op het lijf jagen", "niveau": "C1", "tr": "birinin ödünü koparmak",
         "uitleg": "Birini çok korkutmak. 'De stuipen' = ani kasılmalar.",
         "voorbeeld": "Met dat masker jaag je de kinderen de stuipen op het lijf!", "voorbeeld_tr": "O maskeyle çocukların ödünü koparırsın!"},
    ],

    # woord | soort | betekenis (NL) | voorbeeld | Turks | niveau
    "woordenschat": """de wolf | zn | wild dier dat op een grote hond lijkt | In Nederland leven weer wolven. | kurt | A1
het bos | zn | gebied met veel bomen | We wandelen in het bos. | orman | A1
wandelen | ww | lopen voor je plezier | Op zondag wandelen we graag. | yürüyüş yapmak | A1
bijten | ww | met je tanden in iets happen | Pas op, die hond bijt! | ısırmak | A2
wegrennen | ww | snel weglopen | De kat rent weg voor de hond. | koşarak kaçmak | A2
nieuwsgierig | bn | je wilt alles weten of zien | Kinderen zijn heel nieuwsgierig. | meraklı | A2
gevaarlijk | bn | het kan pijn doen of schade geven | Deze weg is gevaarlijk. | tehlikeli | A2
tegenkomen | ww | iemand of iets onverwacht zien of ontmoeten | Ik kwam mijn buurman tegen in de stad. | rastlamak, karşılaşmak | B1
de roedel | zn | groep wolven (een familie) | Een roedel bestaat uit ouders en jongen. | (kurt) sürüsü | B1
het roofdier | zn | dier dat andere dieren vangt en eet | De wolf is een roofdier. | yırtıcı hayvan | B1
de wenkbrauw | zn | haartjes boven je oog | Ze trok haar wenkbrauwen omhoog. | kaş | B1
achteruit | bw | naar achteren | Doe een stap achteruit. | geriye doğru | B1
aan de lijn | uitdr | (van een hond) vast aan een riem | Honden moeten hier aan de lijn. | tasmalı | B1
de wetenschapper | zn | iemand die onderzoek doet | Wetenschappers bestuderen de wolf. | bilim insanı | B1
dreigend | bn | zo dat iemand bang wordt | Hij keek me dreigend aan. | tehditkâr | B2
oog in oog staan met | uitdr | heel dichtbij tegenover iemand of iets staan | Ineens stond ik oog in oog met een hert. | burun buruna gelmek | B2
struinen | ww | rustig rondlopen en rondkijken | We struinden over de markt. | gezinmek, dolaşmak | B2
onderscheiden | ww | het verschil zien | Ik kan de tweeling niet van elkaar onderscheiden. | ayırt etmek | C1
behoedzaam | bn | heel voorzichtig | Hij liep behoedzaam over het ijs. | temkinli | C1
afdruipen | ww | stil en een beetje beschaamd weggaan | Na de ruzie droop hij af. | sessizce sıvışmak | C1""",

    "grammatica": """1) De gebiedende wijs: een opdracht of advies geven
Je gebruikt de stam van het werkwoord (ik-vorm), zonder 'je'.
• Blijf staan!
• Kijk de wolf boos aan.
• Ren niet weg!
• Hou je hond aan de lijn.
2) Scheidbare werkwoorden: tegenkomen, wegrennen, aankijken, weggaan
In een gewone zin gaat het eerste deel naar het einde. In een bijzin en na een modaal werkwoord blijft het werkwoord heel.
• Ik kom een wolf tegen. → Als ik een wolf tegenkom, …
• De wolf rent weg. → Je moet niet wegrennen.
• Kijk de wolf aan. → Je moet de wolf aankijken.
3) 'Juist' = precies het tegenovergestelde
• Dat moet je juist niet doen! (= absoluut niet; het omgekeerde is goed)
• Wolven vinden een groep niet leuk. Ga juist in een groep wandelen.""",

    # type: mc, tf, gap; cat: begrip (5), woorden (4), uitdrukkingen (5), grammatica (4)
    "toets": [
        {"id": "wf1", "type": "tf", "niveau": "A1", "cat": "begrip", "vraag": "Wolven leven in een groep.",
         "opties": ["Waar", "Niet waar"], "juist": 0, "uitleg": "Klopt: wolven leven in een familiegroep, een roedel."},
        {"id": "wf2", "type": "mc", "niveau": "A2", "cat": "begrip", "vraag": "Sinds wanneer leven er weer wolven in Nederland?",
         "opties": ["sinds 2015", "sinds 150 jaar", "sinds vorig jaar"], "juist": 0,
         "uitleg": "Wolven waren 150 jaar weg, en sinds 2015 zijn ze terug."},
        {"id": "wf3", "type": "mc", "niveau": "B1", "cat": "begrip", "vraag": "Waarom moet je niet wegrennen?",
         "opties": ["Dan gaat de wolf achter je aan", "Dan wordt de wolf moe", "Dan raak je de weg kwijt"], "juist": 0,
         "uitleg": "Een jonge wolf vindt het een spelletje en gaat achter je aan, net als een hond achter een stok."},
        {"id": "wf4", "type": "mc", "niveau": "B1", "cat": "begrip", "vraag": "Wat is het eerste advies van Diederik?",
         "opties": ["Blijf staan en kijk de wolf boos aan", "Ga op de grond liggen", "Geef de wolf eten"], "juist": 0,
         "uitleg": "Blijf staan, kijk boos en doe ondertussen een stapje achteruit."},
        {"id": "wf5", "type": "tf", "niveau": "B2", "cat": "begrip", "vraag": "Volgens de expert kun je in een wolvengebied beter niet in een groep wandelen.",
         "opties": ["Waar", "Niet waar"], "juist": 1,
         "uitleg": "Niet waar: hij raadt juist aan om in een groep te wandelen; een wolf vindt een groep helemaal niks."},
        {"id": "wf6", "type": "gap", "niveau": "A2", "cat": "woorden", "vraag": "Pas op, die hond kan ___!",
         "opties": ["bijten", "wandelen", "roepen"], "juist": 0, "uitleg": "Bijten = met je tanden in iets happen."},
        {"id": "wf7", "type": "gap", "niveau": "B1", "cat": "woorden", "vraag": "Een familie van wolven heet een ___.",
         "opties": ["roedel", "kudde", "zwerm"], "juist": 0, "uitleg": "Een roedel = een groep wolven. (Een kudde = schapen of koeien; een zwerm = vogels of insecten.)"},
        {"id": "wf8", "type": "mc", "niveau": "B1", "cat": "woorden", "vraag": "Een roofdier is een dier dat…",
         "opties": ["andere dieren vangt en eet", "alleen planten eet", "in het water leeft"], "juist": 0,
         "uitleg": "Een roofdier jaagt op andere dieren. De wolf is het grootste roofdier van Nederland."},
        {"id": "wf9", "type": "mc", "niveau": "C1", "cat": "woorden", "vraag": "'Hij liep behoedzaam over het ijs.' Behoedzaam betekent:",
         "opties": ["heel voorzichtig", "heel snel", "vrolijk"], "juist": 0, "uitleg": "Behoedzaam = voorzichtig, met veel aandacht."},
        {"id": "wf10", "type": "mc", "niveau": "A2", "cat": "uitdrukkingen", "vraag": "Iemand roept: 'Wegwezen!' Wat bedoelt hij?",
         "opties": ["Ga weg!", "Kom hier!", "Wacht even!"], "juist": 0, "uitleg": "Wegwezen = ga weg (spreektaal)."},
        {"id": "wf11", "type": "gap", "niveau": "B1", "cat": "uitdrukkingen", "vraag": "Ik hou je in de ___, dus doe geen gekke dingen!",
         "opties": ["gaten", "ogen", "handen"], "juist": 0, "uitleg": "Iemand in de gaten houden = goed op iemand letten."},
        {"id": "wf12", "type": "mc", "niveau": "B2", "cat": "uitdrukkingen", "vraag": "'Toen de politie kwam, koos de dief het hazenpad.' Wat deed de dief?",
         "opties": ["Hij rende snel weg", "Hij gaf zich over", "Hij verstopte zich"], "juist": 0,
         "uitleg": "Het hazenpad kiezen = snel wegrennen, vluchten."},
        {"id": "wf13", "type": "gap", "niveau": "B2", "cat": "uitdrukkingen", "vraag": "Ook toen iedereen protesteerde, hield ze voet bij ___.",
         "opties": ["stuk", "stap", "been"], "juist": 0, "uitleg": "Voet bij stuk houden = niet toegeven, je mening of plek niet veranderen."},
        {"id": "wf14", "type": "mc", "niveau": "C1", "cat": "uitdrukkingen", "vraag": "Een wolf in schaapskleren is iemand die…",
         "opties": ["onschuldig lijkt, maar gevaarlijk is", "bang is voor wolven", "graag verkleedfeestjes geeft"], "juist": 0,
         "uitleg": "Een wolf in schaapskleren lijkt lief en onschuldig, maar heeft slechte bedoelingen."},
        {"id": "wf15", "type": "mc", "niveau": "A2", "cat": "grammatica", "vraag": "Welke zin is een opdracht (gebiedende wijs)?",
         "opties": ["Blijf staan!", "Je blijft staan.", "Hij blijft staan."], "juist": 0,
         "uitleg": "Gebiedende wijs = stam van het werkwoord, zonder onderwerp: Blijf staan!"},
        {"id": "wf16", "type": "gap", "niveau": "B1", "cat": "grammatica", "vraag": "Wat moet ik doen als ik een wolf ___?",
         "opties": ["tegenkom", "kom tegen", "tegen kom"], "juist": 0,
         "uitleg": "In een bijzin (na 'als') blijft een scheidbaar werkwoord heel en staat het aan het einde: tegenkom."},
        {"id": "wf17", "type": "mc", "niveau": "B1", "cat": "grammatica", "vraag": "Welke zin is goed?",
         "opties": ["Ik kom in het bos een wolf tegen.", "Ik tegenkom in het bos een wolf.", "Ik kom tegen in het bos een wolf."], "juist": 0,
         "uitleg": "In een gewone zin gaat 'tegen' naar het einde: Ik kom … tegen."},
        {"id": "wf18", "type": "mc", "niveau": "B1", "cat": "grammatica", "vraag": "'Wegrennen? Dat moet je juist niet doen!' Wat betekent 'juist' hier?",
         "opties": ["Precies dat is fout", "Dat is een beetje fout", "Dat is een goed idee"], "juist": 0,
         "uitleg": "'Juist niet' = absoluut niet; het tegenovergestelde is goed."},
    ],
}
