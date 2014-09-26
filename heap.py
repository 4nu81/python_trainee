from heapq import *

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h,value)
    return [heappop(h) for i in range(len(h))]


l = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
s = heapsort(l)

print l
print s

h = []
heappush( h, (5, 'write code'))
heappush( h, (7, 'release product'))
heappush( h, (1, 'write spec'))
heappush( h, (3, 'create test'))
print h
