# happy numbers are numbers which sum of the squares of its digits will be 1 after finite repetitions.

import sys

def isHappy(n):
    steps = []
    while True:
        digits = str(n)
        n = sum([int(n)**2 for n in digits])
        if n == 1:
            return True
        elif n in steps:
            return False
        else:
            steps.append(n)

def run(val):
    for i in xrange(val):
        s = 'is Happy' if isHappy(i) else 'is not Happy'
        print i,s

if __name__ == '__main__':
    assert len(sys.argv) == 2
    val = int(sys.argv[1])
    run(val)