import pickle

class first_object:
    def __init__(self):
        self.name = "first object"
    def getName(self):
        return self.name

class second_object(first_object):
    def __init__(self):
        self.name = "second one"


instance1 = first_object()
print instance1.getName()
instance2 = second_object()
print instance2.getName()

target = file("objects.dat", "w")

pickle.dump((instance1, instance2), target)
target.close()
print "serialized..."

del instance1
del instance2
del target

source = file("objects.dat")
data = pickle.load(source)
print "...unserialized"

print data

for obj in data:
    print obj.getName()
