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
        self.antwort = antwort
        self.nummer = ''

def fragebogen_nummerieren(fragebogen):
    for i, frage in enumerate(fragebogen.fragen):
        frage.nummer = str(i + 1)

        for j, antwort in enumerate(frage.antworten):
            antwort.nummer = str(i + 1)+'.'+str(j + 1)

