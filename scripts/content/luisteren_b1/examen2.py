"""Luisteren B1 practice exam 2 (own texts, made-up names). Format: see examen1.py."""


def Q(id, vraag, opties, uitleg, bewijs):
    return {"id": id, "vraag": vraag, "opties": opties, "uitleg": uitleg, "bewijs": bewijs}


TEKSTEN = [
    {"id": "b1-radio-buurthuis", "intro": "U hoort een radio-interview met de beheerder van een buurthuis.", "tekst": """
m: In de studio zit Fatma Arslan. Zij is beheerder van buurthuis De Brug. Fatma, het buurthuis bestaat dit jaar twintig jaar. Wat is er veranderd?
v: Vroeger kwamen er vooral ouderen voor een kopje koffie. Nu hebben we veel meer activiteiten voor jongeren en voor gezinnen, zoals huiswerkbegeleiding en een kookclub.
m: Hoe weten mensen wat er te doen is?
v: Vroeger hingen we posters op. Nu gaat bijna alles via onze app en via de buurtgroep op WhatsApp. Maar voor ouderen leggen we nog steeds een papieren programma bij de supermarkt.
m: Wat is de grootste uitdaging?
v: Vrijwilligers vinden. Zonder vrijwilligers kunnen we niet open. We zoeken vooral mensen die één avond per week kunnen helpen.
m: En het feest voor het jubileum?
v: Dat is op zaterdag 14 september, met muziek en eten uit verschillende landen. Iedereen is welkom.""",
     "vragen": [
        Q("b1e2-1", "Wat is er veranderd in het buurthuis?", ["Er zijn meer activiteiten voor jongeren en gezinnen.", "Er komen alleen nog ouderen.", "Het buurthuis is verhuisd."],
          "Eskiden çoğunlukla yaşlılar gelirdi; şimdi gençler ve aileler için daha çok etkinlik var.", "Nu hebben we veel meer activiteiten voor jongeren en voor gezinnen"),
        Q("b1e2-2", "Hoe krijgen ouderen informatie over het programma?", ["Via een papieren programma bij de supermarkt", "Via de app", "Via posters in de bus"],
          "Yaşlılar için markette kâğıt program bırakılıyor.", "Maar voor ouderen leggen we nog steeds een papieren programma bij de supermarkt."),
        Q("b1e2-3", "Wat is volgens Fatma de grootste uitdaging?", ["Vrijwilligers vinden", "Geld voor activiteiten krijgen", "Jongeren naar het buurthuis krijgen"],
          "En büyük zorluk gönüllü bulmak.", "Vrijwilligers vinden."),
        Q("b1e2-4", "Wat is er op 14 september?", ["Een feest voor het jubileum", "Een vergadering voor vrijwilligers", "De opening van de kookclub"],
          "14 Eylül'de 20. yıl için müzikli, yemekli bir parti var.", "Dat is op zaterdag 14 september, met muziek en eten uit verschillende landen."),
     ]},
    {"id": "b1-zwembad-bericht", "intro": "U hoort een voicemailbericht van het zwembad.", "tekst": """
v: Goedemiddag, u spreekt met Marloes van zwembad De Golf. Ik bel over de zwemles van uw dochter Amira. Vanaf volgende week verandert de lestijd. De les begint dan niet meer om vier uur, maar om half vijf, omdat het bad 's middags langer nodig is voor schoolzwemmen. De les duurt nog steeds drie kwartier. Kan Amira niet op de nieuwe tijd? Dan kunt u kiezen voor de les op zaterdagochtend om negen uur. Laat u het ons voor vrijdag weten? U kunt mailen of terugbellen. Ons nummer is 071 - 523 88 10. Fijne dag nog.""",
     "vragen": [
        Q("b1e2-5", "Wat verandert er?", ["De tijd van de zwemles", "De dag van de zwemles", "De zwemleraar"],
          "Yüzme dersinin saati değişiyor: dörtten dört buçuğa.", "Vanaf volgende week verandert de lestijd."),
        Q("b1e2-6", "Waarom verandert dit?", ["Het bad is 's middags langer nodig voor schoolzwemmen.", "Er zijn te veel kinderen.", "De leraar heeft een andere baan."],
          "Havuz öğleden sonra okul yüzmesi için daha uzun süre gerekiyor.", "omdat het bad 's middags langer nodig is voor schoolzwemmen."),
        Q("b1e2-7", "Hoe lang duurt de les?", ["Drie kwartier", "Een uur", "Een half uur"],
          "Ders hâlâ 45 dakika (drie kwartier) sürüyor.", "De les duurt nog steeds drie kwartier."),
        Q("b1e2-8", "Wat moeten de ouders doen als Amira niet kan?", ["Voor vrijdag laten weten of ze de zaterdagles kiezen", "Niets, ze krijgen een nieuwe brief", "Een nieuwe zwemschool zoeken"],
          "Yeni saate uymazsa cumartesi dersini seçebilir; cumadan önce haber vermek gerekiyor.", "Laat u het ons voor vrijdag weten?"),
     ]},
    {"id": "b1-werkoverleg-thuiswerken", "intro": "U hoort een deel van een werkoverleg.", "tekst": """
m: Dan het volgende punt: thuiswerken. Er komen steeds meer vragen over. Op dit moment mag iedereen twee dagen per week thuiswerken. Vanaf maart willen we dat iedereen op dinsdag en donderdag op kantoor is. Dan kunnen teams elkaar echt zien.
v: Ik begrijp het idee, maar ik woon ver weg. Op dinsdag sta ik altijd in de file.
m: Dat snap ik. Daarom krijgen collega's die meer dan vijftig kilometer reizen een uitzondering: zij kiezen zelf hun kantoordagen.
v: Oké, dan geldt dat voor mij. En krijgen we ook iets voor thuis, zoals een goede stoel?
m: Ja, iedereen kan één keer een bedrag van driehonderd euro aanvragen voor een bureau of stoel.""",
     "vragen": [
        Q("b1e2-9", "Wat verandert er vanaf maart?", ["Iedereen moet op dinsdag en donderdag op kantoor zijn.", "Niemand mag meer thuiswerken.", "Iedereen mag drie dagen thuiswerken."],
          "Marttan itibaren herkes salı ve perşembe ofiste olmalı.", "Vanaf maart willen we dat iedereen op dinsdag en donderdag op kantoor is."),
        Q("b1e2-10", "Waarom wil de leidinggevende dit?", ["Zodat teams elkaar echt zien", "Omdat thuiswerken te duur is", "Omdat er nieuwe kantoren zijn"],
          "Ekiplerin birbirini gerçekten görmesi için.", "Dan kunnen teams elkaar echt zien."),
        Q("b1e2-11", "Voor wie geldt een uitzondering?", ["Voor collega's die meer dan vijftig kilometer reizen", "Voor collega's met kinderen", "Voor collega's die in de file staan"],
          "50 kilometreden fazla yol gidenler ofis günlerini kendileri seçiyor.", "Daarom krijgen collega's die meer dan vijftig kilometer reizen een uitzondering"),
        Q("b1e2-12", "Wat kunnen medewerkers aanvragen?", ["Eenmalig driehonderd euro voor een bureau of stoel", "Elke maand driehonderd euro", "Een gratis laptop"],
          "Herkes bir defaya mahsus masa ya da sandalye için 300 € isteyebiliyor.", "Ja, iedereen kan één keer een bedrag van driehonderd euro aanvragen voor een bureau of stoel."),
     ]},
    {"id": "b1-uitleg-zorgtoeslag", "intro": "U hoort een medewerker van een informatiepunt uitleg geven over zorgtoeslag.", "tekst": """
v: Veel mensen vragen ons naar zorgtoeslag. Zorgtoeslag is een bijdrage van de overheid in de kosten van uw zorgverzekering. Of u het krijgt, hangt af van uw inkomen. U vraagt het aan bij de Belastingdienst, op de website, met uw DigiD. Let op: geef veranderingen in uw inkomen altijd snel door. Gaat u meer verdienen en geeft u dat niet door? Dan moet u later misschien een groot bedrag terugbetalen. Twijfelt u of u recht heeft? Kom dan langs op ons spreekuur, elke maandag en woensdag van negen tot twaalf. U hoeft geen afspraak te maken. Neem wel uw loonstrook en uw DigiD-gegevens mee.""",
     "vragen": [
        Q("b1e2-13", "Wat is zorgtoeslag?", ["Een bijdrage van de overheid in de kosten van de zorgverzekering", "Een korting bij de huisarts", "Een verzekering voor mensen zonder werk"],
          "Sağlık sigortası masrafları için devletin verdiği katkı.", "Zorgtoeslag is een bijdrage van de overheid in de kosten van uw zorgverzekering."),
        Q("b1e2-14", "Waar vraagt u zorgtoeslag aan?", ["Bij de Belastingdienst, op de website", "Bij de zorgverzekeraar", "Bij het informatiepunt"],
          "Vergi dairesinin (Belastingdienst) sitesinden DigiD ile başvuruluyor.", "U vraagt het aan bij de Belastingdienst, op de website, met uw DigiD."),
        Q("b1e2-15", "Wat kan er gebeuren als u een hoger inkomen niet doorgeeft?", ["U moet later misschien veel terugbetalen.", "U krijgt een boete van de gemeente.", "U krijgt meer zorgtoeslag."],
          "Gelir artışını bildirmezsen sonra büyük bir tutarı geri ödemen gerekebilir.", "Dan moet u later misschien een groot bedrag terugbetalen."),
        Q("b1e2-16", "Wat moet u meenemen naar het spreekuur?", ["Uw loonstrook en DigiD-gegevens", "Een brief van de huisarts", "Uw paspoort en huurcontract"],
          "Maaş bordrosu ve DigiD bilgileri getirilmeli; randevu gerekmiyor.", "Neem wel uw loonstrook en uw DigiD-gegevens mee."),
     ]},
    {"id": "b1-gesprek-buren", "intro": "U hoort een gesprek tussen twee buren in een flat.", "tekst": """
v: Hoi, ik ben Joke van nummer twaalf. Mag ik je even iets vragen?
m: Ja, natuurlijk.
v: Jouw fiets staat altijd in de gang bij de liften. Daardoor kan mijn moeder met haar rollator er bijna niet langs.
m: Oh, dat wist ik niet. Sorry. In de fietsenstalling is alleen nooit plaats.
v: Dat klopt, die is altijd vol. Maar volgens mij staan er veel oude fietsen die niemand meer gebruikt. Zullen we de woningcorporatie vragen om die weg te halen?
m: Goed idee. Ik stuur vanavond een mail. En tot die tijd zet ik mijn fiets bij mij op het balkon.""",
     "vragen": [
        Q("b1e2-17", "Wat is het probleem?", ["De fiets van de man staat in de weg.", "De lift is kapot.", "De fietsenstalling is dicht."],
          "Adamın bisikleti asansörün yanındaki koridorda duruyor; kadının annesi yürüteçle geçemiyor.", "Jouw fiets staat altijd in de gang bij de liften."),
        Q("b1e2-18", "Waarom zet de man zijn fiets in de gang?", ["De fietsenstalling is altijd vol.", "Hij heeft geen sleutel van de stalling.", "Hij wist niet dat er een stalling was."],
          "Bisiklet parkında hiç yer olmuyor.", "In de fietsenstalling is alleen nooit plaats."),
        Q("b1e2-19", "Wat stelt de vrouw voor?", ["De woningcorporatie vragen om oude fietsen weg te halen", "Een nieuwe fietsenstalling bouwen", "De fiets op straat zetten"],
          "Kira şirketinden kullanılmayan eski bisikletleri kaldırmasını istemeyi öneriyor.", "Zullen we de woningcorporatie vragen om die weg te halen?"),
        Q("b1e2-20", "Waar zet de man zijn fiets voorlopig?", ["Op zijn balkon", "In de fietsenstalling", "Bij de buurvrouw"],
          "Şimdilik bisikletini kendi balkonuna koyacak.", "En tot die tijd zet ik mijn fiets bij mij op het balkon."),
     ]},
    {"id": "b1-nieuws-bieb", "intro": "U hoort een nieuwsbericht van een lokale omroep.", "tekst": """
o: De bibliotheek in Rijnstad gaat vanaf volgend jaar ook op zondag open. Dat heeft de gemeenteraad gisteren besloten. Volgens de wethouder is er veel vraag naar, vooral van studenten en gezinnen. Op zondag is de bibliotheek open van twaalf tot vijf. Er komen geen extra medewerkers; de bibliotheek werkt op zondag met vrijwilligers. Niet iedereen is blij: een aantal raadsleden vindt dat de bibliotheek eerst de openingstijden doordeweeks moet verlengen. De bibliotheek is nu op maandag gesloten.""",
     "vragen": [
        Q("b1e2-21", "Wat heeft de gemeenteraad besloten?", ["De bibliotheek gaat ook op zondag open.", "De bibliotheek gaat op maandag open.", "De bibliotheek gaat sluiten."],
          "Belediye meclisi kütüphanenin pazar günü de açılmasına karar verdi.", "De bibliotheek in Rijnstad gaat vanaf volgend jaar ook op zondag open."),
        Q("b1e2-22", "Voor wie is dit vooral?", ["Studenten en gezinnen", "Ouderen", "Medewerkers van de bibliotheek"],
          "Özellikle öğrencilerden ve ailelerden talep var.", "vooral van studenten en gezinnen."),
        Q("b1e2-23", "Wie werkt er op zondag?", ["Vrijwilligers", "Extra medewerkers", "Medewerkers van de gemeente"],
          "Ek personel yok; pazar günü gönüllüler çalışıyor.", "de bibliotheek werkt op zondag met vrijwilligers."),
        Q("b1e2-24", "Wat vinden sommige raadsleden?", ["Eerst moeten de openingstijden doordeweeks langer.", "De bibliotheek moet op zaterdag dicht.", "Er moeten meer boeken komen."],
          "Bazı meclis üyeleri önce hafta içi saatlerin uzatılmasını istiyor.", "een aantal raadsleden vindt dat de bibliotheek eerst de openingstijden doordeweeks moet verlengen."),
     ]},
    {"id": "b1-cursus-presentatie", "intro": "U hoort een docent die een nieuwe cursus voorstelt.", "tekst": """
m: Goedenavond. Ik ben Ruud en ik geef de cursus 'Solliciteren in Nederland'. De cursus duurt zes weken, met elke week één les van twee uur. In de eerste weken schrijven we samen een cv en een motivatiebrief. Daarna oefenen we sollicitatiegesprekken. Dat doen we met echte werkgevers uit de buurt, die als vrijwilliger meedoen. Aan het eind krijgt u geen diploma, maar wel een certificaat. De cursus is gratis voor mensen met een uitkering. Anderen betalen vijfentwintig euro. U kunt zich aanmelden bij de balie of via de website. Er is plaats voor twaalf mensen, dus wacht niet te lang.""",
     "vragen": [
        Q("b1e2-25", "Hoe lang duurt de cursus?", ["Zes weken, één les per week", "Twee weken, elke dag een les", "Twaalf weken"],
          "Kurs altı hafta sürüyor, her hafta iki saatlik bir ders.", "De cursus duurt zes weken, met elke week één les van twee uur."),
        Q("b1e2-26", "Met wie oefenen de deelnemers sollicitatiegesprekken?", ["Met echte werkgevers uit de buurt", "Met elkaar", "Met de docent"],
          "Gönüllü olarak katılan çevredeki gerçek işverenlerle.", "Dat doen we met echte werkgevers uit de buurt, die als vrijwilliger meedoen."),
        Q("b1e2-27", "Wie betaalt niets?", ["Mensen met een uitkering", "Iedereen", "Mensen die al werk hebben"],
          "İşsizlik ya da sosyal yardım alanlar için ücretsiz; diğerleri 25 €.", "De cursus is gratis voor mensen met een uitkering."),
        Q("b1e2-28", "Waarom moet je je snel aanmelden?", ["Er is plaats voor maar twaalf mensen.", "De cursus begint morgen.", "De prijs gaat omhoog."],
          "Sadece on iki kişilik yer var.", "Er is plaats voor twaalf mensen, dus wacht niet te lang."),
     ]},
    {"id": "b1-apotheek", "intro": "U hoort een gesprek bij de apotheek.", "tekst": """
v: Goedemiddag, u komt een recept ophalen?
m: Ja, van de huisarts, voor antibiotica.
v: Klopt. U neemt deze tabletten drie keer per dag, zeven dagen lang. Het is belangrijk dat u de hele kuur afmaakt, ook als u zich eerder beter voelt.
m: Mag ik er alcohol bij drinken?
v: Liever niet. En neem de tabletten niet tegelijk met melk of yoghurt, want dan werken ze minder goed. Twee uur ertussen is genoeg.
m: En als ik een keer vergeet?
v: Neem de tablet dan zo snel mogelijk. Maar is het al bijna tijd voor de volgende? Sla hem dan over. Neem nooit twee tabletten tegelijk.""",
     "vragen": [
        Q("b1e2-29", "Hoe lang moet de man de tabletten nemen?", ["Zeven dagen", "Drie dagen", "Tot hij zich beter voelt"],
          "Yedi gün boyunca, günde üç kez; kendini iyi hissetse bile kürü bitirmeli.", "U neemt deze tabletten drie keer per dag, zeven dagen lang."),
        Q("b1e2-30", "Waarom mag hij de tabletten niet met melk nemen?", ["Dan werken ze minder goed.", "Dan wordt hij misselijk.", "Dan werken ze te sterk."],
          "Süt ya da yoğurtla alınırsa ilaçlar daha az etkili oluyor.", "want dan werken ze minder goed."),
        Q("b1e2-31", "Hoeveel tijd moet er tussen de tablet en melk zitten?", ["Twee uur", "Een half uur", "Een hele dag"],
          "Arada iki saat olması yeterli.", "Twee uur ertussen is genoeg."),
        Q("b1e2-32", "Wat doet hij als het bijna tijd is voor de volgende tablet en hij er een vergeten is?", ["De vergeten tablet overslaan", "Twee tabletten tegelijk nemen", "De apotheek bellen"],
          "Bir sonrakinin zamanı yaklaşmışsa unutulanı atlamalı; asla iki tablet birden alınmaz.", "Sla hem dan over."),
     ]},
    {"id": "b1-radio-vrijwilliger", "intro": "U hoort een radiogesprek met een vrijwilliger bij de voedselbank.", "tekst": """
v: Tom, u werkt al vijf jaar als vrijwilliger bij de voedselbank. Hoe bent u begonnen?
m: Toen ik met pensioen ging, wilde ik iets nuttigs doen. Een buurman werkte er al en vroeg of ik wilde helpen met de vrachtwagen.
v: Wat doet u nu precies?
m: Ik haal op donderdag eten op bij supermarkten. Vooral producten die bijna over de datum zijn, maar nog prima te eten.
v: Merkt u dat er meer mensen naar de voedselbank komen?
m: Ja, zeker. Vroeger waren het vooral mensen zonder werk. Nu komen er ook mensen die wel werken, maar door de hoge kosten niet rondkomen.
v: Wat is het mooiste aan uw werk?
m: Het contact. Mensen zijn dankbaar, en ik heb er veel nieuwe vrienden gemaakt.""",
     "vragen": [
        Q("b1e2-33", "Waarom begon Tom als vrijwilliger?", ["Hij wilde na zijn pensioen iets nuttigs doen.", "Hij had geen werk meer.", "Hij had zelf eten nodig."],
          "Emekli olunca faydalı bir şey yapmak istemiş.", "Toen ik met pensioen ging, wilde ik iets nuttigs doen."),
        Q("b1e2-34", "Wat doet Tom op donderdag?", ["Eten ophalen bij supermarkten", "Pakketten uitdelen", "Nieuwe vrijwilligers zoeken"],
          "Perşembe günleri marketlerden yiyecek topluyor.", "Ik haal op donderdag eten op bij supermarkten."),
        Q("b1e2-35", "Wat is er veranderd bij de mensen die komen?", ["Er komen nu ook mensen die werken.", "Er komen minder mensen.", "Er komen alleen nog ouderen."],
          "Artık çalışan ama yüksek masraflar yüzünden geçinemeyen insanlar da geliyor.", "Nu komen er ook mensen die wel werken, maar door de hoge kosten niet rondkomen."),
        Q("b1e2-36", "Wat vindt Tom het mooiste aan zijn werk?", ["Het contact met mensen", "Het rijden met de vrachtwagen", "Dat hij gratis eten krijgt"],
          "En güzel bulduğu şey insanlarla temas.", "Het contact."),
     ]},
    {"id": "b1-gemeente-paspoort", "intro": "U hoort een telefoongesprek met de gemeente.", "tekst": """
m: Gemeente Rijnstad, goedemorgen.
v: Goedemorgen. Mijn paspoort verloopt over twee maanden en in juli ga ik op vakantie naar het buitenland. Wat moet ik doen?
m: U maakt online een afspraak om een nieuw paspoort aan te vragen. Neem een recente pasfoto en uw oude paspoort mee. Na ongeveer een week kunt u het nieuwe paspoort ophalen.
v: Moet ik daarvoor weer een afspraak maken?
m: Nee, ophalen kan zonder afspraak, tijdens de openingstijden. Let op: in de maanden voor de zomervakantie is het erg druk. Vraag uw paspoort dus zo snel mogelijk aan.
v: En wat kost het?
m: Voor volwassenen ongeveer tachtig euro. U betaalt bij de aanvraag.""",
     "vragen": [
        Q("b1e2-37", "Waarom belt de vrouw?", ["Haar paspoort verloopt binnenkort.", "Ze is haar paspoort kwijt.", "Ze wil een identiteitskaart voor haar kind."],
          "Pasaportunun süresi iki ay sonra doluyor ve temmuzda yurt dışına gidecek.", "Mijn paspoort verloopt over twee maanden"),
        Q("b1e2-38", "Wat moet ze meenemen naar de afspraak?", ["Een pasfoto en haar oude paspoort", "Alleen haar oude paspoort", "Een brief van haar werkgever"],
          "Yeni bir vesikalık fotoğraf ve eski pasaport.", "Neem een recente pasfoto en uw oude paspoort mee."),
        Q("b1e2-39", "Wat is waar over het ophalen?", ["Daarvoor is geen afspraak nodig.", "Daarvoor moet ze online een afspraak maken.", "Het paspoort wordt thuisgebracht."],
          "Almak için randevu gerekmiyor, açık saatlerde gidilebiliyor.", "Nee, ophalen kan zonder afspraak, tijdens de openingstijden."),
        Q("b1e2-40", "Waarom moet ze het paspoort snel aanvragen?", ["Het is druk voor de zomervakantie.", "De prijs gaat omhoog.", "De gemeente gaat dicht."],
          "Yaz tatilinden önceki aylarda çok yoğun oluyor.", "Let op: in de maanden voor de zomervakantie is het erg druk."),
     ]},
]
