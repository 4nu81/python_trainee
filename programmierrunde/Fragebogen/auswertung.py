class Auswertung:
    def __init__(self, email, dateiname, ergebnis):
        self.email = email;
        self.dateiname = dateiname
        self.ergebnis = ergebnis

def auswertung_erstellen(fragebogen, pruefbogen):
    fragen = 0
    richtig = 0
    for frage in fragebogen.fragen:
        fragen += 1
        for antwort in frage.antworten:
            if antwort.antwort and antwort.markiert:
                richtig += 1
    ergebnis = '{r}/{a} richtige Antworten'.format(r = str(richtig), a = str(fragen))
    result = Auswertung(pruefbogen.email, pruefbogen.fragebogen, ergebnis)
    return result
