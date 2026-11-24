"""Lezen I practice text 13: a loose text at real exam length (not in a practice exam yet).
Format: see t01_t03.py. Uses the new question patterns 18-20 (section summary, what changed, which part) and two
application questions, like the official exams. Waiting-list items used: desnoods, onderling, door de bomen het bos
niet meer zien, laagdrempelig, eens kijken of, (niet) uit het oog verliezen.
The rules on zorgverlof follow Dutch law as we know it (mid 2026); Rijnstad, the amount and the phone number are made up.
"""

T13 = {
    "id": "mantelzorg",
    "titel": "Mantelzorg: zorg voor een ander, maar ook voor jezelf",
    "soort": "Website gemeente",
    "domein": "overig",
    "tekstsoort": "descriptief",
    "inleiding": "Deze tekst staat op de website van de gemeente Rijnstad. De tekst gaat over mantelzorg: zorgen voor iemand in je omgeving die hulp nodig heeft.",
    "tekst": """## I. Wat is mantelzorg?

Zorgt u voor iemand in uw omgeving die ziek is, een beperking heeft of oud is? Dan bent u mantelzorger. U doet dat niet omdat het uw werk is, maar omdat de ander uw partner, ouder, kind, buur of vriend is. U krijgt er geen geld voor. In Nederland zijn ruim vier miljoen mantelzorgers. Velen van hen zien zichzelf niet zo. 'Ik help mijn moeder gewoon met boodschappen en met de post,' zeggen ze dan. Maar ook dat is mantelzorg. Mantelzorg is iets anders dan vrijwilligerswerk. Een vrijwilliger kiest er zelf voor om te helpen, vaak via een organisatie. Een mantelzorger heeft die keuze meestal niet: de zorg komt op zijn pad omdat iemand van wie hij houdt hulp nodig heeft. Indien u langer dan drie maanden of meer dan acht uur per week voor iemand zorgt, kunt u bij de gemeente extra hulp krijgen.

## II. Werk en mantelzorg

Veel mantelzorgers hebben ook een baan. Het is niet altijd makkelijk om die twee te combineren. Als werknemer heeft u daarom recht op zorgverlof. Er zijn twee soorten.
- Kortdurend zorgverlof is bedoeld voor korte periodes, bijvoorbeeld als uw kind of partner plotseling ziek wordt. U mag per twaalf maanden maximaal twee keer het aantal uren nemen dat u in een week werkt. Uw werkgever betaalt tijdens dit verlof minimaal 70 procent van uw loon door. Meld het verlof zo snel mogelijk, desnoods op dezelfde dag.
- Langdurend zorgverlof is voor een langere periode, bijvoorbeeld als een familielid ernstig ziek is. U mag per twaalf maanden maximaal zes keer het aantal uren nemen dat u in een week werkt. Dit verlof is onbetaald, tenzij er in uw cao iets anders staat. U vraagt het minimaal twee weken van tevoren schriftelijk aan.

Uw werkgever mag het verlof alleen weigeren als het bedrijf daardoor in ernstige problemen komt. Bespreek het daarom op tijd met uw leidinggevende. Vaak kunt u onderling ook andere afspraken maken, zoals tijdelijk thuiswerken of andere werktijden.

## III. Steunpunt Mantelzorg

Weet u niet waar u moet beginnen? Er zijn zoveel regels en loketten dat veel mantelzorgers door de bomen het bos niet meer zien. Het Steunpunt Mantelzorg in het wijkcentrum helpt u daarbij. Het steunpunt is laagdrempelig: u hoeft geen afspraak te maken en u hoeft niets te betalen. Kom gewoon langs tijdens het inloopspreekuur op dinsdag- en donderdagochtend van 9.30 tot 12.00 uur. Liever een gesprek bij u thuis? Bel dan 0900-1234 voor een afspraak. Een medewerker gaat samen met u eens kijken of u recht heeft op hulp, bijvoorbeeld van de thuiszorg of van een vrijwilliger die een middag per week de zorg overneemt.

## IV. Wat is er veranderd?

Vroeger moest u het mantelzorgcompliment aanvragen met een papieren formulier dat u bij het stadhuis kon ophalen. Dat is een bedrag van 200 euro per jaar als bedankje van de gemeente. Sinds 1 januari vraagt u het aan via de website van de gemeente; u logt in met DigiD. Het bedrag is hetzelfde gebleven. Nieuw is dat de persoon voor wie u zorgt het formulier niet meer hoeft te ondertekenen. Lukt het u niet online? Dan helpt een medewerker van het steunpunt u.

## V. Vergeet uzelf niet

Mantelzorg geeft vaak voldoening, maar het kan ook zwaar zijn. Een op de tien mantelzorgers voelt zich overbelast. Verlies daarom uw eigen gezondheid niet uit het oog. Sommige mantelzorgers voelen zich schuldig als ze even iets voor zichzelf doen. Dat is niet nodig. Neem regelmatig rust en vraag hulp aan familie of vrienden. Merkt u dat u slecht slaapt of snel boos wordt? Praat er dan over met uw huisarts of met het steunpunt. Zij kunnen een vrijwilliger regelen, zodat u een dagje vrij kunt nemen. Want alleen als u goed voor uzelf zorgt, kunt u ook goed voor een ander blijven zorgen.""",
    "vragen": [
        {"id": "mz1", "patroon": 1, "vraag": "Wat is het belangrijkste doel van deze tekst?",
         "opties": ["mantelzorgers informeren over regels en hulp", "mantelzorgers overtuigen om minder te werken",
                    "werkgevers uitleggen hoe zij zorgverlof moeten geven", "inwoners enthousiast maken om mantelzorger te worden"],
         "uitleg": "Metin türü: belediye web sitesi, bilgi veriyor (izin kuralları, destek noktası, başvuru). Kimseyi ikna etmiyor ya da heveslendirmiyor; işverenlere değil 'u' diye bakıcının kendisine yazılmış.",
         "bewijs": "Zorgt u voor iemand in uw omgeving die ziek is, een beperking heeft of oud is?"},
        {"id": "mz2", "patroon": 18, "vraag": "Welke samenvatting past het best bij deel II?",
         "opties": ["Werknemers die voor iemand zorgen, kunnen verlof krijgen; kort verlof is deels betaald, lang verlof meestal niet.",
                    "Werknemers krijgen altijd hun hele loon als zij voor een familielid zorgen.",
                    "De werkgever bepaalt zelf of een werknemer zorgverlof krijgt.",
                    "Mantelzorgers kunnen het beste thuiswerken."],
         "uitleg": "II. bölümün ana fikri: iki tür bakım izni var; kısa olanda en az %70 ödenir, uzun olan ücretsiz. B yanlış ('altijd hele loon' değil, %70). C yanlış: işveren sadece ciddi sorun varsa reddedebilir. D sadece bir ayrıntı (onderling afspraken).",
         "bewijs": "Als werknemer heeft u daarom recht op zorgverlof."},
        {"id": "mz3", "patroon": 11, "vraag": "Samira werkt 30 uur per week. Haar zoon is plotseling ziek en zij wil drie dagen thuisblijven. Wat geldt voor haar?",
         "opties": ["Zij krijgt kortdurend zorgverlof en ontvangt minimaal 70 procent van haar loon.",
                    "Zij krijgt langdurend zorgverlof en moet het twee weken van tevoren aanvragen.",
                    "Zij krijgt kortdurend zorgverlof, maar geen loon.",
                    "Zij moet een vrije dag opnemen, want zorgverlof is alleen voor partners."],
         "uitleg": "Uygulama sorusu: Samira'nın durumu = ani hastalık, kısa süre → kortdurend zorgverlof. 3 gün = 24 saat, sınır 2 × 30 = 60 saat, yani yeter. Bu izinde maaşın en az %70'i ödenir. B uzun izin kuralı, C ödeme kuralını karıştırıyor, D metinde yok (çocuk da sayılır).",
         "bewijs": "Uw werkgever betaalt tijdens dit verlof minimaal 70 procent van uw loon door."},
        {"id": "mz4", "patroon": 11, "vraag": "Mehmet werkt elke ochtend. Hoe kan hij het beste met iemand van het steunpunt praten?",
         "opties": ["Bellen voor een afspraak voor een gesprek bij hem thuis.",
                    "Op dinsdagochtend naar het inloopspreekuur gaan.",
                    "Op donderdagmiddag naar het inloopspreekuur gaan.",
                    "Een e-mail sturen naar de gemeente."],
         "uitleg": "Kişinin durumunu not et: Mehmet sabahları çalışıyor. Randevusuz görüşme sadece salı ve perşembe SABAHI (9.30–12.00), yani ona uymuyor. Öğleden sonra randevusuz görüşme yok (C tuzak). Tek yol: arayıp evde görüşme için randevu almak.",
         "bewijs": "Bel dan 0900-1234 voor een afspraak."},
        {"id": "mz5", "patroon": 19, "vraag": "Wat is er veranderd aan het mantelzorgcompliment?",
         "opties": ["U vraagt het nu online aan en de persoon voor wie u zorgt, hoeft niet meer te tekenen.",
                    "Het bedrag is hoger geworden.",
                    "U haalt het formulier nu op bij het wijkcentrum.",
                    "U krijgt het nu alleen als u meer dan acht uur per week zorgt."],
         "uitleg": "Eskiden: kâğıt form, belediye binasından alınıyordu. Şimdi: internetten DigiD ile, bakılan kişinin imzası gerekmiyor. Tutar aynı kaldı (B yanlış). C eski ile yeniyi karıştırıyor; D'deki 'sekiz saat' I. bölümdeki başka bir kuraldan alınmış.",
         "bewijs": "Nieuw is dat de persoon voor wie u zorgt het formulier niet meer hoeft te ondertekenen."},
        {"id": "mz6", "patroon": 5, "vraag": "Wat wordt in deel III bedoeld met 'door de bomen het bos niet meer zien'?",
         "opties": ["Er is zoveel informatie dat mantelzorgers het overzicht kwijt zijn.",
                    "Mantelzorgers hebben geen tijd om naar buiten te gaan.",
                    "Mantelzorgers weten niet waar het wijkcentrum is.",
                    "De regels zijn duidelijk, maar er zijn te weinig loketten."],
         "uitleg": "Deyimi cümlenin tamamıyla oku: 'zoveel regels en loketten' → o kadar çok ayrıntı var ki bütünü göremiyorsun. Ağaç ve orman gerçek anlamda değil (B tuzak). D tersini söylüyor.",
         "bewijs": "Er zijn zoveel regels en loketten dat veel mantelzorgers door de bomen het bos niet meer zien."},
        {"id": "mz7", "patroon": 20, "vraag": "In welk deel staat informatie over wat u kunt doen als u zich zelf niet goed voelt?",
         "opties": ["deel V", "deel I", "deel II", "deel III"],
         "uitleg": "Bölüm başlıklarına bak: 'Vergeet uzelf niet' = kendini unutma. Kötü uyku, çabuk sinirlenme ve kendi sağlığın V. bölümde anlatılıyor.",
         "bewijs": "Verlies daarom uw eigen gezondheid niet uit het oog."},
    ],
}

TEKSTEN = [T13]
