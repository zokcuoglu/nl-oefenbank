"""Lezen A2 practice texts 1-8 = practice exam 1 (own texts in the style of the A2 inburgeringsexamen Lezen;
all names, places and organisations are made up).

A2 texts are short everyday texts: e-mails, letters, timetables, websites, forms, rules, messages.
Same text format as the B1 texts (see scripts/content/lezen/t01_t03.py): '## ' heading, '- ' list,
' | ' table rows (first row = header), 'kop' = e-mail header lines.
Questions: 3 options, right one first (the page shuffles), 'uitleg' in Turkish, 'bewijs' = exact sentence
(or table row) from the text that gives the answer, 'patroon' = question pattern number in data/lezen-bank.json.
"""

A01 = {
    "id": "a2-schoolreis",
    "titel": "Schoolreisje naar de dierentuin",
    "soort": "E-mail van school",
    "inleiding": "Deze e-mail krijgen de ouders van groep 4 van basisschool De Regenboog.",
    "kop": ["Van: juf Anouk (groep 4)", "Aan: ouders groep 4", "Onderwerp: schoolreisje"],
    "tekst": """Beste ouders,

Op dinsdag 12 mei gaat groep 4 op schoolreis naar de dierentuin. We vertrekken om 8.30 uur met de bus. We zijn om 15.00 uur weer terug bij school.

Uw kind neemt zelf een lunchpakket en iets te drinken mee. Snoep is niet nodig. Wilt u uw kind makkelijke schoenen en een regenjas geven?

Het schoolreisje kost € 15. U kunt dit tot 1 mei betalen via de app van school.

We zoeken nog twee ouders die mee willen gaan. Heeft u tijd? Stuur dan een berichtje naar juf Anouk.

Met vriendelijke groet,
Juf Anouk""",
    "vragen": [
        {"id": "a1q1", "patroon": 1, "vraag": "Waarom stuurt juf Anouk deze e-mail?",
         "opties": ["Om de ouders te informeren over het schoolreisje", "Om te vragen of de kinderen naar de dierentuin willen", "Om te zeggen dat het schoolreisje niet doorgaat"],
         "uitleg": "E-postanın tamamı okul gezisinin bilgisini veriyor: tarih, saat, ne getirilecek, fiyat. Amaç bilgilendirmek.",
         "bewijs": "Op dinsdag 12 mei gaat groep 4 op schoolreis naar de dierentuin."},
        {"id": "a1q2", "patroon": 13, "vraag": "Wat moet uw kind meenemen?",
         "opties": ["Een lunchpakket en drinken", "Snoep en een tas", "Geld voor de bus"],
         "uitleg": "Çocuk kendi öğle yemeğini ve içeceğini getiriyor. Şeker gerekmiyor, otobüs parası da yazmıyor.",
         "bewijs": "Uw kind neemt zelf een lunchpakket en iets te drinken mee."},
        {"id": "a1q3", "patroon": 8, "vraag": "Wanneer moet u het schoolreisje uiterlijk betalen?",
         "opties": ["Op 1 mei", "Op 12 mei", "Om 15.00 uur"],
         "uitleg": "'tot 1 mei' = 1 Mayıs'a kadar. 12 Mayıs gezi günü, 15.00 dönüş saati.",
         "bewijs": "U kunt dit tot 1 mei betalen via de app van school."},
    ],
}

A02 = {
    "id": "a2-bibliotheek-tijden",
    "titel": "Openingstijden Bibliotheek Oosterhaven",
    "soort": "Rooster",
    "inleiding": "Dit rooster hangt bij de ingang van de bibliotheek.",
    "tekst": """## Openingstijden

dag | open | dicht
maandag | gesloten | gesloten
dinsdag | 10.00 uur | 18.00 uur
woensdag | 10.00 uur | 20.00 uur
donderdag | 10.00 uur | 18.00 uur
vrijdag | 10.00 uur | 17.00 uur
zaterdag | 10.00 uur | 14.00 uur
zondag | gesloten | gesloten

Op feestdagen is de bibliotheek gesloten.

Elke woensdagmiddag om 14.00 uur is er voorlezen voor kinderen tot 6 jaar. Dit is gratis.

Boeken terugbrengen kan ook als de bibliotheek dicht is. Gebruik dan de brievenbus naast de deur.""",
    "vragen": [
        {"id": "a2q1", "patroon": 8, "vraag": "Op welke dag is de bibliotheek het langst open?",
         "opties": ["Woensdag", "Dinsdag", "Zaterdag"],
         "uitleg": "Çarşamba 10.00–20.00, yani 10 saat açık. Diğer günler daha kısa.",
         "bewijs": "woensdag | 10.00 uur | 20.00 uur"},
        {"id": "a2q2", "patroon": 11, "vraag": "Fatima heeft een dochter van 4 jaar. Welke activiteit past bij haar dochter?",
         "opties": ["Voorlezen op woensdagmiddag", "Boeken terugbrengen in de brievenbus", "Op maandag naar de bibliotheek gaan"],
         "uitleg": "Çarşamba öğleden sonra 6 yaşına kadar çocuklara kitap okunuyor. 4 yaşındaki kız için uygun.",
         "bewijs": "Elke woensdagmiddag om 14.00 uur is er voorlezen voor kinderen tot 6 jaar."},
        {"id": "a2q3", "patroon": 13, "vraag": "Het is zondag. U wilt een boek terugbrengen. Wat doet u?",
         "opties": ["Ik stop het boek in de brievenbus naast de deur.", "Ik wacht tot maandag.", "Ik bel de bibliotheek."],
         "uitleg": "Pazar kapalı ama kitabı kapının yanındaki posta kutusuna atabilirsin. Pazartesi de kapalı.",
         "bewijs": "Boeken terugbrengen kan ook als de bibliotheek dicht is."},
    ],
}

A03 = {
    "id": "a2-huisarts",
    "titel": "Huisartsenpraktijk De Linde",
    "soort": "Website",
    "inleiding": "Dit staat op de website van een huisarts.",
    "tekst": """## Afspraak maken

Wilt u een afspraak maken? Bel dan elke werkdag tussen 8.00 en 10.00 uur. U kunt ook een afspraak maken via de website. Een afspraak duurt 10 minuten. Heeft u meer tijd nodig? Zeg dat dan als u belt.

## Spoed

Heeft u spoed? Bel dan het spoednummer: 071 - 555 12 34. 's Avonds en in het weekend belt u de huisartsenpost.

## Herhaalrecept

Heeft u nieuwe medicijnen nodig? Vraag dan een herhaalrecept aan via de website. U kunt de medicijnen na twee werkdagen ophalen bij de apotheek.""",
    "vragen": [
        {"id": "a3q1", "patroon": 8, "vraag": "Wanneer kunt u bellen voor een afspraak?",
         "opties": ["Op werkdagen van 8.00 tot 10.00 uur", "Elke dag de hele dag", "Alleen 's avonds"],
         "uitleg": "Randevu için hafta içi 8.00–10.00 arası aranıyor. Akşamları 'huisartsenpost' aranır, o başka.",
         "bewijs": "Bel dan elke werkdag tussen 8.00 en 10.00 uur."},
        {"id": "a3q2", "patroon": 13, "vraag": "Meneer Bakker heeft veel vragen voor de dokter. Wat moet hij doen?",
         "opties": ["Zeggen dat hij meer tijd nodig heeft als hij belt", "Twee afspraken maken via de website", "Het spoednummer bellen"],
         "uitleg": "Randevu 10 dakika. Daha fazla zaman gerekiyorsa telefonda bunu söylemek gerekiyor.",
         "bewijs": "Heeft u meer tijd nodig? Zeg dat dan als u belt."},
        {"id": "a3q3", "patroon": 14, "vraag": "Hoe lang duurt het voordat u uw medicijnen kunt ophalen?",
         "opties": ["Twee werkdagen", "Tien minuten", "Een week"],
         "uitleg": "Tekrar reçetesi isteyince ilaçlar iki iş günü sonra eczaneden alınabiliyor.",
         "bewijs": "U kunt de medicijnen na twee werkdagen ophalen bij de apotheek."},
    ],
}

A04 = {
    "id": "a2-fiets-te-koop",
    "titel": "Te koop: kinderfiets",
    "soort": "Advertentie",
    "inleiding": "Deze advertentie hangt in de supermarkt.",
    "tekst": """TE KOOP: KINDERFIETS

Blauwe kinderfiets voor een kind van 6 tot 9 jaar. De fiets is 2 jaar oud en nog in goede staat. Er zit een nieuw slot op. De bel doet het niet meer.

Prijs: € 60. Samen met de helm: € 70.

Interesse? Stuur een appje naar Karin: 06 - 123 456 78. Bellen kan na 18.00 uur.

Ophalen in Molendorp. Ik breng de fiets niet.""",
    "vragen": [
        {"id": "a4q1", "patroon": 17, "vraag": "Wat is waar over de fiets?",
         "opties": ["De bel is kapot.", "Het slot is kapot.", "De fiets is nieuw."],
         "uitleg": "'De bel doet het niet meer' = zil artık çalışmıyor. Kilit yeni, bisiklet 2 yaşında.",
         "bewijs": "De bel doet het niet meer."},
        {"id": "a4q2", "patroon": 14, "vraag": "U wilt de fiets en de helm kopen. Hoeveel betaalt u?",
         "opties": ["€ 70", "€ 60", "€ 10"],
         "uitleg": "Kaskla birlikte 70 €. 60 € sadece bisiklet.",
         "bewijs": "Samen met de helm: € 70."},
        {"id": "a4q3", "patroon": 13, "vraag": "Hoe krijgt u de fiets?",
         "opties": ["U haalt hem zelf op in Molendorp.", "Karin brengt hem naar uw huis.", "U haalt hem op in de supermarkt."],
         "uitleg": "Bisikleti Molendorp'tan kendin alıyorsun; Karin getirmiyor.",
         "bewijs": "Ophalen in Molendorp."},
    ],
}

A05 = {
    "id": "a2-afval",
    "titel": "Nieuwe afvalbakken",
    "soort": "Brief van de gemeente",
    "inleiding": "Deze brief krijgen alle bewoners van de wijk Zuid.",
    "tekst": """Beste bewoner,

Vanaf 1 maart krijgt u nieuwe afvalbakken. U krijgt een groene bak voor groente, fruit en tuinafval en een blauwe bak voor papier. Plastic en blik doet u in een oranje zak. Deze zakken haalt u gratis bij het servicepunt in het wijkcentrum.

## Wanneer halen wij het afval op?

- groene bak: elke dinsdag
- blauwe bak: elke eerste vrijdag van de maand
- oranje zakken: elke donderdag

Zet uw bak of zak vóór 7.30 uur aan de straat.

## De oude bak

Uw oude grijze bak halen wij in de week van 4 maart op. Zet hem die week aan de straat. Doe er geen afval meer in.

Heeft u vragen? Bel de gemeente op 14 077.""",
    "vragen": [
        {"id": "a5q1", "patroon": 12, "vraag": "Waar doet u een lege fles van plastic in?",
         "opties": ["In een oranje zak", "In de blauwe bak", "In de groene bak"],
         "uitleg": "Plastik ve teneke turuncu torbaya. Mavi kutu kâğıt, yeşil kutu sebze-meyve için.",
         "bewijs": "Plastic en blik doet u in een oranje zak."},
        {"id": "a5q2", "patroon": 9, "vraag": "Waar kunt u oranje zakken krijgen?",
         "opties": ["Bij het servicepunt in het wijkcentrum", "In de supermarkt", "Bij de vuilniswagen"],
         "uitleg": "Turuncu torbalar mahalle merkezindeki servis noktasından ücretsiz alınıyor.",
         "bewijs": "Deze zakken haalt u gratis bij het servicepunt in het wijkcentrum."},
        {"id": "a5q3", "patroon": 8, "vraag": "Wanneer wordt het papier opgehaald?",
         "opties": ["Elke eerste vrijdag van de maand", "Elke dinsdag", "Elke donderdag"],
         "uitleg": "Kâğıt = mavi kutu, ayın ilk cuması toplanıyor.",
         "bewijs": "blauwe bak: elke eerste vrijdag van de maand"},
        {"id": "a5q4", "patroon": 13, "vraag": "Wat moet u doen met uw oude grijze bak?",
         "opties": ["In de week van 4 maart leeg aan de straat zetten", "Zelf naar het wijkcentrum brengen", "Houden voor het tuinafval"],
         "uitleg": "Eski gri kutuyu 4 Mart haftasında boş olarak sokağa koyuyorsun; belediye alıyor.",
         "bewijs": "Uw oude grijze bak halen wij in de week van 4 maart op."},
    ],
}

A06 = {
    "id": "a2-sportclub",
    "titel": "Aanmelden bij Sportclub Vooruit",
    "soort": "Formulier",
    "inleiding": "Dit is een deel van een formulier van een sportclub.",
    "tekst": """## Aanmeldformulier

Vul dit formulier in en geef het aan de trainer. U kunt het ook mailen naar info@vooruit-sport.nl.

Voornaam: ...
Achternaam: ...
Geboortedatum: ...
Adres: ...
Telefoonnummer: ...

Welke sport kiest u? Kies één sport.
- voetbal (zaterdag)
- zwemmen (woensdag)
- judo (maandag)

## Kosten

Kinderen tot 12 jaar betalen € 10 per maand. Vanaf 12 jaar betaalt u € 15 per maand. De eerste twee lessen zijn gratis. Daarna betaalt u elke maand.

Handtekening ouder (voor kinderen tot 18 jaar): ...""",
    "vragen": [
        {"id": "a6q1", "patroon": 13, "vraag": "Wat moet u doen met het formulier?",
         "opties": ["Aan de trainer geven of mailen", "Opsturen naar het gemeentehuis", "Zelf bewaren"],
         "uitleg": "Formu antrenöre veriyorsun ya da e-postayla gönderiyorsun.",
         "bewijs": "Vul dit formulier in en geef het aan de trainer."},
        {"id": "a6q2", "patroon": 14, "vraag": "Yusuf is 14 jaar. Hoeveel betaalt hij per maand?",
         "opties": ["€ 15", "€ 10", "Niets"],
         "uitleg": "12 yaşından itibaren ayda 15 €. Sadece ilk iki ders ücretsiz.",
         "bewijs": "Vanaf 12 jaar betaalt u € 15 per maand."},
        {"id": "a6q3", "patroon": 12, "vraag": "Wie moet het formulier van Yusuf tekenen?",
         "opties": ["Een ouder", "De trainer", "Yusuf zelf"],
         "uitleg": "18 yaşından küçükler için ebeveyn imzası gerekiyor.",
         "bewijs": "Handtekening ouder (voor kinderen tot 18 jaar): ..."},
    ],
}

A07 = {
    "id": "a2-zwembad",
    "titel": "Regels in zwembad De Golf",
    "soort": "Regels",
    "inleiding": "Deze regels hangen bij de ingang van het zwembad.",
    "tekst": """## Welkom in zwembad De Golf!

- Douche altijd voordat u gaat zwemmen.
- Kinderen zonder zwemdiploma mogen alleen zwemmen met een volwassene erbij.
- Rennen is niet toegestaan.
- Eten en drinken mag alleen in het café.
- Gebruik een kluisje voor uw spullen. U heeft een munt van € 1 nodig. U krijgt de munt terug.

Wij zijn niet verantwoordelijk voor spullen die u kwijtraakt.""",
    "vragen": [
        {"id": "a7q1", "patroon": 12, "vraag": "Wat moet u doen voordat u gaat zwemmen?",
         "opties": ["Douchen", "Eten in het café", "Een munt kopen"],
         "uitleg": "Yüzmeden önce her zaman duş almak gerekiyor.",
         "bewijs": "Douche altijd voordat u gaat zwemmen."},
        {"id": "a7q2", "patroon": 8, "vraag": "Wanneer mag een kind zonder zwemdiploma zwemmen?",
         "opties": ["Als er een volwassene bij is", "Als het ouder is dan 6 jaar", "Nooit"],
         "uitleg": "Diploması olmayan çocuk yanında bir yetişkin varsa yüzebilir.",
         "bewijs": "Kinderen zonder zwemdiploma mogen alleen zwemmen met een volwassene erbij."},
        {"id": "a7q3", "patroon": 17, "vraag": "Wat is waar over het kluisje?",
         "opties": ["U krijgt uw euro later terug.", "Het kluisje kost € 1.", "U kunt geen kluisje gebruiken."],
         "uitleg": "Dolap için 1 €'luk jeton gerekiyor ama jeton geri geliyor; yani dolap aslında ücretsiz.",
         "bewijs": "U krijgt de munt terug."},
    ],
}

A08 = {
    "id": "a2-pakketje",
    "titel": "Bericht van de buurvrouw",
    "soort": "Appbericht",
    "inleiding": "Mevrouw Jansen stuurt een bericht aan haar buurman Ali.",
    "tekst": """Hoi Ali,

Vanmiddag is er een pakketje voor jou bij mij bezorgd. Je was niet thuis. Ik ben vanavond na 19.00 uur thuis. Kom je het dan halen?

Morgen ga ik een week op vakantie. Als je het vanavond niet kunt halen, leg ik het pakketje bij je andere buren, op nummer 14.

Groetjes,
Ria Jansen (nummer 10)""",
    "vragen": [
        {"id": "a8q1", "patroon": 1, "vraag": "Waarom stuurt mevrouw Jansen dit bericht?",
         "opties": ["Ze heeft een pakketje voor Ali.", "Ze vraagt Ali om op haar huis te passen.", "Ze nodigt Ali uit voor het eten."],
         "uitleg": "Komşu Ria, Ali'ye gelen paketi aldığını haber veriyor.",
         "bewijs": "Vanmiddag is er een pakketje voor jou bij mij bezorgd."},
        {"id": "a8q2", "patroon": 8, "vraag": "Wanneer kan Ali het pakketje bij mevrouw Jansen halen?",
         "opties": ["Vanavond na 19.00 uur", "Morgen", "Over een week"],
         "uitleg": "Ria bu akşam 19.00'dan sonra evde. Yarın tatile gidiyor.",
         "bewijs": "Ik ben vanavond na 19.00 uur thuis."},
        {"id": "a8q3", "patroon": 7, "vraag": "Wat gebeurt er als Ali vanavond niet kan komen?",
         "opties": ["Het pakketje gaat naar de buren op nummer 14.", "Het pakketje gaat terug.", "Mevrouw Jansen neemt het mee op vakantie."],
         "uitleg": "Ali bu akşam gelemezse Ria paketi 14 numaradaki komşulara bırakacak.",
         "bewijs": "Als je het vanavond niet kunt halen, leg ik het pakketje bij je andere buren, op nummer 14."},
    ],
}

TEKSTEN = [A01, A02, A03, A04, A05, A06, A07, A08]
