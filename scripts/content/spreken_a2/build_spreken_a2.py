"""Build data/spreken-a2.json (run: python3 scripts/content/spreken_a2/build_spreken_a2.py).

A2 inburgeringsexamen Spreken: on the computer, 35 minutes, 16 tasks with a video or 1, 2 or 3 pictures; you answer by speaking.
Types (as described by practice sites): 'vraag' = a question about your own life (after a short film),
'een' = one picture: say something about the situation, 'twee' = two pictures: choose one and say why,
'drie' = three pictures: tell what happens / name things in order.
We have no pictures or films: the page describes the picture in words ("Op het plaatje ziet u ...") and reads the question aloud.
Our own tasks (made-up situations); 'voorbeeld' = one good A2 answer, not the only one.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent.parent.parent / "data" / "spreken-a2.json"
TYPES = {"vraag": "Vraag over uzelf", "een": "Eén plaatje", "twee": "Twee plaatjes", "drie": "Drie plaatjes"}


def T(id, type, situatie, vraag, voorbeeld, tr):
    return {"id": id, "type": type, "situatie": situatie, "vraag": vraag, "voorbeeld": voorbeeld, "tr": tr}


EXAMEN_1 = [
    T("p1-01", "vraag", "In het filmpje vertelt een vrouw over haar ontbijt.", "Wat eet u meestal 's ochtends? En waarom?",
      "Ik eet meestal brood met kaas en ik drink thee. Dat is lekker en snel, want ik moet vroeg naar mijn werk.",
      "Sabahları genelde ne yediğini ve nedenini söyle."),
    T("p1-02", "vraag", "In het filmpje fietst een man naar zijn werk.", "Hoe gaat u naar uw werk of naar school? Vertel ook waarom.",
      "Ik ga met de fiets naar mijn werk. Het is niet ver en fietsen is gezond.",
      "İşe ya da okula nasıl gittiğini ve nedenini anlat."),
    T("p1-03", "vraag", "In het filmpje zit een gezin samen aan tafel.", "Wat doet u graag in het weekend?",
      "In het weekend ga ik graag wandelen in het park met mijn kinderen. Op zondag eten we samen bij mijn moeder.",
      "Hafta sonu ne yapmaktan hoşlandığını anlat."),
    T("p1-04", "vraag", "In het filmpje zie je een vrouw die boodschappen doet.", "Waar doet u uw boodschappen? Wat koopt u daar?",
      "Ik doe mijn boodschappen bij de supermarkt in mijn straat. Ik koop daar groente, fruit, brood en melk.",
      "Alışverişini nereden yaptığını ve ne aldığını söyle."),
    T("p1-05", "een", "Op het plaatje ziet u een man in de regen. Hij heeft geen paraplu en zijn kleren zijn nat.", "Wat is het probleem van deze man? Wat moet hij doen?",
      "De man is nat, want het regent en hij heeft geen paraplu. Hij moet een paraplu kopen of naar binnen gaan.",
      "Resimdeki adamın sorununu ve ne yapması gerektiğini söyle."),
    T("p1-06", "een", "Op het plaatje ziet u een keuken. Er staat veel vuile afwas op het aanrecht.", "Wat ziet u? Wat vindt u ervan?",
      "Ik zie een keuken met veel vuile borden en pannen. Dat vind ik niet fijn. Iemand moet de afwas doen.",
      "Ne gördüğünü ve bu konuda ne düşündüğünü söyle."),
    T("p1-07", "een", "Op het plaatje ziet u een kind dat huilt. Het kind is van de fiets gevallen.", "Wat is er gebeurd? Wat zegt u tegen het kind?",
      "Het kind is van de fiets gevallen. Ik zeg: Gaat het? Heb je pijn? Kom, ik help je.",
      "Ne olduğunu ve çocuğa ne söyleyeceğini anlat."),
    T("p1-08", "een", "Op het plaatje ziet u een lange rij mensen bij de kassa in de supermarkt.", "Wat ziet u? Wat doet u als er een lange rij is?",
      "Ik zie veel mensen bij de kassa. Ze moeten lang wachten. Als er een lange rij is, ga ik naar de zelfscan.",
      "Ne gördüğünü ve uzun kuyrukta ne yaptığını söyle."),
    T("p1-09", "twee", "Plaatje 1: een man die in een park wandelt. Plaatje 2: een man die thuis op de bank televisie kijkt.", "Wat doet u liever op zondag? Kies een plaatje en zeg waarom.",
      "Ik kies plaatje 1. Ik wandel liever in het park, want dan ben ik buiten en dat is gezond.",
      "Pazar günü hangisini tercih ettiğini seç ve nedenini söyle."),
    T("p1-10", "twee", "Plaatje 1: een kleine auto. Plaatje 2: een fiets.", "U wilt naar uw werk, vijf kilometer van uw huis. Wat neemt u? Waarom?",
      "Ik neem de fiets. Vijf kilometer is niet ver. Fietsen is goedkoop en gezond.",
      "İşe gitmek için hangisini seçeceğini ve nedenini söyle."),
    T("p1-11", "twee", "Plaatje 1: een appartement in de stad. Plaatje 2: een huis met een tuin in een dorp.", "Waar wilt u liever wonen? Waarom?",
      "Ik woon liever in het huis met een tuin. Mijn kinderen kunnen dan buiten spelen en het is rustig.",
      "Nerede oturmayı tercih ettiğini ve nedenini söyle."),
    T("p1-12", "twee", "Plaatje 1: een verjaardagscadeau: bloemen. Plaatje 2: een verjaardagscadeau: een boek.", "Uw buurvrouw is jarig. Welk cadeau geeft u? Waarom?",
      "Ik geef bloemen. Bloemen zijn mooi en iedereen vindt bloemen leuk.",
      "Komşuna hangi hediyeyi vereceğini ve nedenini söyle."),
    T("p1-13", "drie", "Plaatje 1: een vrouw staat op en kijkt op de klok. Plaatje 2: ze ontbijt. Plaatje 3: ze stapt in de bus.", "Vertel wat de vrouw doet. Begin bij plaatje 1.",
      "Eerst staat de vrouw op en ze kijkt hoe laat het is. Daarna eet ze haar ontbijt. Dan gaat ze met de bus naar haar werk.",
      "Kadının sırayla ne yaptığını anlat (önce, sonra, en son)."),
    T("p1-14", "drie", "Plaatje 1: een hamer. Plaatje 2: een schaar. Plaatje 3: een pan.", "Wat ziet u op de plaatjes? Wat doet u ermee?",
      "Op plaatje 1 zie ik een hamer. Daarmee sla ik een spijker in de muur. Op plaatje 2 zie ik een schaar, om papier te knippen. Op plaatje 3 zie ik een pan, om te koken.",
      "Her nesnenin adını söyle ve ne işe yaradığını anlat."),
    T("p1-15", "drie", "Plaatje 1: een man belt de huisarts. Plaatje 2: hij zit in de wachtkamer. Plaatje 3: de dokter onderzoekt hem.", "Vertel wat er gebeurt.",
      "Eerst belt de man de huisarts voor een afspraak. Daarna wacht hij in de wachtkamer. Dan onderzoekt de dokter hem.",
      "Sırayla ne olduğunu anlat."),
    T("p1-16", "drie", "Plaatje 1: een jas. Plaatje 2: een muts. Plaatje 3: handschoenen.", "Wanneer draagt u deze dingen?",
      "Ik draag een jas, een muts en handschoenen in de winter, als het koud is. De muts draag ik op mijn hoofd en de handschoenen aan mijn handen.",
      "Bu eşyaları ne zaman giydiğini anlat."),
]

EXAMEN_2 = [
    T("p2-01", "vraag", "In het filmpje kookt een man het avondeten.", "Wie kookt er bij u thuis? Wat eet u graag?",
      "Bij mij thuis kook ik meestal. Ik eet graag rijst met groente en kip.",
      "Evde kimin yemek yaptığını ve ne yemeyi sevdiğini söyle."),
    T("p2-02", "vraag", "In het filmpje leert een vrouw Nederlands op een cursus.", "Hoe leert u Nederlands? Wat vindt u moeilijk?",
      "Ik ga twee keer per week naar een cursus en ik kijk Nederlandse tv. Ik vind de uitspraak moeilijk.",
      "Hollandacayı nasıl öğrendiğini ve neyi zor bulduğunu söyle."),
    T("p2-03", "vraag", "In het filmpje praat een vrouw met haar buurvrouw.", "Kent u uw buren? Wat doet u samen?",
      "Ja, ik ken mijn buren. Soms drinken we samen koffie en we helpen elkaar met pakketjes.",
      "Komşularını tanıyıp tanımadığını ve birlikte ne yaptığınızı anlat."),
    T("p2-04", "vraag", "In het filmpje gaat een gezin op vakantie.", "Waar gaat u graag naartoe op vakantie? Waarom?",
      "Ik ga graag naar Turkije op vakantie. Daar woont mijn familie en het is er warm.",
      "Tatile nereye gitmeyi sevdiğini ve nedenini söyle."),
    T("p2-05", "een", "Op het plaatje ziet u een vrouw bij de dokter. Ze houdt haar hand op haar buik.", "Wat is er aan de hand met deze vrouw?",
      "De vrouw is ziek. Ze heeft buikpijn. Ze vertelt de dokter waar het pijn doet.",
      "Kadının neyi olduğunu anlat."),
    T("p2-06", "een", "Op het plaatje ziet u een vol vuilnisbak op straat. Er ligt afval naast de bak.", "Wat ziet u? Wat vindt u daarvan?",
      "Ik zie een volle vuilnisbak en er ligt afval op straat. Dat vind ik vies. De gemeente moet de bak leegmaken.",
      "Ne gördüğünü ve bu konuda ne düşündüğünü söyle."),
    T("p2-07", "een", "Op het plaatje ziet u een feest. Er zijn ballonnen en een taart met kaarsjes.", "Wat voor feest is dit? Hoe viert u uw verjaardag?",
      "Dit is een verjaardagsfeest. Ik vier mijn verjaardag thuis met mijn familie. We eten taart.",
      "Bunun nasıl bir parti olduğunu ve doğum gününü nasıl kutladığını söyle."),
    T("p2-08", "een", "Op het plaatje ziet u een man die op het station staat. Op het bord staat: 'vertraging'.", "Wat is het probleem? Wat doet de man nu?",
      "De trein heeft vertraging. De man moet wachten. Misschien belt hij zijn werk dat hij later komt.",
      "Sorunun ne olduğunu ve adamın şimdi ne yapabileceğini söyle."),
    T("p2-09", "twee", "Plaatje 1: koken thuis. Plaatje 2: eten afhalen bij een snackbar.", "Wat doet u liever op vrijdagavond? Waarom?",
      "Ik kook liever thuis. Dat is gezonder en goedkoper.",
      "Cuma akşamı hangisini tercih ettiğini ve nedenini söyle."),
    T("p2-10", "twee", "Plaatje 1: een sportschool. Plaatje 2: zwemmen in een zwembad.", "U wilt meer sporten. Wat kiest u? Waarom?",
      "Ik kies zwemmen. Ik vind water fijn en zwemmen is goed voor je rug.",
      "Daha çok spor için hangisini seçtiğini ve nedenini söyle."),
    T("p2-11", "twee", "Plaatje 1: een brief op papier. Plaatje 2: een e-mail op een laptop.", "U wilt de gemeente iets vragen. Hoe doet u dat? Waarom?",
      "Ik stuur een e-mail. Dat is sneller dan een brief en ik hoef geen postzegel te kopen.",
      "Belediyeye bir şey sormak için hangisini seçtiğini ve nedenini söyle."),
    T("p2-12", "twee", "Plaatje 1: een markt buiten. Plaatje 2: een grote supermarkt.", "Waar koopt u liever groente? Waarom?",
      "Ik koop liever groente op de markt. Het is vers en vaak goedkoper.",
      "Sebzeyi nereden almayı tercih ettiğini ve nedenini söyle."),
    T("p2-13", "drie", "Plaatje 1: een kind pakt zijn tas in. Plaatje 2: het kind fietst naar school. Plaatje 3: het kind zit in de klas.", "Vertel wat het kind doet.",
      "Eerst pakt het kind zijn tas in. Daarna fietst het naar school. Dan zit het in de klas en luistert naar de juf.",
      "Çocuğun sırayla ne yaptığını anlat."),
    T("p2-14", "drie", "Plaatje 1: een tandenborstel. Plaatje 2: een handdoek. Plaatje 3: zeep.", "Wat ziet u? Waarvoor gebruikt u dat?",
      "Ik zie een tandenborstel, die gebruik ik om mijn tanden te poetsen. Met de handdoek droog ik me af. Met zeep was ik mijn handen.",
      "Eşyaların adını söyle ve ne için kullandığını anlat."),
    T("p2-15", "drie", "Plaatje 1: een vrouw kiest kleren in een winkel. Plaatje 2: ze past een jurk. Plaatje 3: ze betaalt bij de kassa.", "Vertel wat er gebeurt.",
      "Eerst kiest de vrouw kleren in de winkel. Daarna past ze een jurk. De jurk past goed, dus ze betaalt bij de kassa.",
      "Sırayla ne olduğunu anlat."),
    T("p2-16", "drie", "Plaatje 1: een paraplu. Plaatje 2: een zonnebril. Plaatje 3: een sjaal.", "Bij welk weer gebruikt u deze dingen?",
      "Een paraplu gebruik ik als het regent. Een zonnebril draag ik als de zon schijnt. Een sjaal draag ik als het koud is.",
      "Bu eşyaları hangi havada kullandığını anlat."),
]

EXAMENS = [{"id": "p-examen-1", "titel": "A2 Spreken proefexamen 1", "taken": EXAMEN_1},
           {"id": "p-examen-2", "titel": "A2 Spreken proefexamen 2", "taken": EXAMEN_2}]

# Scoring help (practice sites describe DUO's A2 model as: does the answer fit the task and is it clear,
# plus vocabulary, grammar, pronunciation and fluency; no answer / not understandable / off-task = 0).
# Our written version for the AI prompt; not DUO's official text.
CRITERIA = [
    {"naam": "Inhoud", "nl": "Het antwoord past bij de vraag en geeft alles wat gevraagd wordt (bijvoorbeeld ook 'waarom')."},
    {"naam": "Duidelijkheid", "nl": "Het antwoord is duidelijk en te begrijpen."},
    {"naam": "Woordenschat", "nl": "Passende woorden voor A2; geen woorden in een andere taal."},
    {"naam": "Grammatica", "nl": "Eenvoudige zinnen; fouten maken het antwoord niet onduidelijk."},
    {"naam": "Samenhang", "nl": "Zinnen zijn verbonden (en, maar, want, eerst, daarna, dan)."},
]


def main():
    ids = set()
    for e in EXAMENS:
        assert len(e["taken"]) == 16, e["id"]
        for t in e["taken"]:
            assert t["id"] not in ids, t["id"]; ids.add(t["id"])
            assert t["type"] in TYPES, t["id"]
        counts = {k: sum(t["type"] == k for t in e["taken"]) for k in TYPES}
        assert all(v == 4 for v in counts.values()), (e["id"], counts)
        e["minuten"] = 35
    OUT.write_text(json.dumps({"_about": "Own A2 Spreken practice tasks. Generated by scripts/content/spreken_a2/build_spreken_a2.py.",
                               "types": TYPES, "examens": EXAMENS, "criteria": CRITERIA}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(ids)} tasks in {len(EXAMENS)} exams -> {OUT}")


if __name__ == "__main__":
    main()
