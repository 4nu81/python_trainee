import random, sys

class Mastermind:

    def __init__(self, slots=4, numbers=6):
        self.game = []
        self.slots = slots
        self.colors_game = {}
        for i in range(slots):
            self.game.append(random.randint(1, numbers))
        for i in range(numbers):
            self.colors_game[i + 1] = 0
        for i in self.game:
            self.colors_game[i] += 1

    def check(self, check):
        correct = 0
        colors = self.slots
        colors_check = {}

        for i in self.colors_game:
            colors_check[i] = 0
        for i,v in enumerate(check):
            if v == self.game[i]:
                correct += 1

        try:
            for i in check:
                colors_check[i] += 1
        except KeyError, e:
            return {'msg':'Falscher Zahlenraum'}

        for color in self.colors_game:
            # fuer jede Farbe, die nicht oder zu wenig geraten wurde,
            # wird vom colors counter 1 abgezogen.
            # wenn 'game - check' negativ wird, wird die Farbe an anderer
            # Stelle fehlen und wir koennen das ignorieren ( 0 abziehen )
            colors -= max( self.colors_game[color] - colors_check[color], 0)

        return {'correct':correct, 'colors':colors - correct}


# der Spieltest:

def play(slots=4, numbers = 6, rounds=12):
    mm = Mastermind(slots, numbers)
    win = False
    i = 0

    while i < rounds:
    #for i in range(rounds):
        leg = []
        for slot in range(slots):
            leg.append(input('Slot {i}: '.format(i = slot + 1)))
        r = mm.check(leg)

        if 'msg' in r:
            print r['msg']
        else:
            i += 1
            print "Richtige Nummern: ", r['colors']
            print "Richtig geraten: ", r['correct']
            if r['correct'] == slots:
                print 'Gewonnen'
                win = True
                break
    if not win:
        print 'Verloren'

if __name__ == '__main__':
    play()
