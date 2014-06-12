class test():
    _name = 'Hi, I am a class'
    
    def test(self):
        return 'Hi, I am a method'

MAP = {
    None     : 'Hi, I am the none-object',
    test     : test()._name,
    test.test : test().test(),
}

MAP.update({
    'str'    : 'Hi, I am a String',
    1        : 'Hi, I am an int',
    1.4      : 'Hi, I am a float',
})

Nn = None

print('\n### keys ###\n')
for key in MAP.keys():
    print(key)
print('\n### values ###\n')
print(MAP[test.test])
print(MAP[test])
print(MAP[1.4])
print(MAP[1])
print(MAP['str'])
print(MAP[None])
print(MAP[Nn])
