def contains(haystack, needle):
    """
    ermittelt ob die Ziffer needle in haystack enthalten ist.
    """
    while haystack > 0:
        if haystack%10 == needle:
            return True
        # haystack /= 10
        haystack = haystack / 10
    return False

import time, sys

def fizz(max):
    t1 = time.clock()
    print t1
    for i in range(1, max+1):
        if i%3 == 0 and i%5 == 0:
            print 'fizzbuzz'
        elif i%3 == 0 or contains(needle=3, haystack=i): #'3' in str(i):
            print 'fizz'
        elif i%5 == 0 or contains(i, 5):
            print 'buzz'
        else:
            print str(i)
    print time.clock() - t1


fizz(int(sys.argv[1]))
