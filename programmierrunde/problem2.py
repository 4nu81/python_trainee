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

def FromRoman(roman):
    roman = Ziffern_uebersetzen(roman)
    roman = SubRegel(roman)
    return Addition(roman)




test = {
    'I' : 1,
    'IV' : 4,
    'IX' : 9,
    'MM' : 2000,
    'CM' : 900,
    'XIX' : 19,
    'A' : 0
}

for i in test:
    try:
        res = FromRoman(i)
        if res == test[i]:
            print i, ' = ', res
        else:
            print 'Fehler:', i, ' ungleich ', res
    except:
        print i, 'is invalid'
