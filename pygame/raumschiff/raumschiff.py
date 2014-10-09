#! /usr/bin/python

import random, time

class Weapon:
    def __init__(self, name, dmg=(3,5)):
        self.name = name
        self.dmg = dmg

class Captain:
    def __init__(self, name, exp=1.0):
        self.name = name
        self._exp = exp

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value

class Asteroid:
    def __init__(self, size, name=None, hp=6):
        self.name = name
        self.hp = hp
        self.size = size

class Ship:
    def __init__(self, name, captain, color='red', armor=2, hull=10):
        self.name = name
        self.color = color
        self.armor = armor
        self.hull = hull
        self.captain = Captain(name=captain)
        self.weapons = [Weapon('Burst Laser I')]

    def getAttack(self):
        attk = 0
        for weapon in self.weapons:
            attk += random.randint(weapon.dmg[0], weapon.dmg[1])
        return attk + self.captain.exp / 10

    def getDamage(self, dmg):
        armor = self.armor * float(self.captain.exp)
        val = dmg - armor
        if val > 0:
            self.hull -= val
            if self.hull <= 0:
                self.hull = 0
        else:
            val = 0
        print "{name} has been hit - {dmg} Damage - {hull} hull - {armor} armor".format(name=self.name, dmg=val, hull=self.hull, armor=armor)

    def getAlive(self):
        if self.hull > 0:
            return True
        else:
            return False

ships = []

ship1 = Ship(name='Enterprise', captain='Cpt. Picard')
ship1.weapons = [Weapon('Burst Laser II', (4,6)), Weapon('Burst Laser II', (4,6))]

ship2 = Ship(name='Orion', captain='Cpt. Balu')
ship1.weapons = [Weapon('Burst Laser I', (3,5)), Weapon('Burst Laser I', (3,5))]

ships.append(ship1)
ships.append(ship2)

for i in range(20):
    print "Round {val}".format(val=i+1)
    for ship in ships:
        dmg = random.randint(1,6)
        if dmg > 2:
            asteroid = Asteroid(size=dmg)
            attk = ship.getAttack()
            asteroid.hp -= attk
            if asteroid.hp <= 0:
                exp = asteroid.size / 10.0
                ship.captain.exp += exp
                print "{ship} - asteroid has been destroyed - attk {attk} - exp +{exp} = {nexp}".format(attk=attk,ship=ship.name,exp=exp,nexp=ship.captain.exp)
            else:
                ship.getDamage(asteroid.size)
                if not ship.getAlive():
                    print "{name} has been destroyed".format(name=ship.name)
                    ships.remove(ship)
    print "\n###\n"
    time.sleep(1)

print '\n'
for ship in ships:
    print "{name} has survived with {hull} hull left".format(name=ship.name, hull=ship.hull)


