# -*- coding: utf-8 -*-

import fileio
import fehlerabschnitt
import zeilendialog

def zeilennummer_pruefen(zeilennummer, nr_ok, worte, zeilen, tdn, wbn):
	if not zeilennummer is None:
		nr_ok(zeilennummer, worte, zeilen, tdn, wbn)

def fehler_gefunden(zeilennummer, worte, zeilen, tdn, wbn):
	fehlerabschnitt.fehlerabschnitt_bilden(zeilennummer, worte, zeilen)
	zeilendialog.anzeigen(fa = fehlerabschnitt.fa, tdn = tdn, wbn = wbn)

def oeffnen(tdn, wbn):
	zeilen = fileio.text_laden(tdn)
	wb = fileio.wb_laden(wbn)
	fehlerabschnitt.fa = fehlerabschnitt.Fehlerabschnitt()
	zeilennummer, worte = fehlerabschnitt.fa.naechste_fehlerzeile_finden(zeilen, wb)
	zeilennummer_pruefen(zeilennummer, fehler_gefunden, worte, zeilen, tdn, wbn)

def naechster_abschnitt(tdn, wbn):
	zeilen = fileio.text_laden(tdn)
	wb = fileio.wb_laden(wbn)
	fehlerabschnitt.fa.zeilennummer_erhoehen()
	zeilennummer, worte = fehlerabschnitt.fa.naechste_fehlerzeile_finden(zeilen, wb)
	zeilennummer_pruefen(zeilennummer, fehler_gefunden, worte, zeilen, tdn, wbn)

def woerter_lernen(indizes, tdn, wbn):
	wb = fileio.wb_laden(wbn)
	worte = fehlerabschnitt.fa.worte_finden(indizes)
	wb.extend(worte)
	fileio.save(wbn, wb)
	fehlerabschnitt.fa.fehlerworte = [x for x in fehlerabschnitt.fa.fehlerworte if x not in worte]
	zeilendialog.anzeigen(fa = fehlerabschnitt.fa, tdn = tdn, wbn = wbn)