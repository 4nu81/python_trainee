#! /usr/bin/python

import random

class Ship:
    def __init__(self, name, color='red', armor=2, hull=10):
        self.name = name
        self.color = color
        self.armor = armor
        self.hull = hull

    def getDamage(self, dmg):
        val = dmg - self.armor
        if val > 0:
            self.hull -= val
            if self.hull <= 0:
                self.hull = 0
            print "{name} has been hit - {dmg} Damage - {hull} hull".format(name=self.name, dmg=val, hull=self.hull)

    def getAlive(self):
        if self.hull > 0:
            return True
        else:
            return False

ships = []

ships.append(Ship('Enterprise'))
ships.append(Ship('Orion'))

for i in range(10):
    print "Round {val}".format(val=i+1)
    for ship in ships:
        dmg = random.randint(1,4)
        ship.getDamage(dmg)
        if not ship.getAlive():
            print "{name} has been destroyed".format(name=ship.name)
            ships.remove(ship)

print '\n'
for ship in ships:
    print "{name} has survived with {hull} hull left".format(name=ship.name, hull=ship.hull)


