"""Help per speech act (handeling) for Spreken I B1.

Shown in the optional hint box under every task. Turkish explanation for the learner,
Dutch sentence patterns (kaliplar) that work for almost every task of that type.
Written for this site; based on what the CvTE scoring model asks for
(answer the question, meet the requirement 'eis', short correct sentences).
"""

HANDELINGEN = {
    "voorkeur": {
        "wat": "İki seçenekten birini seç ve neden seçtiğini söyle. Seçimini ilk cümlede net söyle, sonra gerekçeyi ver.",
        "kaliplar": [
            "Ik kies voor ... , want ...",
            "Ik ... liever ... , omdat ...",
            "Ik vind ... beter/leuker dan ... .",
            "Bovendien ... / Daarnaast ...   (ikinci gerekçe)",
        ],
        "tip": "İstenen sayıda gerekçe ver (2 reden isteniyorsa iki ayrı cümle). Her iki seçeneği de övme: tek birini seç.",
        "valkuil": "'omdat' bijzin'dir: fiil sona gider (omdat ik graag buiten ben). 'want' sonrası normal sıra (want ik ben graag buiten).",
    },
    "instructie": {
        "wat": "Karşındakine ne yapması gerektiğini söyle. Resim varsa her resim = bir adım; sırayı belirten kelimeler kullan.",
        "kaliplar": [
            "Eerst moet je ... .",
            "Daarna/Dan ... je ... .",
            "Tot slot ... je ... .",
            "Wil je ... ? / Kunt u ... ?   (kibar rica)",
        ],
        "tip": "'alle plaatjes' isteniyorsa her resim için bir cümle kur. 'Eerst – daarna – tot slot' sırası hem net hem puan getirir.",
        "valkuil": "'je moet ... + mastar sonda' (Je moet de vloer vegen). 'Daarna' ile başlayınca inversie: Daarna veeg je de vloer.",
    },
    "mening": {
        "wat": "Bir konu hakkında ne düşündüğünü söyle (iyi/kötü/fikir) ve nedenini ekle.",
        "kaliplar": [
            "Ik vind het een goed/slecht idee, want ... .",
            "Ik vind dat ... , omdat ... .",
            "Ik ben het (niet) eens met ... .",
            "Een ander argument is dat ... .",
        ],
        "tip": "İlk cümle = görüşün (goed / niet goed). İkinci cümle = neden. Orta görevde ikinci bir argüman ekle.",
        "valkuil": "'Ik vind dat' sonrası bijzin: fiil sona (Ik vind dat kinderen buiten moeten spelen).",
    },
    "advies": {
        "wat": "Karşındakine tavsiye ver: ne yapmalı? İstenirse neden yapmalı?",
        "kaliplar": [
            "Je kunt het beste ... .",
            "Je moet/zou ... .",
            "Misschien kun je ... .",
            "Ik zou ... , want ... .",
        ],
        "tip": "Soruyu soran kişiye 'je' ile (resmîyse 'u' ile) hitap et. İki tavsiye isteniyorsa iki ayrı öneri say.",
        "valkuil": "'Ik zou ...' + mastar sonda: Ik zou een eerdere trein nemen.",
    },
    "beschrijving": {
        "wat": "Ne olduğunu ya da bir şeyin neye benzediğini anlat. Olmuş bir şeyse geçmiş zaman (perfectum) kullan.",
        "kaliplar": [
            "Ik heb ... ge...d.   (perfectum)",
            "We zijn naar ... gegaan.",
            "Er is/zijn ... .   (bir yeri anlatırken)",
            "Het/De ... is groot/rood/nieuw.",
        ],
        "tip": "Resimdeki her şeyi tek tek söyle: resim başına bir cümle. Renk, boyut, malzeme gibi somut sıfatlar kullan.",
        "valkuil": "hebben/zijn seçimi: hareket ve değişim fiilleri 'zijn' alır (ik ben gevallen, we zijn gegaan).",
    },
    "overtuigen": {
        "wat": "Karşındakini senin fikrine ikna et. Önce ne istediğini söyle, sonra istenen sayıda güçlü gerekçe ver.",
        "kaliplar": [
            "Ik denk dat het beter is om ... , want ... .",
            "We kunnen beter ... .",
            "Bovendien ... .   (ikinci argüman)",
            "Ik begrijp je, maar ... .",
        ],
        "tip": "Her argüman ayrı bir cümle olsun. Karşı tarafın itirazına 'Ik begrijp je, maar ...' ile cevap vermek doğal durur.",
        "valkuil": "Konudan sapma: argümanlar sadece istenen seçeneği desteklemeli.",
    },
    "vraag": {
        "wat": "Kibarca bir şey sor ya da rica et. Durumdaki kişiye uygun hitap (u / je) kullan.",
        "kaliplar": [
            "Mag ik ... ?",
            "Kunt u / Kun je ... ?",
            "Wilt u / Wil je ... ?",
            "Weet u misschien ... ?",
        ],
        "tip": "Soru cümlesinde fiil başa gelir (Kunt u mij helpen?). İki soru isteniyorsa iki ayrı soru sor.",
        "valkuil": "Sadece durumu anlatıp soruyu sormamak. Mutlaka soru işaretiyle biten bir cümle olsun.",
    },
    "informeren": {
        "wat": "Karşındakine bilgi ver: nerede, ne zaman, ne yapıyorsun. Kısa ve net ol.",
        "kaliplar": [
            "... is in/op ... .",
            "Ik ga ... .",
            "We zoeken ... .",
            "Eerst ... , daarna ... .",
        ],
        "tip": "Resimdeki bilgiyi (sayı, saat, oda numarası) doğru aktar. Birden fazla bilgi isteniyorsa hepsini say.",
        "valkuil": "Gereksiz uzun açıklama: istenen bilgiyi ilk cümlede ver.",
    },
    "uitleg": {
        "wat": "Bir şeyin nedenini ya da ne anlama geldiğini açıkla.",
        "kaliplar": [
            "Dat komt doordat ... .",
            "Ik kan niet ... , want ... .",
            "Dit bord betekent dat ... .",
            "Met dit product kunt u ... .",
        ],
        "tip": "Soruya doğrudan cevap ver: 'Waarom?' → 'want / omdat ...'. Resimdeki problemi ismiyle söyle.",
        "valkuil": "'doordat' ve 'omdat' bijzin: fiil sona gider.",
    },
    "reageren": {
        "wat": "Duruma uygun kısa bir tepki ver: uyar, kabul et, itiraz et.",
        "kaliplar": [
            "Pas op! ... .",
            "Wil je ... ?   (kibar uyarı)",
            "Ja, dat is goed. / Sorry, maar ... .",
            "Dat mag hier niet, want ... .",
        ],
        "tip": "Kısa görevde bir-iki cümle yeter, ama ne istediğini açıkça söyle.",
        "valkuil": "Kaba ifade: emir cümlesine 'alsjeblieft' ya da 'Wil je ...' eklemek nazik durur.",
    },
    "voorstel": {
        "wat": "Bir problem için çözüm öner.",
        "kaliplar": [
            "Zullen we ... ?",
            "Misschien kunnen we ... .",
            "Ik stel voor dat ... .",
            "Wat vind je van ... ?",
        ],
        "tip": "Somut bir öneri ver (saat, yer, yöntem). Sadece problemi anlatmak yetmez.",
        "valkuil": "'Ik stel voor dat' bijzin: fiil sona.",
    },
    "troosten": {
        "wat": "Üzgün birini teselli et: anlayış göster ve iyi bir dilekte bulun.",
        "kaliplar": [
            "Wat vervelend voor u/je.",
            "Ik hoop dat ... snel beter wordt.",
            "Kan ik iets voor u/je doen?",
        ],
        "tip": "Önce duyguyu kabul et, sonra dilek ya da yardım teklifi ekle.",
        "valkuil": "Konuyu değiştirmek ya da problemi küçümsemek.",
    },
}
