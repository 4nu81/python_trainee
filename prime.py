import time


def get_primes_new(x):
    zahlen = [True]*(x+1)
    zahlen[0] = False
    zahlen[1] = False
    
    i = 2
    while i * i <= x:
        if zahlen[i] == True:
            for k in range(i*i,x+1,i):
                zahlen[k] = False
        i += 1
    l = []
    for i, v in enumerate(zahlen):
        if v:
            l.append(i)
    return l


def is_prime(nr, lst):
    if nr == 0 or nr == 1:
        return False
    for i in lst:
        if nr%i == 0:
            return False
    return True

def get_primes(x):
    lst = []
    for i in range(1, x):
        if is_prime(i,lst):
            lst.append(i)
            
    return lst

def old():

    start = time.time()
    lst = get_primes(250000)
    ende = time.time()
    print ende - start

def new(x):
    start = time.time()
    lst = get_primes_new(x)
    ende = time.time()
    return ende - start

for i in range(9):
    print "10**{i} : {t}".format(i=i, t=new(10**i))
