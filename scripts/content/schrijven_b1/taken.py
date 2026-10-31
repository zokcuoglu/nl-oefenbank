"""Schrijven I (B1) practice tasks: 3 exams x 12 tasks, built like the official public exams (CvTE beoordelingsmodel 2023-2025).
Own tasks; names, companies and places are made up.

Structure per exam (official):
  1-8   zinstaak: write one or a few sentences in an e-mail/message. 'adequaat' = what the sentence must do,
        'gram' = required construction (hoofdzin, bijzin, inversie, te-inf) or None (no specific requirement).
        Scored: adequaatheid 0-1, grammatica 0-1.
  9     deelschrijftaak: fill in a form ('velden'). Scored: adequaatheid 0-3, grammatica 0-2, spelling 0-1, woordgebruik 0-1 (7).
  10-12 korte schrijftaak: short e-mail with all 'elementen'. Pictures/tables are described in 'bijlage' (no images).
        Scored: adequaatheid 0-3 (all elements = 2 as starting point), grammatica 0-2, spelling, samenhang, woordgebruik 0-1 (8).
  Max 47, pass 25 (2025 table).
'voorbeeld' = one good answer, 'tr' = short Turkish help.
"""


def Z(id, titel, situatie, opdracht, adequaat, gram, voorbeeld, tr):
    return {"id": id, "soort": "zin", "titel": titel, "situatie": situatie, "opdracht": opdracht, "adequaat": adequaat, "gram": gram, "voorbeeld": voorbeeld, "tr": tr}


def F(id, titel, situatie, velden, elementen, voorbeeld, tr):
    return {"id": id, "soort": "formulier", "titel": titel, "situatie": situatie, "opdracht": "Vul het formulier in.", "velden": velden,
            "elementen": elementen, "voorbeeld": voorbeeld, "tr": tr}


def T(id, titel, situatie, opdracht, elementen, doel, voorbeeld, tr, bijlage=None):
    t = {"id": id, "soort": "tekst", "titel": titel, "situatie": situatie, "opdracht": opdracht, "elementen": elementen, "doel": doel, "voorbeeld": voorbeeld, "tr": tr}
    if bijlage:
        t["bijlage"] = bijlage
    return t


EXAMEN_1 = [
    Z("e1-01", "Teamuitje", "Uw collega Sanne organiseert een teamuitje op vrijdag. Zij mailt: 'Kom je ook vrijdag?' U kunt niet.",
      "Schrijf in één zin aan Sanne waarom u niet kunt komen.", "De schrijver geeft een reden waarom hij niet kan komen.", "hoofdzin",
      "Helaas kan ik vrijdag niet komen, want mijn dochter is jarig.", "Neden gelemeyeceğini tek bir ana cümleyle yaz."),
    Z("e1-02", "Informatieavond", "U wilt een cursus Engels volgen. U mailt de taalschool. Maak de zin af: 'Ik wil graag naar de informatieavond komen, omdat …'",
      "Maak de zin af.", "De schrijver geeft een reden om naar de informatieavond te komen.", "bijzin",
      "Ik wil graag naar de informatieavond komen, omdat ik voor mijn werk beter Engels moet spreken.", "'omdat'tan sonra yan cümle: fiil sona."),
    Z("e1-03", "Lift kapot", "De lift in uw flat is al een week kapot. U mailt de woningcorporatie. Maak de zin af: 'Door de kapotte lift …'",
      "Maak de zin af.", "De schrijver beschrijft een gevolg van de kapotte lift.", "inversie",
      "Door de kapotte lift kan mijn moeder haar huis niet meer uit.", "'Door …' cümle başında: ardından fiil gelir (devrik yapı)."),
    Z("e1-04", "Zwemles", "Uw zoon zit op zwemles. U wilt weten of hij extra kan oefenen. U mailt de zwemschool. Maak de zin af: 'Is het mogelijk om …'",
      "Maak de zin af.", "De schrijver stelt een vraag over extra oefenen.", "te-inf",
      "Is het mogelijk om op zaterdag extra te oefenen?", "'om … te + mastar' yapısını kullan."),
    Z("e1-05", "Parkeerplaats", "Een collega vraagt per mail: 'Mag ik morgen jouw parkeerplaats gebruiken? Ik heb een afspraak.' U heeft de parkeerplaats zelf nodig.",
      "Schrijf een antwoord met een andere oplossing.", "De schrijver stelt een andere oplossing voor.", None,
      "Morgen heb ik mijn parkeerplaats zelf nodig, maar je kunt misschien in de garage naast het kantoor parkeren.", "Kendi park yerine ihtiyacın var; başka bir çözüm öner."),
    Z("e1-06", "Kerstmarkt", "Uw sportclub heeft geld nodig voor nieuwe ballen. De voorzitter vraagt per mail om ideeën.",
      "Schrijf één idee om geld te verdienen.", "De schrijver beschrijft een idee om geld te verdienen voor de club.", None,
      "We kunnen op de kerstmarkt zelfgebakken koekjes verkopen.", "Kulübe para kazandırmak için bir fikir yaz."),
    Z("e1-07", "Aanbieding", "U werkt bij een bakkerij. U schrijft een tekst voor de website over een aanbieding: elke tweede taart halve prijs.",
      "Schrijf wat klanten moeten doen om de aanbieding te krijgen.", "De schrijver schrijft wat klanten moeten doen voor de aanbieding.", None,
      "Koop twee taarten en u betaalt voor de tweede taart maar de helft.", "Müşterilerin kampanyadan yararlanmak için ne yapması gerektiğini yaz."),
    Z("e1-08", "Buurtfeest", "U bent secretaris van de bewonersvereniging. Het buurtfeest gaat niet door wegens slecht weer. U schrijft een bericht in de buurtapp.",
      "Schrijf een mededeling over het buurtfeest.", "De schrijver deelt mee dat het buurtfeest niet doorgaat (en eventueel wanneer het wel is).", None,
      "Door het slechte weer gaat het buurtfeest zaterdag niet door; we verplaatsen het naar 21 juni.", "Mahalle şenliğinin olmayacağını duyur."),
    F("e1-09", "Inschrijven cursus EHBO", "Uw werkgever betaalt een cursus EHBO (eerste hulp). U vult het inschrijfformulier in.",
      [["Naam", ""], ["Afdeling", ""], ["Welke datum kiest u? (12 maart / 19 maart)", ""], ["Waarom wilt u deze cursus volgen?", "minstens twee zinnen"], ["Heeft u al eerder een cursus EHBO gedaan? Vertel.", ""]],
      ["Alle velden zijn ingevuld.", "Bij 'waarom' staat een duidelijke reden in hele zinnen.", "Bij 'eerder' staat een antwoord met uitleg."],
      "Naam: Ayşe Yılmaz\nAfdeling: Klantenservice\nDatum: 19 maart\nWaarom: Op mijn afdeling werken veel mensen. Ik wil kunnen helpen als iemand onwel wordt.\nEerder: Nee, ik heb nog nooit een cursus EHBO gedaan, maar ik heb wel eens iemand geholpen die gevallen was.",
      "Her alanı doldur; 'waarom' kısmına en az iki tam cümle yaz."),
    T("e1-10", "Bedrijfsuitje", "U bent met uw afdeling een dag naar Utrecht geweest. Uw leidinggevende vraagt in een e-mail wat u ervan vond.",
      "Schrijf een e-mail aan uw leidinggevende.",
      ["Beschrijf wat jullie in Utrecht hebben gedaan. Gebruik alle drie de plaatjes.", "Schrijf welke activiteit u het leukst vond en waarom.", "Schrijf waar u volgend jaar naartoe wilt en waarom."],
      "De leidinggevende informeren over het uitje en een idee geven voor volgend jaar.",
      "Beste Marjolein,\n\nBedankt voor het leuke uitje. Eerst hebben we een rondvaart door de grachten gemaakt. Daarna hebben we samen geluncht op een terras, en 's middags zijn we naar het Spoorwegmuseum geweest. De rondvaart vond ik het leukst, omdat je de stad dan vanaf het water ziet. Volgend jaar wil ik graag naar Maastricht, want daar ben ik nog nooit geweest en de stad is heel gezellig.\n\nGroeten,\nAyşe",
      "Üç resmi kullanarak ne yaptığınızı anlat; en çok neyi sevdiğini ve gelecek yıl nereye gitmek istediğini nedenleriyle yaz.",
      bijlage="Plaatje 1: een boot op de gracht. Plaatje 2: collega's lunchen op een terras. Plaatje 3: een museum met oude treinen."),
    T("e1-11", "Wasmachine te laat", "U heeft bij webwinkel ElektroPlus een wasmachine besteld. Hij zou op 3 mei komen. Nu krijgt u een mail: de levering wordt 24 mei.",
      "Schrijf een e-mail aan ElektroPlus.",
      ["Schrijf welke wasmachine u heeft besteld en wanneer.", "Schrijf wanneer hij eerst geleverd zou worden en wanneer nu.", "Schrijf wat u van de late levering vindt en waarom.",
       "Noem minimaal twee oplossingen.", "Schrijf welke oplossing uw voorkeur heeft en waarom.", "Schrijf wat u van ElektroPlus verwacht."],
      "ElektroPlus overtuigen een van de oplossingen te bieden.",
      "Geachte heer, mevrouw,\n\nOp 20 april heb ik bij u een witte wasmachine van het merk Wasto besteld. De levering zou op 3 mei zijn, maar nu hoor ik dat hij pas op 24 mei komt. Dat vind ik erg vervelend, want mijn oude wasmachine is kapot en ik heb drie kinderen. Ik zie twee oplossingen: u levert een andere wasmachine die wel op voorraad is, of ik krijg korting. Mijn voorkeur gaat uit naar een andere wasmachine, omdat ik niet drie weken naar de wasserette wil. Ik verwacht binnen twee dagen een antwoord van u.\n\nMet vriendelijke groet,\nAli Demir",
      "Siparişini, eski ve yeni teslim tarihini, ne düşündüğünü, en az iki çözümü, tercihini ve beklentini yaz."),
    T("e1-12", "Stageplek", "U volgt een opleiding tot verkoper. U zoekt samen met medestudent Bram een stageplek. U heeft drie bedrijven gevonden.",
      "Schrijf een e-mail aan Bram.",
      ["Leg uit waarom u de e-mail schrijft.", "Schrijf welke drie bedrijven u heeft gevonden.", "Schrijf welk bedrijf uw voorkeur heeft, met minimaal twee redenen.",
       "Schrijf per ander bedrijf minimaal één reden waarom het minder geschikt is.", "Schrijf hoe jullie contact kunnen opnemen met het bedrijf van uw voorkeur."],
      "Bram overtuigen dat het gekozen bedrijf het meest geschikt is.",
      "Hoi Bram,\n\nIk schrijf je omdat ik drie stageplekken heb gevonden: Sportshop Max, Boekhandel De Pagina en supermarkt Vers. Ik kies het liefst voor Sportshop Max, want het is dichtbij en we krijgen er een stagevergoeding. De boekhandel is minder geschikt, omdat ze alleen op zaterdag stagiairs zoeken. De supermarkt vind ik ook minder goed, omdat we daar vooral vakken moeten vullen. Zullen we morgen samen naar Sportshop Max bellen? Het nummer staat op hun website.\n\nGroetjes,\nFatma",
      "Neden yazdığını, üç şirketi, tercihini (en az iki neden), diğerlerinin neden uygun olmadığını ve nasıl iletişime geçeceğinizi yaz.",
      bijlage="Tabel: Sportshop Max — 10 minuten fietsen, stagevergoeding € 150 per maand, maandag t/m vrijdag. Boekhandel De Pagina — 20 minuten met de bus, geen vergoeding, alleen zaterdag. Supermarkt Vers — 5 minuten lopen, € 100 per maand, vooral vakken vullen."),
]

EXAMEN_2 = [
    Z("e2-01", "Vergadering", "Uw leidinggevende mailt: 'Morgen om 9 uur is er een vergadering.' U heeft dan een afspraak bij de tandarts.",
      "Schrijf in één zin waarom u niet aanwezig kunt zijn.", "De schrijver geeft een reden waarom hij niet bij de vergadering kan zijn.", "hoofdzin",
      "Morgen om 9 uur heb ik een afspraak bij de tandarts.", "Toplantıya neden katılamayacağını tek bir ana cümleyle yaz."),
    Z("e2-02", "Afspraak gemeente", "U wilt een afspraak maken bij de gemeente. Maak de zin af: 'Ik wil graag een afspraak maken, omdat …'",
      "Maak de zin af.", "De schrijver beschrijft het doel van de afspraak.", "bijzin",
      "Ik wil graag een afspraak maken, omdat ik een nieuw paspoort moet aanvragen.", "'omdat'tan sonra fiil sona gider."),
    Z("e2-03", "Printer", "De printer op kantoor is al drie dagen kapot. U mailt de ICT-afdeling. Maak de zin af: 'Omdat de printer kapot is, …'",
      "Maak de zin af.", "De schrijver beschrijft een gevolg van de kapotte printer.", "inversie",
      "Omdat de printer kapot is, kan ik de facturen niet versturen.", "Yan cümle başta: ana cümlede fiil önce gelir."),
    Z("e2-04", "Gitaarles", "Uw dochter wil meer gitaarles. U mailt de muziekschool. Maak de zin af: 'Mijn dochter heeft zin om …'",
      "Maak de zin af.", "De schrijver vertelt wat zijn dochter wil met betrekking tot gitaarles.", "te-inf",
      "Mijn dochter heeft zin om twee keer per week les te nemen.", "'om … te + mastar' kullan."),
    Z("e2-05", "Vrije dag", "Een collega vraagt: 'Kun jij vrijdag mijn dienst overnemen?' U kunt niet, maar u wilt wel helpen.",
      "Schrijf een antwoord met een andere oplossing.", "De schrijver stelt een andere oplossing voor.", None,
      "Vrijdag kan ik niet, maar ik kan wel zaterdag voor je werken als jij dan mijn dienst neemt.", "Yapamadığını ama başka bir çözüm önerdiğini yaz."),
    Z("e2-06", "Tuin school", "De school van uw kind wil een moestuin. De directeur vraagt ouders om ideeën.",
      "Schrijf één idee voor de moestuin.", "De schrijver beschrijft een idee voor de moestuin.", None,
      "De kinderen kunnen elke week samen met een ouder groente water geven en oogsten.", "Okul bahçesi için bir fikir yaz."),
    Z("e2-07", "Spaaractie", "U werkt bij een benzinestation. U schrijft een bordje over een spaaractie: bij 10 keer tanken een gratis autowasbeurt.",
      "Schrijf wat klanten moeten doen.", "De schrijver schrijft wat klanten moeten doen voor de actie.", None,
      "Laat bij elke tankbeurt uw kaart stempelen; na tien stempels krijgt u een gratis wasbeurt.", "Müşterilerin kampanya için ne yapması gerektiğini yaz."),
    Z("e2-08", "Prijs gewonnen", "Uw voetbalclub heeft een prijs van € 500 gewonnen in een wedstrijd 'Schoonste club'. U schrijft een bericht in de clubapp.",
      "Schrijf een mededeling over de prijs.", "De schrijver deelt mee dat de club de prijs heeft gewonnen (en eventueel wat ermee gebeurt).", None,
      "Goed nieuws: we hebben € 500 gewonnen met de wedstrijd 'Schoonste club', en daar kopen we nieuwe doelen van!", "Kulübün ödül kazandığını duyur."),
    F("e2-09", "Aanvraag vrijwilligerswerk", "U wilt vrijwilliger worden bij de voedselbank. U vult het formulier in.",
      [["Naam", ""], ["Telefoonnummer", ""], ["Op welke dagen kunt u helpen?", ""], ["Wat wilt u graag doen? (sorteren / rijden / pakketten uitdelen) Leg uit waarom.", "minstens twee zinnen"], ["Heeft u ervaring met vrijwilligerswerk?", ""]],
      ["Alle velden zijn ingevuld.", "Bij 'wat wilt u doen' staat een keuze met een reden in hele zinnen.", "Bij 'ervaring' staat een antwoord."],
      "Naam: Ali Demir\nTelefoonnummer: 06-12345678\nDagen: dinsdag en zaterdag\nWat: Ik wil graag pakketten uitdelen. Ik vind contact met mensen leuk en ik spreek Turks en Arabisch.\nErvaring: Ja, ik heb twee jaar geholpen bij de moskee met de iftar-maaltijden.",
      "Formu doldur; ne yapmak istediğini ve nedenini tam cümlelerle yaz."),
    T("e2-10", "Verhuizing collega", "U heeft zaterdag uw collega Tom geholpen met verhuizen. Uw leidinggevende vraagt hoe het ging.",
      "Schrijf een e-mail aan uw leidinggevende.",
      ["Beschrijf wat jullie hebben gedaan. Gebruik alle drie de plaatjes.", "Schrijf wat het moeilijkste was en waarom.", "Schrijf of u volgende keer weer helpt en waarom."],
      "De leidinggevende vertellen hoe de verhuizing ging.",
      "Beste Peter,\n\nZaterdag hebben we Tom geholpen. Eerst hebben we alle dozen in de vrachtwagen gezet. Daarna hebben we de bank drie trappen op gedragen, en aan het eind hebben we samen pizza gegeten. Het moeilijkste was de bank, want het trappenhuis is heel smal. Volgende keer help ik graag weer, omdat het gezellig was en het team er sterker van wordt.\n\nGroeten,\nAyşe",
      "Üç resmi kullanarak ne yaptığınızı, en zor kısmı ve tekrar yardım edip etmeyeceğini nedenleriyle yaz.",
      bijlage="Plaatje 1: collega's zetten dozen in een vrachtwagen. Plaatje 2: twee mannen dragen een bank een trap op. Plaatje 3: de collega's eten pizza in de nieuwe woonkamer."),
    T("e2-11", "Sportschool", "U bent lid van sportschool FitNu. De sportschool is drie weken dicht voor een verbouwing, maar u moet wel betalen.",
      "Schrijf een e-mail aan FitNu.",
      ["Schrijf sinds wanneer u lid bent en wat voor abonnement u heeft.", "Schrijf wat het probleem is.", "Schrijf wat u daarvan vindt en waarom.",
       "Noem minimaal twee oplossingen.", "Schrijf welke oplossing uw voorkeur heeft en waarom.", "Schrijf wat u van FitNu verwacht."],
      "FitNu overtuigen een van de oplossingen te bieden.",
      "Beste medewerker van FitNu,\n\nIk ben sinds januari lid en ik heb een abonnement van € 35 per maand. Nu is de sportschool drie weken dicht, maar ik moet toch betalen. Dat vind ik niet eerlijk, omdat ik niet kan sporten. Er zijn twee oplossingen: u geeft mij geld terug voor drie weken, of mijn abonnement wordt drie weken langer. Ik heb liever geld terug, want ik ga in de zomer op vakantie. Ik verwacht voor 1 juli een reactie.\n\nMet vriendelijke groet,\nFatma Arslan",
      "Üyeliğini, sorunu, düşünceni, en az iki çözümü, tercihini ve beklentini yaz."),
    T("e2-12", "Cursus kiezen", "Uw collega Linda en u willen samen een computercursus doen. U heeft drie cursussen gevonden.",
      "Schrijf een e-mail aan Linda.",
      ["Leg uit waarom u de e-mail schrijft.", "Schrijf welke drie cursussen u heeft gevonden.", "Schrijf welke cursus uw voorkeur heeft, met minimaal twee redenen.",
       "Schrijf per andere cursus minimaal één reden waarom die minder geschikt is.", "Schrijf hoe jullie je kunnen aanmelden."],
      "Linda overtuigen dat de gekozen cursus het beste is.",
      "Hoi Linda,\n\nIk heb drie computercursussen gevonden en ik wil graag weten wat jij ervan vindt: Excel Basis bij de bibliotheek, Digitaal Werken bij ROC Midden en een online cursus van LeerNu. Mijn voorkeur gaat uit naar de bibliotheek, want die is gratis en de les is op dinsdagavond. De cursus bij het ROC is minder geschikt, omdat hij € 250 kost. De online cursus vind ik ook minder goed, want dan hebben we geen docent. We kunnen ons aanmelden bij de balie van de bibliotheek. Zullen we vrijdag samen gaan?\n\nGroetjes,\nAli",
      "Neden yazdığını, üç kursu, tercihini (en az iki neden), diğerlerinin eksiklerini ve nasıl kayıt olacağınızı yaz.",
      bijlage="Tabel: Excel Basis (bibliotheek) — gratis, dinsdagavond, 6 lessen, met docent. Digitaal Werken (ROC Midden) — € 250, overdag, 10 lessen, certificaat. LeerNu online — € 40, wanneer je wilt, geen docent."),
]

EXAMEN_3 = [
    Z("e3-01", "Etentje", "Uw buurvrouw nodigt u uit om zaterdag bij haar te eten. U kunt niet.",
      "Schrijf in één zin waarom u niet kunt komen.", "De schrijver geeft een reden waarom hij niet kan komen.", "hoofdzin",
      "Zaterdag kan ik helaas niet, want dan werk ik tot laat.", "Neden gelemeyeceğini tek bir ana cümleyle yaz."),
    Z("e3-02", "Huisarts", "U mailt de huisarts. Maak de zin af: 'Ik wil graag een afspraak, omdat …'",
      "Maak de zin af.", "De schrijver beschrijft waarom hij een afspraak wil.", "bijzin",
      "Ik wil graag een afspraak, omdat ik al twee weken hoofdpijn heb.", "'omdat'tan sonra fiil sona."),
    Z("e3-03", "Verwarming", "De verwarming op uw werk doet het niet. U mailt de beheerder. Maak de zin af: 'Sinds maandag …'",
      "Maak de zin af.", "De schrijver beschrijft een gevolg van de kapotte verwarming.", "inversie",
      "Sinds maandag zitten we met onze jassen aan in het kantoor.", "'Sinds maandag' başta: ardından fiil gelir."),
    Z("e3-04", "Bibliotheek", "U wilt een ruimte in de bibliotheek gebruiken voor uw taalgroep. U mailt de bibliotheek. Maak de zin af: 'Wij zijn van plan om …'",
      "Maak de zin af.", "De schrijver beschrijft wat de groep in de ruimte wil doen.", "te-inf",
      "Wij zijn van plan om elke donderdag samen Nederlands te oefenen.", "'om … te + mastar' kullan."),
    Z("e3-05", "Auto lenen", "Uw buurman vraagt: 'Mag ik zondag je auto lenen?' U heeft de auto zelf nodig.",
      "Schrijf een antwoord met een andere oplossing.", "De schrijver stelt een andere oplossing voor.", None,
      "Zondag heb ik de auto zelf nodig, maar maandag mag je hem lenen.", "Arabaya ihtiyacın var; başka bir çözüm öner."),
    Z("e3-06", "Afscheidscadeau", "Een collega gaat met pensioen. De afdeling zoekt een idee voor een cadeau.",
      "Schrijf één idee voor een cadeau.", "De schrijver beschrijft een idee voor een afscheidscadeau.", None,
      "We kunnen samen een fotoboek maken met leuke foto's van het werk.", "Emekli olan iş arkadaşı için bir hediye fikri yaz."),
    Z("e3-07", "Fietsverhuur", "U werkt bij een fietsenverhuur. U schrijft een tekst voor de folder: studenten krijgen 20% korting.",
      "Schrijf wat studenten moeten doen om korting te krijgen.", "De schrijver schrijft wat studenten moeten doen voor de korting.", None,
      "Laat uw studentenkaart zien bij de balie, dan krijgt u 20% korting.", "Öğrencilerin indirim için ne yapması gerektiğini yaz."),
    Z("e3-08", "Nieuwe speeltuin", "U zit in de buurtcommissie. De gemeente betaalt een nieuwe speeltuin. U schrijft een bericht in de nieuwsbrief.",
      "Schrijf een mededeling over de speeltuin.", "De schrijver deelt mee dat er een nieuwe speeltuin komt (en eventueel wanneer).", None,
      "Goed nieuws: de gemeente betaalt een nieuwe speeltuin aan de Lindelaan, die in september open gaat.", "Yeni oyun parkını duyur."),
    F("e3-09", "Klacht openbaar vervoer", "Uw bus kwam vorige week drie keer te laat. U vult een klachtenformulier in.",
      [["Naam", ""], ["Buslijn", ""], ["Wanneer was de bus te laat?", "datum(s)"], ["Wat was het gevolg voor u?", "minstens twee zinnen"], ["Wat verwacht u van het busbedrijf?", ""]],
      ["Alle velden zijn ingevuld.", "Bij 'gevolg' staat een duidelijk gevolg in hele zinnen.", "Bij 'verwacht' staat een verwachting."],
      "Naam: Fatma Arslan\nBuslijn: 43\nWanneer: 3, 5 en 6 maart\nGevolg: Ik kwam drie keer te laat op mijn werk. Mijn leidinggevende was daar niet blij mee.\nVerwacht: Ik verwacht dat de bus weer op tijd rijdt en dat ik een excuus krijg.",
      "Şikâyet formunu doldur; sonucunu ve beklentini tam cümlelerle yaz."),
    T("e3-10", "Open dag", "U heeft met uw zoon de open dag van een middelbare school bezocht. Een vriendin vraagt in een mail hoe het was.",
      "Schrijf een e-mail aan uw vriendin.",
      ["Beschrijf wat jullie op de open dag hebben gedaan. Gebruik alle drie de plaatjes.", "Schrijf wat uw zoon het leukst vond en waarom.", "Schrijf of uw zoon naar deze school wil en waarom."],
      "De vriendin vertellen over de open dag.",
      "Hoi Esra,\n\nZaterdag zijn we naar de open dag van het Rijncollege geweest. Eerst kregen we een rondleiding door de school. Daarna heeft Emir een proefles scheikunde gevolgd, en tot slot hebben we met een docent gepraat. Emir vond de proefles het leukst, omdat hij zelf een proefje mocht doen. Hij wil graag naar deze school, want de sfeer is goed en zijn vriend gaat er ook naartoe.\n\nGroetjes,\nAyşe",
      "Üç resmi kullanarak ne yaptığınızı, oğlunun en çok neyi sevdiğini ve bu okula gitmek isteyip istemediğini nedenleriyle yaz.",
      bijlage="Plaatje 1: een docent geeft ouders en kinderen een rondleiding. Plaatje 2: een jongen doet een proefje in een scheikundelokaal. Plaatje 3: een moeder praat met een docent aan een tafel."),
    T("e3-11", "Verkeerde bril", "U heeft bij opticien ZiezoBril een nieuwe bril gekocht. Na twee weken krijgt u hoofdpijn: de glazen zijn niet goed.",
      "Schrijf een e-mail aan ZiezoBril.",
      ["Schrijf wanneer u welke bril heeft gekocht.", "Schrijf wat het probleem is.", "Schrijf wat u daarvan vindt en waarom.",
       "Noem minimaal twee oplossingen.", "Schrijf welke oplossing uw voorkeur heeft en waarom.", "Schrijf wat u van ZiezoBril verwacht."],
      "ZiezoBril overtuigen een van de oplossingen te bieden.",
      "Geachte heer, mevrouw,\n\nOp 2 oktober heb ik bij u een zwarte bril met leesglazen gekocht. Sinds ik deze bril draag, heb ik elke dag hoofdpijn. Ik denk dat de glazen niet goed zijn. Dat vind ik vervelend, want ik heb de bril nodig voor mijn werk. Er zijn twee oplossingen: u maakt nieuwe glazen, of ik krijg mijn geld terug. Ik heb liever nieuwe glazen, omdat het montuur wel heel mooi is. Ik verwacht dat u mij deze week belt voor een afspraak.\n\nMet vriendelijke groet,\nAli Demir",
      "Ne aldığını, sorunu, düşünceni, en az iki çözümü, tercihini ve beklentini yaz."),
    T("e3-12", "Uitje kiezen", "U organiseert samen met collega Mark het jaarlijkse uitje van de afdeling. U heeft drie ideeën gevonden.",
      "Schrijf een e-mail aan Mark.",
      ["Leg uit waarom u de e-mail schrijft.", "Schrijf welke drie uitjes u heeft gevonden.", "Schrijf welk uitje uw voorkeur heeft, met minimaal twee redenen.",
       "Schrijf per ander uitje minimaal één reden waarom het minder geschikt is.", "Schrijf hoe jullie het uitje kunnen boeken."],
      "Mark overtuigen dat het gekozen uitje het beste is.",
      "Hoi Mark,\n\nIk schrijf je over ons afdelingsuitje. Ik heb drie ideeën gevonden: een kookworkshop, een dag in een pretpark en een fietstocht langs de kust. Mijn voorkeur gaat uit naar de kookworkshop, omdat iedereen kan meedoen en het eten erbij zit. Het pretpark is minder geschikt, want het kost € 60 per persoon. De fietstocht vind ik ook minder goed, omdat niet alle collega's goed kunnen fietsen. We kunnen de workshop online boeken op de website van KookStudio. Wil jij dat doen?\n\nGroeten,\nFatma",
      "Neden yazdığını, üç fikri, tercihini (en az iki neden), diğerlerinin eksiklerini ve nasıl rezervasyon yapacağınızı yaz.",
      bijlage="Tabel: Kookworkshop (KookStudio) — € 45 per persoon, eten inbegrepen, binnen, voor iedereen. Pretpark Avonturia — € 60 per persoon, lange reis, eten niet inbegrepen. Fietstocht langs de kust — € 20 per persoon, alleen bij goed weer, voor goede fietsers."),
]

EXAMENS = [
    {"id": "sb-examen-1", "titel": "Schrijven I proefexamen 1", "taken": EXAMEN_1},
    {"id": "sb-examen-2", "titel": "Schrijven I proefexamen 2", "taken": EXAMEN_2},
    {"id": "sb-examen-3", "titel": "Schrijven I proefexamen 3", "taken": EXAMEN_3},
]
