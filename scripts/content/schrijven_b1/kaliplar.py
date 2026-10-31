"""Schrijven I (B1) tactics: one entry per task type ('kalıp'), shown on the tactics page and in the hint box of each task.

Each entry: titel (Turkish), wat (what the task asks, Turkish), kaliplar (Dutch patterns to learn by heart; '…' = fill in),
voorbeeld (one short Dutch example), tips (Turkish), valkuil (common mistake, Turkish).
The task types follow the order of the official exams (CvTE 2023-2025): 1 reason, 2 sub-clause, 3 result with inversion,
4 te + infinitive, 5 other solution, 6 idea, 7 instruction, 8 announcement, 9 form, 10 pictures, 11 complaint, 12 choice.
"""

# Three rules shown at the top of the tactics page (kept short on purpose: the user found the long version confusing)
ALGEMEEN = {
    "regels": [
        "Görevdeki her soruya / her noktaya bir cümleyle cevap ver. Bitirince tek tek kontrol et.",
        "Görev metnindeki cümleleri olduğu gibi kopyalama: kopya cümle puan almaz.",
        "Hitabı karıştırma: arkadaşa baştan sona 'je', şirkete / resmî kişiye baştan sona 'u'.",
    ],
}

# E-mail / letter skeleton (tasks 10-12 and often 9). Standard Dutch letter phrases; presented as
# "phrases that work", not as something the official model requires. Every phrase is [Dutch, Turkish].
BRIEF = {
    "delen": [
        {"deel": "Hitap", "wanneer": "Mektubun ilk satırı, sonuna virgül. Adı biliyorsan adını yaz.",
         "je": [["Beste Ahmet,", "Sevgili / Merhaba Ahmet,"], ["Hoi Lisa,", "Selam Lisa, (çok samimi)"]],
         "u": [["Geachte heer De Vries,", "Sayın Bay De Vries, (soyadıyla)"], ["Geachte mevrouw Jansen,", "Sayın Bayan Jansen,"],
               ["Geachte heer/mevrouw,", "Sayın yetkili, (adı bilmiyorsan)"]]},
        {"deel": "Açılış", "wanneer": "İlk cümle: neden yazdığını söyle. Bir mesaja cevap veriyorsan önce teşekkür et.",
         "je": [["Bedankt voor je mail.", "Mailin için teşekkürler."], ["Ik schrijf je omdat …", "Sana yazıyorum, çünkü …"]],
         "u": [["Ik schrijf u omdat …", "Size yazıyorum, çünkü …"], ["Ik wil u laten weten dat …", "Size … olduğunu bildirmek istiyorum."],
               ["Naar aanleiding van uw advertentie …", "İlanınızla ilgili olarak …"]]},
        {"deel": "Gövde", "wanneer": "Görevdeki her nokta için en az bir cümle. Cümleleri bağlantı kelimeleriyle birleştir.",
         "je": [["eerst / daarna / tot slot", "önce / sonra / son olarak"], ["want / omdat / daarom", "çünkü / çünkü (fiil sona) / bu yüzden"],
                ["ook / bovendien / maar", "ayrıca / üstelik / ama"]],
         "u": []},
        {"deel": "Kapanış cümlesi", "wanneer": "Selamdan hemen önce, tek cümle. Cevap bekliyorsan, haber vereceksen ya da teşekkür ediyorsan.",
         "je": [["Ik houd je op de hoogte.", "Seni gelişmelerden haberdar edeceğim."], ["Laat je het me weten?", "Bana haber verir misin?"],
                ["Ik hoor graag van je.", "Senden haber bekliyorum."], ["Tot snel!", "Görüşmek üzere!"]],
         "u": [["Ik hoor graag van u.", "Sizden haber bekliyorum."], ["Ik houd u op de hoogte.", "Sizi gelişmelerden haberdar edeceğim."],
               ["Alvast bedankt voor uw hulp.", "Yardımınız için şimdiden teşekkürler."], ["Ik zie uw antwoord graag tegemoet.", "Cevabınızı bekliyorum. (çok resmî)"]]},
        {"deel": "Selam", "wanneer": "Son satır, sonra alt satıra adın.",
         "je": [["Groetjes,", "Sevgiler,"], ["Hartelijke groet,", "İçten selamlar,"]],
         "u": [["Met vriendelijke groet,", "Saygılarımla,"]]},
    ],
    "situaties": [
        ["Davete evet", [["Wat leuk! Ik kom graag.", "Ne güzel! Seve seve gelirim."], ["Bedankt voor de uitnodiging.", "Davet için teşekkürler."]]],
        ["Davete hayır", [["Helaas kan ik niet komen, want …", "Maalesef gelemiyorum, çünkü …"], ["Misschien kunnen we een andere keer afspreken?", "Belki başka bir zaman buluşabiliriz?"]]],
        ["Şikâyet", [["Ik ben niet tevreden over …", "… konusunda memnun değilim."], ["Ik wil graag dat u …", "… yapmanızı istiyorum."], ["Kunt u … oplossen?", "… sorununu çözebilir misiniz?"]]],
        ["Bilgi isteme", [["Ik wil graag weten …", "… öğrenmek istiyorum."], ["Kunt u mij vertellen …?", "Bana … söyleyebilir misiniz?"]]],
        ["Özür", [["Het spijt me dat …", "… için üzgünüm."], ["Nogmaals sorry.", "Tekrar özür dilerim."]]],
        ["Teşekkür", [["Bedankt voor …", "… için teşekkürler."], ["Ik vond het erg leuk / fijn.", "Çok hoşuma gitti / çok güzeldi."]]],
    ],
    # Example tasks in the style of the exam (invented names), each with a full answer
    "voorbeelden": [
        {"titel": "Davete hayır (je)",
         "opdracht": "Uw collega Sanne viert zaterdag haar verjaardag. U kunt niet komen. Schrijf een e-mail aan Sanne. Schrijf in de e-mail:\n- dat u niet kunt komen en waarom\n- een voorstel om een andere keer af te spreken",
         "tr": "İş arkadaşın Sanne cumartesi doğum gününü kutluyor, gidemiyorsun. Gelemediğini, nedenini ve başka bir zaman için öneri yaz.",
         "antwoord": "Beste Sanne,\n\nBedankt voor je uitnodiging voor je verjaardag. Helaas kan ik niet komen, want ik moet zaterdag werken. Misschien kunnen we volgende week samen koffie drinken?\n\nIk houd je op de hoogte.\n\nGroetjes,\nAyşe"},
        {"titel": "Şikâyet (u)",
         "opdracht": "U heeft bij webwinkel Huisenzo een lamp besteld. De lamp is kapot aangekomen. Schrijf een e-mail aan de klantenservice. Schrijf in de e-mail:\n- wat u heeft besteld en wanneer\n- wat het probleem is\n- wat u wilt dat de winkel doet",
         "tr": "İnternet mağazasından lamba aldın, kırık geldi. Müşteri hizmetlerine ne zaman ne aldığını, sorunu ve ne istediğini yaz.",
         "antwoord": "Geachte heer/mevrouw,\n\nIk schrijf u omdat ik niet tevreden ben over mijn bestelling. Op 3 maart heb ik bij u een lamp besteld. Gisteren kwam het pakket, maar de lamp was kapot. Het glas was gebroken. Ik wil graag dat u mij een nieuwe lamp stuurt. Als dat niet kan, wil ik mijn geld terug.\n\nIk hoor graag van u.\n\nMet vriendelijke groet,\nAyşe Kaya"},
        {"titel": "Bilgi isteme (u)",
         "opdracht": "U wilt op zwemles bij zwembad De Golf. Schrijf een e-mail aan het zwembad. Schrijf in de e-mail:\n- waarom u op zwemles wilt\n- twee vragen over de les",
         "tr": "Yüzme kursuna yazılmak istiyorsun. Havuza neden kursa gitmek istediğini ve kurs hakkında iki soru yaz.",
         "antwoord": "Geachte heer/mevrouw,\n\nIk wil graag op zwemles bij De Golf, omdat ik nooit heb leren zwemmen. Ik wil met mijn kinderen naar het strand kunnen gaan. Kunt u mij vertellen op welke dagen de lessen zijn? Ik wil ook graag weten hoeveel een les kost.\n\nAlvast bedankt voor uw antwoord.\n\nMet vriendelijke groet,\nAyşe Kaya"},
        {"titel": "Gelemeyeceğini bildirme (u)",
         "opdracht": "U volgt een cursus Nederlands. Morgen kunt u niet naar de les, want uw kind is ziek. Schrijf een e-mail aan uw docent, meneer Bakker. Schrijf in de e-mail:\n- dat u morgen niet komt en waarom\n- wat u wilt vragen over het huiswerk",
         "tr": "Hollandaca kursundasın, çocuğun hasta olduğu için yarın gidemiyorsun. Öğretmenine gelemeyeceğini, nedenini ve ödevle ilgili sorunu yaz.",
         "antwoord": "Geachte heer Bakker,\n\nIk wil u laten weten dat ik morgen niet naar de les kan komen. Mijn dochter is ziek en ze moet thuisblijven. Kunt u mij laten weten welk huiswerk we moeten maken? Dan kan ik het thuis doen.\n\nIk houd u op de hoogte.\n\nMet vriendelijke groet,\nAyşe Kaya"},
        {"titel": "Teşekkür + davet (je)",
         "opdracht": "Uw buurman Peter heeft op uw kat gepast toen u op vakantie was. Schrijf een kaartje aan Peter. Schrijf in het kaartje:\n- waarvoor u hem bedankt\n- hoe uw vakantie was\n- een uitnodiging om bij u te komen eten",
         "tr": "Komşun Peter tatildeyken kedine baktı. Ona teşekkür kartı yaz: neye teşekkür ettiğini, tatilin nasıl geçtiğini ve yemeğe davetini yaz.",
         "antwoord": "Beste Peter,\n\nBedankt dat je op onze kat hebt gepast. Dat was heel lief van je! Onze vakantie in Spanje was heerlijk. Het was warm en we hebben veel gezwommen. Kom je zaterdag bij ons eten? Ik maak een Turks gerecht.\n\nLaat je het me weten?\n\nGroetjes,\nAyşe"},
    ],
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
