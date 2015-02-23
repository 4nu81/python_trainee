import fileio, ausgabe
import fragebogen as fb_typ
import cmdlnparser

def execute():
    dateiname, email = cmdlnparser.cmdln_starten()
    fragebogen = fileio.fragebogen_laden(dateiname)
    fb_typ.fragebogen_nummerieren(fragebogen)
    fileio.pruefungsbogen_anlegen(dateiname, email)
    ausgabe.fragebogen_ausgeben(fragebogen)


