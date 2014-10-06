# smthg to test

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

# setup the tests

import unittest
from test import test_support

# define the tests

class MyTestCase1(unittest.TestCase):
    def setUp(self):
        self.t = toTest()

    def test_feature_a(self):
        assert self.t.fizzbuzz(3) == 'fizz', '3 Fehler'

    def test_feature_b(self):
        assert self.t.fizzbuzz(5) == 'buzz', '5 Fehler'

    def test_feature_c(self):
        assert self.t.fizzbuzz(15) == 'fizzbuzz', '15 Fehler'

    def tearDown(self):
        self.t = None

# run the tests

def test_main():
    test_support.run_unittest(MyTestCase1) # bestimmtes Testklasse laufen lassen
    test_support.run_unittest(__name__) # alle Testklassen in diesem Modul laufen lassen

# call the tests

if __name__ == '__main__':
    test_main()
