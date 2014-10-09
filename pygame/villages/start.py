#! /usr/bin/python

import os, sys
from villages import *
from items import *

class game:
    def __init__(self, clear):
        self.village = village('dorf')
        self.clear = clear

    def _clear(self):
        """
        Clears the console screen using the clear_term of Calculator
        """
        os.system(self.clear)

    def _shutdown(self):
        self._clear()
        sys.exit(0)

    def proceed_input(self, value):
        if value in ['e','exit','q','quit']:
            self._shutdown()
        elif value in ['f', 'farm']:
            self.village.add_item(farm)
        elif value in ['spear']:
            self.village.add_item(spear)
        elif value in ['sword']:
            self.village.add_item(sword)
        elif value in ['horse']:
            self.village.add_item(horse)
        elif value in ['v','villager']:
            self.village.add_item(villager)
        elif value in ['m','man','manufacture']:
            self.village.add_item(manufacture)
        elif value in ['n','']:
            self.village.tick()
            if not self.village.status():
                print 'all villagers are dead'
        elif value in ['debug']:
            print self.village.items

    def run(self):
        while True:
            print self.village
            print 'actions:'
            value = raw_input(' Action: ')
            self._clear()
            self.proceed_input(value)


if __name__ == '__main__':
    clear = ''
    if os.name == "nt":
        clear = 'cls'
    else:
        clear = 'clear'
    c = game(clear)
    sys.exit(c.run())
