class toTest:
    def fizzbuzz(self, nbr):
        result = ''
        if nbr % 3 == 0:
            result += 'fizz'
        if nbr % 5 == 0:
            result += 'buzz'
        if not result:
            return str(nbr)
        else:
            return result

import unittest
from test import test_support

class MyTestCase1(unittest.TestCase):
    def test_feature_a(self):
        t = toTest()
        assert t.fizzbuzz(3) == 'fizz', '3 Fehler'

    def test_feature_b(self):
        t = toTest()
        assert t.fizzbuzz(5) == 'buzz', '5 Fehler'

    def test_feature_c(self):
        t = toTest()
        assert t.fizzbuzz(15) == 'fizzbuzz', '15 Fehler'



def test_main():
    test_support.run_unittest(MyTestCase1)

if __name__ == '__main__':
    test_main()

#l = []
#for i in range(30):
#    l.append(toTest.fizzbuzz(i))
#print l
