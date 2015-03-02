def fragebogen_ausgeben(fragebogen):
    for frage in fragebogen.fragen:
        print frage.nummer, frage.text
        for antwort in frage.antworten:
            print ' ' * 2 + antwort.nummer, antwort.antwort and '[x]' or '[ ]', antwort.text
