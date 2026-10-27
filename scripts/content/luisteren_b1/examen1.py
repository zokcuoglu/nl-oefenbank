"""Luisteren B1 practice exam 1 (own texts in the style of Staatsexamen NT2 Programma I Luisteren; made-up names).

Each text: 'intro' (shown before listening), 'tekst' = lines "spreker: zin" (v, v2 = women, m, m2 = men, o = announcer),
'vragen' with 3 options (right one first; the page shuffles), Turkish 'uitleg', 'bewijs' = sentence that gives the answer.
Optional 'video_url' (+ 'video_start'/'video_end' in seconds): the page then plays that video instead of reading the text.
"""


def Q(id, vraag, opties, uitleg, bewijs):
    return {"id": id, "vraag": vraag, "opties": opties, "uitleg": uitleg, "bewijs": bewijs}


TEKSTEN = [
    {"id": "b1-radio-fiets", "intro": "U hoort een radio-interview over fietsen naar het werk.", "tekst": """
v: Welkom bij Radio Rijnstad. Vandaag praat ik met Kees Mulder van de Fietsersbond. Kees, steeds meer mensen fietsen naar hun werk. Hoe komt dat?
m: Dat heeft verschillende redenen. De belangrijkste is de elektrische fiets. Daarmee kun je makkelijk twintig kilometer fietsen zonder dat je moe op je werk aankomt.
v: En werkgevers helpen daar ook bij?
m: Ja, veel werkgevers geven hun personeel een vergoeding per kilometer. Sommige bedrijven betalen zelfs een deel van een nieuwe fiets.
v: Zijn er ook nadelen?
m: Het grootste probleem is de veiligheid. Fietspaden zijn vaak te smal voor snelle elektrische fietsen en gewone fietsen samen. Wij vragen de gemeente om bredere fietspaden.
v: En wat is uw advies aan luisteraars die willen beginnen?
m: Begin rustig, bijvoorbeeld twee dagen per week. Dan merk je vanzelf hoe fijn het is.""",
     "vragen": [
        Q("b1e1-1", "Wat is volgens Kees de belangrijkste reden dat meer mensen naar hun werk fietsen?", ["De elektrische fiets", "De hoge benzineprijzen", "De bredere fietspaden"],
          "Kees en önemli nedenin elektrikli bisiklet olduğunu söylüyor. Daha geniş yollar ise istedikleri bir şey.", "De belangrijkste is de elektrische fiets."),
        Q("b1e1-2", "Hoe helpen werkgevers?", ["Ze geven een vergoeding per kilometer.", "Ze maken bredere fietspaden.", "Ze geven een extra vrije dag."],
          "Birçok işveren kilometre başına ödeme yapıyor; bazıları yeni bisikletin bir kısmını ödüyor.", "Ja, veel werkgevers geven hun personeel een vergoeding per kilometer."),
        Q("b1e1-3", "Wat is volgens Kees het grootste probleem?", ["De fietspaden zijn te smal.", "Elektrische fietsen zijn te duur.", "Werkgevers willen niet meebetalen."],
          "En büyük sorun güvenlik: bisiklet yolları hızlı ve normal bisikletler için birlikte çok dar.", "Fietspaden zijn vaak te smal voor snelle elektrische fietsen en gewone fietsen samen."),
        Q("b1e1-4", "Wat raadt Kees nieuwe fietsers aan?", ["Rustig beginnen, bijvoorbeeld twee dagen per week", "Meteen elke dag fietsen", "Eerst een cursus volgen"],
          "Yavaş başlamayı, örneğin haftada iki gün bisikletle gitmeyi öneriyor.", "Begin rustig, bijvoorbeeld twee dagen per week."),
     ]},
    {"id": "b1-ov-bericht", "intro": "U hoort een bericht op het station.", "tekst": """
o: Goedemiddag reizigers. Door een storing aan het spoor tussen Leiden en Den Haag rijden er de komende twee uur minder treinen. De sprinters naar Den Haag rijden niet. Reizigers naar Den Haag kunnen de intercity nemen, die rijdt wel, maar wel met vertraging. U kunt ook de bus nemen: vanaf het busstation rijdt er elke tien minuten een extra bus naar Den Haag Centraal. Met uw treinkaartje kunt u gratis met deze bus mee. Reizigers naar Schiphol hebben geen last van de storing. Wij verwachten dat de treinen vanaf vijf uur weer normaal rijden. Onze excuses voor het ongemak.""",
     "vragen": [
        Q("b1e1-5", "Welke treinen rijden niet?", ["De sprinters naar Den Haag", "De intercity's naar Den Haag", "De treinen naar Schiphol"],
          "Den Haag'a giden sprinter'lar çalışmıyor; intercity gecikmeli çalışıyor.", "De sprinters naar Den Haag rijden niet."),
        Q("b1e1-6", "Wat is waar over de extra bus?", ["Reizigers met een treinkaartje betalen niets.", "De bus rijdt elk uur.", "De bus gaat naar Schiphol."],
          "Tren biletiyle bu otobüse ücretsiz binilebiliyor; her on dakikada bir.", "Met uw treinkaartje kunt u gratis met deze bus mee."),
        Q("b1e1-7", "Voor wie verandert er niets?", ["Voor reizigers naar Schiphol", "Voor reizigers naar Den Haag", "Voor reizigers met de bus"],
          "Schiphol'e gidenler arızadan etkilenmiyor.", "Reizigers naar Schiphol hebben geen last van de storing."),
        Q("b1e1-8", "Wanneer rijden de treinen waarschijnlijk weer normaal?", ["Vanaf vijf uur", "Over tien minuten", "Morgen"],
          "Trenlerin saat beşten itibaren normal çalışması bekleniyor.", "Wij verwachten dat de treinen vanaf vijf uur weer normaal rijden."),
     ]},
    {"id": "b1-werk-overleg", "intro": "U hoort een gesprek tussen twee collega's in een verpleeghuis.", "tekst": """
v: Hé Marco, heb je even? Ik wil het over het rooster van volgende maand hebben.
m: Ja hoor. Wat is er?
v: Ik sta drie weekenden ingeroosterd. Dat is te veel. Mijn kinderen zijn dan thuis en ik heb geen oppas.
m: Dat begrijp ik. Maar we hebben in december weinig mensen. Twee collega's zijn met verlof.
v: Kunnen we dan niet een uitzendkracht vragen?
m: Dat hebben we geprobeerd, maar het uitzendbureau heeft ook niemand. Weet je wat? Ik kijk of Sanne één weekend met jou wil ruilen. Zij werkt liever in het weekend dan doordeweeks.
v: Dat zou fijn zijn. Laat je het me voor vrijdag weten?
m: Ik spreek haar morgen, dan hoor je het morgenmiddag.""",
     "vragen": [
        Q("b1e1-9", "Wat is het probleem van de vrouw?", ["Ze moet te veel weekenden werken.", "Ze heeft te weinig uren.", "Ze wil met verlof in december."],
          "Kadının üç hafta sonu çalışması planlanmış; bu ona çok fazla geliyor.", "Ik sta drie weekenden ingeroosterd. Dat is te veel."),
        Q("b1e1-10", "Waarom is er in december weinig personeel?", ["Twee collega's hebben verlof.", "Er zijn veel collega's ziek.", "Het verpleeghuis is groter geworden."],
          "Aralıkta iki çalışan izinde.", "Twee collega's zijn met verlof."),
        Q("b1e1-11", "Waarom kan er geen uitzendkracht komen?", ["Het uitzendbureau heeft niemand.", "Het is te duur.", "Marco wil het niet."],
          "Geçici personel ajansında da kimse yok.", "Dat hebben we geprobeerd, maar het uitzendbureau heeft ook niemand."),
        Q("b1e1-12", "Wat gaat Marco doen?", ["Hij vraagt Sanne om een weekend te ruilen.", "Hij werkt zelf een weekend.", "Hij maakt een nieuw rooster."],
          "Marco, Sanne'ye kadınla bir hafta sonunu değiştirip değiştiremeyeceğini soracak.", "Ik kijk of Sanne één weekend met jou wil ruilen."),
     ]},
    {"id": "b1-gemeente-afval", "intro": "U hoort een medewerker van de gemeente op een informatieavond.", "tekst": """
m: Goedenavond allemaal, fijn dat u er bent. Vanaf januari verandert er iets aan het ophalen van het afval in uw wijk. Op dit moment halen we het restafval elke week op. Dat wordt straks één keer per twee weken. Het gft-afval, dus groente, fruit en tuinafval, halen we juist vaker op: in de zomer elke week. Waarom doen we dit? In het restafval zit nog veel afval dat eigenlijk gerecycled kan worden. Door het restafval minder vaak op te halen, hopen we dat u beter gaat scheiden. U krijgt daarvoor een gratis bakje voor in de keuken. Voor gezinnen met kleine kinderen hebben we een uitzondering: wie luiers heeft, kan een extra container aanvragen. Dat kan via de website.""",
     "vragen": [
        Q("b1e1-13", "Wat verandert er in januari aan het restafval?", ["Het wordt minder vaak opgehaald.", "Het wordt vaker opgehaald.", "Bewoners moeten het zelf wegbrengen."],
          "Ev atığı haftada bir yerine iki haftada bir toplanacak.", "Dat wordt straks één keer per twee weken."),
        Q("b1e1-14", "Waarom doet de gemeente dit?", ["Zodat mensen hun afval beter scheiden", "Omdat het goedkoper is voor de bewoners", "Omdat er te weinig vuilniswagens zijn"],
          "Belediye insanların atıkları daha iyi ayırmasını umuyor.", "Door het restafval minder vaak op te halen, hopen we dat u beter gaat scheiden."),
        Q("b1e1-15", "Wat krijgen bewoners gratis?", ["Een bakje voor in de keuken", "Een extra container", "Vuilniszakken"],
          "Mutfak için ücretsiz küçük bir kova veriliyor. Ek konteyner sadece bezli aileler için ve başvuruyla.", "U krijgt daarvoor een gratis bakje voor in de keuken."),
        Q("b1e1-16", "Wie kan een extra container aanvragen?", ["Gezinnen met kinderen die luiers dragen", "Mensen met een grote tuin", "Alle gezinnen in de wijk"],
          "Bez kullanan küçük çocuğu olan aileler ek konteyner isteyebilir.", "wie luiers heeft, kan een extra container aanvragen."),
     ]},
    {"id": "b1-ouderavond", "intro": "U hoort een leerkracht op een ouderavond van de basisschool.", "tekst": """
v: Welkom op deze informatieavond over groep 8. Dit jaar is een belangrijk jaar voor uw kind, want het gaat naar de middelbare school. In februari krijgt uw kind het schooladvies. Dat advies baseren we niet op één toets, maar op wat we de afgelopen jaren van uw kind hebben gezien. Daarna maken de kinderen in april de doorstroomtoets. Is de uitslag van die toets hoger dan het advies? Dan kijken we opnieuw naar het advies. Lager wordt het advies nooit. Wij raden u aan om samen met uw kind naar open dagen van middelbare scholen te gaan. Die zijn meestal in januari en februari. Een lijst met data vindt u in de schoolapp.""",
     "vragen": [
        Q("b1e1-17", "Waarop is het schooladvies gebaseerd?", ["Op wat de school de afgelopen jaren van het kind heeft gezien", "Op de doorstroomtoets in april", "Op één toets in februari"],
          "Okul tavsiyesi tek bir sınava değil, son yıllarda çocukta görülenlere dayanıyor.", "Dat advies baseren we niet op één toets, maar op wat we de afgelopen jaren van uw kind hebben gezien."),
        Q("b1e1-18", "Wat gebeurt er als de toetsuitslag hoger is dan het advies?", ["De school kijkt opnieuw naar het advies.", "Het advies wordt lager.", "Het kind moet de toets opnieuw maken."],
          "Sınav sonucu tavsiyeden yüksekse okul tavsiyeyi yeniden değerlendiriyor. Tavsiye asla düşürülmüyor.", "Dan kijken we opnieuw naar het advies."),
        Q("b1e1-19", "Wat is waar over het advies?", ["Het wordt nooit lager.", "Het wordt altijd hoger na de toets.", "Ouders kiezen het zelf."],
          "'Lager wordt het advies nooit' = tavsiye hiçbir zaman düşmez.", "Lager wordt het advies nooit."),
        Q("b1e1-20", "Waar vinden ouders de data van de open dagen?", ["In de schoolapp", "Op de website van de gemeente", "In een brief van de middelbare school"],
          "Açık günlerin tarihleri okul uygulamasında.", "Een lijst met data vindt u in de schoolapp."),
     ]},
    {"id": "b1-huisarts-telefoon", "intro": "U hoort een telefoongesprek met de assistente van de huisarts.", "tekst": """
v: Huisartsenpraktijk Oost, met Linda.
m: Goedemorgen, met Yusuf Demir. Ik heb al twee weken last van mijn rug. Ik heb pijnstillers genomen, maar het wordt niet beter.
v: Heeft u ook andere klachten, bijvoorbeeld koorts of pijn in uw benen?
m: Nee, alleen mijn onderrug. Vooral 's ochtends.
v: Dan maak ik een afspraak voor u bij de fysiotherapeut van onze praktijk. Daarvoor heeft u geen verwijzing nodig. Hij heeft morgen om half elf plaats.
m: Morgen moet ik werken. Kan het ook later in de week?
v: Donderdag om vier uur?
m: Dat is goed.
v: Neem uw verzekeringspas mee. En als u koorts krijgt, belt u ons dan meteen terug.""",
     "vragen": [
        Q("b1e1-21", "Waarom belt Yusuf?", ["Hij heeft al twee weken rugpijn.", "Hij heeft koorts.", "Hij wil nieuwe pijnstillers."],
          "İki haftadır sırt ağrısı var ve ağrı kesiciler işe yaramamış.", "Ik heb al twee weken last van mijn rug."),
        Q("b1e1-22", "Wat regelt de assistente?", ["Een afspraak bij de fysiotherapeut", "Een afspraak bij de huisarts", "Een verwijzing naar het ziekenhuis"],
          "Asistan muayenehanedeki fizyoterapistten randevu ayarlıyor; sevk gerekmiyor.", "Dan maak ik een afspraak voor u bij de fysiotherapeut van onze praktijk."),
        Q("b1e1-23", "Wanneer gaat Yusuf naar de afspraak?", ["Donderdag om vier uur", "Morgen om half elf", "Vandaag nog"],
          "Yarın çalışıyor; perşembe saat dörtte gidiyor.", "Donderdag om vier uur?"),
        Q("b1e1-24", "Wanneer moet Yusuf terugbellen?", ["Als hij koorts krijgt", "Als de pijn minder wordt", "Als hij zijn pas kwijt is"],
          "Ateşi çıkarsa hemen geri araması gerekiyor.", "En als u koorts krijgt, belt u ons dan meteen terug."),
     ]},
    {"id": "b1-nieuws-energie", "intro": "U hoort een nieuwsbericht op de radio.", "tekst": """
o: Huishoudens in Nederland hebben vorig jaar gemiddeld tien procent minder gas gebruikt dan het jaar daarvoor. Dat blijkt uit nieuwe cijfers van het Centraal Bureau voor de Statistiek. Volgens onderzoekers komt dat vooral door de hoge energieprijzen: mensen zetten de verwarming lager en douchen korter. Ook hebben meer mensen hun huis beter geïsoleerd. Het warme voorjaar speelde ook een rol, maar volgens de onderzoekers een kleinere. Het stroomgebruik is juist iets gestegen. Dat komt door het groeiende aantal warmtepompen en elektrische auto's.""",
     "vragen": [
        Q("b1e1-25", "Wat is er vorig jaar gebeurd?", ["Huishoudens gebruikten minder gas.", "Huishoudens gebruikten meer gas.", "De gasprijs is gedaald."],
          "Haneler bir önceki yıla göre yaklaşık yüzde on daha az gaz kullanmış.", "Huishoudens in Nederland hebben vorig jaar gemiddeld tien procent minder gas gebruikt dan het jaar daarvoor."),
        Q("b1e1-26", "Wat is volgens de onderzoekers de belangrijkste oorzaak?", ["De hoge energieprijzen", "Het warme voorjaar", "De elektrische auto's"],
          "Ana neden yüksek enerji fiyatları; sıcak ilkbaharın etkisi daha küçük.", "Volgens onderzoekers komt dat vooral door de hoge energieprijzen"),
        Q("b1e1-27", "Wat is er met het stroomgebruik gebeurd?", ["Het is iets gestegen.", "Het is ook gedaald.", "Het is gelijk gebleven."],
          "Elektrik kullanımı biraz artmış.", "Het stroomgebruik is juist iets gestegen."),
        Q("b1e1-28", "Waardoor stijgt het stroomgebruik?", ["Door warmtepompen en elektrische auto's", "Door kortere douches", "Door betere isolatie"],
          "Isı pompaları ve elektrikli arabaların sayısı arttığı için.", "Dat komt door het groeiende aantal warmtepompen en elektrische auto's."),
     ]},
    {"id": "b1-sollicitatie", "intro": "U hoort een sollicitatiegesprek bij een supermarkt.", "tekst": """
m: Goedemiddag, mevrouw Haddad. Fijn dat u er bent. U solliciteert naar de functie van teamleider. Kunt u iets over uzelf vertellen?
v: Natuurlijk. Ik werk nu vier jaar als medewerker bij een andere supermarkt. Ik heb daar vaak de nieuwe collega's ingewerkt. Daarom wil ik nu graag leidinggeven.
m: Wat vindt u moeilijk aan leidinggeven, denkt u?
v: Ik denk dat het soms lastig is om iets te zeggen tegen collega's die al lang werken. Maar ik vind eerlijk communiceren belangrijk.
m: Wij zoeken iemand voor 32 uur per week, ook op zaterdag. Kan dat?
v: Dertig uur zou beter passen, omdat ik op woensdagmiddag voor mijn zoon zorg. Maar zaterdag is geen probleem.
m: Daar kunnen we vast iets over afspreken. U hoort volgende week van ons.""",
     "vragen": [
        Q("b1e1-29", "Waarom wil mevrouw Haddad teamleider worden?", ["Ze heeft vaak nieuwe collega's ingewerkt.", "Ze wil meer verdienen.", "Ze wil niet meer op zaterdag werken."],
          "Yeni çalışanlara sık sık işi öğrettiği için artık yönetici olmak istiyor.", "Ik heb daar vaak de nieuwe collega's ingewerkt. Daarom wil ik nu graag leidinggeven."),
        Q("b1e1-30", "Wat vindt ze moeilijk aan leidinggeven?", ["Iets zeggen tegen collega's die al lang werken", "Het rooster maken", "Eerlijk communiceren"],
          "Uzun süredir çalışanlara bir şey söylemeyi zor bulabileceğini düşünüyor; dürüst iletişimi ise önemli buluyor.", "Ik denk dat het soms lastig is om iets te zeggen tegen collega's die al lang werken."),
        Q("b1e1-31", "Waarom wil ze liever 30 uur werken?", ["Ze zorgt op woensdagmiddag voor haar zoon.", "Ze wil op zaterdag vrij zijn.", "Ze doet een opleiding."],
          "Çarşamba öğleden sonraları oğluna bakıyor.", "Dertig uur zou beter passen, omdat ik op woensdagmiddag voor mijn zoon zorg."),
        Q("b1e1-32", "Hoe eindigt het gesprek?", ["Ze hoort volgende week of ze de baan krijgt.", "Ze krijgt de baan meteen.", "Ze moet nog een gesprek doen."],
          "Gelecek hafta haber alacak.", "U hoort volgende week van ons."),
     ]},
    {"id": "b1-bibliotheek-taalcafe", "intro": "U hoort een vrijwilliger vertellen over het taalcafé in de bibliotheek.", "tekst": """
v: Hallo, ik ben Ellen en ik ben vrijwilliger bij het taalcafé. Elke dinsdagavond komen hier mensen die Nederlands leren. We praten in kleine groepen over allerlei onderwerpen: werk, het nieuws, feestdagen. Er is geen les en er zijn geen toetsen. Het gaat om oefenen in een ontspannen sfeer. Je hoeft je niet aan te melden; je kunt gewoon binnenlopen. Het is gratis, alleen de koffie kost vijftig cent. Veel deelnemers vertellen dat ze hier vrienden hebben gemaakt. En wie wil, kan na een paar maanden zelf helpen als gespreksleider.""",
     "vragen": [
        Q("b1e1-33", "Wat gebeurt er in het taalcafé?", ["Mensen oefenen Nederlands in kleine groepen.", "Mensen krijgen les en maken toetsen.", "Mensen lenen boeken."],
          "Küçük gruplarda sohbet ederek Hollandaca pratiği yapılıyor; ders ve sınav yok.", "We praten in kleine groepen over allerlei onderwerpen"),
        Q("b1e1-34", "Wat moet je doen als je wilt meedoen?", ["Niets, je kunt gewoon binnenlopen.", "Je aanmelden via de website", "Een toets maken"],
          "Kayıt gerekmiyor, doğrudan gelebilirsin.", "Je hoeft je niet aan te melden; je kunt gewoon binnenlopen."),
        Q("b1e1-35", "Wat kost geld?", ["De koffie", "Het taalcafé", "Het lidmaatschap van de bibliotheek"],
          "Dil kafesi ücretsiz; sadece kahve elli sent.", "Het is gratis, alleen de koffie kost vijftig cent."),
        Q("b1e1-36", "Wat kunnen deelnemers na een paar maanden doen?", ["Zelf gespreksleider worden", "Een diploma halen", "Les geven in de bibliotheek"],
          "İsteyen birkaç ay sonra kendisi sohbet yöneticisi olarak yardım edebilir.", "En wie wil, kan na een paar maanden zelf helpen als gespreksleider."),
     ]},
    {"id": "b1-woningcorporatie", "intro": "U hoort een gesprek tussen een huurder en een medewerker van de woningcorporatie.", "tekst": """
m: Goedemorgen, ik bel over schimmel in mijn badkamer. Het komt steeds terug, ook als ik het schoonmaak.
v: Vervelend. Zet u na het douchen een raam open of de ventilator aan?
m: Er is geen raam in de badkamer, en de ventilator maakt veel lawaai, dus die zet ik meestal uit.
v: Dan is dat waarschijnlijk de oorzaak. Laat de ventilator na het douchen minstens een half uur aan staan. Maar als hij zoveel lawaai maakt, is hij misschien kapot. Ik stuur een monteur om ernaar te kijken.
m: Moet ik daarvoor betalen?
v: Nee, een kapotte ventilator is onze verantwoordelijkheid. De monteur belt u binnen drie werkdagen voor een afspraak.""",
     "vragen": [
        Q("b1e1-37", "Waarom belt de man?", ["Er komt steeds schimmel in zijn badkamer.", "Zijn ventilator is gestolen.", "Hij wil een raam in de badkamer."],
          "Banyosunda temizlese de sürekli küf oluşuyor.", "Goedemorgen, ik bel over schimmel in mijn badkamer."),
        Q("b1e1-38", "Wat is waarschijnlijk de oorzaak?", ["De man zet de ventilator meestal uit.", "De man maakt de badkamer niet schoon.", "Het raam staat altijd open."],
          "Gürültü yaptığı için vantilatörü genelde kapatıyor; bu yüzden nem çıkmıyor.", "Dan is dat waarschijnlijk de oorzaak."),
        Q("b1e1-39", "Wie betaalt de reparatie?", ["De woningcorporatie", "De huurder", "De huurder en de corporatie samen"],
          "Bozuk vantilatör kira şirketinin sorumluluğu; kiracı ödemiyor.", "Nee, een kapotte ventilator is onze verantwoordelijkheid."),
        Q("b1e1-40", "Wat gebeurt er nu?", ["Een monteur belt binnen drie werkdagen voor een afspraak.", "De monteur komt vandaag.", "De man moet zelf een monteur zoeken."],
          "Teknisyen üç iş günü içinde randevu için arayacak.", "De monteur belt u binnen drie werkdagen voor een afspraak."),
     ]},
]
