# -*- coding: utf-8 -*-

import fileio
import fehlerabschnitt
import zeilendialog

def oeffnen(tdn, wbn):
	zeilen = fileio.textdatei_laden(tdn)
	wb = fileio.textdatei_laden(wbn)
	fehlerabschnitt.fa = fehlerabschnitt.Fehlerabschnitt()
	zeilennummer, worte = fehlerabschnitt.fa.naechste_fehlerzeile_finden(zeilen, wb)
	if not zeilennummer is None:
		fehlerabschnitt.fehlerabschnitt_bilden(zeilennummer, worte, zeilen)
		zeilendialog.anzeigen(fa = fehlerabschnitt.fa, tdn = tdn, wbn = wbn)

def naechster_abschnitt(tdn, wbn):
	zeilen = fileio.textdatei_laden(tdn)
	wb = fileio.textdatei_laden(wbn)
	fehlerabschnitt.fa.zeilennummer += 1
	zeilennummer, worte = fehlerabschnitt.fa.naechste_fehlerzeile_finden(zeilen, wb)
	if not zeilennummer is None:
		fehlerabschnitt.fehlerabschnitt_bilden(zeilennummer, worte, zeilen)
		zeilendialog.anzeigen(fa = fehlerabschnitt.fa, tdn = tdn, wbn = wbn)

def woerter_lernen(indizes, tdn, wbn):
	wb = fileio.textdatei_laden(wbn)
	worte = fehlerabschnitt.fa.worte_finden(indizes)
	wb.extend(worte)
	fileio.save(wbn, wb)
	fehlerabschnitt.fa.fehlerworte = [x for x in fehlerabschnitt.fa.fehlerworte if x not in worte]
	zeilendialog.anzeigen(fa = fehlerabschnitt.fa, tdn = tdn, wbn = wbn)