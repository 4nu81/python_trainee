import sys

romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'C': 100,
    'M': 1000,
    'L': 50,
    'D': 500
}

def Ziffern_uebersetzen(liste):
    """gibt eine Liste mit entsprechenden Werten zu den roemischen Ziffern zurueck"""
    res = []
    for a in liste:
        res.append(romans[a])
    return res

def Addition(liste):
    """summiert alle integer in der Liste"""
    return sum(liste)

def SubRegel(liste):
    """wendet die Subtraktionsregeln fuer roemische Zahlen an"""
    for i in range(len(liste)-1):
        if liste[i] < liste[i+1]:
            liste[i] *= -1
    return liste

def RomanToArab(roman):
    roman = Ziffern_uebersetzen(roman)
    roman = SubRegel(roman)
    return Addition(roman)

def ArabToRoman(zahl):
    return 'roman', zahl

def Konvertierungsart(eingabe, a2r, r2a):
    try:
        a2r(int(eingabe))
    except:
        r2a(eingabe)

def WertVonCommand():
    if len(sys.argv) > 1:
        return sys.argv[1]

def Ausgabe(val):
    print val

def processArabToRoman(eingabe):
    res = ArabToRoman(eingabe)
    Ausgabe(res)

def processRomanToArab(eingabe):
    res = RomanToArab(eingabe)
    Ausgabe(res)

if __name__ == '__main__':
    eingabe = WertVonCommand()
    Konvertierungsart(eingabe,
        processArabToRoman,
        processRomanToArab
    )
