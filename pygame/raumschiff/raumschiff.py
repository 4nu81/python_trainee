import random

class Weapon:
    def __init__(self, name, dmg=(3,5), acc=45):
        self.name = name
        self.dmg = dmg
        self.accuracy = acc

class Captain:
    def __init__(self, name, exp=1.0):
        self.name = name
        self._exp = exp
        self.level = 1

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
            if random.randint(0,100) <= (weapon.accuracy + self.captain.exp):
                attk += random.randint(weapon.dmg[0], weapon.dmg[1])
            else:
                print "{weapon} missed".format(weapon=weapon.name)
        return attk

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

