# -*- coding: utf-8 -*-

def strip_lines(lines):
	result = []
	for line in lines:
		line = line.strip()
		result.append(line)
	return result

def textdatei_laden(filename):
	f = open(filename, 'r+')
	lines = f.readlines()
	f.close()
	lines = strip_lines(lines)
	return lines

def save(filename, lines):
	f = open(filename, 'w')
	for line in lines:
		f.write(line + '\n')
	f.close()
	
def text_laden(filename):
	return textdatei_laden(filename)

def wb_laden(filename):
	return textdatei_laden(filename)