"""Lezen I practice texts 7-8 (own texts in exam style; all names and places are made up). Format: see t01_t03.py.
t07 = persuasive work text; t08 = long 'search' text (read the question first, then look up the answer),
like the last text of the official exam.
"""

T07 = {
    "id": "kinderopvang",
    "titel": "Werken in de kinderopvang: iets voor jou?",
    "soort": "Website",
    "domein": "werk",
    "tekstsoort": "persuasief",
    "inleiding": "Deze tekst komt van de website van een organisatie voor kinderopvang. De organisatie zoekt nieuwe medewerkers.",
    "tekst": """Ben je geduldig, vrolijk en vind je het leuk om met kinderen te werken? Dan is een baan in de kinderopvang misschien iets voor jou. Bij Kinderopvang Zonnebloem werken ruim 300 pedagogisch medewerkers op 25 locaties in de regio. En we zoeken nog meer collega's. Want steeds meer ouders werken allebei, en daardoor groeit de vraag naar opvang voor hun kinderen.

## Wat doe je als pedagogisch medewerker?

Als pedagogisch medewerker zorg je samen met een collega voor een groep van maximaal twaalf kinderen. Je speelt met de kinderen, leest voor, gaat met ze naar buiten en helpt ze met eten en drinken. Maar je doet meer dan alleen oppassen. Je let goed op hoe elk kind zich ontwikkelt. Merk je dat een kind achterloopt met praten of dat het niet lekker in zijn vel zit? Dan bespreek je dat met je collega's en met de ouders. Zo help je kinderen om zich zo goed mogelijk te ontwikkelen.

## Waarom kiezen voor Zonnebloem?

'Geen dag is hetzelfde,' vertelt Samira (34), die vijf jaar geleden bij Zonnebloem begon. 'Eerst werkte ik op een kantoor. Ik verdiende goed, maar ik miste het contact met mensen. Nu ga ik elke ochtend met plezier naar mijn werk. Als een kind voor het eerst zelf loopt of een nieuw woord zegt, ben ik erbij. Dat is echt bijzonder.'

Bij Zonnebloem krijg je na één jaar een vast contract, als je goed functioneert. Je kiest zelf of je 24, 28 of 32 uur per week werkt. Heb je zelf kinderen? Dan krijg je 50 procent korting op de opvang bij een van onze locaties. Daarnaast mag je elk jaar gratis een cursus volgen, bijvoorbeeld over EHBO bij kinderen of over taalontwikkeling.

## Nog geen diploma?

Je hebt een mbo-diploma Pedagogisch Medewerker nodig om bij ons te werken. Heb je dat nog niet? Geen probleem. In onze leerwerkopleiding werk je drie dagen per week op een groep en ga je één dag per week naar school. Wij betalen je opleiding en je krijgt vanaf de eerste dag salaris. Na twee jaar heb je je diploma. Je moet wel minimaal 18 jaar zijn en Nederlands spreken op minimaal B1-niveau.

## Kom kennismaken

Twijfel je nog? Kom dan een dagje meelopen op een van onze locaties. Zo zie je zelf hoe het werk eruitziet en kun je al je vragen stellen. Meld je aan via het formulier op deze website. Je hoort binnen een week van ons. Wij kijken uit naar je komst!""",
    "vragen": [
        {"id": "k1", "patroon": 1, "vraag": "Wat is het belangrijkste doel van deze tekst?",
         "opties": ["Mensen overhalen om bij Zonnebloem te gaan werken", "Ouders informeren over de opvang van hun kinderen", "Uitleggen hoe kinderen zich ontwikkelen"],
         "uitleg": "İkna eden (persuasief) bir metin: okuru doğrudan 'je' diye çağırıyor, avantajları sayıyor ve sonunda 'Kom kennismaken' diyor. Amaç okuru işe başvurmaya ikna etmek.",
         "bewijs": "Dan is een baan in de kinderopvang misschien iets voor jou."},
        {"id": "k2", "patroon": 6, "vraag": "Waarom zoekt Zonnebloem nieuwe medewerkers, volgens de tekst?",
         "opties": ["Steeds meer ouders werken allebei, waardoor er meer vraag naar opvang is", "Veel medewerkers stoppen met hun werk", "Zonnebloem opent 25 nieuwe locaties"],
         "uitleg": "'Want … en daardoor …' cümlesi sebebi veriyor. 25 lokasyon zaten var, yeni açılmıyor.",
         "bewijs": "Want steeds meer ouders werken allebei, en daardoor groeit de vraag naar opvang voor hun kinderen."},
        {"id": "k3", "patroon": 13, "vraag": "Een pedagogisch medewerker merkt dat een kind niet lekker in zijn vel zit. Wat doet zij?",
         "opties": ["Ze bespreekt het met haar collega's en met de ouders", "Ze zet het kind in een andere groep", "Ze vraagt de ouders om met het kind naar de dokter te gaan"],
         "uitleg": "'niet lekker in zijn vel zitten' = kendini iyi hissetmemek. Metin tam bu durumu soruyor ve 'Dan bespreek je dat…' diye cevap veriyor.",
         "bewijs": "Dan bespreek je dat met je collega's en met de ouders."},
        {"id": "k4", "patroon": 2, "vraag": "Waarom vertelt de schrijver over Samira?",
         "opties": ["Om te laten zien dat het werk veel voldoening geeft", "Om te laten zien dat je in de kinderopvang goed verdient", "Om uit te leggen hoe je van kantoorwerk overstapt naar de kinderopvang"],
         "uitleg": "Samira ofiste iyi kazanıyormuş ama insanlarla teması özlemiş; şimdi işine severek gidiyor. Örnek, işin tatmin edici olduğunu göstermek için.",
         "bewijs": "Nu ga ik elke ochtend met plezier naar mijn werk."},
        {"id": "k5", "patroon": 11, "vraag": "Tom (25) heeft geen diploma, maar wil graag in de kinderopvang werken. Hij spreekt Nederlands op A2-niveau. Wat geldt voor hem?",
         "opties": ["Hij moet eerst beter Nederlands leren voordat hij de leerwerkopleiding kan doen", "Hij kan meteen met de leerwerkopleiding beginnen", "Hij kan zonder diploma als pedagogisch medewerker werken", "Hij moet de leerwerkopleiding zelf betalen"],
         "uitleg": "Kişinin şartlarını metindeki koşullarla tek tek karşılaştır: yaşı uygun (18+), ama Hollandacası A2; en az B1 gerekiyor. Eğitim Zonnebloem tarafından ödeniyor.",
         "bewijs": "Je moet wel minimaal 18 jaar zijn en Nederlands spreken op minimaal B1-niveau."},
        {"id": "k6", "patroon": 17, "vraag": "Welke bewering over werken bij Zonnebloem is juist?",
         "opties": ["Je mag elk jaar gratis een cursus volgen", "Je krijgt meteen een vast contract", "Je werkt altijd 32 uur per week"],
         "uitleg": "Kalıcı sözleşme bir yıl sonra ve şartlı; saatleri kendin seçiyorsun (24, 28 veya 32). Sadece A doğru.",
         "bewijs": "Daarnaast mag je elk jaar gratis een cursus volgen, bijvoorbeeld over EHBO bij kinderen of over taalontwikkeling."},
    ],
}

T08 = {
    "id": "studiegids",
    "titel": "Studiegids Taalcentrum De Brug: praktische informatie",
    "soort": "Website",
    "domein": "educatie",
    "tekstsoort": "instructief",
    "zoektekst": True,
    "inleiding": "Deze tekst komt van de website van Taalcentrum De Brug. Lees eerst de vraag. Zoek het antwoord in de tekst.",
    "tekst": """Welkom bij Taalcentrum De Brug! Op deze pagina vind je alle praktische informatie over je cursus. Lees deze informatie goed door. Heb je daarna nog vragen? Kijk dan onder 'Wie helpt je waarmee?' bij wie je terecht kunt.

## Lestijden

Onze lessen worden op drie momenten van de dag gegeven:
- ochtend: van 9.00 tot 12.00 uur
- middag: van 13.30 tot 16.30 uur
- avond: van 19.00 tot 21.30 uur

Elke les heeft halverwege een pauze van een kwartier. Kom op tijd. Wie meer dan 15 minuten te laat komt, mag de les pas na de pauze in. Zo worden de andere cursisten niet gestoord. In de schoolvakanties zijn er geen lessen. De vakanties staan in de jaarplanning op onze website.

## Afwezigheid

Ben je ziek of kun je om een andere reden niet naar de les komen? Meld dit dan vóór het begin van de les via de app van De Brug. Lukt dat niet, bel dan de receptie. Je docent houdt bij wie er in de les aanwezig is. Om een certificaat te krijgen, moet je minimaal 80 procent van de lessen aanwezig zijn. Ben je drie keer afwezig zonder dat je het hebt gemeld? Dan nodigt de coördinator je uit voor een gesprek.

## Cursusgeld

Een dagcursus (ochtend of middag) duurt twaalf weken en kost € 350. Een avondcursus duurt ook twaalf weken en kost € 290. Je kunt het cursusgeld in één keer betalen of in drie termijnen. Kies je voor betalen in termijnen, dan betaal je € 15 extra administratiekosten. Je ontvangt de factuur per e-mail, uiterlijk een week voor de eerste les.

Betaalt je werkgever je cursus? Dan moet het formulier 'Betaling door werkgever' worden ingevuld. Dit formulier moet zowel door je werkgever als door jezelf worden ondertekend. Lever het formulier vóór de eerste les in bij de administratie. Daarna sturen wij de factuur naar je werkgever. Hebben wij het formulier niet op tijd ontvangen, dan blijf je zelf verantwoordelijk voor de betaling.

## Geld terug

Wil je stoppen met je cursus? Of je geld terugkrijgt, hangt af van het moment waarop je stopt:
- Meld je je af vóór de eerste les, dan krijg je het hele cursusgeld terug, min € 25 administratiekosten.
- Stop je na de eerste les, maar binnen twee weken na de start van de cursus, dan krijg je de helft van het cursusgeld terug.
- Stop je later, dan krijg je geen geld terug. Alleen bij ernstige ziekte kan een uitzondering worden gemaakt. Je hebt dan wel een verklaring van een arts nodig.

Terugbetaling gaat niet vanzelf. Je moet het altijd zelf aanvragen met het formulier 'Terugbetaling cursusgeld'. Dit formulier vind je op de website.

## Lesboeken

De lesboeken zitten niet in de prijs van de cursus. Je bestelt ze zelf via onze webwinkel. Cursisten van De Brug krijgen daar 10 procent korting. Je kunt ook tweedehands boeken kopen van andere cursisten: kijk hiervoor op het prikbord bij de kantine. Let op: werkboeken waarin al geschreven is, kun je in de les niet meer gebruiken.

## Computerlokaal en wifi

In het computerlokaal (lokaal 0.12) kun je zelfstandig oefenen. Het lokaal is open van maandag tot en met vrijdag van 8.30 tot 17.00 uur. Je logt in met je cursistennummer. Printen kost 10 cent per pagina. Je betaalt met printtegoed, dat je bij de receptie kunt kopen met je pinpas. Voor wifi gebruik je het netwerk 'DeBrug-Gast'. Het wachtwoord krijg je bij de receptie.

## Examens

Tijdens de cursus maak je na zes weken en aan het einde van de cursus een toets. Zo weet je hoe je ervoor staat. Wil je daarna het Staatsexamen NT2 doen? Dan moet je je daar zelf voor aanmelden; dat kan niet via De Brug. Twijfel je welk examen het beste bij je past? Maak dan een afspraak met mevrouw Van Dijk, onze coördinator examens. Zij geeft je graag advies.

## Klachten

Ben je ergens niet tevreden over? Praat er dan eerst over met je docent. Vaak is het probleem dan snel opgelost. Lukt dat niet, stuur dan binnen vier weken een schriftelijke klacht naar de coördinator. Je krijgt binnen twee weken antwoord. Ben je niet tevreden met dat antwoord, dan kun je je klacht voorleggen aan de klachtencommissie.

## Wie helpt je waarmee?

- Vragen over je rooster of over de lessen: je docent
- Vragen over betalen en facturen: de administratie (kamer 1.04, maandag tot en met donderdag van 9.00 tot 13.00 uur)
- Advies over examens of over een vervolgcursus: de coördinator examens
- Wachtwoord vergeten of printtegoed kopen: de receptie""",
    "vragen": [
        {"id": "g1", "patroon": 8, "vraag": "Ahmed heeft ochtendles. Hij komt om 9.20 uur binnen. Wanneer mag hij de les in?",
         "opties": ["Na de pauze", "Meteen", "Pas bij de volgende les"],
         "uitleg": "Ders 9.00'da başlıyor; Ahmed 20 dakika geç. 15 dakikadan fazla geç kalan ancak aradan sonra girebiliyor. Önce soruyu oku, sonra 'Lestijden' başlığını bul.",
         "bewijs": "Wie meer dan 15 minuten te laat komt, mag de les pas na de pauze in."},
        {"id": "g2", "patroon": 14, "vraag": "Lena volgt een avondcursus. Ze betaalt het cursusgeld in drie termijnen. Hoeveel betaalt ze in totaal?",
         "opties": ["€ 305", "€ 290", "€ 350", "€ 365"],
         "uitleg": "Akşam kursu 290 €; taksitle ödemede 15 € ek masraf: 290 + 15 = 305 €. 350 € gündüz kursu.",
         "bewijs": "Kies je voor betalen in termijnen, dan betaal je € 15 extra administratiekosten."},
        {"id": "g3", "patroon": 13, "vraag": "De werkgever van Johan wil zijn cursus betalen. Wat moet Johan doen?",
         "opties": ["Zorgen dat hij en zijn werkgever het formulier ondertekenen en het vóór de eerste les inleveren", "Zijn werkgever vragen de factuur van Johan te betalen", "Eerst zelf betalen en het geld later terugvragen"],
         "uitleg": "Formu hem işveren hem de kursiyer imzalamalı ve ilk dersten önce teslim edilmeli; yoksa ödeme sorumluluğu kursiyerde kalıyor.",
         "bewijs": "Dit formulier moet zowel door je werkgever als door jezelf worden ondertekend."},
        {"id": "g4", "patroon": 7, "vraag": "Fatima stopt met haar cursus in de tweede week, na de eerste les. Wat gebeurt er?",
         "opties": ["Ze krijgt de helft van het cursusgeld terug als ze dat aanvraagt", "Ze krijgt het hele cursusgeld terug, min € 25", "Ze krijgt automatisch de helft van het cursusgeld terug"],
         "uitleg": "İlk dersten sonra ve iki hafta içinde: yarısı geri. Ama iade kendiliğinden olmuyor ('gaat niet vanzelf'); C bu yüzden yanlış.",
         "bewijs": "Stop je na de eerste les, maar binnen twee weken na de start van de cursus, dan krijg je de helft van het cursusgeld terug."},
        {"id": "g5", "patroon": 9, "vraag": "Mei Ling wil weten welk staatsexamen het beste bij haar past. Bij wie kan ze terecht?",
         "opties": ["Bij de coördinator examens", "Bij haar docent", "Bij de administratie"],
         "uitleg": "Hem 'Examens' bölümünde hem de 'Wie helpt je waarmee?' listesinde: sınav tavsiyesi = coördinator examens.",
         "bewijs": "Maak dan een afspraak met mevrouw Van Dijk, onze coördinator examens."},
        {"id": "g6", "patroon": 12, "vraag": "Welke regel geldt voor printen in het computerlokaal?",
         "opties": ["Je betaalt met printtegoed dat je bij de receptie koopt", "Printen is gratis voor cursisten", "Je kunt alleen printen met je pinpas in het lokaal"],
         "uitleg": "Sayfa başı 10 sent; ödeme resepsiyondan pinpas ile alınan baskı kredisiyle. Pinpas lokalde değil, resepsiyonda kullanılıyor.",
         "bewijs": "Je betaalt met printtegoed, dat je bij de receptie kunt kopen met je pinpas."},
        {"id": "g7", "patroon": 13, "vraag": "Karel heeft een klacht over zijn docent. Een gesprek met de docent heeft niet geholpen. Wat moet hij nu doen?",
         "opties": ["Binnen vier weken een schriftelijke klacht sturen naar de coördinator", "Zijn klacht meteen voorleggen aan de klachtencommissie", "Zijn klacht melden bij de receptie"],
         "uitleg": "Sıra: önce öğretmen → sonra dört hafta içinde koordinatöre yazılı şikâyet → hâlâ memnun değilse şikâyet komisyonu.",
         "bewijs": "Lukt dat niet, stuur dan binnen vier weken een schriftelijke klacht naar de coördinator."},
    ],
}

TEKSTEN = [T07, T08]
