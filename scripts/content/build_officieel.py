"""Build data/officieel.json: our study guide to the official Lezen I practice exams (openbaar examen) 2023, 2024 and 2025.

The exams themselves are made on the official practice site (oefenexamensnt2.nl). This file holds NO question text
and NO answer options (they belong to the CvTE): only the answer key, how many options each question has, the
question type, the text it belongs to and OUR OWN explanation in Turkish (where in the text the answer is, which
trap the wrong options use). The page lezen/officieel.html checks the letters someone typed in and explains.
Answer keys and score tables: beoordelingsmodel Lezen I 2023, 2024 and 2025 (2025 key with the correction of Feb 2026:
question 2 = A). Run: python3 scripts/content/build_officieel.py (part of scripts/build_all.py).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "officieel.json"

TYPES = {   # question type -> label (Turkish) and the tip shown with a wrong answer of that type
    "doel": ("Metnin amacı", "Metin türüne bak: ikna eden → overtuigen / enthousiast maken; tanıtan → informeren / uitleggen; talimat → uitleggen hoe / op de hoogte brengen; tartışan → voor- en nadelen."),
    "toepassing": ("Kişiye uygulama", "Kişinin durumunu not et (yaş, saat, ne istiyor) ve metinde tam o duruma uyan kuralı bul."),
    "detail": ("Ayrıntı", "Soruda geçen anahtar kelimeyi metinde bul ve sadece o cümleyi ve bir öncekini oku."),
    "voorbeeld": ("Örneğin amacı", "Örneğin hemen önündeki ya da sonundaki cümle, örneğin neyi gösterdiğini söyler."),
    "mening": ("Görüş", "Kişinin kendi sözlerine (tırnak içi) bak; yazarın ya da senin görüşün değil."),
    "wie-bepaalt": ("Kim karar veriyor", "'bepaalt / beslist / besluit' fiilinin öznesini bul; yanlış şıklar rolleri değiştirir."),
    "bij-wie": ("Kime başvurulur", "Kurum ve kişi adlarını tara; 'kun je terecht bij' cümlesini bul."),
    "wat-moet": ("Ne yapmalı", "'moet / dient / eerst … dan' sırasına dikkat et."),
    "wanneer": ("Ne zaman / hangi koşulda", "'als / indien / zodra' ile başlayan koşul cümlesini bul; koşul kimin için geçerli, kontrol et."),
    "hoeveel": ("Ne kadar", "Sayıyı bulduğun cümlenin konusu soruyla aynı mı? 'én / plus / daarnaast' varsa iki parçayı topla."),
    "bedoeld-met": ("Kelimenin anlamı", "Kelimenin geçtiği cümleyi ve bir sonrakini oku; metin genelde kendisi açıklar."),
    "samenvatting": ("Bölüm özeti", "Sadece o ara başlığın altını oku; başka bölümün fikrini içeren şık tuzaktır."),
    "conclusie": ("Sonuç", "Son paragrafa ve 'dus / kortom / daarom' kelimelerine bak."),
    "vindplaats": ("Bilgi nerede", "Her paragrafın ilk cümlesine bak; konuyu birden fazla paragraf anlatabilir."),
}

EXAMS = {
"2023": {
  "titel": "Openbaar examen Lezen I 2023", "geslaagd": 23,
  "score": [276, 337, 364, 380, 393, 403, 411, 419, 426, 432, 438, 443, 448, 453, 458, 462, 467, 471, 476, 480, 485, 490, 494, 500,
            505, 511, 518, 525, 533, 542, 554, 568, 586, 611, 651, 740],
  "teksten": [("Vijf fabels over mbo-opleidingen van Ameda", "persuasief", 1, 6), ("De rol van de ondernemingsraad", "descriptief", 7, 11),
              ("Maakt geld ons gelukkig?", "beschouwend", 12, 17), ("Emma is dolfijnentrainer", "descriptief", 18, 23),
              ("Maak het verschil, word buddy!", "persuasief", 24, 30), ("Examenreglement", "instructief", 31, 35)],
  # (number of options, right letter, type, our explanation)
  "vragen": [
   (3, "B", "voorbeeld", "Alinea I: dierenartsassistent örneği bir mesleğin bütün yönlerini (alet, hijyen, iletişim, resepsiyon) gösteriyor; paragraf 'alle aspecten van een beroep' diye bitiyor. 'Çok çeşitli eğitim var' bilgisi doğru ama örneğin amacı bu değil."),
   (3, "B", "detail", "Alinea III: öğretmenler ödevleri 'doorgaans binnen 48 uur' kontrol ediyor = çoğu zaman hızlı tepki. Dijital ortam (Ameda Campus) öğrenciler arası; 'sabit öğretmen' metinde yok."),
   (3, "A", "toepassing", "Alinea V (stage): stajda öğrendiğin teoriyi pratikte uyguluyorsun. Geri bildirim veren BPV-begeleider ama sorulan 'neden önemli' sorusunun cevabı teori + pratik."),
   (4, "D", "vindplaats", "Rehberlik iki yerde anlatılıyor: alinea III (öğretmenler) ve alinea V (stajda praktijkbegeleider ve BPV-begeleider). İkisini de bulman gerekiyor."),
   (3, "B", "toepassing", "Alinea IV: Ameda diploması resmî, değeri bir ROC diplomasıyla 'exact dezelfde'. 'Alleen bij Ameda…' kesin ifadesi tuzak; Ameda küçük değil, en büyüklerden biri."),
   (3, "A", "doel", "Persuasief metin: her yanlış inancı 'Niet waar!' diye çürütüp Ameda'yı övüyor → okuru Ameda'nın iyi bir okul olduğuna ikna etmek."),
   (4, "C", "detail", "'Taken' bölümü: OR, çalışanların isteklerini işverene anlatır ('de wensen van de werknemers aan de werkgever duidelijk maken'). Karar almak ya da hazırlamak işverenin işi."),
   (4, "B", "wie-bepaalt", "İşten çıkarma kuralları 'instemmingsrecht' altında. OR onay vermezse işveren önce bedrijfscommissie'ye, sonuç çıkmazsa kantonrechter'e gider; son kararı kantonrechter verir. Ondernemingskamer 'adviesrecht' içindir."),
   (3, "B", "wat-moet", "'Initiatiefrecht': işveren karar vermeden önce en az bir kez OR ile görüşür, sonra karar verip OR'a yazılı ve gerekçeli bildirir. Sıra: overleggen → beslissen → informeren."),
   (4, "B", "bedoeld-met", "'Informatierecht': işveren OR'a bilgi vermek zorunda. Yanlış şıklar rolleri ters çeviriyor (bilgiyi alan OR, veren işveren)."),
   (3, "C", "wanneer", "'Informatierecht' son cümlesi: işveren bilgi vermezse OR bedrijfscommissie'den arabuluculuk ister. 'Besluit tegen de wil van de OR' durumunda bedrijfscommissie'ye giden işverendir, OR değil."),
   (3, "B", "detail", "İlk bölüm: toplumlar elli yılda daha zengin oldu ama daha mutlu olmadı ('veel rijker maar niet gelukkiger'). 'Ongelukkiger' daha sonra ve başka konuda (hep birlikte daha çok çalışmak) geçiyor."),
   (3, "C", "samenvatting", "'Gewenning' bölümü: daha iyi yaşam standardını çabuk normal buluyoruz. 'Başkalarından zengin olmak' bir sonraki bölümün (Vergelijken met buren) fikri; tuzak bu."),
   (3, "C", "toepassing", "Layard'a göre en önemli açıklama karşılaştırma: insanlar başkalarından fazla aldıklarında daha mutlu. Tom, komşusunun çok daha az kazandığını bilirse en memnun olur."),
   (3, "B", "wanneer", "'Onze tevredenheid … verdwijnt zodra we horen dat een collega nog meer salarisverhoging krijgt.' Karşılaştırma bir iş arkadaşıyla."),
   (3, "B", "detail", "'Vrije tijd': öğrencilerin çoğu, başkaları sekiz hafta alsa bile kendileri dört hafta (daha çok) tatili seçti. Boş zamanda yarışmıyoruz; yani mümkün olan en çok tatil."),
   (3, "B", "conclusie", "Metnin ana fikri: para ancak başkalarından fazlaysa mutlu ediyor (gelir karşılaştırması). 'Para mutlu etmez' fazla genel; ilk cümle 'Wie rijker wordt, wordt gelukkiger' diyor."),
   (3, "C", "detail", "'Bijzondere baan': Emma hayvanlarla ilgili olmayan çok farklı eğitimler almış ('Behalve iets met dieren'). Dierenverzorging en iyi yol olarak anılıyor ama Emma onu yapmamış; dolfijnentrainer eğitimi ise yok."),
   (3, "B", "detail", "'Bijzondere baan' sonu: misafirler şaşırıyor 'omdat je het gewoon niet zo vaak hoort'; az kişi bu mesleği yapıyor. Fiziksel zorluk metinde var ama şaşkınlığın sebebi değil."),
   (4, "D", "detail", "'Werken als dolfijnentrainer': insanlar onun hep suda olduğunu sanıyor ama etrafında çok iş var, sağlık kontrolleri de bunlardan. Yani mesleğin az bilinen bir parçası."),
   (3, "B", "detail", "'Wel of niet zielig?': Dolfinarium'da ortalama ölüm yaşı 25, doğada 17. Yani doğadaki yunuslar daha kısa yaşıyor. Mutluluk ve yavrular Dolfinarium hakkında söyleniyor."),
   (4, "C", "detail", "Son bölüm: 'Zolang ik het hier leuk vind, blijf ik dit voorlopig nog even doen.' 35 yaş başkalarının durduğu yaş; Emma için plan değil."),
   (4, "A", "doel", "Descriptief metin (rubrikteki bir meslek portresi): okuru dolfijnentrainer mesleği hakkında bilgilendirmek. Nasıl olunacağını anlatmıyor, başvuruya çağırmıyor."),
   (3, "B", "wie-bepaalt", "'Wat doet een buddy?': 'De cliënt stelt een doel…'. Hedefi buddy ya da coördinator değil cliënt belirliyor."),
   (4, "B", "detail", "'Ontstaan': eskiden ölüme refakat (hiv/aids), 'tegenwoordig' ise yaşamaya devam etmeye yardım. Eskiden/şimdi tuzağı: eski görev yanlış şık."),
   (3, "C", "hoeveel", "'Praktisch': haftada en az bir dagdeel, ayrıca zorunlu eğitim ve düzenli toplantılar. İki parçayı da içeren şık doğru."),
   (4, "D", "hoeveel", "'Praktisch': masraflar ödeniyor ('Eventuele kosten worden betaald') VE ayrıca ayda € 25,-. 'Daarnaast' = iki parça birden."),
   (3, "B", "wat-moet", "'Praktisch' ve 'Training': zorunlu, birkaç günlük temel eğitim. Tanışma görüşmesini coördinator yeni cliëntlerle yapıyor (tuzak); 21 yaş tek başına yetmiyor."),
   (3, "B", "bij-wie", "'Begeleiding': buddy'ler her zaman coördinator'a başvurabilir ve grup toplantılarında birbirlerine destek olur. Trainer burada geçmiyor."),
   (4, "C", "doel", "Persuasief broşür, başlık 'word buddy!': yeni buddy bulmak. Rolleri ters çeviren şık (cliënt bulmak) tuzak."),
   (3, "B", "toepassing", "Arama metni 4.4: secretaresse sınavına girmek için önce administratief medewerker bölümünü başarıyla bitirmiş olmak gerekiyor. Saydığı dersler sınavın içeriği, koşul değil."),
   (3, "A", "toepassing", "Arama metni 7 (Bijzondere gevallen): Hollandaca ana dil değilse ve 5 yıldan kısa süredir buradaysa 30 dakika ek süre (ve sözlük; bilgisayar değil). Sözlü sınav tıbbi durum için."),
   (3, "C", "bij-wie", "Arama metni 6 (Bezwaar en beroep): itiraz yazılı olarak management'a. Hoofdkantoor sınav kâğıdını görmek ve özel durum başvurusu için (tuzak)."),
   (3, "C", "toepassing", "Arama metni 2.2: 'Bij te laat komen beslist de examenleider…'. 50 dakika, salondan erken çıkma kuralı (başka yerden alınmış sayı)."),
   (3, "B", "doel", "Instructief metin (sınav yönetmeliği): okuru kurallar hakkında bilgilendirmek ('goed geïnformeerd'). İkna ya da reklam yok."),
  ]},
"2024": {
  "titel": "Openbaar examen Lezen I 2024", "geslaagd": 24,
  "score": [283, 332, 356, 372, 384, 394, 402, 410, 417, 423, 430, 435, 441, 446, 451, 456, 461, 466, 471, 476, 482, 487, 493, 498,
            504, 511, 518, 525, 534, 543, 553, 566, 581, 601, 631, 694],
  "teksten": [("Bakkerij", "persuasief", 1, 6), ("De beursstand", "instructief", 7, 11),
              ("Verzuim op het werk", "descriptief", 12, 17), ("Met deze opleiding heb je echt een voorsprong", "beschouwend", 18, 24),
              ("Arbeidsmarkt: jongere op zoek naar zekerheid, oudere naar uitdaging", "beschouwend", 25, 30),
              ("Abonnement Wonderrijk", "descriptief", 31, 35)],
  "vragen": [
   (3, 'B', 'toepassing', "Kantoor listesi: planlamaları 'bedrijfsbureau' yapıyor. Administratie sadece idari işleri, personeelszaken personel işlerini yürütüyor; Sanne planlama istiyor."),
   (3, 'B', 'toepassing', "'Decentrale bakkerij' bölümü: krem çekmek, krema sıkmak, pasta süslemek (gebak decoreren) burada öğreniliyor. Proefbakkerij yeni ürün geliştiriyor, centrale bakkerij makinelerle seri üretim yapıyor."),
   (3, 'B', 'detail', "Decentrale bakkerijde iş 7.00'de başlıyor. 2.00–4.00 şoförlerin başlama saati, 17.00 ise işin bittiği saat: sayı başka bir cümleden alınmış tuzak."),
   (3, 'A', 'toepassing', "'Heb je gevoel voor techniek, vind je het leuk om met machines te werken…' cümlesi centrale bakkerij bölümünde. Teknik ve makine = centrale bakkerij."),
   (3, 'C', 'detail', "'Uitdagende werkomgeving': fırın geçmişi ya da gıda ile çalışma deneyimi olan kişiler aranıyor. BBL eğitimi bir seçenek (staj), şart değil; 'zelfstandig en stressbestendig' sadece şoförler için yararlı."),
   (3, 'B', 'doel', "Persuasief metin (işe alım sayfası): 'dan is dit de plek voor jou', 'stuur dan je cv' → okuru başvurmaya ikna etmek. Süreçleri anlatması sadece araç."),
   (4, 'A', 'detail', "'De meeste mogelijkheden biedt een eilandstand' → düzenlemede en çok çeşitlilik eilandstand'da. Tussenstand en az imkân veriyor."),
   (3, 'C', 'toepassing', "'Verlichting': takılar (sieraden) sıcak ışık ister; küpe = takı. Renkleri gösteren ışık giysi içindir. Girişte fazla ışık sevilmiyor (B ters)."),
   (4, 'D', 'vindplaats', "'Routing': insanlar hangi yönde yürüyor, önce ne görüyor, bütün bölümlerin önünden mantıklı bir sırayla geçiyorlar → ürünlerin yeri. Diğer başlıklar giriş, oturma yeri ve ışık hakkında."),
   (3, 'A', 'detail', "Son paragraf: 'laat je zakelijke kennissen weten dat je er zult zijn' = ilişkilerini bilgilendir. 'Flinke investering' bir uyarı, tavsiye değil; looprichting ise ziyaretçi geldikten sonra."),
   (4, 'A', 'doel', 'Instructief metin (ders kitabından): stand nasıl seçilir, düzenlenir, hazırlanır → fuar katılımını hazırlama konusunda tavsiye. Kira şartları ve standbouwer sadece ayrıntı.'),
   (3, 'B', 'toepassing', "'Frequent kortdurend verzuim': iş stresi gibi sebeplerde 'de oorzaken op te sporen en maatregelen te nemen'. Bedrijfsarts uzun süreli hastalıkta; iki bekleme günü cao kuralı, öneri değil."),
   (3, 'B', 'wanneer', "Altı hafta veya daha uzun = langdurend verzuim → Wet verbetering poortwachter: işe dönüş planı (re-integratietraject). Bedrijfsarts'a bildirim ilk günlerde olur; sigorta işverenin seçimi."),
   (3, 'B', 'detail', "Sigorta maaşı karşılıyor 'en biedt vaak dienstverlening bij het voorkomen en verminderen van verzuim'. WIA ve yerine birini bulma metinde maliyet olarak geçiyor, sigortanın hizmeti olarak değil."),
   (3, 'A', 'toepassing', "'Verzuim in kleuren': wit = gerçekten hasta, çalışamıyor. Kırık kolla çalışamayan Carmen gerçekten çalışamıyor; spor kazası da normal hastalık bildirimi sayılıyor."),
   (3, 'B', 'detail', "'Sporten is gezond en vermindert over het algemeen het arbeidsverzuim' → çoğunlukla daha az devamsızlık. Sakatlanma mümkün ama genel etkisi azaltmak."),
   (3, 'A', 'doel', 'Giriş: türleri, önleme yolları ve finansal riskleri sigortalama → işverene tavsiye. Sigorta sadece bir bölüm (B), uzun süreli devamsızlık da sadece bir tür (C).'),
   (3, 'B', 'detail', "'De auto's worden beschikbaar gesteld door het ministerie van Defensie' = arabaları veriyor. Öğretmen 'Defensie için eleman yetiştirmiyoruz' diyor (A ve C tuzak)."),
   (3, 'B', 'detail', 'Seçim: iyi notlar tek başına yetmez; azim, disiplin, motivasyon ve ekip çalışması da önemli → B üçünü birleştiriyor. Mentor görüşmesi öğretmenlerle mentor arasında, öğrenciyle değil (C tuzak).'),
   (3, 'A', 'mening', "Bitar: traject'i geliştirmek en büyük zorluk değil; en büyük zorluk onu sürdürmek, 'in dit geval ook financieel'. Sponsorlara bağımlılar. B tam tersini söylüyor."),
   (3, 'C', 'detail', "'allebei' tuzağı: ikisi için de geçerli olan tek şey hevesli olmaları. Race branşında devam etmek sadece Abel'in sözü, niveau 3'ten 4'e geçmek sadece Hussam'ın hikâyesi."),
   (3, 'B', 'detail', "Ramos raceklas'ı tek sezonla sınırlamayıp örneğin üç sezona yaymak istiyor. Leerbedrijven bu isteği dile getirenlerden biri (A tuzak); ayrı bir traject olması Newton'un isteği."),
   (3, 'C', 'mening', "Marelis: 'Maar het meest leren de studenten in de praktijk, tijdens de races.' 'Maar' kelimesinden sonra geliyor: geziler ve misafir dersler önce sayılıyor ama en öğretici olan pratik."),
   (3, 'A', 'conclusie', 'Metnin ana mesajı başlıkta ve ilk paragrafta: sadece en iyi öğrencilerin girebildiği, zorlu ve heyecanlı ek bir program. Genişletme ve uluslararası kariyer sadece bölümler.'),
   (3, 'C', 'detail', "'De resultaten zijn soms verrassend': 'we denken vaak dat jongeren eerder risico's willen nemen dan ouderen. Maar het tegenovergestelde is waar.' Gençler risk almak istemiyor. A ve B fazla genel/aşırı."),
   (3, 'B', 'detail', "Yaşlıların 1 numarası 'creatief denken'; gençlerin yüzde 26'sı da yaratıcı düşünmeyi önemli buluyor. Diğer iki madde gençler için metinde geçmiyor."),
   (3, 'A', 'mening', "Tames: 'Veel 45-plussers hebben een financiële basis' → güvenceleri zaten var, yaratıcı olmak istediklerini söylemek bu yüzden kolay. Bahçe ve boya örneği bir yıl işsiz kaldıktan sonrası için, sebep değil."),
   (4, 'D', 'mening', "Van Veen: 'Onder werklozen is het voor 50-plussers vaak heel lastig om werk te vinden. Toch willen juist zij zich ontwikkelen.' 'zij' = işsiz yaşlılar. Grubu tam oku: sadece 'ouderen' ya da sadece 'werklozen' eksik."),
   (4, 'A', 'mening', "Bregman: 'Werkgevers kunnen steeds gemakkelijker van hun werknemers af' → işten çıkarılmaktan korkuyorlar. Ev ve çocuk güvenceyi önemli kılıyor ama korktukları şey değil (C tuzak)."),
   (3, 'A', 'detail', "Son bölüm: 'Van Veen adviseert werkgevers die zoeken naar jong personeel…' Sonuçları kullanabilecek olanlar genç personel arayan işverenler."),
   (3, 'A', 'toepassing', "Arama metni 4.1 (ve 5.1): aylık ödenen abonelik ilk yıldan sonra 'loopt door voor onbepaalde tijd'. Otomatik biten abonelik tek seferde ödenen (C tuzak)."),
   (3, 'B', 'toepassing', "1.1: 'Hoewel jouw gegevens … geregistreerd staan, wordt de toegang geweigerd als je het abonnement niet kan tonen.' A'daki 'geregistreerd' kelimesi metinden alınmış tuzak."),
   (3, 'C', 'toepassing', "3.4: park aboneliği 'geen voorrang of garantie op een parkeerplaats'; yer yoksa para geri istenemez. Özel park yeri metinde yok."),
   (3, 'A', 'toepassing', "4.5: kayıp, hırsızlık VEYA hasar durumunda kopya istenebilir; idari ücret 'per abonnement' 7 euro. Hasar da sayıldığı için herkes öder; 'alleen bij verlies' tuzak."),
   (3, 'C', 'toepassing', "6: fiyat değişikliği ilk 12 aydan sonra mümkün; aylık iptal edilebilen abonelikte 'word je minimaal één maand van tevoren geïnformeerd'. Meryem iki yıldır abone → ancak bir ay önceden haber verilirse. 'op ieder moment' fazla kesin."),
  ]},
"2025": {
  "titel": "Openbaar examen Lezen I 2025", "geslaagd": 24,
  "score": [295, 345, 369, 384, 395, 404, 412, 419, 426, 431, 437, 442, 447, 452, 456, 461, 465, 469, 473, 477, 482, 486, 490, 495,
            500, 505, 510, 516, 522, 529, 537, 547, 559, 574, 598, 649],
  "teksten": [("Ruud wordt rij-instructeur", "persuasief", 1, 6), ("Een potje huilen", "descriptief", 7, 12),
              ("Verkopen is een vak", "instructief", 13, 18), ("Overuren", "descriptief", 19, 23),
              ("De buurt-whatsapp", "beschouwend", 24, 28), ("Algemene informatie Vision College", "instructief", 29, 35)],
  "vragen": [
   (3, "C", "detail", "İlk paragraf: Ruud 'stopt bij zijn huidige werkgever' ve yardımı 'werkgever Jeurissen'den alıyor. Yani Jeurissen şu an marangoz olarak çalıştığı şirket; eğitim kurumu ya da sürücü kursu değil."),
   (3, "A", "mening", "'Denk op tijd na…': 'Dat geldt zeker voor de zware beroepen.' Ruud tıbbi kontrolleri ağır meslekler için özellikle yararlı buluyor. (2025 anahtarındaki bu soru Şubat 2026'da A olarak düzeltildi.)"),
   (3, "C", "voorbeeld", "35 yaşındaki iş arkadaşı sırtından ameliyat olmuş ve bu işte 30 yıl daha dayanamayacak: ağır mesleği uzun süre yapamamak. Hemen sonraki cümle: 'Voor de zware beroepen is dat niet te doen.'"),
   (3, "A", "mening", "'Bewustwording': 'het op deze leeftijd lastig is. Maar als je heel goed je best doet, lukt het echt wel.' Zor ama çalışınca oluyor; 'makkelijk' ya da 'te oud' değil."),
   (3, "C", "detail", "Joke: Ruud 'regie pakt op zijn loopbaan' ve inisiyatifi kendisi aldı; yaşıtları ise 'afwachtend'. Ruud geç haber vermiş ama bu onu diğerlerinden ayıran şey değil."),
   (3, "A", "doel", "Persuasief metin: başarılı bir örnekle (Ruud) okuru meslek değiştirmeye heveslendirmek. 'Çok zaman ve emek' ya da 'herkes yapamaz' metinde var ama amaç değil."),
   (3, "C", "detail", "'Alleen mensen huilen van emotie': hayvanların gözyaşı bezi sadece gözü temizler; duygudan (iyi ya da kötü) ağlamak sadece insanda var."),
   (3, "A", "detail", "'Huilen als communicatiemiddel': bebekte ağlamak yardım çağrısı; davranış bilimcilere göre yetişkinde de 'die functie' var. Yani aynı işlev."),
   (3, "C", "detail", "'Vrouwen huilen meer dan mannen': hem hormonlar (testosteron / prolactine) hem de gözyaşı kanallarının büyüklüğü. 'Zowel … als …' sorusu: iki sebep birden."),
   (3, "C", "detail", "'Waarom lucht huilen zo op?' son cümlesi: endorfin gibi mutluluk hormonları 'die je kalm maken'. Ağrı kesici etki başka hormonlarla ilgili (prolactine vb.)."),
   (3, "A", "mening", "'Huilen mag!': duyguları bastırmak yazık; stresliysen ara sıra 'een potje huilen'. Yani ağlamak sağlıklı ve bazen yapmak sorun değil."),
   (3, "A", "doel", "Descriptief metin: 'een paar leuke weetjes over huilen' = ağlama hakkında farklı bilgiler vermek. Uyarı yok."),
   (3, "A", "toepassing", "'Goed kijken': müşteri ilgisini gösterince (kumaşa dokunuyor, etikete bakıyor) yanına git. Hemen gitmek çoğu müşteriyi sıkıştırır; sormasını beklemek de gerekmez."),
   (3, "C", "toepassing", "'Een deskundig en zakelijk advies': 'Je stelt eerst gerichte vragen…'. Önce soru sor, sonra tavsiye ver. 'Eerst' kelimesi sırayı veriyor."),
   (3, "A", "voorbeeld", "Bu sorular okuru kendi şirketinin hizmetini düşündürmek için; bölümün konusu iyi hizmet sunmak. Soruları yanıtlamak ya da kibar olmak hizmetin sadece bir parçası."),
   (3, "C", "detail", "'Service maakt het verschil' son cümlesi: 'jouw vriendelijke houding (draagt) het meest bij aan een goed imago'. 'Het meest' = en önemlisi."),
   (3, "A", "wat-moet", "'Neem klager en klacht serieus': müşteriyi ciddiye al, sakin kal, nedenini öğren; sadece memnun müşteri iyi reklam yapar. Her zaman haklı demek ya da şikâyeti haksız göstermek metinde yok."),
   (3, "B", "doel", "Instructief metin (satış eğitim kitabı): satıcının müşteriyle en iyi nasıl ilgileneceğini anlatmak."),
   (3, "B", "toepassing", "İlk madde: günde 8 saat içinde ama çizelge dışında çalışılan saatler 'verschoven uren'. Joseph yine 8 saat çalışıyor; fazla mesai değil."),
   (3, "B", "toepassing", "Gece 24.00'e kadar fazla mesaiden sonra ilk 11 saat çalışmak gerekmiyor (o saatler yine ödenir). Yani 11 saat dinlenmeden başlamıyor; ertesi günün tamamı değil."),
   (4, "B", "toepassing", "'Overwerk verplicht…': 55 yaş ve üstü en fazla 5 saat / dört hafta zorunlu tutulabilir. 10 saat genel kural; 18 yaş altı ve sağlık sebebi muaf. Claire 56 ve sağlıklı."),
   (3, "C", "toepassing", "'Betaling van overuren': 'u kan kiezen hoe u de overuren wil laten vergoeden': para ya da serbest zaman. Seçim çalışanda."),
   (3, "B", "doel", "Descriptief metin (iş sözleşmesi şartlarından bir bölüm): fazla mesai kurallarını açıklamak."),
   (3, "C", "detail", "Giriş: bu gruplar 'bedoeld om verdachte situaties te melden aan buurtgenoten' = şüpheli bir şey görünce komşuları uyarmak. Kavga, grubun sorunlarından biri."),
   (3, "C", "detail", "'Gevoel van veiligheid': 'Wat kon ik doen om de buurt snel te informeren over mogelijke gevaren?' Mahalleyi tehlikeye karşı uyarmak. Polis aramayı zaten başlatmıştı."),
   (3, "B", "mening", "'Gevaren…': Wajid: 'Het is niet verantwoord als mensen zelf politie gaan spelen.' Hiçbir koşulda iyi bulmuyor."),
   (3, "B", "wanneer", "Son bölüm: grup ilanlar için değil (kayıp kedi, çöp poşetleri); Van de Kuilen o zaman müdahale ediyor. İnsanlar 'overbodige berichten' yüzünden gruptan çıkıyor; çıkmaları müdahalenin sebebi değil, sonucu."),
   (3, "B", "doel", "Beschouwend metin: buurt-whatsapp'ın hem yararını (güvenlik hissi) hem tehlikelerini anlatıyor → artılar ve eksiler hakkında bilgi."),
   (3, "C", "toepassing", "'Uitjes': ders programının parçasıysa katılım zorunlu ve ücretsiz; değilse webshop'tan ayrıca ödenir. 'Alleen als…' burada doğru, çünkü metinde gerçekten bir koşul var."),
   (3, "A", "toepassing", "'Derdenmachtiging': 'zowel door de werkgever als door jezelf getekend'. Team debiteuren formu veriyor, imzalamıyor."),
   (3, "C", "hoeveel", "'Je bent je Visionpas kwijt': € 5,- idari masraf ve € 5,- kart. 'én' tipi soru: iki parçayı topla."),
   (3, "B", "toepassing", "'Cursusgeld': 29 ders saatinden az vavo eğitimi için ders saati başına € 30,- → toplam saat sayısı belirliyor. Seviye (236 / 573 €) BBL için."),
   (4, "C", "toepassing", "'Calamiteit': alarm çalarsa en yakın acil çıkıştan toplanma yerine git. Görevliyi/resepsiyonu uyarmak ve 100 / 8888 aramak, alarm HENÜZ çalmadıysa (başka bölüm)."),
   (3, "A", "toepassing", "'Decaan': Gezondheidszorg sektöründe decaan kaydı silebilir ('je wilt laten uitschrijven'). Mentor sadece sektör Techniek için. STIP'e decaan yönlendirir."),
   (3, "B", "detail", "İki yerde: 'Aanwezigheid' (kartla binaya girişin kaydı) ve 'Visionpas' listesinin son maddesi (hangi derslikte olduğun). Derse katılımı öğretmen kaydediyor. Arama metninde anahtar kelimeyi her yerde tara."),
  ]},
}


def main():
    out = {"_about": "Our guide to the official Lezen I practice exams (made on oefenexamensnt2.nl): answer key, number of options, "
                     "question type and our own Turkish explanation per question. No CvTE question text. Generated by scripts/content/build_officieel.py.",
           "site": "https://oefenexamensnt2.nl", "types": {k: {"label": v[0], "tip": v[1]} for k, v in TYPES.items()}, "examens": []}
    for year, e in EXAMS.items():
        assert len(e["vragen"]) == 35 and len(e["score"]) == 36, year
        teksten = [{"nr": k + 1, "titel": t, "tekstsoort": s, "van": a, "tot": b} for k, (t, s, a, b) in enumerate(e["teksten"])]
        vragen = []
        for n, (opts, juist, soort, uitleg) in enumerate(e["vragen"], 1):
            assert soort in TYPES and juist in "ABCD"[:opts], (year, n)
            tekst = next(t["nr"] for t in teksten if t["van"] <= n <= t["tot"])
            vragen.append({"nr": n, "tekst": tekst, "opties": opts, "juist": juist, "soort": soort, "uitleg": uitleg})
        out["examens"].append({"id": year, "titel": e["titel"], "geslaagd": e["geslaagd"], "score": e["score"], "teksten": teksten, "vragen": vragen})
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(out['examens'])} exams -> {OUT}")


if __name__ == "__main__":
    main()
