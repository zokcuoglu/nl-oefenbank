"""Luisteren A2 practice fragments (own texts in the style of the A2 inburgeringsexamen Luisteren; made-up names).

Each fragment: 'intro' (what you are going to hear, shown before playing), 'tekst' = lines "spreker: zin"
(spreker: v = woman, m = man, o = announcement voice; the page gives each a different voice when the browser has them),
one question with 3 options (right one first; the page shuffles) and a Turkish 'uitleg'.
'bewijs' = the sentence in the fragment that gives the answer (shown in the transcript after answering).
"""

def F(id, intro, tekst, vraag, opties, uitleg, bewijs):
    return {"id": id, "intro": intro, "tekst": tekst.strip(), "vraag": vraag, "opties": opties, "uitleg": uitleg, "bewijs": bewijs}

EXAMEN_1 = [
    F("l1-huisarts", "U belt naar de huisarts.", """
v: Huisartsenpraktijk De Linde, goedemorgen.
m: Goedemorgen, met Ahmed Karim. Ik wil graag een afspraak maken. Ik heb al drie dagen keelpijn.
v: Kunt u vanmiddag om half drie komen?
m: Nee, dan moet ik werken. Kan het morgen?
v: Morgenochtend om tien uur is er plaats.
m: Prima, dan kom ik morgen om tien uur.""",
      "Wanneer gaat Ahmed naar de huisarts?", ["Morgenochtend om tien uur", "Vanmiddag om half drie", "Over drie dagen"],
      "Bugün öğleden sonra çalışıyor; yarın sabah saat onda gidiyor.", "Prima, dan kom ik morgen om tien uur."),
    F("l1-supermarkt", "U bent in de supermarkt. U hoort een omroepbericht.", """
o: Beste klanten, vandaag zijn alle appels in de aanbieding. Twee kilo voor maar twee euro. De aanbieding is alleen vandaag geldig. Let op: de winkel gaat vanavond om acht uur dicht.""",
      "Wat kost twee kilo appels vandaag?", ["Twee euro", "Acht euro", "Één euro"],
      "İki kilo elma bugün sadece iki avro. 'acht uur' kapanış saati.", "Twee kilo voor maar twee euro."),
    F("l1-trein", "U staat op het station. U hoort een omroepbericht.", """
o: De trein naar Utrecht van tien over negen vertrekt niet van spoor 5, maar van spoor 8. Ik herhaal: de trein naar Utrecht vertrekt van spoor 8.""",
      "Van welk spoor vertrekt de trein naar Utrecht?", ["Spoor 8", "Spoor 5", "Spoor 9"],
      "Tren 5. perondan değil, 8. perondan kalkıyor.", "Ik herhaal: de trein naar Utrecht vertrekt van spoor 8."),
    F("l1-juf", "De juf praat met de moeder van Sara.", """
v: Dag mevrouw Yılmaz. Ik wil even iets zeggen over Sara.
v2: Ja, natuurlijk, juf.
v: Sara is vaak moe in de klas. Gaat ze laat naar bed?
v2: Ja, ze kijkt 's avonds lang tv.
v: Misschien kan ze om acht uur naar bed? Dan is ze beter uitgerust.""",
      "Wat is het probleem met Sara?", ["Ze is vaak moe in de klas.", "Ze komt vaak te laat.", "Ze is vaak ziek."],
      "Öğretmen Sara'nın sınıfta sık sık yorgun olduğunu söylüyor.", "Sara is vaak moe in de klas."),
    F("l1-buurman", "Uw buurman praat met u.", """
m: Hallo! Ik ga morgen een week op vakantie. Wil jij mijn planten water geven?
v: Ja hoor, dat is goed. Hoe vaak moet dat?
m: Twee keer per week is genoeg. De sleutel leg ik vanavond bij jou in de brievenbus.""",
      "Hoe krijgt de vrouw de sleutel?", ["De buurman doet de sleutel in haar brievenbus.", "Ze haalt de sleutel morgen op.", "De sleutel ligt onder de mat."],
      "Komşu anahtarı bu akşam kadının posta kutusuna bırakacak.", "De sleutel leg ik vanavond bij jou in de brievenbus."),
    F("l1-weer", "U luistert naar het weerbericht op de radio.", """
o: Vandaag wordt het een grijze dag met veel regen. Het is ongeveer twaalf graden. Morgen wordt het droog en komt de zon tevoorschijn. Dan wordt het zeventien graden.""",
      "Hoe is het weer morgen?", ["Droog en zonnig", "Grijs met veel regen", "Koud met sneeuw"],
      "Yarın hava kuru ve güneşli, 17 derece. Yağmur bugün.", "Morgen wordt het droog en komt de zon tevoorschijn."),
    F("l1-collega", "Twee collega's praten op het werk.", """
v: Hoi Tom, kun jij zaterdag voor mij werken? Mijn zus gaat trouwen.
m: Zaterdag? Hmm, ik heb dan voetbal. Maar 's middags kan ik wel.
v: Super, dan werk ik 's ochtends en jij 's middags.""",
      "Waarom kan de vrouw zaterdag niet de hele dag werken?", ["Haar zus gaat trouwen.", "Ze heeft voetbal.", "Ze is ziek."],
      "Kadının kız kardeşi evleniyor. Futbol Tom'un sebebi.", "Mijn zus gaat trouwen."),
    F("l1-apotheek", "U bent bij de apotheek.", """
v: Hier zijn uw medicijnen. U neemt drie keer per dag één tablet, na het eten.
m: Ook 's nachts?
v: Nee, alleen bij het ontbijt, de lunch en het avondeten.""",
      "Wanneer neemt de man de tabletten?", ["Na het eten, drie keer per dag", "Alleen 's nachts", "Eén keer per dag voor het ontbijt"],
      "Günde üç kez, yemekten sonra bir tablet. Geceleri değil.", "U neemt drie keer per dag één tablet, na het eten."),
    F("l1-gemeente", "U belt naar de gemeente.", """
v: Gemeente Rijnstad, goedemiddag.
m: Goedemiddag. Ik ben verhuisd en ik wil mijn nieuwe adres doorgeven.
v: Dat kunt u het beste online doen, op onze website. U heeft dan wel uw DigiD nodig.""",
      "Wat moet de man doen?", ["Zijn adres op de website doorgeven", "Langskomen bij de gemeente", "Een brief sturen"],
      "Yeni adresini en iyisi internet sitesinden DigiD ile bildirmek.", "Dat kunt u het beste online doen, op onze website."),
    F("l1-bus", "U zit in de bus. De chauffeur zegt iets.", """
m: Beste reizigers, door werkzaamheden aan de weg rijdt deze bus vandaag niet langs het ziekenhuis. Wilt u naar het ziekenhuis? Stap dan uit bij de halte Markt en neem lijn 4.""",
      "U wilt naar het ziekenhuis. Wat moet u doen?", ["Uitstappen bij de Markt en lijn 4 nemen", "Blijven zitten tot het ziekenhuis", "Uitstappen en lopen"],
      "Otobüs bugün hastaneye uğramıyor; Markt durağında inip 4 numaralı hatta binmek gerekiyor.", "Stap dan uit bij de halte Markt en neem lijn 4."),
    F("l1-sportclub", "Een vader praat met een trainer van de voetbalclub.", """
m: Mijn zoon wil graag voetballen. Hij is acht jaar. Wanneer trainen de kinderen?
v: Kinderen van acht jaar trainen op woensdagmiddag om vier uur. Op zaterdag spelen ze een wedstrijd.
m: En wat kost het?
v: Honderd euro per jaar.""",
      "Wanneer trainen de kinderen van acht jaar?", ["Op woensdagmiddag", "Op zaterdagochtend", "Elke dag om vier uur"],
      "8 yaşındakiler çarşamba öğleden sonra saat dörtte antrenman yapıyor; cumartesi maç var.", "Kinderen van acht jaar trainen op woensdagmiddag om vier uur."),
    F("l1-bibliotheek", "U bent in de bibliotheek.", """
v: Ik wil dit boek lenen, maar mijn pasje is verlopen.
m: Dan kunt u het hier verlengen. Dat kost twintig euro per jaar. U kunt met de pin betalen.""",
      "Wat is het probleem van de vrouw?", ["Haar pasje is verlopen.", "Ze heeft geen geld.", "Het boek is weg."],
      "Kadının kütüphane kartının süresi dolmuş.", "Ik wil dit boek lenen, maar mijn pasje is verlopen."),
    F("l1-pakket", "U krijgt een voicemail.", """
m: Goedemiddag, dit is PakketPost. We hebben vandaag een pakket voor u geprobeerd te bezorgen, maar u was niet thuis. U kunt het pakket vanaf morgen ophalen bij de tabakswinkel in de Dorpsstraat.""",
      "Waar kunt u uw pakket ophalen?", ["Bij de tabakswinkel in de Dorpsstraat", "Bij het postkantoor", "Bij de buren"],
      "Paket yarından itibaren Dorpsstraat'taki tütüncüden alınabilir.", "U kunt het pakket vanaf morgen ophalen bij de tabakswinkel in de Dorpsstraat."),
    F("l1-tandarts", "U belt naar de tandarts.", """
v: Tandartspraktijk Witte Lach.
m: Goedemorgen, ik heb heel erg kiespijn.
v: Oh, wat vervelend. Kunt u over een uur komen?
m: Ja, graag. Dank u wel.""",
      "Waarom belt de man?", ["Hij heeft kiespijn.", "Hij wil zijn afspraak afzeggen.", "Hij wil een controle."],
      "Adamın çok kötü diş ağrısı var ('kiespijn').", "Goedemorgen, ik heb heel erg kiespijn."),
    F("l1-markt", "U bent op de markt.", """
m: Wat mag het zijn?
v: Een kilo tomaten en een komkommer, alstublieft.
m: Dat is samen drie euro vijftig.
v: Alstublieft, hier is vijf euro.
m: En dan krijgt u anderhalve euro terug.""",
      "Hoeveel geld krijgt de vrouw terug?", ["Anderhalve euro", "Drie euro vijftig", "Vijf euro"],
      "Toplam 3,50 €; 5 € veriyor, 1,50 € (anderhalve euro) para üstü alıyor.", "En dan krijgt u anderhalve euro terug."),
    F("l1-verjaardag", "Twee vriendinnen bellen.", """
v: Hoi Mila! Kom je zaterdag op mijn verjaardag?
v2: Ja, leuk! Hoe laat?
v: Vanaf vier uur. Je hoeft niks mee te nemen.
v2: Oké, ik kom met mijn man en de kinderen.""",
      "Met wie komt Mila naar de verjaardag?", ["Met haar man en de kinderen", "Alleen", "Met haar zus"],
      "Mila eşi ve çocuklarıyla geliyor.", "Oké, ik kom met mijn man en de kinderen."),
    F("l1-fietsenmaker", "U bent bij de fietsenmaker.", """
m: Uw fiets is klaar. De band was kapot en de remmen waren niet goed. Ik heb alles gemaakt.
v: Wat moet ik betalen?
m: Vijfentwintig euro.""",
      "Wat was er kapot aan de fiets?", ["De band en de remmen", "Het licht", "De bel en het slot"],
      "Lastik patlakmış, frenler de iyi değilmiş.", "De band was kapot en de remmen waren niet goed."),
    F("l1-zwembad", "U hoort een bericht in het zwembad.", """
o: Beste bezoekers, het grote bad gaat over tien minuten dicht voor zwemles. Het kleine bad blijft open tot vijf uur.""",
      "Wat gebeurt er over tien minuten?", ["Het grote bad gaat dicht.", "Het hele zwembad gaat dicht.", "Het kleine bad gaat dicht."],
      "On dakika sonra büyük havuz yüzme dersi için kapanıyor; küçük havuz açık.", "Beste bezoekers, het grote bad gaat over tien minuten dicht voor zwemles."),
    F("l1-schoonmaak", "Een vrouw belt met de woningcorporatie.", """
v: Goedemiddag, de lamp in de hal van onze flat is al een week kapot. Het is 's avonds helemaal donker.
m: Bedankt voor het melden. Er komt donderdag iemand om de lamp te maken.""",
      "Wanneer wordt de lamp gemaakt?", ["Donderdag", "Over een week", "Vanavond"],
      "Lamba perşembe günü tamir edilecek. 'Bir haftadır' bozuk.", "Er komt donderdag iemand om de lamp te maken."),
    F("l1-cursus", "U belt over een cursus Nederlands.", """
m: Ik wil graag een cursus Nederlands doen. Is er nog plaats?
v: Ja, er is nog plaats in de avondcursus. De les is op dinsdag en donderdag van zeven tot negen uur.""",
      "Wanneer is de les?", ["Op dinsdag en donderdag 's avonds", "Elke ochtend", "Alleen op zaterdag"],
      "Akşam kursu salı ve perşembe 19.00–21.00.", "De les is op dinsdag en donderdag van zeven tot negen uur."),
]

EXAMEN_2 = [
    F("l2-ziek", "Een man belt naar zijn werk.", """
m: Hallo, met Peter. Ik ben ziek, ik heb koorts. Ik kan vandaag niet komen.
v: Oh, beterschap! Weet je al wanneer je terug bent?
m: Ik denk maandag.""",
      "Wanneer denkt Peter weer te werken?", ["Maandag", "Vandaag", "Morgen"],
      "Peter pazartesi işe döneceğini düşünüyor.", "Ik denk maandag."),
    F("l2-kapper", "U belt naar de kapper.", """
v: Kapsalon Knip, goedemiddag.
m: Kan ik zaterdag langskomen om mijn haar te laten knippen?
v: Zaterdag zijn we vol. Vrijdagavond om zeven uur kan wel.
m: Goed, dan kom ik vrijdag.""",
      "Wanneer gaat de man naar de kapper?", ["Vrijdagavond", "Zaterdag", "Vanmiddag"],
      "Cumartesi dolu; cuma akşamı saat yedide gidiyor.", "Goed, dan kom ik vrijdag."),
    F("l2-school-voicemail", "U krijgt een voicemail van school.", """
v: Goedemorgen, u spreekt met de school van Daan. Daan heeft vandaag zijn gymspullen niet bij zich. Wilt u ze vóór twaalf uur naar school brengen?""",
      "Wat moet de ouder doen?", ["De gymspullen naar school brengen", "Daan vroeg ophalen", "De juf terugbellen"],
      "Okul, Daan'ın spor eşyalarını saat on ikiden önce getirmeni istiyor.", "Wilt u ze vóór twaalf uur naar school brengen?"),
    F("l2-winkel-ruilen", "Een vrouw is in een kledingwinkel.", """
v: Ik heb deze trui gisteren gekocht, maar hij is te klein. Kan ik hem ruilen?
m: Ja, dat kan. Heeft u de kassabon?
v: Ja, hier.
m: Welke maat wilt u?
v: Een maat groter, graag.""",
      "Waarom wil de vrouw de trui ruilen?", ["Hij is te klein.", "Hij is kapot.", "Ze vindt de kleur niet mooi."],
      "Kazak küçük geliyor, bir beden büyüğünü istiyor.", "Ik heb deze trui gisteren gekocht, maar hij is te klein."),
    F("l2-parkeren", "U hoort een bericht in de parkeergarage.", """
o: Let op: de parkeergarage gaat vanavond om elf uur dicht. Haal uw auto voor die tijd op. Betalen kan bij de automaat bij de uitgang.""",
      "Waar kunt u betalen?", ["Bij de automaat bij de uitgang", "In de winkel", "Bij de ingang"],
      "Ödeme çıkıştaki otomatta yapılıyor.", "Betalen kan bij de automaat bij de uitgang."),
    F("l2-afspraak-gemeente", "U praat met een medewerker van de gemeente.", """
v: Voor een nieuw paspoort moet u een afspraak maken. Neem een pasfoto en uw oude paspoort mee.
m: Hoe lang duurt het?
v: Na een week kunt u het nieuwe paspoort ophalen.""",
      "Wat moet de man meenemen?", ["Een pasfoto en zijn oude paspoort", "Alleen geld", "Een brief van zijn werk"],
      "Vesikalık fotoğraf ve eski pasaport getirilmeli.", "Neem een pasfoto en uw oude paspoort mee."),
    F("l2-buren-feest", "Uw buurvrouw praat met u.", """
v: Hoi! Zaterdagavond geef ik een feestje. Het kan een beetje laat worden. Ik hoop dat het niet te veel lawaai maakt.
m: Geen probleem. Bedankt dat je het zegt.""",
      "Waarom praat de buurvrouw met de man?", ["Ze wil zeggen dat ze een feestje geeft.", "Ze wil klagen over lawaai.", "Ze vraagt hulp bij het feest."],
      "Komşu cumartesi parti vereceğini ve gürültü olabileceğini haber veriyor.", "Zaterdagavond geef ik een feestje."),
    F("l2-weer-wind", "U luistert naar het weerbericht.", """
o: Morgen is er veel wind aan de kust. Fietsers moeten voorzichtig zijn. In het binnenland is het rustiger. Overal blijft het droog.""",
      "Hoe is het weer morgen aan de kust?", ["Er is veel wind.", "Het regent veel.", "Het is heel warm."],
      "Yarın sahilde çok rüzgâr var; her yerde kuru.", "Morgen is er veel wind aan de kust."),
    F("l2-huiswerkklas", "Een moeder praat met de juf.", """
v: Mijn zoon vindt rekenen moeilijk. Kan hij extra hulp krijgen?
v2: Ja, op maandag na school is er een huiswerkklas. Daar helpt een leraar met rekenen. Het is gratis.""",
      "Wat is waar over de huiswerkklas?", ["Het is gratis.", "Het is op vrijdag.", "Het is alleen voor taal."],
      "Ödev sınıfı ücretsiz, pazartesi okuldan sonra, matematik yardımı.", "Het is gratis."),
    F("l2-trein-vertraging", "U staat op het station.", """
o: De trein naar Amsterdam Centraal van twaalf uur heeft ongeveer twintig minuten vertraging. Onze excuses voor het ongemak.""",
      "Wat is er met de trein?", ["Hij heeft twintig minuten vertraging.", "Hij rijdt niet.", "Hij vertrekt van een ander spoor."],
      "Tren yaklaşık 20 dakika rötarlı.", "De trein naar Amsterdam Centraal van twaalf uur heeft ongeveer twintig minuten vertraging."),
    F("l2-sollicitatie", "Een vrouw praat met een werkgever.", """
m: U wilt hier werken in de keuken. Heeft u ervaring?
v: Ja, ik heb drie jaar in een restaurant gewerkt.
m: Goed. Kunt u ook in het weekend werken?
v: Ja, dat kan.""",
      "Hoeveel jaar ervaring heeft de vrouw?", ["Drie jaar", "Eén jaar", "Geen ervaring"],
      "Kadın üç yıl bir restoranda çalışmış.", "Ja, ik heb drie jaar in een restaurant gewerkt."),
    F("l2-dokter-advies", "De huisarts praat met een patiënt.", """
m: U heeft griep. U moet veel water drinken en goed rusten. Blijf een paar dagen thuis. Wordt het niet beter na een week? Bel dan opnieuw.""",
      "Wat zegt de dokter?", ["De patiënt moet thuis blijven en rusten.", "De patiënt moet medicijnen halen.", "De patiënt moet morgen terugkomen."],
      "Doktor bol su içmesini, dinlenmesini ve birkaç gün evde kalmasını söylüyor.", "Blijf een paar dagen thuis."),
    F("l2-bieb-kinderen", "U hoort een bericht in de bibliotheek.", """
o: Op woensdagmiddag is er voorlezen voor kinderen. Het begint om drie uur in de kinderhoek. Ouders mogen erbij blijven.""",
      "Waar is het voorlezen?", ["In de kinderhoek", "In de klas", "In het café"],
      "Kitap okuma çocuk köşesinde, saat üçte.", "Het begint om drie uur in de kinderhoek."),
    F("l2-taxi", "U belt een taxi.", """
v: Taxi Snel, goedenavond.
m: Ik wil graag een taxi naar het station. Ik sta bij het ziekenhuis, bij de hoofdingang.
v: De taxi is er over tien minuten.""",
      "Waar staat de man?", ["Bij de hoofdingang van het ziekenhuis", "Bij het station", "Thuis"],
      "Adam hastanenin ana girişinde bekliyor; istasyona gidecek.", "Ik sta bij het ziekenhuis, bij de hoofdingang."),
    F("l2-energie", "U krijgt een telefoontje van uw energiebedrijf.", """
m: Goedemiddag. Volgende week komt er een monteur om de meter in uw huis te vervangen. Hij komt op dinsdag tussen acht en twaalf uur. Er moet iemand thuis zijn.""",
      "Wat gebeurt er volgende week?", ["Er komt een monteur voor de meter.", "De stroom gaat een week uit.", "U krijgt een nieuwe rekening."],
      "Gelecek hafta sayacı değiştirmek için bir teknisyen geliyor.", "Volgende week komt er een monteur om de meter in uw huis te vervangen."),
    F("l2-markt-kaas", "U bent bij de kaaswinkel.", """
v: Ik wil graag een stuk jonge kaas.
m: Hoe groot moet het stuk zijn?
v: Ongeveer een pond.
m: Wilt u het stuk gesneden?
v: Ja, graag.""",
      "Wat koopt de vrouw?", ["Een pond jonge kaas, gesneden", "Een kilo oude kaas", "Een heel stuk kaas, niet gesneden"],
      "Yarım kilo (pond) taze peynir, dilimlenmiş.", "Ongeveer een pond."),
    F("l2-kinderopvang", "Een vader belt met de kinderopvang.", """
m: Mijn dochter Lina is ziek. Ze komt vandaag niet.
v: Dank u voor het bellen. Beterschap voor Lina! Komt ze morgen wel?
m: Dat weet ik nog niet. Ik bel morgen vroeg.""",
      "Wat doet de vader morgen?", ["Hij belt vroeg naar de kinderopvang.", "Hij brengt Lina naar de dokter.", "Hij brengt Lina naar de opvang."],
      "Baba yarın erkenden kreşi arayacak; Lina'nın gelip gelmeyeceğini henüz bilmiyor.", "Ik bel morgen vroeg."),
    F("l2-container", "U hoort een bericht van de gemeente.", """
o: Heeft u oude meubels of een kapotte koelkast? Op zaterdag kunt u deze gratis brengen naar de milieustraat aan de Havenweg. De milieustraat is open van negen tot vier uur.""",
      "Waar kunt u oude meubels brengen?", ["Naar de milieustraat aan de Havenweg", "Naar het gemeentehuis", "Naar de supermarkt"],
      "Eski mobilyalar cumartesi Havenweg'deki atık merkezine (milieustraat) ücretsiz götürülebilir.", "Op zaterdag kunt u deze gratis brengen naar de milieustraat aan de Havenweg."),
    F("l2-collega-lunch", "Twee collega's praten.", """
m: Ga je mee lunchen in de kantine?
v: Nee, ik heb om twaalf uur een vergadering. Ik eet straks wel.
m: Oké, dan ga ik met Jan.""",
      "Waarom gaat de vrouw niet mee lunchen?", ["Ze heeft een vergadering.", "Ze heeft geen honger.", "Ze gaat met Jan."],
      "Kadının saat on ikide toplantısı var.", "Nee, ik heb om twaalf uur een vergadering."),
    F("l2-verhuizen", "Twee vrienden praten.", """
v: We gaan volgende maand verhuizen. Wil jij helpen met dozen dragen?
m: Ja natuurlijk. Welke dag?
v: Zaterdag de vijftiende. We beginnen om negen uur.
m: Ik ben er!""",
      "Waarmee wil de vrouw hulp?", ["Met dozen dragen", "Met schilderen", "Met koken"],
      "Kadın taşınırken kutuları taşımak için yardım istiyor.", "Wil jij helpen met dozen dragen?"),
]

EXAMENS = [
    {"id": "l-examen-1", "titel": "A2 Luisteren proefexamen 1", "fragmenten": EXAMEN_1},
    {"id": "l-examen-2", "titel": "A2 Luisteren proefexamen 2", "fragmenten": EXAMEN_2},
]
