alist = {
    'name' : 'Max',
    'schule' : 'Saengerstadt',
}

for element in alist:
    key = element
    value = alist [ element ]
    print "{key} : {value}".format (key = key, value = value)

def add(a,b):
    c = a+b
    return c

print add(1,5)
