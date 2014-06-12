def summe(a, b):
    return a + b

def hoch(a, b):
    if b == 0:
        return 1
    i = 1
    e = a
    while i < b:
        e = e * a
        i = i + 1
    return e

def fak(a):
    if a < 1:
        return "Fehler"
    else:
        if a == 1:
            return a
        else:
            return a * fak(a-1)

def quad(a):
    return hoch(a, 2)
    
def _fibun(a, result=[]):
    if a < 1:
        return 0
    else:
        if a < 3:
            return 1
        else:
            return (_fibun(a-1, result) + _fibun(a-2, result))

def fibun(a):
    result = []
    for i in range(a):
        result.append(_fibun(i))
    return result

d = 15
print '%d^2 = %d'%(d,quad(d))
print '%d! = %s'%(d,str(fak(d)))
print 'fibunacci(%d) = %s'%(d, str(fibun(d)))

