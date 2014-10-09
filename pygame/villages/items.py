class item(object):
    health = 0
    attack = 0
    defend = 0
    price_gold = 0
    price_food = 0
    price_villager = 0
    run_gold = 0
    run_food = 0
    name = ''

    def getType(self):
        return ['item']

class person(item):
    def getType(self):
        result = super(person, self).getType()
        result.append('person')
        return result

class troop(person):
    def getType(self):
        result = super(troop, self).getType()
        result.append('troop')
        return result

class building(item):
    def getType(self):
        result = super(building, self).getType()
        result.append('building')
        return result

class farm(building):
    health = 50
    attack = 0
    defend = 0
    price_gold = 250
    price_food = 0
    price_villager = -10
    run_gold = -5
    run_food = 10
    name = 'farm'

    def getType(self):
        result = super(farm, self).getType()
        result.append('farm')
        return result

class manufacture(building):
    health = 80
    attack = 0
    defend = 2
    price_gold = 500
    price_food = 0
    price_villager = -1
    run_gold = 10
    run_food = 0
    name = 'manufacture'

    def getType(self):
        result = super(manufacture, self).getType()
        result.append('manufacture')
        return result

class villager(person):
    health = 10
    attack = 0
    defend = 1
    price_gold = 10
    price_food = 50
    price_villager = 0
    run_gold = 5
    run_food = -1
    name = 'villager'

    def getType(self):
        result = super(villager, self).getType()
        result.append('villager')
        return result

class spear(troop):
    health = 14
    attack = 4
    defend = 5
    price_gold = 100
    price_food = 0
    price_villager = -2
    run_gold = -10
    run_food = -2
    name = 'spear'

    def getType(self):
        result = super(spear, self).getType()
        result.append('spear')
        return result

class sword(troop):
    health = 18
    attack = 6
    defend = 4
    price_gold = 250
    price_food = 0
    price_villager = -3
    run_gold = -25
    run_food = -3
    name = 'sword'

    def getType(self):
        result = super(sword, self).getType()
        result.append('sword')
        return result

class horse(troop):
    health = 20
    attack = 8
    defend = 2
    price_gold = 500
    price_food = 0
    price_villager = -4
    run_gold = -30
    run_food = -5
    name = 'horse'

    def getType(self):
        result = super(horse, self).getType()
        result.append('horse')
        return result
