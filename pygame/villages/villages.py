from items import *

class village:
    def __init__(self, name, gold=1000, food=200):
        self.year = 1
        self.name = name
        self.gold = 2000
        self.food = 2000
        self.gold_balance = 0
        self.food_balance = 0
        self.items = []
        self.add_item(villager, 15)
        self.add_item(farm)
        self.gold = gold
        self.food = food

    def tick(self):

        self.year += 1

        self.gold += self.gold_balance
        self.food += self.food_balance

    def add_item(self, item, count=1):
        if count <= 0:
            return False
        price_gold = item.price_gold * count
        price_food = item.price_food * count
        price_villager = item.price_villager * count * -1

        if price_gold <= self.gold and price_food <= self.food and price_villager <= self.count('villager'):
            for i in range(count):
                self.items.append(item())
            self.gold_balance += item.run_gold * count
            self.food_balance += item.run_food * count
            self.gold -= price_gold
            self.food -= price_food

            self._remove(obj_name='villager', count=price_villager)
            return True
        else:
            return False

    def _remove(self, obj_name, count=1):
        to_rem = []
        if count <= 0:
            return False
        for item in self.items:
            if obj_name in item.getType():
                count -= 1
                to_rem.append(item)
                if count == 0:
                    break
        for item in to_rem:
            self.items.remove(item)
            self.food_balance -= item.run_food
            self.gold_balance -= item.run_gold
        return False

    def count(self, obj_name):
        i = 0
        for item in self.items:
            if obj_name in item.getType():
                i += 1
        return i

    def status(self):
        while self.food < 0:
            if self.count('person') > 0:
                self.remove('person')
                self.food += 1
            else:
                return False
        if self.gold < 0:
            return False
        return True

    def defend(self, troop):
        pass

    def __str__(self):
        buildings = []
        for item in self.items:
            if 'building' in item.getType():
                buildings.append(item.name)
        return """{name}
    year          {year}
    gold          {gold}
    food          {food}
    spear         {spear}
    sword         {sword}
    horse         {horse}
    villagers     {vill}
    buildings     {buildings}
    balance food  {bf}
    balance gold  {bg}
            """.format(
            name=self.name,
            year=self.year,
            gold=self.gold,
            food=self.food,
            vill=self.count('villager'),
            spear=self.count('spear'),
            sword=self.count('sword'),
            horse=self.count('horse'),
            buildings=', '.join(buildings),
            bf = self.food_balance,
            bg = self.gold_balance,
        )
