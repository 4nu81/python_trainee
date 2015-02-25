class Pruefungsbogen:
    def __init__(self, fragebogen, email, antworten = [] ):
        self.email = email
        self.fragebogen = fragebogen
        self.antworten = antworten

def antwort_eintragen(an, fb, pb):
    for frage in fb.fragen:
        antworten = [str(ant) for ant in frage.antworten]
        if str(an) in antworten:
            pb.antworten = list(set(pb.antworten) - set(antworten))
            pb.antworten.append(an)
