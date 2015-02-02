#! /usr/bin/python

class Ork:
    bloedheit = 5


def p(obj):
    obj.bloedheit = 2
    print obj

o1 = Ork()

print o1
p(o1)

print o1.bloedheit


