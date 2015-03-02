class Fragebogen:
    def __init__(self):
        self.fragen = []

class Frage:
    def __init__(self, text):
        self.antworten = []
        self.text = text
        self.nummer = ''

class Anwortmgl:
    def __init__(self, text, antwort = False):
        self.text = text
        self.antwort = False;
        self.richtige_antwort = antwort
        self.nummer = ''
    def __str__(self):
        return self.nummer

def fragebogen_nummerieren(fragebogen):
    for i, frage in enumerate(fragebogen.fragen):
        frage.nummer = str(i + 1)

        for j, antwort in enumerate(frage.antworten):
            antwort.nummer = str(i + 1)+'.'+str(j + 1)

def antworten_markieren(pruefbogen, fragebogen):
    for frage in fragebogen.fragen:
        for antwort in frage.antworten:
            if antwort.nummer in pruefbogen.antworten:
                antwort.antwort = True;
            else:
                antwort.antwort = False;
