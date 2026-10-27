"""Build data/schrijven-a2.json (run: python3 scripts/content/schrijven_a2/build_schrijven_a2.py).

A2 inburgeringsexamen Schrijven: on paper, 40 minutes, 4 tasks (filling in a form, short e-mails, notes, messages).
These are our own practice tasks in that style (made-up names and places), grouped in practice exams of 4 tasks.

Task fields:
  soort      formulier | e-mail | briefje | bericht
  situatie   the situation (Dutch, A2 words)
  opdracht   what the answer must contain (Dutch, one point per line); the result page turns these into a checklist
  tr         short Turkish help
  velden     formulier only: the fields to fill in [label, hint]
  voorbeeld  a model answer (one possible good answer, not the only one)
The scoring help on the page follows the CEFR A2 writing description (short, simple texts about everyday things);
DUO's own A2 scoring model is not public in this repo, so the page says so.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent
OUT = ROOT / "data" / "schrijven-a2.json"
SOORTEN = {"formulier", "e-mail", "briefje", "bericht"}

TAKEN = [
    # ---------- exam 1 ----------
    {"id": "s1-zwemles", "soort": "formulier", "titel": "Aanmelden voor zwemles",
     "situatie": "Uw dochter Noor (7 jaar) wil zwemles. U vult het aanmeldformulier van zwembad De Golf in.",
     "opdracht": "Vul alle velden in.\nSchrijf bij 'Opmerking' één zin: Noor is een beetje bang voor water.",
     "tr": "Formdaki her alanı doldur. 'Opmerking' kısmına kızının sudan biraz korktuğunu yaz.",
     "velden": [["Naam kind", "voornaam en achternaam"], ["Geboortedatum kind", "dag-maand-jaar"], ["Naam ouder", ""], ["Telefoonnummer", ""],
                ["Welke dag? (woensdag / zaterdag)", "kies één dag"], ["Opmerking", "één zin"]],
     "voorbeeld": "Naam kind: Noor Yılmaz\nGeboortedatum kind: 14-03-2019\nNaam ouder: Ayşe Yılmaz\nTelefoonnummer: 06-12345678\nWelke dag? zaterdag\nOpmerking: Noor is een beetje bang voor water."},
    {"id": "s1-ziek-werk", "soort": "e-mail", "titel": "Ziek melden",
     "situatie": "U bent ziek en u kunt morgen niet werken. U schrijft een e-mail aan uw leidinggevende, meneer De Boer.",
     "opdracht": "Zeg dat u ziek bent.\nZeg dat u morgen niet kunt werken.\nVraag wie uw werk kan doen.\nSchrijf een begin en een einde (aanhef en groet).",
     "tr": "Hasta olduğunu, yarın çalışamayacağını yaz ve işini kimin yapabileceğini sor. 'Beste meneer De Boer' ile başla, 'Met vriendelijke groet' ile bitir.",
     "voorbeeld": "Beste meneer De Boer,\n\nIk ben ziek. Ik heb koorts. Daarom kan ik morgen niet werken. Wie kan mijn werk doen?\n\nMet vriendelijke groet,\nAyşe Yılmaz"},
    {"id": "s1-buurman", "soort": "briefje", "titel": "Briefje voor de buurman",
     "situatie": "Uw buurman heeft een pakketje voor u aangenomen. U was niet thuis. Nu is hij niet thuis. U schrijft een briefje en doet het in zijn brievenbus.",
     "opdracht": "Bedank de buurman.\nZeg wanneer u het pakketje komt halen.\nSchrijf uw naam en huisnummer.",
     "tr": "Komşuna teşekkür et, paketi ne zaman alacağını yaz, adını ve kapı numaranı ekle.",
     "voorbeeld": "Hallo buurman,\n\nBedankt voor het pakketje! Ik kom het vanavond om 19.00 uur halen.\n\nGroetjes,\nAyşe (nummer 12)"},
    {"id": "s1-huisarts", "soort": "e-mail", "titel": "Afspraak verzetten",
     "situatie": "U heeft donderdag om 10.00 uur een afspraak bij de huisarts. Maar dan moet u werken. U schrijft een e-mail aan de huisartsenpraktijk.",
     "opdracht": "Zeg welke afspraak u heeft.\nZeg waarom u niet kunt komen.\nVraag om een nieuwe afspraak en noem een dag die u wel kunt.",
     "tr": "Hangi randevun olduğunu, neden gelemeyeceğini yaz ve uygun olduğun bir gün söyleyerek yeni randevu iste.",
     "voorbeeld": "Beste mevrouw, meneer,\n\nIk heb donderdag om 10.00 uur een afspraak bij dokter Smit. Maar ik moet dan werken. Kan ik een nieuwe afspraak maken? Vrijdagmiddag kan ik wel.\n\nMet vriendelijke groet,\nAli Demir"},
    # ---------- exam 2 ----------
    {"id": "s2-bibliotheek", "soort": "formulier", "titel": "Lid worden van de bibliotheek",
     "situatie": "U wilt lid worden van de bibliotheek. U vult het formulier in.",
     "opdracht": "Vul alle velden in.\nSchrijf bij 'Waarom wilt u lid worden?' één of twee zinnen.",
     "tr": "Formu doldur. Neden üye olmak istediğini bir iki cümleyle yaz.",
     "velden": [["Voornaam", ""], ["Achternaam", ""], ["Adres", "straat en huisnummer"], ["Postcode en woonplaats", ""], ["E-mailadres", ""],
                ["Waarom wilt u lid worden?", "één of twee zinnen"]],
     "voorbeeld": "Voornaam: Ali\nAchternaam: Demir\nAdres: Kerkstraat 8\nPostcode en woonplaats: 2311 AB Leiden\nE-mailadres: ali.demir@mail.nl\nWaarom wilt u lid worden? Ik wil boeken lenen om Nederlands te leren. Ook mijn kinderen willen boeken lezen."},
    {"id": "s2-school-ziek", "soort": "bericht", "titel": "Bericht aan de juf",
     "situatie": "Uw zoon Emir zit in groep 5. Hij is vandaag ziek. U stuurt een bericht aan de juf via de app van school.",
     "opdracht": "Zeg dat Emir ziek is.\nZeg wat hij heeft.\nVraag of Emir huiswerk moet maken.",
     "tr": "Oğlunun hasta olduğunu, neyi olduğunu yaz ve ödevi olup olmadığını sor.",
     "voorbeeld": "Beste juf,\n\nEmir is vandaag ziek. Hij heeft buikpijn en koorts. Moet hij thuis huiswerk maken?\n\nGroeten,\nAyşe (moeder van Emir)"},
    {"id": "s2-feest", "soort": "e-mail", "titel": "Uitnodiging verjaardag",
     "situatie": "U wordt 40 jaar. U geeft een feest. U schrijft een e-mail aan uw collega's.",
     "opdracht": "Nodig uw collega's uit.\nSchrijf de dag, de tijd en het adres.\nVraag of ze laten weten of ze komen.",
     "tr": "İş arkadaşlarını davet et; gün, saat ve adres yaz; gelip gelmeyeceklerini bildirmelerini iste.",
     "voorbeeld": "Hallo allemaal,\n\nIk word 40 jaar! Daarom geef ik een feest. Jullie zijn welkom op zaterdag 15 juni om 19.00 uur, Kerkstraat 8 in Leiden.\nLaten jullie weten of jullie komen?\n\nGroetjes,\nAli"},
    {"id": "s2-reparatie", "soort": "e-mail", "titel": "Kapotte verwarming",
     "situatie": "De verwarming in uw huurhuis is kapot. Het is koud in huis. U schrijft een e-mail aan de woningcorporatie.",
     "opdracht": "Zeg wat er kapot is.\nZeg sinds wanneer.\nVraag wanneer iemand komt om het te maken.",
     "tr": "Neyin bozuk olduğunu, ne zamandan beri bozuk olduğunu yaz ve tamire ne zaman gelineceğini sor.",
     "voorbeeld": "Beste mevrouw, meneer,\n\nDe verwarming in mijn huis is kapot. Sinds maandag is het heel koud in huis. Wanneer kan iemand komen om de verwarming te maken?\n\nMet vriendelijke groet,\nAyşe Yılmaz\nKerkstraat 8, Leiden"},
    # ---------- exam 3 ----------
    {"id": "s3-verhuizing", "soort": "formulier", "titel": "Verhuizing doorgeven",
     "situatie": "U gaat verhuizen. U geeft uw nieuwe adres door aan de gemeente.",
     "opdracht": "Vul alle velden in.\nSchrijf bij 'Wie verhuizen er mee?' de namen van uw gezinsleden.",
     "tr": "Taşınma formunu doldur; seninle birlikte taşınanların adlarını yaz.",
     "velden": [["Naam", ""], ["Oud adres", ""], ["Nieuw adres", ""], ["Datum verhuizing", "dag-maand-jaar"], ["Wie verhuizen er mee?", "namen"]],
     "voorbeeld": "Naam: Ali Demir\nOud adres: Kerkstraat 8, Leiden\nNieuw adres: Molenweg 21, Leiderdorp\nDatum verhuizing: 01-07-2026\nWie verhuizen er mee? Ayşe Demir (mijn vrouw), Emir Demir en Noor Demir (mijn kinderen)"},
    {"id": "s3-cursus", "soort": "e-mail", "titel": "Informatie over een cursus",
     "situatie": "U ziet een advertentie van een computercursus in het buurthuis. U wilt meer informatie. U schrijft een e-mail.",
     "opdracht": "Zeg dat u de cursus wilt doen.\nVraag hoeveel de cursus kost.\nVraag op welke dagen de les is.",
     "tr": "Kursa katılmak istediğini yaz; ücretini ve derslerin hangi günler olduğunu sor.",
     "voorbeeld": "Beste mevrouw, meneer,\n\nIk heb uw advertentie gezien. Ik wil graag de computercursus doen. Hoeveel kost de cursus? En op welke dagen is de les?\n\nMet vriendelijke groet,\nAyşe Yılmaz"},
    {"id": "s3-oppas", "soort": "briefje", "titel": "Briefje voor de oppas",
     "situatie": "Vanavond past Lisa op uw kinderen. U gaat weg. U schrijft een briefje voor Lisa en legt het op de tafel.",
     "opdracht": "Schrijf hoe laat de kinderen naar bed gaan.\nSchrijf wat ze mogen eten.\nSchrijf hoe laat u terug bent.",
     "tr": "Çocukların kaçta yatacağını, ne yiyebileceklerini ve senin kaçta döneceğini yaz.",
     "voorbeeld": "Hoi Lisa,\n\nDe kinderen gaan om 20.00 uur naar bed. Ze mogen een boterham en een appel eten. Ik ben om 23.00 uur terug.\n\nBedankt!\nAyşe"},
    {"id": "s3-klacht", "soort": "e-mail", "titel": "Verkeerde bestelling",
     "situatie": "U heeft online een blauwe jas besteld. U krijgt een zwarte jas. U schrijft een e-mail aan de winkel.",
     "opdracht": "Zeg wat u besteld heeft.\nZeg wat er fout is.\nVraag wat u nu moet doen.",
     "tr": "Ne sipariş ettiğini, neyin yanlış geldiğini yaz ve şimdi ne yapman gerektiğini sor.",
     "voorbeeld": "Beste mevrouw, meneer,\n\nIk heb een blauwe jas besteld. Maar ik heb een zwarte jas gekregen. Wat moet ik nu doen? Kan ik de jas terugsturen?\n\nMet vriendelijke groet,\nAli Demir"},
    # ---------- exam 4 ----------
    {"id": "s4-tandarts", "soort": "formulier", "titel": "Nieuwe patiënt bij de tandarts",
     "situatie": "U wilt patiënt worden bij een nieuwe tandarts. U vult het formulier in.",
     "opdracht": "Vul alle velden in.\nSchrijf bij 'Heeft u nu klachten?' één zin.",
     "tr": "Diş hekimi formunu doldur; şu an bir şikâyetin olup olmadığını bir cümleyle yaz.",
     "velden": [["Naam", ""], ["Geboortedatum", ""], ["Telefoonnummer", ""], ["Zorgverzekering", "naam van de verzekering"], ["Heeft u nu klachten?", "één zin"]],
     "voorbeeld": "Naam: Ayşe Yılmaz\nGeboortedatum: 22-09-1990\nTelefoonnummer: 06-12345678\nZorgverzekering: Zorg en Zeker\nHeeft u nu klachten? Ja, ik heb soms pijn aan een tand links boven."},
    {"id": "s4-vakantie", "soort": "e-mail", "titel": "Vrij vragen",
     "situatie": "U wilt in juli twee weken op vakantie. U schrijft een e-mail aan uw leidinggevende, mevrouw Bos.",
     "opdracht": "Vraag of u vrij kunt krijgen.\nSchrijf welke weken.\nSchrijf waar u naartoe gaat.",
     "tr": "İzin isteyebilir miyim diye sor; hangi haftalar olduğunu ve nereye gideceğini yaz.",
     "voorbeeld": "Beste mevrouw Bos,\n\nMag ik in juli twee weken vrij? Ik wil graag van 6 tot en met 19 juli op vakantie. Ik ga naar mijn familie in Turkije.\n\nMet vriendelijke groet,\nAli Demir"},
    {"id": "s4-sleutel", "soort": "bericht", "titel": "Sleutel vergeten",
     "situatie": "U staat voor de deur. U heeft uw sleutel vergeten. Uw partner is op het werk. U stuurt een appbericht.",
     "opdracht": "Zeg wat het probleem is.\nZeg waar u nu bent.\nVraag wanneer uw partner thuiskomt.",
     "tr": "Sorunu, şu an nerede olduğunu yaz ve eşinin eve ne zaman geleceğini sor.",
     "voorbeeld": "Hoi schat, ik ben mijn sleutel vergeten! Ik sta nu voor de deur. Ik ga even naar de buurvrouw. Hoe laat kom je thuis?"},
    {"id": "s4-afmelden", "soort": "e-mail", "titel": "Afmelden voor de cursus",
     "situatie": "U doet een cursus Nederlands. Volgende week kunt u twee lessen niet komen. U schrijft een e-mail aan de docent.",
     "opdracht": "Zeg welke lessen u niet komt.\nZeg waarom.\nVraag of de docent het huiswerk wil sturen.",
     "tr": "Hangi derslere gelemeyeceğini ve nedenini yaz; öğretmenden ödevi göndermesini iste.",
     "voorbeeld": "Beste meneer Van Dam,\n\nVolgende week kan ik op maandag en woensdag niet naar de les komen. Mijn moeder komt uit Turkije en ik haal haar op van Schiphol. Wilt u mij het huiswerk sturen?\n\nMet vriendelijke groet,\nAyşe Yılmaz"},
]

EXAMENS = [{"id": f"s-examen-{k}", "titel": f"A2 Schrijven proefexamen {k}", "taken": [t["id"] for t in TAKEN if t["id"].startswith(f"s{k}-")], "minuten": 40}
           for k in range(1, 5)]

# Short A2 writing criteria for the self-check and the AI prompt (CEFR A2 writing: short, simple notes and messages
# about everyday needs; simple sentences linked with 'en', 'maar', 'want'). Not DUO's official scoring model.
CRITERIA = [
    {"id": "inhoud", "naam": "Inhoud", "nl": "Alle punten uit de opdracht staan erin.", "tr": "Görevin istediği her nokta cevapta var mı?"},
    {"id": "begrijpelijk", "naam": "Begrijpelijk", "nl": "De lezer begrijpt de tekst zonder moeite.", "tr": "Okuyan kişi metni rahatça anlıyor mu?"},
    {"id": "vorm", "naam": "Vorm", "nl": "Passende aanhef en groet (e-mail, brief); bij een formulier: alle velden goed ingevuld.", "tr": "E-postada hitap ve kapanış var mı; formda alanlar doğru doldurulmuş mu?"},
    {"id": "taal", "naam": "Woorden en zinnen", "nl": "Eenvoudige, correcte zinnen; fouten maken de tekst niet onduidelijk.", "tr": "Cümleler basit ve büyük ölçüde doğru mu; hatalar anlamı bozuyor mu?"},
]


def main():
    ids = set()
    for t in TAKEN:
        assert t["id"] not in ids, t["id"]; ids.add(t["id"])
        assert t["soort"] in SOORTEN, t["id"]
        assert t["situatie"] and t["opdracht"] and t["tr"] and t["voorbeeld"], t["id"]
        assert (t["soort"] == "formulier") == bool(t.get("velden")), f"{t['id']}: velden only for formulier"
        t["punten"] = [p.strip() for p in t["opdracht"].split("\n") if p.strip()]
    for e in EXAMENS:
        assert len(e["taken"]) == 4, e["id"]
    OUT.write_text(json.dumps({"_about": "Own A2 Schrijven practice tasks. Generated by scripts/content/schrijven_a2/build_schrijven_a2.py.",
                               "taken": TAKEN, "examens": EXAMENS, "criteria": CRITERIA}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(TAKEN)} tasks, {len(EXAMENS)} exams -> {OUT}")


if __name__ == "__main__":
    main()
