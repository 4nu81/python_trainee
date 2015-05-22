# -*- coding: utf-8 -*-

global fa

class Fehlerabschnitt():
	def __init__(self, zeilennummer = 0, fehlerzeile = '', vor_fehlerzeile = '', nach_fehlerzeile = '', fehlerworte = ''):
		self.fehlerzeile = fehlerzeile
		self.vor_fehlerzeile = vor_fehlerzeile
		self.nach_fehlerzeile = nach_fehlerzeile
		self.fehlerworte = fehlerworte
		self.zeilennummer = zeilennummer

	def naechste_fehlerzeile_finden(self, zeilen, wb):
		zeilennummer = self.zeilennummer
		worte = []
		if zeilennummer < len(zeilen) - 1:
			for nummer ,zeile in enumerate(zeilen[zeilennummer:]):
				line = zeile.split()
				for wort in line:
					wort = wort.strip(',.?!»«')
					if not wort in wb:
						worte.append(wort)
				if worte:
					break
			return nummer + zeilennummer, worte
		else:
			return None, None
	
	def worte_finden(self, indizes):
		global fa
		result = []
		for nr in indizes:
			result.append(fa.fehlerworte[int(nr)])
		return result
	
	def zeilennummer_erhoehen(self):
		self.zeilennummer += 1

def fehlerabschnitt_bilden(zeilennummer, fehlerworte, zeilen):
	global fa
	fehlerzeile = zeilen[zeilennummer]

	if zeilennummer > 0:
		vor_fehlerzeile = zeilen[zeilennummer - 1]
	else:
		vor_fehlerzeile = ''

	if zeilennummer < len(zeilen) - 1:
		nach_fehlerzeile = zeilen[zeilennummer + 1]
	else:
		nach_fehlerzeile = ''

	fa = Fehlerabschnitt(
		zeilennummer = zeilennummer,
		fehlerworte = fehlerworte,
		fehlerzeile = fehlerzeile,
		vor_fehlerzeile = vor_fehlerzeile,
		nach_fehlerzeile = nach_fehlerzeile
	)