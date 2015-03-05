"""

() -> Pruefungsbogen laden -> FB
PB -> Fragebogen laden -> FB
FB -> Fragebogen nummerieren -> FB
FB, RB -> Auswertung erstellen -> Aw
Aw -> Auswertung in Log schreiben -> ()
Aw -> Auswertung ausgeben -> ()

"""

import fileio, ausgabe, cmdlnparser, pruefungsbogen
import fragebogen as fb_typ
import auswertung as aw_typ

def execute():
    pb = fileio.pruefungsbogen_laden()
    fb = fileio.fragebogen_laden(pb.fragebogen)
    fb_typ.fragebogen_nummerieren(fb)
    fb_typ.antworten_markieren(pb, fb)
    auswertung = aw_typ.auswertung_erstellen(fb,pb)
    fileio.log_schreiben(auswertung)
    ausgabe.auswertung_ausgeben(auswertung)
