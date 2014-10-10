#! /usr/bin/python

import os, sys
from space import Space
from raumschiff import Ship, Weapon

class game:
    def __init__(self, clear):
        self.clear_term = clear
        self.space = Space()
        enterprise = Ship('Enterprise', 'Cpt. Pickard')
        enterprise.weapons = [
            Weapon(name='Burst Laser II', dmg=(4,6), acc=60),
            Weapon(name='Burst Laser II', dmg=(4,6), acc=60)
        ]
        self.space.ships.append(enterprise)
        self.space.ships.append(Ship('Orion', 'Cpt. Clark'))
        self.space.ships.append(Ship('Deathstar', 'Darth Vader'))
        print self.space.ships

    def run(self):
        while len(self.space.ships) > 1:
            ship1 = self.space.ships[0]
            ship2 = self.space.ships[1]
            self.space.combat(ship1, ship2)
            if not ship1.getAlive():
                self.space.ships.remove(ship1)
            if not ship2.getAlive():
                self.space.ships.remove(ship2)

if __name__ == '__main__':
    clear = ''
    if os.name == "nt":
        clear = 'cls'
    else:
        clear = 'clear'
    c = game(clear)
    sys.exit(c.run())
