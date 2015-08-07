from _functools import partial

def greet(greeting, target):
    return '%s! %s' % (greeting, target)

greets = partial(greet, 'bob')
greets2 = partial(greet, target='bob')

print greets('hallo')
print greets2('hallo')