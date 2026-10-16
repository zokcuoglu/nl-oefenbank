"""Lezen I practice texts 4-6 (own texts in exam style; all names and places are made up). Format: see t01_t03.py."""

T04 = {
    "id": "sportschool",
    "titel": "Kies het abonnement dat bij jou past",
    "soort": "Website sportschool",
    "domein": "overig",
    "tekstsoort": "descriptief",
    "inleiding": "Deze tekst komt van de website van een sportschool. De tekst gaat over de abonnementen en de regels.",
    "tekst": """Bij sportschool FitPunt kun je sporten wanneer het jou uitkomt. We hebben drie abonnementen.

Abonnement | Wanneer sporten | Prijs per maand
Basis | maandag tot en met vrijdag, tot 16.00 uur | € 22,50
Flex | elke dag, de hele dag | € 29,95
Student | elke dag, de hele dag | € 19,95

Het Student-abonnement is alleen geldig met een studentenkaart van een mbo, hbo of universiteit. Bij alle abonnementen mag je gratis meedoen aan de groepslessen, zoals yoga en spinning. Voor een groepsles moet je je wel van tevoren aanmelden via de app.

## Inschrijven

Je schrijft je in bij de balie of online. Je betaalt eenmalig € 15 inschrijfkosten. Schrijf je je in de maand september in? Dan betaal je geen inschrijfkosten. Een abonnement loopt minimaal twaalf maanden. Daarna kun je elke maand opzeggen.

## Opzeggen en pauzeren

Wil je stoppen? Zeg je abonnement dan schriftelijk of via de app op. Er geldt een opzegtermijn van één maand. Ben je langer dan een maand ziek of ga je op reis? Dan kun je je abonnement maximaal drie maanden pauzeren. Je betaalt in die tijd niets. Vraag dit minimaal een week van tevoren aan bij de balie.

## Huisregels

Om het voor iedereen prettig te houden, gelden bij FitPunt een paar regels. Neem altijd een handdoek mee en leg die op de toestellen. Draag schone sportschoenen: buitenschoenen zijn in de zalen niet toegestaan. Maak de toestellen na gebruik schoon met de doekjes die overal klaarliggen. Kinderen onder de 16 jaar mogen alleen sporten onder begeleiding van een volwassene.

## Neem een vriend mee

Wil je samen met een vriend of vriendin sporten? Met elk abonnement mag je één keer per maand gratis iemand meenemen. Je vriend moet zich wel eerst bij de balie melden met een geldig identiteitsbewijs. Besluit je vriend daarna lid te worden, dan krijg jij een maand gratis sporten.""",
    "vragen": [
        {"id": "s1", "patroon": 11, "vraag": "Fatma werkt van 8.00 tot 16.00 uur en wil na haar werk of in het weekend sporten. Ze studeert niet. Welk abonnement past bij haar?",
         "opties": ["Flex", "Basis", "Student"],
         "uitleg": "Basis sadece hafta içi 16.00'ya kadar; Student için öğrenci kartı gerekiyor. Akşam ve hafta sonu için tek seçenek Flex.",
         "bewijs": "Flex | elke dag, de hele dag | € 29,95"},
        {"id": "s2", "patroon": 13, "vraag": "Wat moet je doen om aan een groepsles mee te doen?",
         "opties": ["Je van tevoren aanmelden via de app", "Extra betalen bij de balie", "Een Flex-abonnement nemen"],
         "uitleg": "Grup dersleri bütün abonelerde ücretsiz, ama uygulamadan önceden kayıt gerekiyor.",
         "bewijs": "Voor een groepsles moet je je wel van tevoren aanmelden via de app."},
        {"id": "s3", "patroon": 14, "vraag": "Hoeveel inschrijfkosten betaal je als je je in september inschrijft?",
         "opties": ["Niets", "€ 15", "€ 19,95"],
         "uitleg": "Normalde 15 € ama eylülde kayıt olursan kayıt ücreti yok.",
         "bewijs": "Schrijf je je in de maand september in? Dan betaal je geen inschrijfkosten."},
        {"id": "s4", "patroon": 8, "vraag": "Wanneer kun je je abonnement opzeggen?",
         "opties": ["Na de eerste twaalf maanden, elke maand", "Na één maand", "Op elk moment, via de app"],
         "uitleg": "Abonelik en az 12 ay sürüyor ('minimaal'); ondan sonra her ay iptal edilebilir. 'Bir ay' iptal için bildirim süresi.",
         "bewijs": "Een abonnement loopt minimaal twaalf maanden. Daarna kun je elke maand opzeggen."},
        {"id": "s5", "patroon": 7, "vraag": "Karim gaat twee maanden op reis. Wat kan hij doen?",
         "opties": ["Zijn abonnement pauzeren; hij betaalt dan niets", "Zijn abonnement opzeggen en later gratis opnieuw beginnen", "Zijn abonnement omzetten naar Basis"],
         "uitleg": "Seyahat ya da uzun hastalıkta en fazla üç ay dondurulabiliyor ve o sürede ödeme yok.",
         "bewijs": "Dan kun je je abonnement maximaal drie maanden pauzeren. Je betaalt in die tijd niets."},
    ],
}

T05 = {
    "id": "omscholing",
    "titel": "Op je vijftigste nog een nieuw vak leren",
    "soort": "Tijdschriftartikel",
    "domein": "educatie",
    "tekstsoort": "beschouwend",
    "inleiding": "Deze tekst komt uit een tijdschrift over werk en opleiding. De tekst gaat over omscholing: iets nieuws leren om ander werk te kunnen doen.",
    "tekst": """Marja Bakker (54) werkte dertig jaar als secretaresse bij een verzekeraar. Toen haar baan twee jaar geleden verdween, dacht ze dat haar werkende leven voorbij was. 'Wie neemt er nu iemand van boven de vijftig aan?' Inmiddels werkt ze als doktersassistent in een huisartsenpraktijk. 'Ik had nooit gedacht dat ik op mijn leeftijd nog een diploma zou halen.'

Marja is niet de enige. Steeds meer mensen kiezen op latere leeftijd voor omscholing. Volgens onderzoek van een opleidingsinstituut is het aantal cursisten boven de vijftig in vijf jaar bijna verdubbeld. Dat komt deels doordat banen in bijvoorbeeld de administratie verdwijnen, terwijl er in de zorg en het onderwijs juist veel mensen nodig zijn.

Toch is de stap niet voor iedereen makkelijk. Een opleiding kost tijd en geld, en niet iedereen kan een paar jaar met minder inkomen leven. Ook twijfelen veel oudere werknemers aan zichzelf. 'Ze denken dat ze niet meer goed kunnen leren,' zegt loopbaanadviseur Peter de Graaf. 'Maar dat is een misverstand. Ouderen leren misschien iets langzamer, maar ze hebben veel ervaring. Ze weten hoe je met mensen omgaat en hoe je problemen oplost.'

Werkgevers spelen hierbij een belangrijke rol. Sommige bedrijven betalen het cursusgeld als een werknemer zich wil laten omscholen, ook als het nieuwe beroep buiten het bedrijf ligt. 'Dat lijkt vreemd,' zegt De Graaf, 'want dan verlies je een medewerker. Maar een werknemer die met plezier werkt, is minder vaak ziek. En mensen praten positief over zo'n werkgever.'

Hoe begin je zo'n omscholing? De Graaf adviseert om eerst goed na te denken over wat je wilt en kunt. 'Kijk niet alleen naar wat je vroeger hebt gedaan, maar vooral naar wat je leuk vindt en waar je goed in bent. Praat met mensen die het werk al doen, of loop een dag mee.' Daarna is het belangrijk om te kijken naar de praktische kant. Hoe lang duurt de opleiding? Kun je ernaast blijven werken? En wie betaalt? 'Soms betaalt de werkgever, soms is er een regeling van de overheid. Vraag het in elk geval na voordat je begint.'

Ook Marja moest goed rekenen. Ze volgde haar opleiding in de avonduren en werkte overdag nog drie dagen per week als oproepkracht. 'Het was zwaar, zeker in het begin. Ik had al dertig jaar niet meer in de schoolbanken gezeten. Maar mijn klasgenoten, die vaak twintig jaar jonger waren, hielpen me met de computer. En ik hielp hen met plannen en met het contact met patiënten. Zo leerden we van elkaar.'

Volgens De Graaf is het belangrijkste dat mensen niet te lang wachten. 'Wie merkt dat zijn werk verandert of verdwijnt, moet op tijd advies vragen. Hoe eerder je begint, hoe meer keuze je hebt.'

Marja is in elk geval tevreden. 'Ik ben elke avond moe, maar gelukkig. Mijn kinderen zeggen dat ik er tien jaar jonger uitzie.'""",
    "vragen": [
        {"id": "o1", "patroon": 1, "vraag": "Wat is het belangrijkste doel van deze tekst?",
         "opties": ["Laten zien dat omscholing ook op latere leeftijd mogelijk en zinvol is", "Werkgevers overtuigen om meer ouderen aan te nemen", "Uitleggen hoe je doktersassistent wordt"],
         "uitleg": "Bütün paragraflar aynı fikri destekliyor: 50'den sonra da meslek değiştirmek mümkün ve faydalı. B ve C metinde sadece küçük ayrıntılar.",
         "bewijs": "Steeds meer mensen kiezen op latere leeftijd voor omscholing."},
        {"id": "o2", "patroon": 2, "vraag": "Wat wil de schrijver met het voorbeeld van Marja duidelijk maken?",
         "opties": ["Dat je ook na je vijftigste nog een nieuw beroep kunt leren", "Dat secretaresses vaak hun baan verliezen", "Dat werken in de zorg zwaar is"],
         "uitleg": "Örneğin hemen arkasındaki cümle cevabı veriyor: 'Marja is niet de enige' = birçok kişi geç yaşta yeniden eğitim alıyor.",
         "bewijs": "Ik had nooit gedacht dat ik op mijn leeftijd nog een diploma zou halen."},
        {"id": "o3", "patroon": 6, "vraag": "Waardoor kiezen steeds meer ouderen voor omscholing, volgens de tekst?",
         "opties": ["Er verdwijnen banen, terwijl er in andere sectoren veel mensen nodig zijn", "Ouderen leren tegenwoordig sneller", "Opleidingen zijn goedkoper geworden"],
         "uitleg": "'Dat komt deels doordat …' = sebep cümlesi. Metin opleidingen ucuzladı demiyor; tersine 'tijd en geld' kostuyor.",
         "bewijs": "Dat komt deels doordat banen in bijvoorbeeld de administratie verdwijnen, terwijl er in de zorg en het onderwijs juist veel mensen nodig zijn."},
        {"id": "o4", "patroon": 5, "vraag": "Wat wordt in alinea 3 bedoeld met 'een misverstand'?",
         "opties": ["Het idee dat ouderen niet meer goed kunnen leren, klopt niet", "Ouderen begrijpen de lessen vaak verkeerd", "Opleidingen leggen de stof niet duidelijk uit"],
         "uitleg": "'misverstand' = yanlış anlama, yanlış düşünce. Önceki cümleye bak: 'Ze denken dat ze niet meer goed kunnen leren.' Bu düşünce yanlış.",
         "bewijs": "'Ze denken dat ze niet meer goed kunnen leren,' zegt loopbaanadviseur Peter de Graaf. 'Maar dat is een misverstand."},
        {"id": "o5", "patroon": 6, "vraag": "Waarom betalen sommige werkgevers het cursusgeld, volgens De Graaf?",
         "opties": ["Tevreden werknemers zijn minder vaak ziek en het geeft de werkgever een goede naam", "Ze willen zo de werknemer in het bedrijf houden", "Het is verplicht voor werknemers boven de vijftig"],
         "uitleg": "Yeni meslek şirket dışında olsa bile ödüyorlar; yani amaç çalışanı tutmak değil. İki sebep: daha az hastalık ve iyi itibar.",
         "bewijs": "Maar een werknemer die met plezier werkt, is minder vaak ziek. En mensen praten positief over zo'n werkgever."},
        {"id": "o6", "patroon": 3, "vraag": "Wat is het belangrijkste advies van De Graaf?",
         "opties": ["Vraag op tijd advies als je werk verandert", "Wacht met omscholing tot je zeker weet dat je baan verdwijnt", "Kies altijd voor een beroep in de zorg"],
         "uitleg": "'het belangrijkste' kelimesi soruda ve metinde aynı: sonuç cümlesi 'Hoe eerder je begint, hoe meer keuze je hebt.'",
         "bewijs": "Wie merkt dat zijn werk verandert of verdwijnt, moet op tijd advies vragen."},
    ],
}

T06 = {
    "id": "buurtbemiddeling",
    "titel": "Problemen met de buren? Buurtbemiddeling helpt",
    "soort": "Folder",
    "domein": "overig",
    "tekstsoort": "instructief",
    "inleiding": "Deze tekst komt uit een folder van Buurtbemiddeling. De tekst gaat over problemen met buren.",
    "tekst": """Harde muziek, een blaffende hond of een schutting op de verkeerde plek: problemen met de buren kunnen veel stress geven. Vaak is een gesprek de beste oplossing. Maar wat als dat niet lukt? Dan kan Buurtbemiddeling Rijnstad helpen.

Uit onderzoek blijkt dat bijna de helft van de Nederlanders zich weleens ergert aan de buren. Toch praten veel mensen er niet over. Ze zijn bang dat de ruzie dan groter wordt, of ze weten niet hoe ze moeten beginnen. Het gevolg is dat de ergernis steeds groter wordt. Soms durven mensen niet meer naar buiten als de buurman in de tuin staat.

## Wat doet Buurtbemiddeling?

Twee getrainde vrijwilligers praten eerst met u en daarna met uw buren. Daarna organiseren zij een gesprek met u allebei, op een neutrale plek, bijvoorbeeld in het buurthuis. De bemiddelaars kiezen geen partij en zeggen niet wie er gelijk heeft. Ze helpen u wel om samen afspraken te maken.

## Wanneer kunt u ons inschakelen?

U kunt ons bellen als u al zelf geprobeerd heeft om met uw buren te praten. Buurtbemiddeling is niet bedoeld voor problemen met geweld of bedreiging. Neem in dat geval direct contact op met de politie. Ook bij problemen met uw huurbaas of woningcorporatie kunnen wij u niet helpen.

## Wat kost het?

Buurtbemiddeling is gratis. De gemeente betaalt de kosten. Meedoen is vrijwillig: als uw buren niet willen, kunnen wij niets doen.

## Hoe meldt u zich aan?

Bel ons op werkdagen tussen 9.00 en 17.00 uur, of vul het formulier op onze website in. Binnen twee weken neemt een bemiddelaar contact met u op. Alles wat u vertelt, blijft tussen u en de bemiddelaars.

## Een voorbeeld

Familie Bos ergerde zich al maanden aan de hond van de buren, die elke dag urenlang blafte. 'We hebben het één keer gezegd, maar toen werd de buurman boos,' vertelt mevrouw Bos. 'Daarna zeiden we niets meer tegen elkaar.' Via Buurtbemiddeling kwamen de buren toch met elkaar in gesprek. Het bleek dat de buurman niet wist hoe vaak de hond blafte, omdat hij overdag werkte. Nu brengt hij de hond twee dagen per week naar een hondenoppas. 'We groeten elkaar weer,' zegt mevrouw Bos. 'Dat had ik nooit verwacht.'""",
    "vragen": [
        {"id": "b1", "patroon": 9, "vraag": "Uw buurman bedreigt u. Bij wie kunt u terecht?",
         "opties": ["Bij de politie", "Bij Buurtbemiddeling", "Bij de woningcorporatie"],
         "uitleg": "Tehdit ve şiddet arabuluculuğun konusu değil; metin doğrudan polisi arayın diyor.",
         "bewijs": "Neem in dat geval direct contact op met de politie."},
        {"id": "b2", "patroon": 8, "vraag": "Wanneer kunt u Buurtbemiddeling inschakelen?",
         "opties": ["Als u zelf al geprobeerd heeft met uw buren te praten", "Als uw huurbaas uw huis niet repareert", "Als de politie u dat aanraadt"],
         "uitleg": "Koşul: önce kendin konuşmayı denemiş olmalısın. Ev sahibiyle sorunlar kapsam dışında.",
         "bewijs": "U kunt ons bellen als u al zelf geprobeerd heeft om met uw buren te praten."},
        {"id": "b3", "patroon": 6, "vraag": "Wat doen de bemiddelaars, volgens de tekst?",
         "opties": ["Ze helpen de buren om samen afspraken te maken", "Ze beslissen wie er gelijk heeft", "Ze geven de buren een waarschuwing"],
         "uitleg": "Arabulucular taraf tutmuyor ve kimin haklı olduğunu söylemiyor; sadece anlaşmaya yardım ediyor.",
         "bewijs": "Ze helpen u wel om samen afspraken te maken."},
        {"id": "b4", "patroon": 7, "vraag": "Wat gebeurt er als uw buren niet willen meedoen?",
         "opties": ["Dan kan Buurtbemiddeling niets doen", "Dan moeten de buren toch komen", "Dan betaalt u de kosten zelf"],
         "uitleg": "'vrijwillig' = gönüllü. Komşu istemezse hiçbir şey yapılamıyor.",
         "bewijs": "Meedoen is vrijwillig: als uw buren niet willen, kunnen wij niets doen."},
        {"id": "b5", "patroon": 14, "vraag": "Hoeveel kost Buurtbemiddeling voor u?",
         "opties": ["Niets, de gemeente betaalt", "Een klein bedrag per gesprek", "Dat hangt af van het probleem"],
         "uitleg": "'gratis' ve 'De gemeente betaalt de kosten.'",
         "bewijs": "Buurtbemiddeling is gratis. De gemeente betaalt de kosten."},
        {"id": "b6", "patroon": 17, "vraag": "Welke bewering is juist?",
         "opties": ["De bemiddelaars praten eerst met u alleen", "Het gesprek met de buren is altijd bij u thuis", "De bemiddelaars vertellen de gemeente wat u zegt"],
         "uitleg": "Önce seninle, sonra komşunla ayrı konuşuyorlar. Ortak görüşme tarafsız bir yerde; söylediklerin aranızda kalıyor.",
         "bewijs": "Twee getrainde vrijwilligers praten eerst met u en daarna met uw buren."},
    ],
}

TEKSTEN = [T04, T05, T06]
