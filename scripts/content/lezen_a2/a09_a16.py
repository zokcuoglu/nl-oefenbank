"""Lezen A2 practice texts 9-16 = practice exam 2 (own texts, made-up names). Format: see a01_a08.py."""

A09 = {
    "id": "a2-werkrooster",
    "titel": "Nieuw rooster",
    "soort": "E-mail van het werk",
    "inleiding": "Sanne werkt in een supermarkt. Ze krijgt deze e-mail van haar leidinggevende.",
    "kop": ["Van: Mark de Groot", "Aan: alle medewerkers", "Onderwerp: rooster december"],
    "tekst": """Hallo allemaal,

Het rooster voor december staat in de app. In december is het druk in de winkel. Daarom werken we op zondag ook van 12.00 tot 18.00 uur.

Kun je op een dag niet werken? Ruil dan zelf met een collega. Geef de ruil aan mij door, minstens drie dagen van tevoren.

Ben je ziek? Bel dan vóór 7.00 uur naar de winkel. Een appje is niet genoeg.

Op 24 december gaat de winkel om 16.00 uur dicht. Na het werk drinken we samen iets in de kantine.

Groeten,
Mark""",
    "vragen": [
        {"id": "a9q1", "patroon": 6, "vraag": "Waarom werken de medewerkers in december ook op zondag?",
         "opties": ["Omdat het druk is in de winkel", "Omdat er veel collega's ziek zijn", "Omdat de winkel nieuw is"],
         "uitleg": "Aralıkta mağaza kalabalık, bu yüzden pazar da çalışılıyor. 'Daarom' = bu yüzden.",
         "bewijs": "In december is het druk in de winkel."},
        {"id": "a9q2", "patroon": 13, "vraag": "Sanne kan op 10 december niet werken. Wat moet ze doen?",
         "opties": ["Ruilen met een collega en dit aan Mark doorgeven", "Een appje sturen naar de winkel", "Niets, Mark zoekt iemand anders"],
         "uitleg": "Kendisi bir iş arkadaşıyla değiş tokuş yapıp en az üç gün önce Mark'a bildirmeli.",
         "bewijs": "Ruil dan zelf met een collega."},
        {"id": "a9q3", "patroon": 13, "vraag": "Sanne is ziek. Wat moet ze doen?",
         "opties": ["Vóór 7.00 uur naar de winkel bellen", "Een appje sturen aan Mark", "Een e-mail sturen"],
         "uitleg": "Hastaysa 7.00'den önce mağazayı aramalı; mesaj yetmiyor.",
         "bewijs": "Bel dan vóór 7.00 uur naar de winkel."},
    ],
}

A10 = {
    "id": "a2-buslijn",
    "titel": "Buslijn 22: Station – Ziekenhuis",
    "soort": "Dienstregeling",
    "inleiding": "Dit is een deel van de dienstregeling van buslijn 22.",
    "tekst": """## Maandag tot en met vrijdag

Station | Markt | Ziekenhuis
07.15 | 07.22 | 07.35
07.45 | 07.52 | 08.05
08.15 | 08.22 | 08.35
08.45 | 08.52 | 09.05

## Let op

In het weekend rijdt lijn 22 maar één keer per uur. Kijk dan op de website voor de tijden.

U kunt in de bus niet met contant geld betalen. Betaal met uw bankpas of OV-chipkaart.""",
    "vragen": [
        {"id": "a10q1", "patroon": 14, "vraag": "Hoe lang duurt de rit van het station naar het ziekenhuis?",
         "opties": ["20 minuten", "7 minuten", "35 minuten"],
         "uitleg": "07.15'te istasyondan çıkıp 07.35'te hastanede: 20 dakika.",
         "bewijs": "07.15 | 07.22 | 07.35"},
        {"id": "a10q2", "patroon": 11, "vraag": "Linda heeft om 9.00 uur een afspraak in het ziekenhuis. Welke bus neemt zij op het station?",
         "opties": ["De bus van 08.15 uur", "De bus van 08.45 uur", "De bus van 07.15 uur"],
         "uitleg": "08.15'teki otobüs hastaneye 08.35'te varıyor; 9.00 randevusu için uygun. 08.45'teki 09.05'te varır, geç kalır.",
         "bewijs": "08.15 | 08.22 | 08.35"},
        {"id": "a10q3", "patroon": 12, "vraag": "Hoe kunt u betalen in de bus?",
         "opties": ["Met uw bankpas of OV-chipkaart", "Met contant geld", "Alleen met een kaartje van de website"],
         "uitleg": "Otobüste nakit yok; banka kartı ya da OV-chipkaart.",
         "bewijs": "Betaal met uw bankpas of OV-chipkaart."},
    ],
}

A11 = {
    "id": "a2-tandarts",
    "titel": "Tandartspraktijk Witte Lach",
    "soort": "Folder",
    "inleiding": "Deze folder ligt in de wachtkamer van de tandarts.",
    "tekst": """## Twee keer per jaar naar de tandarts

Kom twee keer per jaar voor controle. Zo vinden we problemen op tijd.

## Kinderen

Kinderen tot 18 jaar betalen niets voor de controle. Neem uw kind mee vanaf het eerste tandje.

## Afspraak afzeggen

Kunt u niet komen? Zeg de afspraak dan minstens 24 uur van tevoren af. Doet u dat niet? Dan moet u € 25 betalen.

## Pijn

Heeft u veel pijn? Bel ons dan meteen. U kunt meestal dezelfde dag nog komen.""",
    "vragen": [
        {"id": "a11q1", "patroon": 15, "vraag": "Voor wie is deze folder?",
         "opties": ["Voor de patiënten van de tandarts", "Voor tandartsen", "Alleen voor kinderen"],
         "uitleg": "Bekleme salonundaki broşür hastalara hitap ediyor: kontrol, iptal, ağrı.",
         "bewijs": "Kom twee keer per jaar voor controle."},
        {"id": "a11q2", "patroon": 7, "vraag": "Wat gebeurt er als u een afspraak een uur van tevoren afzegt?",
         "opties": ["U moet € 25 betalen.", "U krijgt een nieuwe afspraak op dezelfde dag.", "Er gebeurt niets."],
         "uitleg": "En az 24 saat önce iptal etmezsen 25 € ödüyorsun. Bir saat önce iptal = geç.",
         "bewijs": "Dan moet u € 25 betalen."},
        {"id": "a11q3", "patroon": 17, "vraag": "Wat is waar?",
         "opties": ["De controle is gratis voor een kind van 10 jaar.", "Kinderen mogen pas vanaf 6 jaar komen.", "Met pijn moet u een week wachten."],
         "uitleg": "18 yaşına kadar kontrol ücretsiz. Çocuklar ilk dişten itibaren gelebilir; ağrıda genelde aynı gün.",
         "bewijs": "Kinderen tot 18 jaar betalen niets voor de controle."},
    ],
}

A12 = {
    "id": "a2-buurtfeest",
    "titel": "Uitnodiging buurtfeest",
    "soort": "Uitnodiging",
    "inleiding": "Deze uitnodiging zit in de brievenbus van alle bewoners van de Lindelaan.",
    "tekst": """BUURTFEEST LINDELAAN

Zaterdag 7 juni van 15.00 tot 21.00 uur op het grasveld

Voor de kinderen is er een springkussen en schminken. Om 18.00 uur eten we samen. Iedereen neemt iets te eten mee voor de tafel, bijvoorbeeld een salade of een taart.

Kosten: € 5 per volwassene. Kinderen gratis.

Meld je aan vóór 1 juni bij Henk, Lindelaan 3.

Regent het? Dan is het feest in het buurthuis.""",
    "vragen": [
        {"id": "a12q1", "patroon": 13, "vraag": "Wat moet iedereen meenemen?",
         "opties": ["Iets te eten voor de tafel", "Een springkussen", "Een stoel"],
         "uitleg": "Herkes masaya yiyecek bir şey getiriyor, örneğin salata ya da pasta.",
         "bewijs": "Iedereen neemt iets te eten mee voor de tafel, bijvoorbeeld een salade of een taart."},
        {"id": "a12q2", "patroon": 14, "vraag": "Familie Öztürk komt met 2 volwassenen en 3 kinderen. Hoeveel betalen zij?",
         "opties": ["€ 10", "€ 25", "€ 5"],
         "uitleg": "Yetişkin başına 5 €, çocuklar ücretsiz: 2 × 5 = 10 €.",
         "bewijs": "Kosten: € 5 per volwassene. Kinderen gratis."},
        {"id": "a12q3", "patroon": 7, "vraag": "Wat gebeurt er als het regent?",
         "opties": ["Het feest is in het buurthuis.", "Het feest gaat niet door.", "Het feest is een week later."],
         "uitleg": "Yağmur yağarsa parti mahalle evinde (buurthuis) yapılıyor.",
         "bewijs": "Dan is het feest in het buurthuis."},
    ],
}

A13 = {
    "id": "a2-onderhoud",
    "titel": "Nieuwe ramen",
    "soort": "Brief van de woningcorporatie",
    "inleiding": "Deze brief krijgen de huurders van de flat aan de Parkweg.",
    "tekst": """Beste huurder,

In uw flat komen nieuwe ramen. Hierdoor wordt uw huis warmer en betaalt u minder voor gas. U hoeft niets extra te betalen. Uw huur blijft hetzelfde.

De werkmannen komen bij u op maandag 14 oktober. Ze werken van 8.00 tot 16.00 uur. Er moet iemand thuis zijn. Kan dat niet? Geef uw sleutel dan aan de huismeester.

Wilt u de ramen vrij maken? Haal planten en gordijnen weg voor 14 oktober.

Heeft u vragen? Mail naar onderhoud@woonstede.nl.

Met vriendelijke groet,
Woonstede""",
    "vragen": [
        {"id": "a13q1", "patroon": 1, "vraag": "Wat is het doel van deze brief?",
         "opties": ["Vertellen dat er nieuwe ramen komen", "Vragen of de huurders nieuwe ramen willen", "Zeggen dat de huur omhoog gaat"],
         "uitleg": "Mektup yeni pencerelerin takılacağını haber veriyor. Kira değişmiyor.",
         "bewijs": "In uw flat komen nieuwe ramen."},
        {"id": "a13q2", "patroon": 17, "vraag": "Wat is waar?",
         "opties": ["De huur wordt niet hoger.", "De huurders betalen de ramen zelf.", "De gasrekening wordt hoger."],
         "uitleg": "Kira aynı kalıyor, ekstra ödeme yok; gaz faturası tersine azalıyor.",
         "bewijs": "Uw huur blijft hetzelfde."},
        {"id": "a13q3", "patroon": 13, "vraag": "Mevrouw Rossi werkt op 14 oktober. Wat moet zij doen?",
         "opties": ["Haar sleutel aan de huismeester geven", "Een andere dag kiezen", "Niets"],
         "uitleg": "Evde kimse olamıyorsa anahtar bina görevlisine (huismeester) verilmeli.",
         "bewijs": "Geef uw sleutel dan aan de huismeester."},
        {"id": "a13q4", "patroon": 13, "vraag": "Wat moeten de huurders vóór 14 oktober doen?",
         "opties": ["Planten en gordijnen bij de ramen weghalen", "Een e-mail sturen", "De ramen schoonmaken"],
         "uitleg": "Pencerelerin önünü boşaltmak için bitkileri ve perdeleri kaldırmak gerekiyor.",
         "bewijs": "Haal planten en gordijnen weg voor 14 oktober."},
    ],
}

A14 = {
    "id": "a2-bezorgen",
    "titel": "Boodschappen laten bezorgen",
    "soort": "Website",
    "inleiding": "Dit staat op de website van supermarkt Dagvers.",
    "tekst": """## Zo werkt het

Kies uw boodschappen op de website of in de app. Kies daarna een dag en een tijd. Wij brengen de boodschappen tot aan uw voordeur.

## Wat kost het?

Bestelt u voor meer dan € 75? Dan is bezorgen gratis. Bestelt u voor minder? Dan betaalt u € 4,95.

## Niet thuis?

Bent u niet thuis als wij komen? Dan nemen wij de boodschappen weer mee. U kunt dan een nieuwe tijd kiezen. U betaalt de bezorgkosten opnieuw.""",
    "vragen": [
        {"id": "a14q1", "patroon": 14, "vraag": "Kemal bestelt voor € 50. Hoeveel betaalt hij voor het bezorgen?",
         "opties": ["€ 4,95", "Niets", "€ 75"],
         "uitleg": "75 €'nun altındaki siparişte teslimat 4,95 €. 50 € < 75 €.",
         "bewijs": "Dan betaalt u € 4,95."},
        {"id": "a14q2", "patroon": 7, "vraag": "Wat gebeurt er als u niet thuis bent?",
         "opties": ["De boodschappen gaan terug en u kiest een nieuwe tijd.", "De boodschappen staan bij de buren.", "De boodschappen staan voor de deur."],
         "uitleg": "Evde değilsen market alışverişi geri götürüyor; yeni bir saat seçiyorsun.",
         "bewijs": "Dan nemen wij de boodschappen weer mee."},
        {"id": "a14q3", "patroon": 6, "vraag": "Waar brengt de supermarkt de boodschappen naartoe?",
         "opties": ["Tot aan uw voordeur", "Naar de keuken", "Naar een afhaalpunt"],
         "uitleg": "Alışveriş ön kapına kadar getiriliyor.",
         "bewijs": "Wij brengen de boodschappen tot aan uw voordeur."},
    ],
}

A15 = {
    "id": "a2-bieb-regels",
    "titel": "Boeken lenen",
    "soort": "Regels",
    "inleiding": "Deze informatie krijgt u als u lid wordt van de bibliotheek.",
    "tekst": """## Boeken lenen

- U mag 10 boeken tegelijk lenen.
- U mag een boek 3 weken houden.
- Wilt u het boek langer houden? Verleng het dan in de app. Dat kan twee keer.
- Brengt u een boek te laat terug? Dan betaalt u € 0,25 per dag.
- Bent u een boek kwijt? Dan betaalt u een nieuw boek.

Kinderen tot 18 jaar betalen geen boete.""",
    "vragen": [
        {"id": "a15q1", "patroon": 14, "vraag": "Hoe lang mag u een boek houden zonder te verlengen?",
         "opties": ["3 weken", "10 dagen", "2 weken"],
         "uitleg": "Bir kitap 3 hafta tutulabiliyor. 10 = aynı anda alınabilecek kitap sayısı.",
         "bewijs": "U mag een boek 3 weken houden."},
        {"id": "a15q2", "patroon": 13, "vraag": "U wilt een boek langer houden. Wat doet u?",
         "opties": ["Ik verleng het in de app.", "Ik betaal € 0,25.", "Ik koop een nieuw boek."],
         "uitleg": "Daha uzun tutmak için uygulamadan süreyi uzatıyorsun (iki kez yapılabilir).",
         "bewijs": "Verleng het dan in de app."},
        {"id": "a15q3", "patroon": 12, "vraag": "Een jongen van 12 jaar brengt een boek te laat terug. Welke regel geldt voor hem?",
         "opties": ["Hij betaalt geen boete.", "Hij betaalt € 0,25 per dag.", "Hij moet een nieuw boek betalen."],
         "uitleg": "18 yaşından küçükler ceza ödemiyor.",
         "bewijs": "Kinderen tot 18 jaar betalen geen boete."},
    ],
}

A16 = {
    "id": "a2-ouderavond",
    "titel": "Tien-minutengesprekken",
    "soort": "Bericht van school",
    "inleiding": "Dit bericht staat in de app van de school.",
    "tekst": """Beste ouders,

Volgende week zijn de tien-minutengesprekken. U praat dan met de leerkracht over uw kind. U kunt kiezen uit dinsdagavond of donderdagmiddag.

Kies vóór vrijdag een tijd in de app. Heeft u geen tijd gekozen? Dan kiest de leerkracht een tijd voor u.

Wilt u een tolk? Zeg dat dan tegen de leerkracht. Uw kind mag ook mee naar het gesprek.

Tot volgende week!
Team De Kleine Prins""",
    "vragen": [
        {"id": "a16q1", "patroon": 6, "vraag": "Waar gaat het gesprek over?",
         "opties": ["Over het kind", "Over het schoolreisje", "Over de app van school"],
         "uitleg": "Görüşmede öğretmenle çocuğun durumu konuşuluyor.",
         "bewijs": "U praat dan met de leerkracht over uw kind."},
        {"id": "a16q2", "patroon": 7, "vraag": "Wat gebeurt er als u vóór vrijdag geen tijd kiest?",
         "opties": ["De leerkracht kiest een tijd.", "Er is geen gesprek.", "U moet de school bellen."],
         "uitleg": "Cumadan önce saat seçmezsen öğretmen senin için bir saat seçiyor.",
         "bewijs": "Dan kiest de leerkracht een tijd voor u."},
        {"id": "a16q3", "patroon": 9, "vraag": "U wilt een tolk bij het gesprek. Tegen wie zegt u dat?",
         "opties": ["Tegen de leerkracht", "Tegen de directeur", "Tegen de gemeente"],
         "uitleg": "Tercüman istiyorsan öğretmene söylüyorsun.",
         "bewijs": "Zeg dat dan tegen de leerkracht."},
    ],
}

TEKSTEN = [A09, A10, A11, A12, A13, A14, A15, A16]
