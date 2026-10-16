"""Lezen I practice texts 1-3 (own texts in exam style; all names and places are made up).

Text format: blocks separated by a blank line. '## ' = heading, '- ' lines = list,
lines with ' | ' = table (first line is the header). 'kop' = e-mail header lines.
Questions: 3 options, the right one first (the page shuffles), 'uitleg' in Turkish,
'bewijs' = the exact sentence from the text that gives the answer (highlighted on the result page).
'patroon' = number of the question pattern (1-17) in data/lezen-bank.json patterns.
"""

T01 = {
    "id": "parkeren",
    "titel": "Parkeervergunning voor bewoners",
    "soort": "Website gemeente",
    "domein": "overig",
    "tekstsoort": "instructief",
    "inleiding": "Deze tekst komt van de website van de gemeente Rijnstad. De tekst gaat over parkeren in het centrum.",
    "tekst": """Woont u in het centrum van Rijnstad en heeft u een auto? Dan mag u in uw straat alleen parkeren met een parkeervergunning. Op deze pagina leest u hoe u een vergunning aanvraagt en wat het kost.

## Wie kan een vergunning aanvragen?

U kunt een vergunning aanvragen als u ingeschreven staat op een adres in het vergunninggebied. De auto moet op uw naam staan. Rijdt u in een auto van uw werkgever of in een leaseauto? Dan stuurt u een verklaring van uw werkgever of het leasebedrijf mee. Hierin staat dat u de auto ook privé mag gebruiken.

## Wat kost het?

Per adres krijgt u maximaal twee vergunningen. De eerste vergunning kost € 65 per jaar. Voor een tweede vergunning betaalt u € 130 per jaar.

## Hoe vraagt u de vergunning aan?

U vraagt de vergunning aan via de website van de gemeente. U logt in met uw DigiD. Binnen vijf werkdagen ontvangt u bericht of u de vergunning krijgt. Heeft u geen DigiD? Maak dan een afspraak bij de balie in het stadhuis. Neem een geldig identiteitsbewijs en uw kentekenbewijs mee.

## Bezoek

Krijgt u bezoek met de auto? Dan kunt u een bezoekersvergunning aanvragen. Uw bezoek kan daarmee maximaal 40 uur per maand parkeren voor € 0,50 per uur. U meldt uw bezoek aan via de app of de website.

## Laden van een elektrische auto

Heeft u een elektrische auto en geen eigen oprit? Dan kunt u bij de gemeente een openbare laadpaal in uw straat aanvragen. De gemeente plaatst een laadpaal als er binnen 250 meter van uw huis nog geen laadpaal is. U betaalt alleen voor de stroom die u gebruikt. Een parkeervergunning blijft wel nodig, ook als u bij een laadpaal staat.

## Mensen met een beperking

Kunt u door een ziekte of handicap niet ver lopen? Dan kunt u een gehandicaptenparkeerkaart aanvragen. Met deze kaart mag u in het centrum gratis parkeren. In sommige gevallen kan de gemeente ook een eigen parkeerplaats bij uw huis maken. Hiervoor is eerst een medisch onderzoek nodig.

## Veranderingen

Heeft u een andere auto gekocht? Geef het nieuwe kenteken dan uiterlijk binnen twee weken door. Dit is gratis. Gaat u verhuizen, ook binnen Rijnstad? Dan vervalt uw vergunning op de dag van de verhuizing en moet u een nieuwe vergunning aanvragen. Parkeert u zonder geldige vergunning, dan kunt u een boete krijgen.""",
    "vragen": [
        {"id": "p1", "patroon": 15, "vraag": "Voor wie is deze tekst vooral bedoeld?",
         "opties": ["Bewoners van het centrum met een auto", "Mensen die op bezoek komen in Rijnstad", "Werkgevers met leaseauto's"],
         "uitleg": "Metin ilk cümlede okura hitap ediyor: merkezde oturan ve arabası olanlar. Ziyaretçiler ve işverenler sadece yan konular.",
         "bewijs": "Woont u in het centrum van Rijnstad en heeft u een auto?"},
        {"id": "p2", "patroon": 8, "vraag": "Sara rijdt in een leaseauto van haar werk. Wanneer kan zij een vergunning krijgen?",
         "opties": ["Als zij een verklaring van haar werkgever of het leasebedrijf meestuurt", "Als haar werkgever de vergunning betaalt", "Als zij de auto alleen voor haar werk gebruikt"],
         "uitleg": "Leaseauto için işverenden ya da leasing şirketinden bir yazı (verklaring) gerekiyor. C şıkkı tam tersi: yazıda arabayı özel kullanım için de kullanabildiği yazmalı.",
         "bewijs": "Dan stuurt u een verklaring van uw werkgever of het leasebedrijf mee."},
        {"id": "p3", "patroon": 14, "vraag": "De familie De Vries heeft twee auto's. Hoeveel betalen zij per jaar voor twee vergunningen?",
         "opties": ["€ 195", "€ 65", "€ 130"],
         "uitleg": "İlk izin 65 €, ikinci izin 130 €: toplam 195 €. Rakam sorularında iki bilgiyi toplamak gerekebilir.",
         "bewijs": "De eerste vergunning kost € 65 per jaar. Voor een tweede vergunning betaalt u € 130 per jaar."},
        {"id": "p4", "patroon": 13, "vraag": "Meneer Ahmadi heeft geen DigiD. Wat moet hij doen?",
         "opties": ["Een afspraak maken bij de balie in het stadhuis", "De vergunning via de app aanvragen", "Een brief sturen met zijn kentekenbewijs"],
         "uitleg": "'Heeft u geen DigiD? Maak dan …' kalıbı: soru + 'dan' ile ne yapılacağı söyleniyor.",
         "bewijs": "Heeft u geen DigiD? Maak dan een afspraak bij de balie in het stadhuis."},
        {"id": "p5", "patroon": 7, "vraag": "Wat gebeurt er als u binnen Rijnstad verhuist?",
         "opties": ["Uw vergunning stopt en u moet een nieuwe aanvragen", "U neemt uw vergunning mee naar het nieuwe adres", "U geeft binnen twee weken uw nieuwe adres door"],
         "uitleg": "'vervalt' = geçersiz olur, biter. 'Binnen twee weken' yeni plaka içindi, taşınma için değil: tuzak şık.",
         "bewijs": "Dan vervalt uw vergunning op de dag van de verhuizing en moet u een nieuwe vergunning aanvragen."},
        {"id": "p6", "patroon": 17, "vraag": "Welke bewering is juist volgens de tekst?",
         "opties": ["Bezoek mag maximaal 40 uur per maand parkeren", "Een nieuw kenteken doorgeven kost geld", "U hoort binnen twee weken of u een vergunning krijgt"],
         "uitleg": "Her şıkkı metinde kontrol et: plaka değişikliği ücretsiz ('Dit is gratis'), cevap 5 iş günü içinde geliyor. Sadece A doğru.",
         "bewijs": "Uw bezoek kan daarmee maximaal 40 uur per maand parkeren voor € 0,50 per uur."},
    ],
}

T02 = {
    "id": "examentraining",
    "titel": "Belangrijke informatie over de examentraining",
    "soort": "E-mail",
    "domein": "educatie",
    "tekstsoort": "instructief",
    "inleiding": "Deze e-mail is gestuurd door een taalcentrum aan zijn cursisten.",
    "kop": ["Van: Taalcentrum De Brug", "Aan: cursisten Nederlands B1", "Onderwerp: Belangrijke informatie over de examentraining"],
    "tekst": """Beste cursist,

Over vier weken start de examentraining voor het Staatsexamen NT2. In deze e-mail leest u wat u moet weten.

## Aanmelden

De examentraining is niet verplicht, maar wij raden hem iedereen aan die dit jaar examen doet. U meldt zich aan via het formulier op onze website. Doe dit uiterlijk vrijdag 6 november. Er zijn maximaal 14 plaatsen per groep. Zodra een groep vol is, komt u op een wachtlijst.

## Lessen en aanwezigheid

De training bestaat uit zes lessen van twee uur, op zaterdagochtend van 10.00 tot 12.00 uur. Om een certificaat te krijgen, moet u minimaal vijf lessen aanwezig zijn. Bent u ziek of kunt u een keer niet komen? Meld dit dan vóór 9.00 uur bij uw docent. U kunt een gemiste les niet inhalen, maar u krijgt het lesmateriaal wel per e-mail.

## Wat doe je in de training?

In de training oefen je met examens van vorige jaren. Je leert hoe je je tijd goed verdeelt en hoe je de vragen snel kunt beantwoorden. Na elke les bespreekt je docent welke fouten veel voorkomen. Ook oefen je voor het examen Spreken: in kleine groepjes en met opnames van jezelf. De laatste les is een proefexamen onder echte examenomstandigheden. Daarna hoor je hoe je ervoor staat.

## Kosten

De training kost € 90. Voor cursisten die nu al een cursus bij ons volgen, is de prijs € 60. Werkt u? Vraag dan aan uw werkgever of hij de kosten wil betalen. Veel werkgevers vergoeden een taalcursus.

## Het examen zelf

Het staatsexamen zelf vindt niet bij ons plaats. U meldt zich daarvoor zelf aan. Doe dat op tijd, want de plaatsen zijn vaak snel vol. Wij kunnen u helaas niet aanmelden.

## Vragen?

Heeft u vragen over de training of over het examen zelf? Mevrouw Van Dijk, onze coördinator examens, is bereikbaar op maandag en woensdag tussen 13.00 en 16.00 uur. Voor vragen over betalen kunt u terecht bij de receptie.

Met vriendelijke groet,
Team Taalcentrum De Brug""",
    "vragen": [
        {"id": "e1", "patroon": 1, "vraag": "Wat is het belangrijkste doel van deze e-mail?",
         "opties": ["Cursisten informeren over de examentraining", "Cursisten uitnodigen voor het staatsexamen", "Cursisten vertellen dat de training verplicht is"],
         "uitleg": "Giriş paragrafı amacı söylüyor: bilmeniz gerekenleri anlatmak (informeren). Eğitim zorunlu değil, C yanlış.",
         "bewijs": "In deze e-mail leest u wat u moet weten."},
        {"id": "e2", "patroon": 8, "vraag": "Wanneer moet u zich uiterlijk aanmelden?",
         "opties": ["Op vrijdag 6 november", "Over vier weken", "Zodra de groep vol is"],
         "uitleg": "'uiterlijk' = en geç. 'Over vier weken' eğitimin başladığı zaman, kayıt tarihi değil.",
         "bewijs": "Doe dit uiterlijk vrijdag 6 november."},
        {"id": "e3", "patroon": 13, "vraag": "Wat moet u doen om een certificaat te krijgen?",
         "opties": ["Minimaal vijf van de zes lessen aanwezig zijn", "Alle zes lessen volgen en het lesmateriaal lezen", "De gemiste lessen inhalen"],
         "uitleg": "'minimaal vijf lessen' = en az beş ders. Kaçırılan ders telafi edilemiyor, C yanlış.",
         "bewijs": "Om een certificaat te krijgen, moet u minimaal vijf lessen aanwezig zijn."},
        {"id": "e4", "patroon": 14, "vraag": "Ali volgt nu de cursus B1 bij Taalcentrum De Brug. Hoeveel kost de examentraining voor hem?",
         "opties": ["€ 60", "€ 90", "Niets, zijn werkgever betaalt"],
         "uitleg": "Ali zaten kursiyer, indirimli fiyat 60 €. İşverenin ödeyip ödemeyeceği metinde kesin değil, sadece 'sor' deniyor.",
         "bewijs": "Voor cursisten die nu al een cursus bij ons volgen, is de prijs € 60."},
        {"id": "e5", "patroon": 9, "vraag": "Bij wie kunt u terecht met een vraag over betalen?",
         "opties": ["Bij de receptie", "Bij mevrouw Van Dijk", "Bij uw docent"],
         "uitleg": "Mevrouw Van Dijk eğitim ve sınav soruları için; ödeme soruları için resepsiyon.",
         "bewijs": "Voor vragen over betalen kunt u terecht bij de receptie."},
        {"id": "e6", "patroon": 7, "vraag": "Wat gebeurt er als u een les mist?",
         "opties": ["U krijgt het lesmateriaal per e-mail", "U kunt de les in een andere week inhalen", "U krijgt geen certificaat"],
         "uitleg": "Ders telafi edilmiyor ama materyal e-postayla geliyor. Bir ders kaçırmak sertifikayı engellemez (en az 5/6).",
         "bewijs": "U kunt een gemiste les niet inhalen, maar u krijgt het lesmateriaal wel per e-mail."},
    ],
}

T03 = {
    "id": "ziekmelden",
    "titel": "Ziek? Zo meld je je af",
    "soort": "Personeelsinformatie",
    "domein": "werk",
    "tekstsoort": "descriptief",
    "inleiding": "Deze tekst komt uit de personeelsinformatie van een zorgcentrum. De tekst gaat over de regels bij ziekte.",
    "tekst": """Iedereen is weleens ziek. Om goed voor onze cliënten te kunnen zorgen, moeten we snel weten wie er niet komt. Daarom gelden bij zorgcentrum De Linde de volgende regels.

## Ziek melden

Ben je ziek? Bel dan zo snel mogelijk, maar uiterlijk een uur voordat je dienst begint, naar je leidinggevende. Een sms of WhatsApp is niet genoeg: we willen je spreken. Je leidinggevende vraagt hoe het met je gaat en hoe lang je denkt dat je ziek blijft. Je hoeft niet te vertellen wat je precies hebt.

## Tijdens je ziekte

Blijf bereikbaar op je telefoonnummer en je huisadres. Ga je tijdens je ziekte ergens anders logeren, bijvoorbeeld bij familie? Geef dan het adres door aan je leidinggevende. Ben je langer dan een week ziek, dan neemt je leidinggevende contact met je op om samen te bespreken hoe het gaat.

## Ziek tijdens je vakantie

Word je ziek tijdens je vakantie? Meld je dan op dezelfde manier ziek bij je leidinggevende, ook als je in het buitenland bent. Stuur daarna een verklaring van een arts waarin staat hoe lang je ziek bent geweest. De dagen dat je ziek was, gelden dan niet als vakantiedagen. Zonder verklaring van een arts worden je vakantiedagen wel van je saldo afgehaald.

## De bedrijfsarts

Ben je na vier weken nog niet beter? Dan krijg je een afspraak met de bedrijfsarts. De bedrijfsarts geeft advies over je herstel en over werk dat je misschien al wel kunt doen. Alleen de bedrijfsarts mag weten wat je ziekte is. Hij vertelt je leidinggevende alleen wat je wel en niet kunt. Ben je het niet eens met het advies van de bedrijfsarts? Dan mag je een tweede mening vragen aan een andere bedrijfsarts. De kosten daarvan betaalt De Linde.

## Gedeeltelijk werken

Soms kun je al een deel van je werk doen, terwijl je nog niet helemaal beter bent. Je kunt bijvoorbeeld eerst een paar uur per dag werken, of alleen taken doen die niet zwaar zijn. Dit heet 'aangepast werk'. Je leidinggevende en de bedrijfsarts bespreken samen met jou wat mogelijk is. Voor de uren dat je aangepast werk doet, krijg je gewoon je salaris.

## Beter melden

Ben je weer beter? Meld je dan beter bij je leidinggevende, uiterlijk de dag voordat je weer gaat werken. Zo kan je leidinggevende het rooster op tijd aanpassen.

## Vragen

Heb je vragen over je rechten en plichten bij ziekte? Kijk dan in het personeelshandboek of neem contact op met Personeelszaken.""",
    "vragen": [
        {"id": "z2", "patroon": 13, "vraag": "Wat moet je doen als je ziek bent?",
         "opties": ["Uiterlijk een uur voor je dienst je leidinggevende bellen", "Een WhatsApp sturen naar je leidinggevende", "Je ziek melden bij Personeelszaken"],
         "uitleg": "Telefon etmek gerekiyor; mesaj yetmiyor ('niet genoeg'). Personeelszaken sadece haklarınla ilgili sorular için.",
         "bewijs": "Een sms of WhatsApp is niet genoeg: we willen je spreken."},
        {"id": "z3", "patroon": 12, "vraag": "Welke regel geldt volgens de tekst?",
         "opties": ["Je hoeft niet te vertellen welke ziekte je hebt", "Je moet thuis blijven tijdens je ziekte", "Je moet na een week naar de bedrijfsarts"],
         "uitleg": "Hastalığını söylemek zorunda değilsin. Başka yerde kalabilirsin (adresi bildirmek şartıyla); işyeri doktoru 4 hafta sonra.",
         "bewijs": "Je hoeft niet te vertellen wat je precies hebt."},
        {"id": "z4", "patroon": 8, "vraag": "Wanneer krijg je een afspraak met de bedrijfsarts?",
         "opties": ["Als je na vier weken nog niet beter bent", "Als je langer dan een week ziek bent", "Als je je weer beter meldt"],
         "uitleg": "Bir haftadan sonra yönetici arıyor; işyeri doktoru dört haftadan sonra. İki süreyi karıştırma.",
         "bewijs": "Ben je na vier weken nog niet beter? Dan krijg je een afspraak met de bedrijfsarts."},
        {"id": "z5", "patroon": 5, "vraag": "Wat wordt in de tekst bedoeld met 'je beter melden'?",
         "opties": ["Laten weten dat je weer kunt werken", "Een betere melding doen dan de eerste keer", "De bedrijfsarts vertellen hoe je je voelt"],
         "uitleg": "'beter' burada 'daha iyi' değil, 'iyileşmiş'. Kendini iyileşmiş olarak bildirmek = işe dönebileceğini haber vermek.",
         "bewijs": "Ben je weer beter? Meld je dan beter bij je leidinggevende, uiterlijk de dag voordat je weer gaat werken."},
        {"id": "z6", "patroon": 6, "vraag": "Wie mag weten wat je ziekte is, volgens de tekst?",
         "opties": ["Alleen de bedrijfsarts", "Je leidinggevende", "Personeelszaken"],
         "uitleg": "'Alleen' kelimesine dikkat: sadece işyeri doktoru. Yönetici sadece neyi yapıp yapamayacağını öğrenir.",
         "bewijs": "Alleen de bedrijfsarts mag weten wat je ziekte is."},
    ],
}

TEKSTEN = [T01, T02, T03]
