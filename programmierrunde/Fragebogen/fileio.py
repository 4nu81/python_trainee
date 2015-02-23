from fragebogen import *

def fragebogen_laden(dateiname):
    f = open(dateiname, 'r')
    lst = f.readlines()
    f.close()

    fb = Fragebogen()

    for line in lst:
        text = line.replace('\n','')
        if '?' in line:
            frage = Frage(text)
            fb.fragen.append(frage)
            frage.antworten.append(Anwortmgl('keine Ahnung', False))
        else:
            antwort = line.startswith('*')
            if antwort:
                text = text[1:]
            frage.antworten.append(Anwortmgl(text, antwort))
    return fb

def pruefungsbogen_anlegen(dateiname, email):
    f = open('brain', 'w')
    f.write(dateiname +'\n')
    f.write(email +'\n')
    f.close()
