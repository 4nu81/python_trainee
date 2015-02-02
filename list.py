d = {'a':1,'b':2,'c':3,}

print 'check for a key in dict'
print str([name for name in d])
print 'a' in d and d['a']
print ','.join([str(d[s]) for s in d if s == 'a'])
print ''
print 'check for items in iterables'
nmbrs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print 'nmbrs = ', nmbrs
print '[nr for nr in nmbrs if nr%2 == 0]'
print [nr for nr in nmbrs if nr%2 == 0]
print '[nr for nr in nmbrs if nr%5 == 0]'
print [nr for nr in nmbrs if nr%5 == 0]
print ''
negative_numbers = [num for num in nmbrs if num < 0]
print bool(negative_numbers)
print ''
def append_t(var=None):
    if var is None:
        var = []
    var.append('t')
    return var


def append_s(l=[]):
    l.append('s')
    return l

print append_s()
print append_s()
print append_s()

print append_t()
print append_t()
print append_t()

print "reverse Strings:"
print nmbrs # 1,2,3,4,...,19,20
print nmbrs[::-1] # 20,19,18,...,1,0
