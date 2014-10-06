def walktrough(n):
    a = 0
    for item in n:
        a += item

import timeit
def test(z):
    m = range(z)
    t = timeit.timeit('walktrough(m)', setup="from __main__ import walktrough; m={m}".format(m=m), number=1)
    print t

for i in range(7):
    test(10**i)
