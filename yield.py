"""
Iteraor vs. Generator:

Ein mit dem 'yield-operator' erstelltes Object (uselessGenerator) kann nur
einmal iteriert werden. Der Inhalt wird dabei on-the-fly erstellt und danach
verworfen. Das schont den Speicher. 'yield' wirkt dabei wie das 'return'.

Der Iterator hingegen kann beliebig oft aufgerufen werden. Bsp.: "mylist"

a ** b = a hoch b
"""

def uselessGenerator(size):
    mylist = range(size)
    for i in mylist:
        yield 2 ** i

size = 10

mygenerator = uselessGenerator(size) # create a generator

mylist = range(size)

generator_1 = []
generator_2 = []
iterator_1 = []
iterator_2 = []

# Generatoren:

for i in mygenerator:
    generator_1.append(i)

for i in mygenerator:
    generator_2.append(i)

# Iteratoren:

for i in mylist:
    iterator_1.append(2 ** i)

for i in mylist:
    iterator_2.append(2 ** i)

print('\n\n\n')
print 'generator 1', '=', generator_1
print 'generator 2', '=', generator_2
print 'iterator 1', '=', iterator_1
print 'iterator 2', '=', iterator_2




l = [1,2,3,4,5,6,7,8,9,10]

def gen():
    for item in l:
        yield item

for item in gen():
    print item
