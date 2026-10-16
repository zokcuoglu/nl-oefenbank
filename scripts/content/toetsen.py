"""Mixed test after every three news items."""

TOETSEN = [
    {
        "id": "toets-1",
        "nr": 1,
        "titel": "Toets 1 · Nieuws 1–3",
        "items": ["kroket", "wolken", "gluten"],
        "per_item": 4,  # random questions taken from each item's own quiz
        "extra": [
            {"id": "m1", "type": "mc", "niveau": "B1", "cat": "begrip", "vraag": "In welke video krijgt iets twee lagen om het knapperig te maken?",
             "opties": ["De kroket: eiwit en paneermeel", "De wolken: water en ijs", "De gluten: kneden en wassen"], "juist": 0,
             "uitleg": "De kroketten krijgen twee keer eiwit en paneermeel."},
            {"id": "m2", "type": "mc", "niveau": "B1", "cat": "begrip", "vraag": "Wat speelt zowel in de wolkenvideo als in de glutenvideo een hoofdrol?",
             "opties": ["water", "suiker", "olie"], "juist": 0,
             "uitleg": "Waterdamp wordt druppels (wolken) en water maakt van eiwitten gluten (brood)."},
            {"id": "m3", "type": "mc", "niveau": "B2", "cat": "uitdrukkingen", "vraag": "'De fabriek vertelt het recept niet; dat is ___.' Welke uitdrukking past?",
             "opties": ["het geheim van de smid", "gebakken lucht", "een koukleum"], "juist": 0,
             "uitleg": "Het geheim van de smid = een trucje dat iemand niet vertelt."},
            {"id": "m4", "type": "mc", "niveau": "A2", "cat": "uitdrukkingen", "vraag": "Welke uitdrukking betekent 'heel blij zijn'?",
             "opties": ["in de wolken zijn", "het regent pijpenstelen", "zijn brood verdienen"], "juist": 0,
             "uitleg": "In de wolken zijn = heel blij zijn."},
            {"id": "m5", "type": "mc", "niveau": "B1", "cat": "grammatica", "vraag": "Welke zin staat in het passief?",
             "opties": ["De kroketten worden getest.", "De bakker kneedt het deeg.", "De wolk is wit."], "juist": 0,
             "uitleg": "Passief = worden + voltooid deelwoord: worden … getest."},
            {"id": "m6", "type": "mc", "niveau": "C1", "cat": "uitdrukkingen", "vraag": "Welke uitdrukking past bij 'mooie woorden zonder inhoud'?",
             "opties": ["holle frasen", "zich niet in de kaart laten kijken", "iets aan den lijve ervaren"], "juist": 0,
             "uitleg": "Holle frasen (en gebakken lucht) = woorden zonder inhoud."},
            {"id": "m7", "type": "gap", "niveau": "B1", "cat": "woorden", "vraag": "Een taalcafé zonder inschrijving is heel ___.",
             "opties": ["laagdrempelig", "verzadigd", "vertrouwelijk"], "juist": 0,
             "uitleg": "Laagdrempelig = iedereen kan er makkelijk naartoe."},
        ],
    }
]
