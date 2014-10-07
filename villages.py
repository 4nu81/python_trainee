#! /usr/bin/python

class village:
    def __init__(self, name, gold=1000, food=200):
        self.year = 0
        self.name = name
        self.gold = gold
        self.food = food
        self.troops = {
            'spear' : 0,
            'sword' : 0,
            'horse' : 0,
        }
        self.villagers = 5
        self.buildings = {
            'fields' : 1,
        }

    def tick(self):

        self.year += 1

        gold = 0
        gold -= self.troops['spear'] * 10
        gold -= self.troops['sword'] * 25
        gold -= self.troops['horse'] * 30
        gold += self.villagers * 5
        self.gold += gold

        food = 0
        food += self.buildings['fields'] * 10
        food -= self.villagers
        food -= self.troops['spear'] * 2
        food -= self.troops['sword'] * 3
        food -= self.troops['horse'] * 5
        self.food += food

        self.villagers += int(self.villagers * 0.6)

    def add_troops(self, spear=0, sword=0, horse=0):
        price = 0
        price += spear * 100
        price += sword * 250
        price += horse * 500

        if price > self.gold or self.villagers < (spear + sword + horse * 2):
            return False
        else:
            self.gold -= price
            self.troops['spear'] += spear
            self.troops['sword'] += sword
            self.troops['horse'] += horse
            self.villagers -= spear + sword + horse * 2

    def status(self):
        if self.gold < 0:
            return False

        while self.food < 0:
            if self.villagers > 0:
                self.villagers -= 1
                self.food += 1

        if self.villagers == 0:
            return False

    def __str__(self):
        return """{name}
    year={year}
    gold={gold}
    food={food}
    villagers={vill}
    spear={spear}
    sword={sword}
    horse={horse}
            """.format(
            name=self.name,
            year=self.year,
            gold=self.gold,
            food=self.food,
            vill=self.villagers,
            spear=self.troops['spear'],
            sword=self.troops['sword'],
            horse=self.troops['horse'],
        )

villages = [
    village('horse'),
    village('sword'),
    village('spear'),
    village('normal'),
]

for i in range(20):
    for village in villages:
        village.tick()
        village.status()
        if i == 10 and village.name == 'spear':
            village.add_troops(spear=1)
        elif i == 10 and village.name == 'sword':
            village.add_troops(sword=1)
        elif i == 10 and village.name == 'horse':
            village.add_troops(horse=1)


for village in villages:
    print village
