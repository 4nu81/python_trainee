import time

def quer(zahl):
    res = zahl % 10
    for i in range(6):
        zahl = int(zahl / 10)
        res += zahl % 10 
    return res

class random:
    def __init__(self, seed):
        self.seed = seed

    def randint(self, lo, hi):
        systime = int(time.time()*1000)
        self.seed += systime
        self.seed /= quer(self.seed)
        return self.seed % (hi - lo + 1) + lo

def count():
    hi = 100; lo = 0; r = random(1); lst = {}
    for i in range(101):
        lst[i] = 0
    for i in range(500):
        lst[r.randint(lo,hi)] += 1
    for key in lst:
        print "{key} - {cnt}".format(key=key, cnt=lst[key])

def doit():
    hi = 100; lo = 0; r = random(565218); lst = []
    for i in range(300):
        lst.append(r.randint(lo,hi))
    print '\n'
    print lst
    print '\n'

doit()
count()
