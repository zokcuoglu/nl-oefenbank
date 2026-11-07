# Builds oyunlar/voorzetsels.json for two daily games in the "Günün oyunları" tab:
#   - "voorzetsels": fixed prepositions (denken aan, luisteren naar ...), 10 a day
#   - "erop":        er + preposition (erop, eraan, ermee, er ... over ...), 5 a day
# Sentences come first from our own site texts (news, Lezen, Luisteren, KNM, Spreken, Schrijven, word examples).
# The script looks each sentence up in data/*.json and writes where it comes from; a sentence that is not found
# there must be marked EIGEN (own example sentence), otherwise the build stops - so copying mistakes are caught.
# Run from the repo root:  python3 scripts/content/build_voorzetsels.py
import json, re, html, unicodedata
from pathlib import Path

EIGEN = "eigen"   # own example sentence (the combination does not occur in our texts yet)

# (combination, answer, other accepted answers, Turkish meaning, sentence with ___ , source or EIGEN)
VZ = [
 ("denken aan", "aan", [], "düşünmek; aklında tutmak", "Je denkt veel ___ de problemen in jouw land.", None),
 ("denken aan", "aan", [], "düşünmek; aklında tutmak", "Denk ___ je paspoort als je op reis gaat.", EIGEN),
 ("luisteren naar", "naar", [], "dinlemek", "Luister ___ de politieagent en vertel hem wat u gezien hebt.", None),
 ("kijken naar", "naar", [], "bakmak, izlemek", "De laptop staat op de keukentafel, dus je kijkt 's avonds nog even ___ je mail.", None),
 ("kijken naar", "naar", [], "bakmak, izlemek", "Kijk ___ een briefje van tien euro.", None),
 ("wachten op", "op", [], "beklemek", "U trekt een nummertje en wacht ___ uw beurt.", None),
 ("zorgen voor", "voor", [], "bakmak, ilgilenmek", "Daar zorgen ze ___ jonge zeehonden.", None),
 ("zorgen voor", "voor", [], "sağlamak, -e yol açmak", "Een dubbele laag eiwit en paneermeel zorgt ___ de kenmerkende krokante korst.", None),
 ("zorgen voor", "voor", [], "sağlamak", "En zorg thuis ___ een vaste werkplek en vaste werktijden.", None),
 ("houden van", "van", [], "sevmek", "Hij is sportief, houdt ___ geld en kan zelfs een Schwalbe maken – 'hartstikke professioneel'.", None),
 ("houden van", "van", [], "sevmek", "Ik kies de bakkerij, want ik houd ___ brood en gebak.", None),
 ("letten op", "op", [], "dikkat etmek", "Je let goed ___ hoe elk kind zich ontwikkelt.", None),
 ("letten op", "op", [], "dikkat etmek", "Let ___: geef veranderingen in uw inkomen altijd snel door.", None),
 ("rekenen op", "op", [], "güvenmek, beklemek", "Zo'n twee miljoen Nederlanders kunnen volgend jaar vermoedelijk rekenen ___ een hoger pensioen.", None),
 ("rekenen op", "op", [], "güvenmek, beklemek", "Het centrum rekende ___ steun van gemeente en provincie, maar die blijft uit – tot onbegrip van de directeur.", None),
 ("bestaan uit", "uit", [], "-den oluşmak", "De training bestaat ___ zes lessen van twee uur, op zaterdagochtend van 10.00 tot 12.00 uur.", None),
 ("bestaan uit", "uit", [], "-den oluşmak", "Wolken bestaan ___ kleine waterdruppels.", None),
 ("leiden tot", "tot", [], "-e yol açmak", "Te weinig slaap kan leiden ___ problemen op je werk.", EIGEN),
 ("lijken op", "op", [], "-e benzemek", "Er blijft iets over dat lijkt ___ elastiek.", None),
 ("lijken op", "op", [], "-e benzemek", "Hij lijkt ___ zijn vader.", None),
 ("genieten van", "van", [], "-den keyif almak", "We hebben genoten ___ het mooie weer.", EIGEN),
 ("vragen om", "om", [], "istemek, talep etmek", "Wij vragen de gemeente ___ bredere fietspaden.", None),
 ("vragen om", "om", [], "istemek, talep etmek", "Uw werkgever vraagt ___ een Verklaring Omtrent Gedrag (VOG).", None),
 ("zoeken naar", "naar", [], "aramak", "Samen zoeken we ___ een oplossing, bijvoorbeeld een betalingsregeling.", None),
 ("op zoek zijn naar", "naar", [], "-i arıyor olmak", "Starters op de woningmarkt zijn mensen die voor het eerst op zoek zijn ___ een woning.", None),
 ("beginnen met", "met", [], "-e başlamak", "'Johan Cruijff begon ook ___ voetballen tegen een muurtje,' zegt hij.", None),
 ("beginnen met", "met", [], "ile başlamak", "Alles begint ___ een stuk karton.", None),
 ("stoppen met", "met", [], "bırakmak", "In Nederland stop je op je 67e ___ werken.", None),
 ("stoppen met", "met", [], "bırakmak", "Hij stopte ___ voetbal toen hij 11 was.", None),
 ("praten over", "over", [], "hakkında konuşmak", "We praten in kleine groepen ___ allerlei onderwerpen: werk, het nieuws, feestdagen.", None),
 ("praten met", "met", [], "biriyle konuşmak", "Daar praat hij ___ een meteoroloog: iemand die het weer bestudeert.", None),
 ("praten met", "met", [], "biriyle konuşmak", "Vandaag praat ik ___ Kees Mulder van de Fietsersbond.", None),
 ("reageren op", "op", [], "-e tepki vermek, cevap vermek", "Maria reageert ___ een vacature en stuurt een brief en haar cv.", None),
 ("reageren op", "op", [], "-e tepki vermek", "Ze reageerde laconiek ___ het nieuws.", None),
 ("meedoen aan", "aan", [], "-e katılmak", "Bij alle abonnementen mag je gratis meedoen ___ de groepslessen, zoals yoga en spinning.", None),
 ("doen aan (sport)", "aan", [], "(bir spor) yapmak", "Abel doet ___ freestyle voetbal: in je eentje, zonder veel regels, de bal hoog houden.", None),
 ("deelnemen aan", "aan", [], "-e katılmak", "Ik neem deel ___ de vergadering.", None),
 ("zich aanmelden voor", "voor", [], "-e kaydolmak", "Petra wil zich aanmelden ___ zwemles.", None),
 ("helpen met", "met", ["bij"], "-de yardım etmek", "Maar mijn klasgenoten, die vaak twintig jaar jonger waren, hielpen me ___ de computer.", None),
 ("helpen met", "met", ["bij"], "-de yardım etmek", "Je speelt met de kinderen, leest voor, gaat met ze naar buiten en helpt ze ___ eten en drinken.", None),
 ("helpen bij", "bij", ["met"], "-de yardım etmek", "Het uitzendbureau helpt u ___ het zoeken naar werk.", None),
 ("hopen op", "op", [], "-i ummak", "We hopen ___ mooi weer voor het buurtfeest.", EIGEN),
 ("twijfelen aan", "aan", [], "-den şüphe etmek", "Ook twijfelen veel oudere werknemers ___ zichzelf.", None),
 ("gaan over", "over", [], "hakkında olmak, konusu olmak", "'Het gaat ___ veel meer dan alleen maar zeehonden,' benadrukt hij.", None),
 ("gaan over", "over", [], "hakkında olmak, konusu olmak", "De tekst gaat ___ vakantie en verlof: tijd dat je niet hoeft te werken.", None),
 ("horen bij", "bij", [], "-e ait olmak", "De pincode is geheim en hoort alléén ___ uw bankpas.", None),
 ("betalen voor", "voor", [], "-e para ödemek", "U betaalt alleen ___ de stroom die u gebruikt.", None),
 ("kiezen voor", "voor", [], "-i seçmek", "Steeds meer mensen kiezen op latere leeftijd ___ omscholing.", None),
 ("kiezen voor", "voor", [], "-i seçmek", "Kies dan ___ een BBL-opleiding.", None),
 ("werken aan", "aan", [], "üzerinde çalışmak", "Maak een planning en werk elke dag een paar uur ___ je werkstuk.", None),
 ("werken bij", "bij", [], "-de çalışmak (işyeri)", "Nu werk ik ___ een installatiebedrijf en over een jaar heb ik mijn diploma.", None),
 ("schrijven over", "over", [], "hakkında yazmak", "Ik schrijf je ___ ons afdelingsuitje.", None),
 ("vertellen over", "over", [], "hakkında anlatmak", "Dan vertelt hij ___ zijn grote droom.", None),
 ("nadenken over", "over", [], "üzerine düşünmek", "De Graaf adviseert om eerst goed na te denken ___ wat je wilt en kunt.", None),
 ("klagen over", "over", [], "-den şikâyet etmek", "Ik wil niet klagen ___ een collega.", None),
 ("informeren over", "over", [], "hakkında bilgi vermek", "U wilt de gemeente informeren ___ uw nieuwe adres.", None),
 ("beslissen over", "over", [], "hakkında karar vermek", "Je beslist zelf ___ je leven.", None),
 ("vergelijken met", "met", [], "ile karşılaştırmak", "Vergelijk de prijzen ___ die van andere winkels.", EIGEN),
 ("trouwen met", "met", [], "ile evlenmek", "Mijn zus trouwt volgend jaar ___ haar vriend.", EIGEN),
 ("passen bij", "bij", [], "-e uymak, yakışmak", "Het beroep van kok past ___ mij, omdat ik creatief ben in de keuken.", None),
 ("passen op", "op", [], "-e göz kulak olmak", "Uw buurman Peter heeft ___ uw kat gepast toen u op vakantie was.", None),
 ("bellen naar", "naar", [], "-i (telefonla) aramak", "Bel dan vóór 7.00 uur ___ de winkel.", None),
 ("verwijzen naar", "naar", [], "-e atıfta bulunmak", "De naam verwijst ___ ons verleden.", None),
 ("verwijzen naar", "naar", [], "-e sevk etmek", "De huisarts verwijst u ___ een specialist.", EIGEN),
 ("verlangen naar", "naar", [], "-i özlemek", "Na de lange winter verlang ik ___ de zomer.", EIGEN),
 ("zich voorbereiden op", "op", [], "-e hazırlanmak", "Ik bereid me goed voor ___ het examen.", EIGEN),
 ("zich concentreren op", "op", [], "-e odaklanmak", "In de klas kan ik me niet concentreren ___ de les.", EIGEN),
 ("zich ergeren aan", "aan", [], "-e sinirlenmek", "Familie Bos ergerde zich al maanden ___ de hond van de buren, die elke dag urenlang blafte.", None),
 ("zich houden aan", "aan", [], "-e uymak (kural)", "Houd je ___ de regels.", None),
 ("zich zorgen maken over", "over", [], "için endişelenmek", "U maakt zich zorgen ___ zijn gedrag.", None),
 ("afhangen van", "van", [], "-e bağlı olmak", "Of u het krijgt, hangt af ___ uw inkomen.", None),
 ("afhangen van", "van", [], "-e bağlı olmak", "Wie de reparatie betaalt, hangt af ___ wat er kapot is.", None),
 ("profiteren van", "van", [], "-den yararlanmak", "Iedereen profiteert ___ de lagere prijzen.", EIGEN),
 ("omgaan met", "met", [], "ile geçinmek, davranmak", "Hoe kunt u het beste omgaan ___ mensen die anders leven of denken dan u?", None),
 ("rekening houden met", "met", [], "-i hesaba katmak", "Houd rekening ___ de buren.", None),
 ("bang zijn voor", "voor", [], "-den korkmak", "Ik werk liever bij woonhuizen, want ik ben bang ___ hoogte.", None),
 ("trots zijn op", "op", [], "-den gurur duymak", "Ik ben trots ___ mijn kinderen.", EIGEN),
 ("verantwoordelijk zijn voor", "voor", [], "-den sorumlu olmak", "Wij zijn niet verantwoordelijk ___ spullen die u kwijtraakt.", None),
 ("afhankelijk zijn van", "van", [], "-e bağımlı olmak", "De storing legt bloot hoe afhankelijk een moderne supermarktketen ___ haar IT is.", None),
 ("geïnteresseerd zijn in", "in", [], "-e ilgi duymak", "Ik ben erg geïnteresseerd ___ deze vacature.", EIGEN),
 ("tevreden zijn over", "over", ["met"], "-den memnun olmak", "Ik schrijf u omdat ik niet tevreden ben ___ mijn bestelling.", None),
 ("boos zijn op", "op", [], "-e kızgın olmak", "Mijn chef werd heel boos ___ mij.", None),
 ("blij zijn met", "met", [], "-e sevinmek", "De jarige is wel blij ___ uw cadeautje.", None),
 ("goed zijn in", "in", [], "-de iyi olmak", "Je bent goed ___ praten met mensen.", None),
 ("bekend zijn met", "met", [], "-i bilmek, -e aşina olmak", "Bent u bekend ___ dit computerprogramma?", EIGEN),
 ("klaar zijn met", "met", [], "-i bitirmiş olmak", "De zoon van Jan is klaar ___ de basisschool.", None),
 ("gewend zijn aan", "aan", [], "-e alışkın olmak", "Na een jaar was ik gewend ___ het Nederlandse weer.", EIGEN),
 ("nodig zijn voor", "voor", [], "için gerekli olmak", "U heeft een diploma nodig ___ het werk dat u wilt gaan doen.", None),
 ("belangrijk zijn voor", "voor", [], "için önemli olmak", "Daarom is zwemles belangrijk ___ de kinderen.", None),
 ("geschikt zijn voor", "voor", [], "için uygun olmak", "Deze baan is geschikt ___ studenten.", None),
 ("benieuwd zijn naar", "naar", [], "-i merak etmek", "Ik ben benieuwd ___ de uitslag van het examen.", EIGEN),
 ("jaloers zijn op", "op", [], "-i kıskanmak", "Hij is jaloers ___ zijn broer.", EIGEN),
 ("verliefd zijn op", "op", [], "-e âşık olmak", "Ze is verliefd ___ haar collega.", EIGEN),
 ("het eens zijn met", "met", [], "ile aynı fikirde olmak", "Louisa is het niet eens ___ haar leidinggevende.", None),
 ("bezig zijn met", "met", [], "ile meşgul olmak", "We zijn volop bezig ___ de verhuizing.", None),
 ("de kans op", "op", [], "-e şans, ihtimal", "Als je vrijwilligerswerk doet, heb je meer kans ___ een baan.", None),
 ("de vraag naar", "naar", [], "-e talep", "Want steeds meer ouders werken allebei, en daardoor groeit de vraag ___ opvang voor hun kinderen.", None),
 ("de invloed op", "op", [], "-e etki", "Het weer heeft invloed ___ je humeur.", None),
 ("de interesse in", "in", [], "-e ilgi", "U praat met een vrouw die interesse heeft ___ de vacature.", None),
 ("het tekort aan", "aan", [], "-in eksikliği", "Er is een groot tekort ___ leraren.", EIGEN),
 ("de behoefte aan", "aan", [], "-e ihtiyaç", "Veel mensen hebben behoefte ___ rust.", EIGEN),
 ("het antwoord op", "op", [], "-e cevap", "Ik wacht nog op een antwoord ___ mijn e-mail.", EIGEN),
 ("de reden voor", "voor", [], "-in sebebi", "Wat is de reden ___ je verhuizing?", EIGEN),
]

# er + preposition. "er" is visible in the sentence  -> type only the preposition part (over, mee, toe ...)
#                    "er" is not visible (one gap)   -> type the whole word (erop, eraan, ermee ...)
# (base combination, answer, other accepted answers, Turkish meaning, sentence with ___ , source or EIGEN)
ER = [
 ("praten over", "over", [], "hakkında konuşmak", "Toch praten veel mensen er niet ___.", None),
 ("praten over", "over", [], "hakkında konuşmak", "Praat er dan eerst ___ met je docent.", None),
 ("kijken naar", "ernaar", [], "bakmak", "Ik stuur een monteur om ___ te kijken.", None),
 ("doen met", "ermee", [], "ile yapmak", "Twee vrouwen die vroeger in het onderwijs werkten, weten al wat ze ___ doen: reizen en leuke dingen doen met de kinderen en kleinkinderen.", None),
 ("uitgaan van", "ervan", [], "varsaymak, -den yola çıkmak", "Het bedrijf gaat ___ uit dat dat niet is gebeurd, al is dat niet zeker.", None),
 ("vinden van", "ervan", [], "hakkında düşünmek (fikir)", "Ik ben benieuwd wat zij ___ vindt.", None),
 ("het hebben over", "erover", [], "-den bahsetmek", "Ik had het ___ dat we later beginnen.", None),
 ("de vraag naar", "naar", [], "-e talep", "Volgens de wethouder is er veel vraag ___, vooral van studenten en gezinnen.", None),
 ("gebruiken voor", "voor", [], "için kullanmak", "Je moet de uren dan wel later inhalen of er vakantie-uren ___ gebruiken.", None),
 ("achter iets zitten", "achter", [], "bir şeyin arkasında olmak", "Net werd bekend dat er waarschijnlijk hackers uit het buitenland ___ zitten.", None),
 ("zweren bij", "erbij", [], "-e çok güvenmek, yemin etmek", "Gluten zijn de laatste jaren een veelbesproken onderwerp: sommige mensen mijden ze, anderen zweren ___.", None),
 ("staan te kijken van", "ervan", [], "-e şaşırmak", "Wie nu nog denkt dat het om papier gaat, zal ___ staan te kijken: briefgeld is gemaakt van katoen, hetzelfde materiaal als veel van onze kleding.", None),
 ("overlijden aan", "eraan", [], "-den ölmek", "Je kunt ___ overlijden.", None),
 ("erbij komen kijken", "erbij", [], "işin içinde olmak, gerekmek", "Ik weet nog niet wat ___ komt kijken.", None),
 ("drinken bij", "bij", [], "yanında içmek", "Mag ik er alcohol ___ drinken?", None),
 ("eruitzien", "eruit", [], "görünmek", "Hoe ziet de nieuwe studieruimte ___?", None),
 ("denken aan", "eraan", [], "düşünmek, unutmamak", "Denk ___ dat je morgen je paspoort meeneemt.", EIGEN),
 ("denken aan", "aan", [], "düşünmek", "Sorry, ik heb er niet ___ gedacht.", EIGEN),
 ("wachten op", "erop", [], "beklemek", "Ik wacht ___ dat hij terugbelt.", EIGEN),
 ("rekenen op", "erop", [], "güvenmek", "Je kunt ___ rekenen dat ik op tijd ben.", EIGEN),
 ("uitkijken naar", "ernaar", [], "dört gözle beklemek", "Ik kijk ___ uit om je weer te zien!", EIGEN),
 ("stoppen met", "ermee", [], "bırakmak", "Hij rookte twintig jaar, maar vorig jaar is hij ___ gestopt.", EIGEN),
 ("klaar zijn met", "mee", [], "-i bitirmiş olmak", "Ben je al klaar met je huiswerk? Ja, ik ben er al ___ klaar.", EIGEN),
 ("zorgen voor", "ervoor", [], "sağlamak", "Zorg ___ dat je op tijd bent.", EIGEN),
 ("bang zijn voor", "voor", [], "-den korkmak", "Spinnen? Ik ben er erg bang ___.", EIGEN),
 ("trots zijn op", "op", [], "-den gurur duymak", "Je hebt je diploma gehaald. Je mag er trots ___ zijn!", EIGEN),
 ("leiden tot", "ertoe", [], "-e yol açmak", "Het slechte weer leidde ___ dat de wedstrijd niet doorging.", EIGEN),
 ("afhangen van", "ervan", [], "-e bağlı olmak", "Gaan we morgen naar het strand? Dat hangt ___ af.", EIGEN),
 ("bedoelen met", "ermee", [], "ile kastetmek", "Wat bedoel je ___?", EIGEN),
 ("zin hebben in", "in", [], "-i canı istemek", "Gaan we zwemmen? Nee, ik heb er geen zin ___.", EIGEN),
 ("het eens zijn met", "ermee", [], "aynı fikirde olmak", "Ik vind het een goed plan. Ik ben het ___ eens.", EIGEN),
 ("twijfelen aan", "aan", [], "-den şüphe etmek", "Ik weet niet of ik de baan neem. Ik twijfel er nog ___.", EIGEN),
 ("betalen voor", "voor", [], "-e para ödemek", "Is de cursus gratis, of moet ik er iets ___ betalen?", EIGEN),
]

# ---------- Look up where each sentence comes from ----------
ROOT = Path(__file__).resolve().parents[2]
def clean(s):
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    return unicodedata.normalize("NFC", s.replace("’", "'").replace("‘", "'"))
def norm(s):   # compare without case, quotes and extra spaces
    return re.sub(r"\s+", " ", re.sub(r"['\"*]", "", clean(s))).strip().lower()

texts = []   # (source label, normalised text)
news = json.loads((ROOT / "data/nieuws.json").read_text())
for it in news["items"]:
    texts.append((f"Nieuws · {it['titel']}", norm(json.dumps(it, ensure_ascii=False))))
for f, lab in [("lezen-teksten.json", "Lezen B1"), ("lezen-a2.json", "Lezen A2")]:
    for t in json.loads((ROOT / "data" / f).read_text())["teksten"]:
        texts.append((f"{lab} · {t['titel']}", norm(json.dumps(t, ensure_ascii=False))))
for f, lab in [("luisteren-b1.json", "Luisteren B1"), ("luisteren-a2.json", "Luisteren A2")]:
    for e in json.loads((ROOT / "data" / f).read_text())["examens"]:
        for fr in e["fragmenten"]:
            texts.append((f"{lab} · {fr.get('intro', '').rstrip('.')}", norm(json.dumps(fr, ensure_ascii=False))))
for f, lab in [("knm.json", "KNM"), ("spreken.json", "Spreken B1"), ("spreken-a2.json", "Spreken A2"), ("spreken-hulp.json", "Spreken B1"),
               ("schrijven-b1.json", "Schrijven B1"), ("schrijven-a2.json", "Schrijven A2"),
               ("woorden.json", "Woordenlijst"), ("lezen-bank.json", "Lezen woordenlijst")]:
    texts.append((lab, norm((ROOT / "data" / f).read_text())))
# json.dumps escapes nothing for ensure_ascii=False, but the raw files may contain \" etc.: unescape those too
texts = [(lab, t.replace("\\n", " ").replace('\\"', "")) for lab, t in texts]

def source(full):
    n = norm(full)
    for lab, t in texts:
        if n in t: return lab
    return None

def build(rows, prefix):
    out, missing, ids = [], [], set()
    for k, ans, alt, tr, zin, src in rows:
        assert zin.count("___") == 1, zin
        full = zin.replace("___", ans)   # the sentence as it appears in the text
        bron = "Eigen voorbeeldzin" if src == EIGEN else source(full)
        if bron is None: missing.append(full)
        base = prefix + "-" + re.sub(r"[^a-z]+", "-", unicodedata.normalize("NFKD", k).encode("ascii", "ignore").decode().lower()).strip("-")
        i, qid = 1, base
        while qid in ids: i += 1; qid = f"{base}-{i}"
        ids.add(qid)
        out.append({"id": qid, "k": k, "a": ans, "alt": alt, "tr": tr, "zin": zin, "bron": bron, "eigen": src == EIGEN})
    return out, missing

vz, m1 = build(VZ, "vz")
er, m2 = build(ER, "er")
if m1 or m2:
    print("Not found in our texts (fix the sentence or mark it EIGEN):")
    for s in m1 + m2: print("  -", s)
    raise SystemExit(1)
data = {
    "_about": "Daily games 'Günün edatları' (vaste voorzetsels) and 'er + edat'. Generated by scripts/content/build_voorzetsels.py - edit that file, not this one.",
    "voorzetsels": vz,
    "erop": er,
}
(ROOT / "oyunlar/voorzetsels.json").write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
own = sum(x["eigen"] for x in vz), sum(x["eigen"] for x in er)
print(f"voorzetsels: {len(vz)} sentences ({len(vz) - own[0]} from our texts, {own[0]} own), "
      f"{len({x['k'] for x in vz})} combinations")
print(f"erop: {len(er)} sentences ({len(er) - own[1]} from our texts, {own[1]} own)")
