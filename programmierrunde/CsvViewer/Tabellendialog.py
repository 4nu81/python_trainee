import csvviewer

def ergebnis_anzeigen(str_list):
    print ''.join(str_list)

def menu_anzeigen():
    print '\nN(ext page, P(revious page, F(irst page, L(ast page, eX(it'

def kommando_erwarten(bei_L, bei_F, bei_P, bei_N):
    while True:
        command = raw_input(' $ : ')
        if   command in ['l','L']: bei_L()
        elif command in ['f','F']: bei_F()
        elif command in ['n','N']: bei_N()
        elif command in ['p','P']: bei_P()
        elif command in ['x','X']: return

def seite_darstellen(str_list):
    ergebnis_anzeigen(str_list)
    menu_anzeigen()
    
def sag_hallo():
    print 'Hallo'

def sag_byebye():
    print 'ByeBye'
