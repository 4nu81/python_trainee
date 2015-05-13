# -*- coding: utf-8 -*-

import spellcheck

def menu(tdn, wbn):
	op = raw_input('Menu: (n)ächster Abschnitt / (w)örter Lernen :')
	
	if op == 'n':
		spellcheck.naechster_abschnitt(tdn, wbn)
	elif op.startswith('w'):
		op = op[2:]
		params = op.split(',')
		spellcheck.woerter_lernen(params, tdn, wbn)

def anzeigen(fa, tdn, wbn):
	print """
	Fehler:
	{vor}
	{zeile}
	{nach}
	
	---
	
	{worte}
	""".format(
		vor = fa.vor_fehlerzeile,
		nach = fa.nach_fehlerzeile,
		zeile = fa.fehlerzeile,
		worte = ', '.join(['{indx}:"{word}"'.format(indx = i, word = word) for i, word in enumerate(fa.fehlerworte)])
	)
	menu(tdn, wbn)