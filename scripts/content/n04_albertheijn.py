"""Item 4: Lege schappen bij Albert Heijn (NOS Journaal in Makkelijke Taal, 13 October, part 0:40-3:10).
Written only from the transcript the user provided. Facts not in the transcript are not added.
"""

ITEM = {
    "id": "albertheijn",
    "nr": 4,
    "titel": "Lege schappen bij Albert Heijn",
    "bron": "NOS Journaal in Makkelijke Taal",
    "video_url": "https://www.youtube.com/watch?v=wkdogkhwfgk",
    "video_start": 40,
    "video_end": 190,
    "afbeelding_url": "https://i.ytimg.com/vi/wkdogkhwfgk/hqdefault.jpg",
    "niveau_video": "A2–B1",
    "niveau_uitleg": "NOS Journaal in Makkelijke Taal yavaş ve kısa cümlelerle konuşuyor (A2). Röportajlardaki müşteriler ve muhabir ise hızlı, günlük dille konuşuyor ('mazzel', 'zo erg is dat niet', 'gerommeld'); o kısımlar B1.",

    # A0: absolute beginner – very short present-tense sentences, only the most common words
    "a0": """Albert Heijn is een <strong>supermarkt</strong>.

De <strong>computers</strong> werken niet. Er komt weinig eten.

Veel schappen zijn <strong>leeg</strong>. Er is geen fruit.

Een vrouw heeft druiven. Ze is blij.

Een man zegt: 'Het is niet erg.'""",
    "gloss_a0": "de supermarkt = süpermarket • de computer = bilgisayar • werken = çalışmak • weinig = az • het eten = yiyecek • het schap = raf • leeg = boş • het fruit = meyve • de druif = üzüm • blij = mutlu • niet erg = önemli değil",

    "a1": """Albert Heijn is een grote <strong>supermarkt</strong> in Nederland. Er zijn heel veel winkels van Albert Heijn.

Nu is er een probleem. De <strong>computers</strong> werken niet goed. Daarom komen er weinig spullen naar de winkels.

Veel schappen zijn <strong>leeg</strong>. Er is geen groente en geen fruit. Een vrouw vindt nog één doosje druiven voor haar dochter. Ze heeft <strong>mazzel</strong>!

Een man zegt: 'Ik heb alles van mijn lijstje. <strong>Zo erg is het niet</strong>.'

Wat is er precies mis? Dat weet nog niemand.""",
    "gloss_a1": "de supermarkt = süpermarket • de spullen = ürünler, eşyalar • het schap = raf • leeg = boş • de groente = sebze • het fruit = meyve • de druiven = üzümler • mazzel hebben = şansı yaver gitmek • het lijstje = (alışveriş) listesi • zo erg is het niet = o kadar da kötü değil",

    "a2": """Er is nog veel <strong>onduidelijk</strong> over de problemen bij Albert Heijn. Het computersysteem van de supermarkt werkt al twee dagen niet goed. Albert Heijn brengt nu weer spullen naar de winkels, maar veel <strong>schappen</strong> zijn nog leeg.

In één winkel zie je dat goed: er is geen groente en fruit, en er staan veel lege <strong>kratten</strong>. Een moeder vindt nog net een doosje van de <strong>lievelingsdruiven</strong> van haar dochter. Mazzel!

Normaal staat er biologische melk, maar die is er nu minder. Dat komt doordat de computers alles regelen. Je kunt niet zomaar met de telefoon <strong>bestellen</strong>, want Albert Heijn heeft 1000 winkels.

Veel klanten vinden het niet zo erg. Een man heeft alles van zijn <strong>boodschappenlijstje</strong>. Een vrouw vindt boerenkool, maar die is wel <strong>een stuk</strong> duurder.""",
    "gloss_a2": "onduidelijk = belirsiz • het schap = raf • de krat = kasa • lievelings- = en sevdiği • biologisch = organik • doordat = yüzünden, -dığı için • zomaar = öylece, kolayca • bestellen = sipariş etmek • het boodschappenlijstje = alışveriş listesi • de boerenkool = kara lahana • een stuk duurder = epey pahalı",

    "b1": """Nog steeds is niet duidelijk wat er precies is misgegaan met het computersysteem van Albert Heijn. Wel begint de supermarkt weer met het brengen van spullen naar de winkels, want veel schappen zijn leeg.

In een van de winkels was dat vanochtend goed te zien. Er lag geen groente en geen fruit, en er stonden veel lege kratten. Een klant vertelt dat ze nog net één doosje druiven voor haar dochter had gevonden. 'Dus ze heeft <strong>mazzel</strong>.'

Bedrijfsleider Dominique legt uit dat de schappen leeg raken, omdat alles door computers wordt geregeld. Even bellen om spullen te bestellen, kan niet meer: voor duizend winkels een telefooncentrale opzetten, kost een paar dagen.

Toch vinden veel klanten het niet zo erg. Een man heeft alles van zijn lijstje en is verbaasd hoeveel er nog ligt. Een vrouw vond wel boerenkool, maar die was <strong>een stuk</strong> duurder.

Volgens de verslaggever zag Albert Heijn dit weekend dat er in de systemen werd gerommeld. <strong>Uit voorzorg</strong> zette het bedrijf daarom systemen uit, zodat klantgegevens niet gestolen konden worden. Net werd bekend dat er waarschijnlijk hackers uit het buitenland achter zitten. Hoe lang het herstel duurt? Dat is nog <strong>koffiedik kijken</strong>.""",
    "gloss_b1": "misgaan = ters gitmek • de bedrijfsleider = mağaza müdürü • de telefooncentrale = telefon santrali • opzetten = kurmak • verbaasd = şaşkın • de verslaggever = muhabir • rommelen = kurcalamak • uit voorzorg = önlem olarak • de klantgegevens = müşteri bilgileri • ergens achter zitten = bir şeyin arkasında olmak • het herstel = düzelme, onarım • koffiedik kijken = falcılık etmek, kimse bilemez",

    "b2": """Twee dagen na het begin van een grote <strong>storing</strong> is nog altijd onduidelijk wat er bij Albert Heijn precies <strong>in de soep is gelopen</strong>. Terwijl de supermarktketen de <strong>bevoorrading</strong> van haar winkels voorzichtig weer op gang brengt, blijven veel schappen leeg – vooral bij groente en fruit.

Dat komt doordat vrijwel het hele bestelproces door computers wordt aangestuurd, en die systemen <strong>liggen plat</strong>. Terugvallen op de telefoon, zoals vroeger, is volgens bedrijfsleider Dominique geen optie: een telefooncentrale voor zo'n duizend winkels opzetten neemt al snel een paar dagen in beslag. Biologische melk is daardoor schaars, gewone melk is er juist meer.

Opvallend genoeg reageren klanten <strong>laconiek</strong>. 'Iedereen zegt lege schappen, maar zo erg is het niet,' vindt een man die alles van zijn lijstje heeft kunnen vinden.

Achter de schermen speelt intussen meer. Albert Heijn ontdekte dit weekend dat er in de systemen werd gerommeld en zette <strong>uit voorzorg</strong> een deel ervan uit, om te voorkomen dat klantgegevens zoals namen en adressen zouden worden gestolen. Het bedrijf gaat ervan uit dat dat niet is gebeurd, al is dat niet zeker. Inmiddels is bekend dat de systemen vermoedelijk zijn aangevallen door hackers uit het buitenland.""",
    "gloss_b2": "de storing = arıza • in de soep lopen = suya düşmek, ters gitmek • de keten = zincir (mağaza) • de bevoorrading = mal sevkiyatı • op gang brengen = yeniden başlatmak • aansturen = yönetmek • plat liggen = çökmüş olmak, çalışmamak • terugvallen op = -e geri dönmek • in beslag nemen = (zaman) almak • schaars = kıt • laconiek = soğukkanlı, umursamadan • achter de schermen = perde arkasında • ervan uitgaan dat = varsaymak • vermoedelijk = muhtemelen",

    "c1": """Twee dagen nadat het computersysteem van Albert Heijn <strong>plat kwam te liggen</strong>, <strong>tast</strong> iedereen nog <strong>in het duister</strong> over de precieze oorzaak. Wel komt de <strong>bevoorrading</strong> moeizaam op gang, al zal het volgens het bedrijf nog even duren voordat alle schappen weer gevuld zijn.

De storing legt bloot hoe afhankelijk een moderne supermarktketen van haar IT is. Waar een filiaal vroeger simpelweg de telefoon pakte om bij te bestellen, is dat bij zo'n duizend vestigingen ondenkbaar: het opzetten van een telefooncentrale alleen al vergt dagen. Het gevolg is een opmerkelijk scheef assortiment – biologische melk is schaars, gewone melk ruim voorradig.

Klanten lijken het overigens gelaten te ondergaan; sommigen verbazen zich eerder over hoeveel er nog ligt dan over wat er ontbreekt.

Het eigenlijke verhaal speelt zich achter de schermen af. Toen Albert Heijn afgelopen weekend merkte dat er in de systemen werd gerommeld, besloot het onderdelen uit te schakelen om <strong>de schade te beperken</strong> en diefstal van klantgegevens te voorkomen. Als de eerste inschatting klopt, zijn er geen gegevens <strong>buitgemaakt</strong> en lijkt het incident op dat punt <strong>met een sisser af te lopen</strong>. Zekerheid is er echter niet, en hoe lang het herstel duurt, is <strong>koffiedik kijken</strong>. Inmiddels wijzen de aanwijzingen in de richting van hackers uit het buitenland.""",
    "gloss_c1": "plat komen te liggen = çökmek • in het duister tasten = karanlıkta el yordamıyla aramak, hiçbir fikri olmamak • moeizaam = zahmetli • blootleggen = gözler önüne sermek • het filiaal / de vestiging = şube • vergen = gerektirmek • scheef = dengesiz, çarpık • voorradig = stokta olan • gelaten ondergaan = sessizce katlanmak • de schade beperken = zararı sınırlamak • buitmaken = ele geçirmek • met een sisser aflopen = ucuz atlatmak • de aanwijzing = ipucu",

    "uitdrukkingen": [
        "n-albertheijn-u1",
        "n-albertheijn-u2",
        "n-albertheijn-u3",
        "n-albertheijn-u4",
        "n-albertheijn-u5",
        "n-albertheijn-u6",
        "n-albertheijn-u7",
        "n-albertheijn-u8",
        "n-albertheijn-u9",
        "n-albertheijn-u10"
    ],

    # woord | soort | betekenis (NL) | voorbeeld | Turks | niveau
    "woordenschat": [
        "n-albertheijn-w1",
        {"id": "b274", "voorbeeld": "De koelkast is leeg."},
        "n-albertheijn-w3",
        "n-albertheijn-w4",
        "n-albertheijn-w5",
        "n-albertheijn-w6",
        "n-albertheijn-w7",
        "n-albertheijn-w8",
        "n-albertheijn-w9",
        "n-albertheijn-w10",
        "n-albertheijn-w11",
        "n-albertheijn-w12",
        "n-albertheijn-w13",
        "n-albertheijn-w14",
        "n-albertheijn-w15",
        {"id": "s019", "voorbeeld": "Iemand heeft in de systemen gerommeld.", "definitie": "(hier) zonder toestemming ergens aan zitten"},
        "n-albertheijn-w17",
        "n-albertheijn-w18",
        "n-albertheijn-w19",
        "n-albertheijn-w20",
        "n-albertheijn-w21"
    ],

    "grammatica": """1) Oorzaak en gevolg: omdat – doordat – daardoor – daarom
Doordat/daardoor gebruik je vooral als niemand het zo wilde. Omdat/daarom kan altijd, ook bij een bewuste keuze.
• De schappen raken leeg, doordat de computers niet goed werken.
• Er is een storing. Daardoor zijn de schappen leeg.
• Er werd gerommeld in de systemen. Daarom zette Albert Heijn ze uit.
Na omdat en doordat staat het werkwoord aan het einde (bijzin). Na daardoor en daarom komt het werkwoord meteen (inversie).
2) Vertellen wat een ander zegt of denkt: dat – of – hoe
• 'De gegevens zijn niet gestolen.' → Albert Heijn denkt dat de gegevens niet gestolen zijn.
• 'Is het snel opgelost?' → Niemand weet of het snel opgelost is.
• 'Hoe lang duurt het?' → Het is onduidelijk hoe lang het duurt.
Bij een ja/nee-vraag gebruik je 'of'. Het werkwoord staat steeds aan het einde.""",

    # type: mc, tf, gap; cat: begrip (5), woorden (4), uitdrukkingen (5), grammatica (4)
    "toets": [
        {"id": "ah1", "type": "tf", "niveau": "A1", "cat": "begrip", "vraag": "Bij Albert Heijn zijn veel schappen leeg.",
         "opties": ["Waar", "Niet waar"], "juist": 0, "uitleg": "Klopt: vooral bij groente en fruit zijn de schappen leeg."},
        {"id": "ah2", "type": "mc", "niveau": "A2", "cat": "begrip", "vraag": "Waarom raken de schappen leeg?",
         "opties": ["Omdat de computers niet goed werken", "Omdat klanten te veel kopen", "Omdat de vrachtwagens kapot zijn"], "juist": 0,
         "uitleg": "Alles wordt door computers geregeld, en die werken nu niet goed."},
        {"id": "ah3", "type": "mc", "niveau": "B1", "cat": "begrip", "vraag": "Waarom kan de winkel niet gewoon met de telefoon bestellen?",
         "opties": ["Een telefooncentrale voor 1000 winkels opzetten duurt dagen", "De telefoons doen het ook niet", "Bellen is te duur"], "juist": 0,
         "uitleg": "Dominique zegt: voor 1000 winkels een telefooncentrale opzetten, duurt een paar dagen."},
        {"id": "ah4", "type": "tf", "niveau": "B1", "cat": "begrip", "vraag": "Albert Heijn weet zeker dat er geen klantgegevens zijn gestolen.",
         "opties": ["Waar", "Niet waar"], "juist": 1, "uitleg": "Niet waar: ze dénken dat de gegevens niet gestolen zijn, maar ze weten het niet helemaal zeker."},
        {"id": "ah5", "type": "mc", "niveau": "B2", "cat": "begrip", "vraag": "Waarom zette Albert Heijn computersystemen uit?",
         "opties": ["Om te voorkomen dat klantgegevens werden gestolen", "Omdat de systemen te oud waren", "Om stroom te besparen"], "juist": 0,
         "uitleg": "Er werd gerommeld in de systemen; uit voorzorg gingen ze uit, zodat namen en adressen niet gestolen konden worden."},
        {"id": "ah6", "type": "gap", "niveau": "A2", "cat": "woorden", "vraag": "De melk staat op het bovenste ___.",
         "opties": ["schap", "lijstje", "krat"], "juist": 0, "uitleg": "Een schap is een plank in een winkel waar de producten op staan."},
        {"id": "ah7", "type": "gap", "niveau": "B1", "cat": "woorden", "vraag": "Door een ___ rijden er vandaag geen treinen.",
         "opties": ["storing", "voorraad", "bestelling"], "juist": 0, "uitleg": "Een storing = iets werkt (tijdelijk) niet."},
        {"id": "ah8", "type": "mc", "niveau": "B2", "cat": "woorden", "vraag": "'De klanten reageerden laconiek.' Wat betekent dat?",
         "opties": ["Rustig, zonder zich druk te maken", "Heel boos", "Verdrietig"], "juist": 0, "uitleg": "Laconiek = kalm, je maakt je er niet druk om."},
        {"id": "ah9", "type": "mc", "niveau": "C1", "cat": "woorden", "vraag": "'Er zijn geen gegevens buitgemaakt.' Wat betekent buitmaken?",
         "opties": ["stelen", "verliezen", "verwijderen"], "juist": 0, "uitleg": "Buitmaken = stelen, als buit meenemen."},
        {"id": "ah10", "type": "mc", "niveau": "A2", "cat": "uitdrukkingen", "vraag": "'Ik vond nog net de laatste druiven. Mazzel!' Wat betekent mazzel?",
         "opties": ["geluk", "pech", "haast"], "juist": 0, "uitleg": "Mazzel hebben = geluk hebben. Het tegenovergestelde is pech."},
        {"id": "ah11", "type": "gap", "niveau": "B1", "cat": "uitdrukkingen", "vraag": "Hoe lang de storing nog duurt? Dat is nog ___ kijken.",
         "opties": ["koffiedik", "koffiekop", "koffietijd"], "juist": 0, "uitleg": "Het is koffiedik kijken = niemand kan het voorspellen."},
        {"id": "ah12", "type": "mc", "niveau": "B1", "cat": "uitdrukkingen", "vraag": "'Uit voorzorg is de school vandaag dicht.' Wat betekent 'uit voorzorg'?",
         "opties": ["om problemen te voorkomen", "omdat de leraren ziek zijn", "per ongeluk"], "juist": 0,
         "uitleg": "Uit voorzorg = je doet iets vooraf, zodat er geen (grotere) problemen komen."},
        {"id": "ah13", "type": "mc", "niveau": "B2", "cat": "uitdrukkingen", "vraag": "'Door het slechte weer liep het feest in de soep.' Wat gebeurde er?",
         "opties": ["Het feest mislukte", "Er werd soep gegeten", "Het feest duurde langer"], "juist": 0,
         "uitleg": "In de soep lopen = mislukken, misgaan."},
        {"id": "ah14", "type": "gap", "niveau": "C1", "cat": "uitdrukkingen", "vraag": "Er raakte niemand gewond: het ongeluk liep met een ___ af.",
         "opties": ["sisser", "knal", "zucht"], "juist": 0, "uitleg": "Met een sisser aflopen = zonder ernstige gevolgen eindigen."},
        {"id": "ah15", "type": "gap", "niveau": "B1", "cat": "grammatica", "vraag": "Er is een grote storing. ___ zijn veel schappen leeg.",
         "opties": ["Daardoor", "Doordat", "Omdat"], "juist": 0,
         "uitleg": "Een nieuwe hoofdzin begint met 'daardoor' (+ werkwoord meteen). Doordat en omdat beginnen een bijzin."},
        {"id": "ah16", "type": "mc", "niveau": "B1", "cat": "grammatica", "vraag": "Welke zin is goed?",
         "opties": ["De schappen zijn leeg, doordat de computers niet werken.", "De schappen zijn leeg, doordat werken de computers niet.", "De schappen zijn leeg, doordat de computers werken niet."], "juist": 0,
         "uitleg": "Na 'doordat' komt een bijzin: het werkwoord (werken) staat aan het einde."},
        {"id": "ah17", "type": "gap", "niveau": "A2", "cat": "grammatica", "vraag": "Albert Heijn denkt ___ de gegevens niet gestolen zijn.",
         "opties": ["dat", "of", "wat"], "juist": 0, "uitleg": "Na denken/zeggen + een gewone mededeling gebruik je 'dat'."},
        {"id": "ah18", "type": "mc", "niveau": "B2", "cat": "grammatica", "vraag": "'Is het opgelost?' vraagt de klant. Hoe vertel je dat aan iemand anders?",
         "opties": ["De klant vraagt of het opgelost is.", "De klant vraagt dat het opgelost is.", "De klant vraagt of is het opgelost."], "juist": 0,
         "uitleg": "Een ja/nee-vraag wordt een bijzin met 'of'; het werkwoord gaat naar het einde."},
    ],
}
