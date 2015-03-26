#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileio, Tabellendialog, sys

class SeitenManager:

    def seite_bilden(self, aktuelle_position):
        seiten_laenge = 10
        return self.alles[ aktuelle_position : aktuelle_position + seiten_laenge]

class Global:
    seitenmanager = None
    pager = None

class Pager:

    def __init__(self):
        self.aktuelle_position = 0

    def position_naechste_seite(self, laenge_alles):
        seiten_laenge = 10
        if self.aktuelle_position + seiten_laenge < laenge_alles - 1:
            self.aktuelle_position += seiten_laenge
        return self.aktuelle_position
        
    def position_vorige_seite(self, laenge_alles):
        seiten_laenge = 10
        if self.aktuelle_position - seiten_laenge >= 0:
            self.aktuelle_position -= seiten_laenge
        return self.aktuelle_position
        
    def position_erste_seite(self):
        self.aktuelle_position = 0
        return self.aktuelle_position
    
    def position_letzte_seite(self, laenge_alles):
        seiten_laenge = 10
        self.aktuelle_position = laenge_alles - laenge_alles%seiten_laenge
        return self.aktuelle_position

def dateiname_auslesen():
    return sys.argv[1]

def alles_laden():
    if Global.seitenmanager is None:
        Global.seitenmanager = SeitenManager()
        dateiname = dateiname_auslesen()
        Global.seitenmanager.alles = fileio.datei_einlesen(dateiname)
        Global.seitenmanager.zeilen_anzahl = len(Global.seitenmanager.alles)

    if Global.pager is None:
        Global.pager = Pager()

def erste_seite_bilden():
    aktuelle_position = Global.pager.position_erste_seite()
    return Global.seitenmanager.seite_bilden(aktuelle_position)

def letzte_seite_bilden():
    aktuelle_position = Global.pager.position_letzte_seite(Global.seitenmanager.zeilen_anzahl)
    return Global.seitenmanager.seite_bilden(aktuelle_position)

def naechste_seite_bilden():
    aktuelle_position = Global.pager.position_naechste_seite(Global.seitenmanager.zeilen_anzahl)
    return Global.seitenmanager.seite_bilden(aktuelle_position)

def vorige_seite_bilden():
    aktuelle_position = Global.pager.position_vorige_seite(Global.seitenmanager.zeilen_anzahl)
    return Global.seitenmanager.seite_bilden(aktuelle_position)

def erste_seite_aufblaettern():
    alles_laden()
    lines = erste_seite_bilden()
    Tabellendialog.seite_darstellen(lines)

def letzte_seite_aufblaettern():
    alles_laden()
    lines = letzte_seite_bilden()
    Tabellendialog.seite_darstellen(lines)

def naechste_seite_aufblaettern():
    alles_laden()
    lines = naechste_seite_bilden()
    Tabellendialog.seite_darstellen(lines)

def vorige_seite_aufblaettern():
    alles_laden()
    lines = vorige_seite_bilden()
    Tabellendialog.seite_darstellen(lines)

def main():
    erste_seite_aufblaettern()
    Tabellendialog.kommando_erwarten(
        bei_L = letzte_seite_aufblaettern,
        bei_F = erste_seite_aufblaettern,
        bei_N = naechste_seite_aufblaettern,
        bei_P = vorige_seite_aufblaettern
    )

if __name__ == '__main__':
    main()
