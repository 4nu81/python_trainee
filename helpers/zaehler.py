#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Counter:
	def __init__(self):
		self.counter = {}
	
	def add(self, item, val):
		if item in self.counter:
			self.counter[item] += float(val)
		else:
			self.counter[item] = float(val)
	
	def __str__(self):
		result = ''
		for item in self.counter:
			result += item + ' : ' + str(self.counter[item]) + '\n'
		return result
	
	def print_counter(self):
		print str(self)
	
	def store(self):
		f = open('counter.txt','w')
		f.write(str(self))
		f.close()

def run():
	counter = Counter()
	while True:
		os.system('clear')
		counter.print_counter()
		item = raw_input('item: ')
		if item == 's':
			counter.store()
		elif item == 'x':
			break
		else:
			vals = item.split(',')
			try:
				counter.add(vals[0], vals[1])
			except Exception,e:
				pass
		
if __name__ == '__main__':
	run()