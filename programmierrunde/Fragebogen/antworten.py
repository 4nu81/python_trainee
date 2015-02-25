"""
Anummer, Fb, Pb -> Antwort in PB -> PB

"""

import fileio, ausgabe, cmdlnparser, pruefungsbogen
import fragebogen as fb_typ

def execute():
    antwortnummer = cmdlnparser.cmdln_antworten()
    pb = fileio.pruefungsbogen_laden()
    fb = fileio.fragebogen_laden(pb.fragebogen)
    fb_typ.fragebogen_nummerieren(fb)
    pruefungsbogen.antwort_eintragen(antwortnummer, fb, pb)
    fb_typ.antworten_markieren(pb, fb)
    fileio.pruefungsbogen_speichern(pb)
    
    ausgabe.fragebogen_ausgeben(fb)
