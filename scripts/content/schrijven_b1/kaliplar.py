"""Schrijven I (B1) tactics: one entry per task type ('kalıp'), shown on the tactics page and in the hint box of each task.

Each entry: titel (Turkish), wat (what the task asks, Turkish), kaliplar (Dutch patterns to learn by heart; '…' = fill in),
voorbeeld (one short Dutch example), tips (Turkish), valkuil (common mistake, Turkish).
The task types follow the order of the official exams (CvTE 2023-2025): 1 reason, 2 sub-clause, 3 result with inversion,
4 te + infinitive, 5 other solution, 6 idea, 7 instruction, 8 announcement, 9 form, 10 pictures, 11 complaint, 12 choice.
"""

ALGEMEEN = {
    "titel": "Her görevde işe yarayan kurallar",
    "tips": [
        "Görevdeki cümleyi kopyalama: kopyalanan cümle puan almaz. Aynı fikri kendi kelimelerinle yaz.",
        "Kısa ve doğru, uzun ve hatalıdan iyidir. Fazladan yazdığın hatalı cümleler de puanını düşürür.",
        "Kelime sırası her zaman doğru olmalı: ana cümlede fiil 2. sırada, yan cümlede (omdat, als, dat, zodat) fiil sonda.",
        "de/het hatası sayılmaz, ama artikeli hiç yazmamak (ik heb vraag) hata sayılır.",
        "Resim ve tablo e-postaya eklenmez: 'op plaatje 1' yazma, ne gördüğünü anlat.",
        "Uzun görevlerde (10-12) önce istenen noktaları say, her biri için en az bir cümle yaz, sonunda tek tek kontrol et.",
        "Bağlantı kelimeleri samenhang puanı getirir: eerst, daarna, tot slot, want, omdat, daarom, maar, bovendien, ten eerste / ten tweede.",
    ],
    "aanhef": ["Beste meneer De Vries, / Beste mevrouw Jansen,", "Geachte heer, mevrouw, (şirkete, adı bilinmiyorsa)", "Hoi Sanne, / Beste Sanne, (iş arkadaşı, arkadaş)"],
    "slot": ["Met vriendelijke groet, + adın (resmî)", "Groeten, / Groetjes, + adın (samimi)", "Alvast bedankt voor uw antwoord.", "Ik hoor graag van u."],
}

KALIPLAR = {
    "reden": {
        "titel": "Neden söyle (ana cümle)",
        "wat": "Bir şeye gelemediğini/yapamadığını tek cümleyle ve nedeniyle söylüyorsun. Çoğu zaman 'een hoofdzin' istenir.",
        "kaliplar": ["Helaas kan ik … niet komen, want ik …", "Ik kan … niet, want ik heb dan …", "Op … heb ik helaas een afspraak bij …"],
        "voorbeeld": "Helaas kan ik woensdag niet komen, want ik heb een afspraak bij de tandarts.",
        "tips": ["'want' ana cümle bağlar: want'tan sonra normal sıra (want ik heb).", "Neden somut olsun: afspraak, ziek kind, werk, cursus."],
        "valkuil": "'want ik … heb' yazmak (fiili sona atmak) yanlış; o 'omdat' kuralı.",
    },
    "bijzin": {
        "titel": "Yan cümle (omdat …)",
        "wat": "Verilen cümleyi tamamlıyorsun; çoğu zaman 'omdat' ya da 'dat' ile başlayan bir yan cümle istenir.",
        "kaliplar": ["…, omdat ik … wil / moet / heb.", "…, omdat ik graag meer wil weten over …", "…, zodat ik … kan …"],
        "voorbeeld": "Ik wil graag een afspraak maken, omdat ik een nieuw paspoort moet aanvragen.",
        "tips": ["Yan cümlede çekimli fiil EN SONA: omdat ik een paspoort moet aanvragen.", "İki fiil varsa ikisi de sonda: moet aanvragen, wil volgen."],
        "valkuil": "'omdat ik moet een paspoort aanvragen' — fiil ortada kalırsa gramer puanı 0.",
    },
    "gevolg": {
        "titel": "Sonuç + devrik cümle (inversie)",
        "wat": "Bir sorunun sonucunu yazıyorsun. Cümle 'Door …', 'Omdat … ,' ya da 'Sinds …' ile başlar, bu yüzden devrik yapı (fiil özneden önce) gerekir.",
        "kaliplar": ["Door de kapotte … kan ik niet …", "Omdat de … kapot is, moet ik …", "Sinds … kunnen wij niet meer …", "Daardoor kan ik …"],
        "voorbeeld": "Door de kapotte printer kan ik de facturen niet versturen.",
        "tips": ["Cümle başında başka bir şey varsa (Door…, Sinds…, Daardoor, Daarom) hemen ardından FİİL gelir: Door de lift kan mijn moeder…", "'Omdat …, ' yan cümlesinden sonra da ana cümle fiille başlar: Omdat de printer kapot is, kan ik…"],
        "valkuil": "'Door de kapotte lift mijn moeder kan niet…' — özne fiilden önce: devrik değil.",
    },
    "te-inf": {
        "titel": "'om … te + mastar'",
        "wat": "Cümle 'Is het mogelijk om …', 'Ik heb zin om …', 'Wij zijn van plan om …' gibi biter; 'te + mastar' ile tamamlarsın.",
        "kaliplar": ["Is het mogelijk om … te …?", "Ik heb zin om … te …", "Wij zijn van plan om … te …", "Ik probeer om … te …"],
        "voorbeeld": "Is het mogelijk om op zaterdag extra te oefenen?",
        "tips": ["'te' + mastar EN SONDA: om op zaterdag extra te oefenen.", "Ayrılabilir fiilde 'te' araya girer: mee te doen, op te halen, af te spreken."],
        "valkuil": "'om te oefenen op zaterdag extra' gibi 'te + mastar'ı ortada bırakmak ya da 'te'yi unutmak.",
    },
    "voorstel": {
        "titel": "Başka bir çözüm öner",
        "wat": "Birinin isteğini olduğu gibi yapamıyorsun ama başka bir çözüm öneriyorsun.",
        "kaliplar": ["… kan ik helaas niet, maar ik kan wel …", "Misschien kun je …", "Zullen we …?", "Wat vind je van …?"],
        "voorbeeld": "Morgen heb ik mijn parkeerplaats zelf nodig, maar je kunt misschien in de garage naast het kantoor parkeren.",
        "tips": ["İki parça: hayır + çözüm. Sadece 'nee' yazmak görevi karşılamaz.", "'maar … wel' yapısı çok iş görür."],
        "valkuil": "Çözüm önermeden sadece neden yapamadığını anlatmak.",
    },
    "idee": {
        "titel": "Bir fikir yaz",
        "wat": "Bir kulüp, okul ya da iş için fikir istiyorlar (para toplamak, hediye, etkinlik).",
        "kaliplar": ["We kunnen …", "Mijn idee is om … te …", "Het lijkt me leuk om …", "Misschien kunnen we …"],
        "voorbeeld": "We kunnen op de kerstmarkt zelfgebakken koekjes verkopen.",
        "tips": ["Tek, somut ve uygulanabilir bir fikir yeter.", "'Mijn idee is om … te …' aynı zamanda te-inf pratiği."],
        "valkuil": "Konudan sapmak: fikir, istenen amaca (para kazanmak, hediye…) uymalı.",
    },
    "instructie": {
        "titel": "Ne yapmalı? (talimat)",
        "wat": "Bir kampanya, ilan ya da kural için müşterilere/okurlara ne yapmaları gerektiğini yazıyorsun.",
        "kaliplar": ["Koop … en u krijgt …", "Laat … zien, dan krijgt u …", "U moet … om … te krijgen.", "Meld u aan via …"],
        "voorbeeld": "Laat uw studentenkaart zien bij de balie, dan krijgt u 20% korting.",
        "tips": ["Emir kipi (Koop, Laat zien, Meld u aan) kısa ve doğrudur.", "Ne yapacağını VE ne kazanacağını yaz."],
        "valkuil": "Sadece kampanyayı tekrar etmek ('Elke tweede taart halve prijs') — görev ne yapılacağını soruyor.",
    },
    "mededeling": {
        "titel": "Duyuru",
        "wat": "Bir grup (mahalle, kulüp, bülten) için bir haber/duyuru yazıyorsun.",
        "kaliplar": ["Goed nieuws: …", "Helaas gaat … niet door, omdat …", "… verplaatsen we naar …", "Graag tot …!"],
        "voorbeeld": "Door het slechte weer gaat het buurtfeest zaterdag niet door; we verplaatsen het naar 21 juni.",
        "tips": ["Ne oldu + (varsa) ne zaman / ne olacak.", "'Helaas … niet door, omdat …' iptal duyurularında hazır kalıp."],
        "valkuil": "Görevdeki cümleyi aynen kopyalamak.",
    },
    "formulier": {
        "titel": "Form doldurma",
        "wat": "Bir formu dolduruyorsun. Her alan dolu olunca 2 puandan başlarsın; açıklama alanlarında tam cümle beklenir.",
        "kaliplar": ["Ik wil deze cursus volgen, omdat …", "Ik heb (nog) geen ervaring met …, maar …", "Ik wil graag …, want ik …", "Ik verwacht dat …"],
        "voorbeeld": "Waarom: Op mijn afdeling werken veel mensen. Ik wil kunnen helpen als iemand onwel wordt.",
        "tips": ["HİÇBİR alanı boş bırakma; bilmiyorsan uydur, doğruluğu puanlanmaz.", "'minstens twee zinnen' yazıyorsa iki tam cümle yaz.", "Evet/hayır sorusunda bir cümle açıklama ekle."],
        "valkuil": "Açıklama alanına tek kelime yazmak ('helpen').",
    },
    "plaatjes": {
        "titel": "Resimlerle anlatma (e-posta)",
        "wat": "Resimlerdeki olayları sırayla anlatıyor, sonra fikrini ve önerini nedeniyle yazıyorsun. Okuyan resimleri görmüyor.",
        "kaliplar": ["Eerst hebben we … / Daarna zijn we naar … geweest. / Tot slot hebben we …",
                     "Het leukst vond ik …, omdat …", "Volgend jaar wil ik graag naar …, want …", "Bedankt voor …"],
        "voorbeeld": "Eerst hebben we een rondvaart gemaakt. Daarna hebben we geluncht, en tot slot zijn we naar een museum geweest.",
        "tips": ["Her resim için bir cümle: eerst – daarna – tot slot (samenhang puanı).", "Geçmiş zaman: hebben/zijn + voltooid deelwoord (hebben gemaakt, zijn geweest).", "Her 'waarom' için 'omdat/want' ile bir neden."],
        "valkuil": "'Op plaatje 1 zie je…' yazmak; okuyan resmi görmüyor.",
    },
    "klacht": {
        "titel": "Şikâyet + çözüm (ikna e-postası)",
        "wat": "Bir şirkete şikâyet ediyorsun: ne aldın, ne oldu, ne düşünüyorsun, iki çözüm, tercihin ve beklentin.",
        "kaliplar": ["Op … heb ik bij u … besteld / gekocht.", "De levering zou op … zijn, maar nu …", "Dat vind ik erg vervelend, omdat …",
                     "Ik zie twee oplossingen: … of …", "Mijn voorkeur gaat uit naar …, omdat …", "Ik verwacht dat u … / Ik verwacht binnen … een reactie."],
        "voorbeeld": "Ik zie twee oplossingen: u levert een andere wasmachine, of ik krijg korting. Mijn voorkeur gaat uit naar een andere wasmachine, omdat …",
        "tips": ["Bu görevde 6 nokta var; kalıplar sırayla 6 noktayı karşılıyor — ezberle, sınavda doldur.", "'Geachte heer, mevrouw,' ile başla, 'Met vriendelijke groet,' ile bitir.", "Kibar ama net ol: 'Ik verwacht …'."],
        "valkuil": "Sadece bir çözüm yazmak — en az iki çözüm isteniyor.",
    },
    "keuze": {
        "titel": "Karşılaştır ve seç (tablodan)",
        "wat": "Tablodaki seçenekleri karşılaştırıp birini seçiyor, nedenlerini ve diğerlerinin eksiklerini yazıyorsun.",
        "kaliplar": ["Ik schrijf je omdat …", "Ik heb drie … gevonden: …, … en …", "Ik kies het liefst voor …, want … Bovendien …",
                     "… is minder geschikt, omdat …", "… vind ik ook minder goed, want …", "Zullen we … bellen / mailen / langsgaan?"],
        "voorbeeld": "Ik kies het liefst voor Sportshop Max, want het is dichtbij. Bovendien krijgen we een stagevergoeding. De boekhandel is minder geschikt, omdat …",
        "tips": ["Seçtiğin için EN AZ iki neden ('want … Bovendien …').", "Diğer HER seçenek için en az bir neden.", "Tablodaki bilgiyi cümleye çevir; tabloyu kopyalama."],
        "valkuil": "Diğer seçeneklerin neden uygun olmadığını unutmak — puan kaybettirir.",
    },
}


def kalip_van(t):
    """Task type of one task (used by build_schrijven_b1.py)."""
    if t["soort"] == "formulier":
        return "formulier"
    if t["soort"] == "tekst":
        if t.get("bijlage", "").startswith("Plaatje"):
            return "plaatjes"
        if any("oplossingen" in e for e in t["elementen"]):
            return "klacht"
        if t.get("bijlage", "").startswith("Tabel"):
            return "keuze"
        raise ValueError(f"{t['id']}: unknown text task type")
    if t["gram"] == "hoofdzin":
        return "reden"
    if t["gram"] == "bijzin":
        return "bijzin"
    if t["gram"] == "inversie":
        return "gevolg"
    if t["gram"] == "te-inf":
        return "te-inf"
    a = t["adequaat"]
    for key, word in (("voorstel", "oplossing"), ("idee", "idee"), ("instructie", "moeten doen"), ("mededeling", "deelt mee")):
        if word in a:
            return key
    raise ValueError(f"{t['id']}: unknown sentence task type")
