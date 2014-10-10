class Space:
    def __init__(self):
        self.ships = []

    def combat(self, attacker, defender):
        atk = attacker
        dfd = defender
        while True:
            dmg = atk.getAttack()
            if dmg > 0:
                print "{attacker} attacks {defender} with {damage} damage".format(
                    attacker=atk.name,
                    defender=dfd.name,
                    damage = dmg,
                )
                dfd.getDamage(dmg)
                if not dfd.getAlive():
                    print "{name} has been destroyed".format(name=dfd.name)
                    return True
            (atk, dfd) = (dfd, atk)
