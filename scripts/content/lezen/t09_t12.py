"""Lezen I practice texts 9-12 for practice exam 2 (own texts in exam style; all names and places are made up).
Format: see t01_t03.py. t12 is the long 'search' text (read the question first, then look up the answer).
"""

T09 = {
    "id": "thuiswerken",
    "titel": "Thuiswerken: vrijheid of eenzaamheid?",
    "soort": "Tijdschriftartikel",
    "domein": "werk",
    "tekstsoort": "beschouwend",
    "inleiding": "Deze tekst komt uit een tijdschrift over werk. De tekst gaat over thuiswerken: werken vanuit je eigen huis in plaats van op kantoor.",
    "tekst": """Sinds een paar jaar werken veel meer Nederlanders een deel van de week thuis. Voor sommigen is dat een droom: geen file, geen lange reistijd en meer tijd voor het gezin. Voor anderen is het juist moeilijk. Zij missen hun collega's en merken dat werk en privé door elkaar gaan lopen. Is thuiswerken nu goed of slecht? Het antwoord is minder eenvoudig dan het lijkt.

## De voordelen

Wie thuiswerkt, bespaart vaak veel tijd. Ingrid de Wit (41), beleidsmedewerker bij een gemeente, werkte vroeger elke dag op kantoor. 'Ik zat elke dag twee uur in de auto. Nu werk ik drie dagen thuis en heb ik die tijd voor mezelf. Ik ga 's ochtends hardlopen en ik haal de kinderen zelf van school.' Ook kan ze zich thuis beter concentreren, zegt ze. 'Op kantoor werd ik steeds gestoord. Thuis kan ik rustig een rapport schrijven.'

Werkgevers zien ook voordelen. Ze hebben minder kantoorruimte nodig en kunnen medewerkers aannemen die ver weg wonen. Bovendien zijn thuiswerkers volgens sommige onderzoeken minder vaak ziek.

## De nadelen

Toch is niet iedereen positief. Arbeidspsycholoog Mark Visser waarschuwt voor de nadelen. 'Thuiswerkers werken vaak langer dan ze zouden moeten. De laptop staat op de keukentafel, dus je kijkt 's avonds nog even naar je mail. Zo ben je nooit echt vrij.' Daarnaast ziet hij dat vooral jonge werknemers last hebben van eenzaamheid. 'Wie net begint, leert veel van collega's. Je ziet hoe zij problemen oplossen en je kunt even iets vragen bij het koffieapparaat. Thuis mis je dat.'

Ook de werkplek zelf is niet altijd goed. Niet iedereen heeft een aparte werkkamer. 'Veel mensen werken aan een te lage tafel of op de bank,' zegt Visser. 'Dat geeft na een tijd rug- en nekklachten.'

## Een goede balans

Volgens Visser is de oplossing niet om thuiswerken te verbieden, maar om goede afspraken te maken. 'Spreek met je team af op welke dagen iedereen op kantoor is. Zo zie je elkaar regelmatig. En zorg thuis voor een vaste werkplek en vaste werktijden. Klap na je werk je laptop dicht.' Werkgevers kunnen daarbij helpen, bijvoorbeeld door een goede bureaustoel te betalen of een vergoeding voor de internetkosten te geven.

Ingrid herkent dat. 'In het begin werkte ik thuis tot laat in de avond. Nu heb ik met mezelf afgesproken: om half zes is het klaar. En op dinsdag en donderdag ga ik naar kantoor, want dan zijn mijn collega's er ook. Die dagen zijn eigenlijk het gezelligst van de week.'""",
    "vragen": [
        {"id": "w1", "patroon": 3, "vraag": "Wat is de belangrijkste conclusie van de tekst?",
         "opties": ["Thuiswerken gaat goed als je er duidelijke afspraken over maakt", "Thuiswerken is slecht voor je gezondheid", "Werkgevers moeten thuiswerken verbieden"],
         "uitleg": "Son bölüm ('Een goede balans') sonucu veriyor: yasaklamak değil, iyi anlaşmalar yapmak. B sadece bir dezavantaj, C metinde açıkça reddediliyor.",
         "bewijs": "Volgens Visser is de oplossing niet om thuiswerken te verbieden, maar om goede afspraken te maken."},
        {"id": "w2", "patroon": 6, "vraag": "Waarom vindt Ingrid thuiswerken prettig, volgens de tekst?",
         "opties": ["Ze reist minder en kan zich thuis beter concentreren", "Ze verdient meer geld", "Ze ziet haar collega's vaker"],
         "uitleg": "İki sebep: yolda geçen iki saat kazanıyor ve evde daha iyi odaklanıyor.",
         "bewijs": "Thuis kan ik rustig een rapport schrijven."},
        {"id": "w3", "patroon": 5, "vraag": "Wat bedoelt Visser met 'Zo ben je nooit echt vrij'?",
         "opties": ["Thuiswerkers blijven ook in hun vrije tijd met hun werk bezig", "Thuiswerkers mogen hun werktijden niet zelf kiezen", "Thuiswerkers moeten vaker naar kantoor"],
         "uitleg": "Önceki cümle açıklıyor: laptop mutfak masasında, akşam yine e-postaya bakıyorsun. Yani iş ile serbest zaman ayrılmıyor.",
         "bewijs": "De laptop staat op de keukentafel, dus je kijkt 's avonds nog even naar je mail."},
        {"id": "w4", "patroon": 4, "vraag": "Wat staat er in de tekst over jonge werknemers?",
         "opties": ["Ze missen het leren van collega's als ze thuiswerken", "Ze werken het liefst thuis", "Ze hebben vaker last van hun rug"],
         "uitleg": "Genç çalışanlar yalnızlıktan şikâyetçi; yeni başlayan biri iş arkadaşlarından çok şey öğreniyor ve evde bunu kaçırıyor.",
         "bewijs": "Daarnaast ziet hij dat vooral jonge werknemers last hebben van eenzaamheid."},
        {"id": "w5", "patroon": 13, "vraag": "Wat kan een werkgever volgens de tekst doen om thuiswerkers te helpen?",
         "opties": ["Een goede bureaustoel betalen", "Thuiswerken op dinsdag en donderdag verbieden", "Iedere werknemer een tweede laptop geven"],
         "uitleg": "'Werkgevers kunnen daarbij helpen, bijvoorbeeld…' cümlesi iki örnek veriyor: büro sandalyesi ve internet masrafı.",
         "bewijs": "Werkgevers kunnen daarbij helpen, bijvoorbeeld door een goede bureaustoel te betalen of een vergoeding voor de internetkosten te geven."},
        {"id": "w6", "patroon": 2, "vraag": "Waarom vertelt de schrijver aan het einde nog een keer over Ingrid?",
         "opties": ["Om te laten zien hoe het advies van Visser in de praktijk werkt", "Om te laten zien dat Ingrid liever op kantoor werkt", "Om te laten zien dat thuiswerken niet voor iedereen geschikt is"],
         "uitleg": "Ingrid tam Visser'in önerdiği şeyi yapıyor: sabit bitiş saati ve ekiple aynı ofis günleri. Örnek, tavsiyenin işe yaradığını gösteriyor.",
         "bewijs": "Nu heb ik met mezelf afgesproken: om half zes is het klaar."},
    ],
}

T10 = {
    "id": "opendag",
    "titel": "Open dag ROC Rijnstad: ontdek jouw toekomst!",
    "soort": "Website",
    "domein": "educatie",
    "tekstsoort": "persuasief",
    "inleiding": "Deze tekst komt van de website van een mbo-school. De school nodigt mensen uit voor een open dag.",
    "tekst": """Weet je nog niet wat je na de middelbare school wilt doen? Of wil je na een paar jaar werken toch nog een diploma halen? Kom dan naar de open dag van ROC Rijnstad op zaterdag 21 november. Je bent van harte welkom tussen 10.00 en 15.00 uur op onze locatie aan de Stationsweg.

## Meer dan 120 opleidingen

Bij ROC Rijnstad kun je kiezen uit meer dan 120 mbo-opleidingen, van kok tot verpleegkundige en van ICT'er tot automonteur. Tijdens de open dag kun je bij elke opleiding een kijkje nemen. Docenten en studenten vertellen je wat je leert, hoe de lessen eruitzien en welk werk je later kunt doen. Je kunt ook zelf aan de slag: in de keuken een gerecht maken, in de werkplaats een band verwisselen of in het oefenlokaal een bloeddruk meten.

## Leren én werken

Wil je liever niet de hele week op school zitten? Kies dan voor een BBL-opleiding. Je werkt dan vier dagen per week bij een leerbedrijf en gaat één dag per week naar school. Je verdient dus al salaris terwijl je leert. 'Voor mij was dat de beste keuze,' zegt Kevin (23), die de opleiding tot elektricien volgt. 'Ik heb twee kinderen, dus ik kon niet zonder inkomen. Nu werk ik bij een installatiebedrijf en over een jaar heb ik mijn diploma. Mijn baas wil me daarna graag houden.' Heb je nog geen leerbedrijf? Onze medewerkers van het Leerbanenpunt helpen je er een te vinden.

## Voor volwassenen

Ben je ouder dan 27? Ook dan kun je bij ons terecht. Speciaal voor volwassenen hebben we verkorte opleidingen, vaak in de avond. Heb je al werkervaring? Dan kun je soms vrijstelling krijgen voor een deel van de opleiding, zodat je sneller klaar bent. Vraag tijdens de open dag naar de mogelijkheden bij de stand 'Volwassenenonderwijs'.

## Nederlands nog niet goed genoeg?

Om een mbo-opleiding te kunnen volgen, moet je Nederlands minimaal op niveau B1 zijn. Is dat nog niet zo? Dan kun je eerst een schakeljaar volgen. In dat jaar leer je vooral Nederlands en maak je kennis met verschillende beroepen.

## Kom langs!

Voor de open dag hoef je je niet aan te melden. Je kunt gewoon binnenlopen. Wil je een persoonlijk gesprek met een studieadviseur? Plan dit dan vooraf via onze website, want de plekken zijn beperkt. Neem gerust je ouders, partner of een vriend mee. Wij zien je graag op 21 november!""",
    "vragen": [
        {"id": "r1", "patroon": 1, "vraag": "Wat is het belangrijkste doel van deze tekst?",
         "opties": ["Mensen overhalen om naar de open dag te komen", "Uitleggen hoe je een leerbedrijf vindt", "Informeren over de kosten van een mbo-opleiding"],
         "uitleg": "Metin okuru doğrudan davet ediyor ('Kom dan…', 'Kom langs!') ve okulun avantajlarını sayıyor: ikna edici (persuasief) bir metin.",
         "bewijs": "Kom dan naar de open dag van ROC Rijnstad op zaterdag 21 november."},
        {"id": "r2", "patroon": 11, "vraag": "Mohammed (30) werkt overdag als kok en wil zijn baan houden. Hij wil nu ook een diploma halen. Welke mogelijkheid past het best bij hem?",
         "opties": ["Een verkorte opleiding in de avond, misschien met vrijstelling", "Een schakeljaar Nederlands", "Een gewone opleiding overdag op school", "Een BBL-opleiding bij een ander bedrijf"],
         "uitleg": "Kişinin şartları: 27'den büyük, gündüz çalışıyor, iş deneyimi var. Yetişkinlere akşam kısa eğitim ve deneyim için muafiyet sunuluyor.",
         "bewijs": "Dan kun je soms vrijstelling krijgen voor een deel van de opleiding, zodat je sneller klaar bent."},
        {"id": "r3", "patroon": 2, "vraag": "Waarom vertelt de schrijver over Kevin?",
         "opties": ["Om te laten zien dat je bij BBL kunt leren en tegelijk geld kunt verdienen", "Om te laten zien dat elektricien een goed beroep is", "Om te laten zien dat je met kinderen moeilijk kunt studeren"],
         "uitleg": "Kevin örneği BBL bölümünde ve hemen önceki cümleyi destekliyor: öğrenirken maaş alıyorsun.",
         "bewijs": "Je verdient dus al salaris terwijl je leert."},
        {"id": "r4", "patroon": 13, "vraag": "Wat moet je doen als je op de open dag met een studieadviseur wilt praten?",
         "opties": ["Vooraf een gesprek plannen via de website", "Je aanmelden voor de open dag", "Naar de stand 'Volwassenenonderwijs' gaan"],
         "uitleg": "Açık güne kayıt gerekmiyor, ama danışmanla görüşme için önceden web sitesinden randevu almak lazım.",
         "bewijs": "Plan dit dan vooraf via onze website, want de plekken zijn beperkt."},
        {"id": "r5", "patroon": 8, "vraag": "Wanneer kun je een mbo-opleiding volgen, volgens de tekst?",
         "opties": ["Als je Nederlands minimaal op niveau B1 is", "Als je ouder bent dan 27", "Als je eerst een schakeljaar hebt gedaan"],
         "uitleg": "Koşul cümlesi: 'Om … te kunnen volgen, moet je …'. Schakeljaar sadece B1 olmayanlar için bir yol, şart değil.",
         "bewijs": "Om een mbo-opleiding te kunnen volgen, moet je Nederlands minimaal op niveau B1 zijn."},
    ],
}

T11 = {
    "id": "verlof",
    "titel": "Vakantie en verlof",
    "soort": "Personeelsgids",
    "domein": "werk",
    "tekstsoort": "descriptief",
    "inleiding": "Deze tekst komt uit de personeelsgids van een transportbedrijf. De tekst gaat over vakantie en verlof: tijd dat je niet hoeft te werken.",
    "tekst": """Iedere medewerker van Transportbedrijf Van Leeuwen heeft recht op vakantie. Bij een volledige werkweek van 38 uur heb je recht op 25 vakantiedagen per jaar. Werk je minder uren, dan krijg je naar verhouding minder dagen. Werk je bijvoorbeeld 19 uur per week, dan heb je recht op 12,5 dag.

## Vakantie aanvragen

Vraag je vakantie altijd aan via het personeelsportaal. Voor de zomervakantie (juni tot en met augustus) moet je dat uiterlijk 1 februari doen. Andere vakanties vraag je minimaal vier weken van tevoren aan. Je leidinggevende laat binnen twee weken weten of je vakantie is goedgekeurd.

In de zomer mogen maximaal drie medewerkers per afdeling tegelijk op vakantie. Willen meer mensen in dezelfde weken weg? Dan gaat de medewerker voor die vorig jaar niet in die periode op vakantie kon. Zo komt iedereen een keer aan de beurt.

## Niet opgenomen dagen

Probeer je vakantiedagen in het jaar zelf op te nemen. Rust is belangrijk, ook voor je gezondheid. Dagen die je niet opneemt, kun je meenemen naar het volgende jaar. Ze vervallen wel als je ze niet binnen zes maanden na het einde van het jaar opneemt. Vakantiedagen worden niet uitbetaald, behalve als je uit dienst gaat.

## Bijzonder verlof

Soms heb je vrij nodig om een andere reden dan vakantie. Daarvoor bestaat bijzonder verlof. Je hoeft hiervoor geen vakantiedagen te gebruiken en je krijgt gewoon je salaris. Je krijgt bijzonder verlof in de volgende situaties:
- bij je eigen huwelijk: twee dagen
- bij de geboorte van je kind (voor de partner): vijf dagen
- bij het overlijden van je partner, kind of ouder: vier dagen
- bij een verhuizing: één dag per jaar

Bijzonder verlof vraag je zo snel mogelijk aan bij je leidinggevende. Bij een verhuizing doe je dat minimaal twee weken van tevoren.

## Huisarts en tandarts

Probeer afspraken met de huisarts of tandarts zoveel mogelijk buiten je werktijd te plannen. Lukt dat niet, dan mag je ervoor weg. Je moet de uren dan wel later inhalen of er vakantie-uren voor gebruiken. Voor een bezoek aan de bedrijfsarts geldt dit niet: dat valt altijd onder werktijd.

## Ouderschapsverlof

Heb je kinderen jonger dan acht jaar? Dan kun je ouderschapsverlof opnemen. Je werkt dan een tijd minder uren om voor je kinderen te zorgen. Hoeveel uur je kunt opnemen en of je daarvoor betaald krijgt, hangt af van je situatie. Personeelszaken legt je graag uit wat de mogelijkheden zijn. Maak hiervoor een afspraak via het personeelsportaal.""",
    "vragen": [
        {"id": "l1", "patroon": 14, "vraag": "Anouk werkt 19 uur per week. Op hoeveel vakantiedagen heeft zij per jaar recht?",
         "opties": ["12,5", "19", "25"],
         "uitleg": "Metin tam bu örneği veriyor: haftada 19 saat = 12,5 gün. 25 gün tam zamanlı (38 saat) çalışanlar için.",
         "bewijs": "Werk je bijvoorbeeld 19 uur per week, dan heb je recht op 12,5 dag."},
        {"id": "l2", "patroon": 8, "vraag": "Wanneer moet je je zomervakantie uiterlijk aanvragen?",
         "opties": ["Op 1 februari", "Vier weken van tevoren", "Twee weken van tevoren"],
         "uitleg": "Yaz tatili için özel kural: en geç 1 şubat. 'Dört hafta önceden' diğer tatiller için.",
         "bewijs": "Voor de zomervakantie (juni tot en met augustus) moet je dat uiterlijk 1 februari doen."},
        {"id": "l3", "patroon": 10, "vraag": "Te veel medewerkers van één afdeling willen in dezelfde zomerweken op vakantie. Wie gaat voor?",
         "opties": ["De medewerker die vorig jaar in die periode niet weg kon", "De medewerker die de vakantie het eerst heeft aangevraagd", "De medewerker die het langst bij het bedrijf werkt"],
         "uitleg": "'Dan gaat de medewerker voor die …' cümlesi kimin öncelikli olduğunu söylüyor. Diğer iki kural metinde yok.",
         "bewijs": "Dan gaat de medewerker voor die vorig jaar niet in die periode op vakantie kon."},
        {"id": "l4", "patroon": 7, "vraag": "Wat gebeurt er met vakantiedagen die je in een jaar niet opneemt?",
         "opties": ["Je kunt ze meenemen, maar ze vervallen als je ze niet binnen zes maanden opneemt", "Ze vervallen aan het einde van het jaar", "Ze worden aan het einde van het jaar uitbetaald"],
         "uitleg": "Kullanılmayan günler bir sonraki yıla geçiyor ama altı ay içinde kullanılmazsa siliniyor. Para olarak ödenmiyor (işten ayrılma hariç).",
         "bewijs": "Ze vervallen wel als je ze niet binnen zes maanden na het einde van het jaar opneemt."},
        {"id": "l5", "patroon": 12, "vraag": "Welke regel geldt voor een afspraak bij de tandarts onder werktijd?",
         "opties": ["Je moet de uren inhalen of er vakantie-uren voor gebruiken", "Je krijgt er bijzonder verlof voor", "Het valt altijd onder werktijd"],
         "uitleg": "Diş hekimi için gidebilirsin ama saatleri telafi etmen ya da tatil saati kullanman gerekiyor. 'Her zaman çalışma saati' sadece işyeri doktoru için.",
         "bewijs": "Je moet de uren dan wel later inhalen of er vakantie-uren voor gebruiken."},
        {"id": "l6", "patroon": 6, "vraag": "Sander gaat volgende maand verhuizen. Wat geldt voor hem, volgens de tekst?",
         "opties": ["Hij krijgt één dag bijzonder verlof als hij het minimaal twee weken van tevoren aanvraagt", "Hij moet er een vakantiedag voor gebruiken", "Hij krijgt vier dagen bijzonder verlof"],
         "uitleg": "Taşınma için yılda bir gün özel izin; en az iki hafta önceden istenmeli. Dört gün, bir yakının ölümü için.",
         "bewijs": "Bij een verhuizing doe je dat minimaal twee weken van tevoren."},
    ],
}

T12 = {
    "id": "huurders",
    "titel": "Informatie voor huurders",
    "soort": "Website",
    "domein": "overig",
    "tekstsoort": "instructief",
    "zoektekst": True,
    "inleiding": "Deze tekst komt van de website van woningstichting Rijnwonen. Lees eerst de vraag. Zoek het antwoord in de tekst.",
    "tekst": """Welkom bij Rijnwonen. Op deze pagina leest u wat u moet weten over het huren van een woning bij ons: van huur betalen tot reparaties en van huisdieren tot verhuizen.

## Huur betalen

De huur moet uiterlijk op de eerste dag van de maand op onze rekening staan. De makkelijkste manier is automatische incasso: wij schrijven de huur dan elke maand rond de 28e van uw rekening af. U kunt ook zelf maandelijks overmaken. Vermeld dan altijd uw huurdersnummer.

Heeft u moeite om de huur te betalen? Wacht dan niet, maar neem zo snel mogelijk contact op met onze afdeling Huurincasso. Samen zoeken we naar een oplossing, bijvoorbeeld een betalingsregeling. Hoe eerder u belt, hoe meer we kunnen doen. Betaalt u twee maanden geen huur, dan geven wij uw dossier door aan een incassobureau. Daarvoor betaalt u extra kosten.

## Huurverhoging

Elk jaar op 1 juli kan uw huur omhooggaan. U krijgt hierover uiterlijk twee maanden van tevoren een brief. Bent u het niet eens met de huurverhoging? Dan kunt u bezwaar maken. Stuur uw bezwaar vóór 1 juli per brief of via het klantportaal.

## Reparaties

Is er iets kapot in uw woning? Wie de reparatie betaalt, hangt af van wat er kapot is.

Rijnwonen betaalt en regelt onder andere:
- reparaties aan het dak, de gevel en de dakgoten
- lekkages van leidingen in de muur of de vloer
- de cv-ketel en de mechanische ventilatie
- kapotte kozijnen en buitendeuren

U betaalt en regelt zelf onder andere:
- kleine reparaties, zoals een lekkende kraan of een kapot stopcontact
- het vervangen van lampen en van batterijen van rookmelders
- het ontstoppen van de afvoer van gootsteen, douche en wc
- schade die u of uw bezoek zelf heeft veroorzaakt

Wilt u de kleine reparaties niet zelf doen? Neem dan een onderhoudsabonnement. Voor € 4,50 per maand voeren wij deze reparaties voor u uit.

Een reparatie meldt u via het klantportaal of telefonisch op werkdagen tussen 8.30 en 17.00 uur. Bij spoed buiten kantooruren, zoals een grote lekkage of een cv-ketel die in de winter niet werkt, belt u het storingsnummer. Dit nummer is 24 uur per dag bereikbaar.

## Zelf veranderingen aanbrengen

U mag uw woning naar uw eigen smaak inrichten. Voor kleine veranderingen, zoals schilderen, behangen of een nieuwe vloer, heeft u geen toestemming nodig. Voor grotere veranderingen wel. Denk aan het plaatsen van een nieuwe keuken, het weghalen van een muur of het plaatsen van een dakkapel. Vraag hiervoor vooraf schriftelijk toestemming aan via het klantportaal. Binnen vier weken hoort u of u de verandering mag uitvoeren. Bij uw vertrek moet u sommige veranderingen weer ongedaan maken. Dat staat in de brief waarin u toestemming krijgt.

## Huisdieren

Huisdieren zijn toegestaan, zolang ze geen overlast veroorzaken voor uw buren. In appartementengebouwen moeten honden in de gemeenschappelijke ruimtes, zoals de lift en het trappenhuis, altijd aangelijnd zijn. Het houden van meer dan twee honden of katten in een appartement is niet toegestaan.

## Overlast

Heeft u last van uw buren? Praat er dan eerst zelf met hen over. Vaak weten buren niet dat ze overlast veroorzaken. Komt u er samen niet uit? Dan kunt u gratis gebruikmaken van buurtbemiddeling. Rijnwonen kan u daarvoor aanmelden. Is er sprake van ernstige overlast, zoals bedreiging, meld dit dan direct bij de politie en daarna bij ons.

## Huur opzeggen

Gaat u verhuizen? Zeg uw huurcontract dan op via het klantportaal of per brief. De opzegtermijn is één maand. U kunt op elke dag van de maand opzeggen. Ongeveer twee weken voor het einde van de huur komt een medewerker bij u langs voor een voorinspectie. Hij vertelt u dan wat u nog moet herstellen of weghalen. Op de laatste dag van de huur levert u alle sleutels in bij de eindinspectie.

## Contact

- Klantportaal: 24 uur per dag, voor reparaties, vragen en het aanpassen van uw gegevens
- Klantenservice: op werkdagen van 8.30 tot 17.00 uur
- Storingsnummer: 24 uur per dag, alleen voor spoed buiten kantooruren
- Kantoor aan de Marktstraat: alleen op afspraak""",
    "vragen": [
        {"id": "h1", "patroon": 6, "vraag": "De kraan in de keuken van Ilse lekt. Wie moet de reparatie regelen, volgens de tekst?",
         "opties": ["Ilse zelf, behalve als ze een onderhoudsabonnement heeft", "Rijnwonen, want het is een lekkage", "Het storingsnummer, want het is spoed"],
         "uitleg": "Önce soruyu oku, sonra 'Reparaties' başlığındaki iki listeye bak: sızdıran musluk kiracının listesinde. Duvar içindeki boru sızıntısı ise Rijnwonen'in işi.",
         "bewijs": "kleine reparaties, zoals een lekkende kraan of een kapot stopcontact"},
        {"id": "h2", "patroon": 13, "vraag": "Omar wil de muur tussen de keuken en de woonkamer weghalen. Wat moet hij doen?",
         "opties": ["Vooraf schriftelijk toestemming vragen via het klantportaal", "Niets, hij mag zijn woning zelf inrichten", "Het eerst aan zijn buren laten weten"],
         "uitleg": "Duvar kaldırmak 'büyük değişiklik'; önceden yazılı izin gerekiyor. Boya, duvar kâğıdı gibi küçük değişiklikler için izin gerekmiyor.",
         "bewijs": "Vraag hiervoor vooraf schriftelijk toestemming aan via het klantportaal."},
        {"id": "h3", "patroon": 14, "vraag": "Hoeveel kost het onderhoudsabonnement per jaar?",
         "opties": ["€ 54", "€ 4,50", "€ 45", "€ 50"],
         "uitleg": "Metin aylık fiyat veriyor: 4,50 € × 12 ay = 54 €. Soru 'yıllık' diye soruyor; hesap yapmayı unutma.",
         "bewijs": "Voor € 4,50 per maand voeren wij deze reparaties voor u uit."},
        {"id": "h4", "patroon": 9, "vraag": "Op een zondagavond in januari doet de cv-ketel het niet. Waar kan de huurder terecht?",
         "opties": ["Bij het storingsnummer", "Bij de klantenservice", "Bij het kantoor aan de Marktstraat"],
         "uitleg": "Kış ve mesai dışı = acil durum. Müşteri hizmetleri sadece hafta içi; ofis sadece randevuyla.",
         "bewijs": "Bij spoed buiten kantooruren, zoals een grote lekkage of een cv-ketel die in de winter niet werkt, belt u het storingsnummer."},
        {"id": "h5", "patroon": 7, "vraag": "Wat gebeurt er als een huurder twee maanden geen huur betaalt?",
         "opties": ["Het dossier gaat naar een incassobureau en de huurder betaalt extra kosten", "De huurder moet de woning meteen verlaten", "Rijnwonen maakt automatisch een betalingsregeling"],
         "uitleg": "İki ay ödenmezse dosya tahsilat bürosuna gidiyor ve ek masraf çıkıyor. Ödeme planı ancak kiracı kendisi erken ararsa.",
         "bewijs": "Betaalt u twee maanden geen huur, dan geven wij uw dossier door aan een incassobureau."},
        {"id": "h6", "patroon": 12, "vraag": "Welke regel geldt voor honden in een appartementengebouw?",
         "opties": ["In de lift en het trappenhuis moeten ze aangelijnd zijn", "Honden zijn niet toegestaan", "Je mag maximaal één hond hebben"],
         "uitleg": "Evcil hayvanlara izin var; ortak alanlarda köpek tasmalı olmalı. Daire başına en fazla iki köpek veya kedi.",
         "bewijs": "In appartementengebouwen moeten honden in de gemeenschappelijke ruimtes, zoals de lift en het trappenhuis, altijd aangelijnd zijn."},
    ],
}

TEKSTEN = [T09, T10, T11, T12]
