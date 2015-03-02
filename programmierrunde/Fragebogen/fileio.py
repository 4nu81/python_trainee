from fragebogen import *
from pruefungsbogen import *

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

def pruefungsbogen_laden():
    f = open('brain', 'r')
    lst = f.readlines()
    f.close()

    for i in range(len(lst)):
        lst[i] = lst[i].replace('\n', '')

    pb = Pruefungsbogen(lst[0], lst[1], lst[2:])
    return pb

def pruefungsbogen_speichern(pb):
    f = open('brain', 'w')
    f.write(pb.fragebogen + '\n')
    f.write(pb.email + '\n')
    for nr in pb.antworten:
        f.write(nr + '\n')
    f.close()
