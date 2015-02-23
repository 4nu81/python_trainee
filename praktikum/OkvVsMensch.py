
import random
from Ausgabe import Ausgabe


class Character(object):
    def __init__(self):
        self.name = ""
        self.leben = 0
        self.schaden_max = 0
        self.schaden_min = 0

    def angriff(self):
        return random.randint( self.schaden_min, self.schaden_max )
    
    def isAlive(self):
        return self.leben > 0


class Mensch(Character):
    def __init__(self, name):

        super(Mensch, self).__init__()

        self.name = name
        self.schaden_max = 13
        self.schaden_min = 4
        self.leben = 60


class Ork(Character):
    def __init__(self, name):

        super(Ork, self).__init__()

        self.name = name
        self.schaden_max = 15
        self.schaden_min = 5
        self.leben = 50

def spiel():

    mensch = Mensch('Helmut')
    ork = Ork('Whaaaagh')
    nr = 0
    a = Ausgabe('OrkVsMenschResult.txt')

    while mensch.isAlive() and ork.isAlive():
        nr += 1
        m_att = mensch.angriff()
        o_att = ork.angriff()

        mensch.leben -= o_att
        ork.leben -= m_att

        a.write("\nRunde {nr}".format(nr = nr))
        a.write("\nSchaden {name}: {m_att}".format(m_att = m_att, name = ork.name))
        a.write("\nSchaden {name}: {o_att}\n".format(o_att = o_att, name = mensch.name))

    if not mensch.isAlive():
        a.write("\n{name} hat verloren".format(name = mensch.name))
    if not ork.isAlive():
        a.write("\n{name} hat verloren".format(name = ork.name))
    a.close()

spiel()
