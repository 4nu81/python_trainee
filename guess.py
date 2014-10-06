import os, sys, random

class game:
    def clear(self):
        os.system(self.clear_str)
    
    def __init__(self, clear_str):
        self.number = random.randint(0, 9)
        self.clear_str = clear_str

    def call(self):
        trys = 0
        while True:
            print('Hello Buddy')
            guess = int(input('Guess the Number: '))
            trys += 1
            if guess == self.number:
                print('Well Done, you are right. You needed {count} attempts.'.format(count=trys))
                return 0
            elif trys >= 6:
                self.clear()
                print('You failed')
                return 0
            else:
                self.clear()
                val = guess < self.number and 'bigger' or 'smaller'
                print('Try again, number is {val} than {guess}'.format(val=val, guess=guess))


if __name__ == '__main__':
    if os.name == 'nt':
        g=game('cls')
    else:
        g = game('clear')
    sys.exit(g.call())
