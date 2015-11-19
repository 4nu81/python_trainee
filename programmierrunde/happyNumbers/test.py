from happyNumber import isHappy
import unittest


class TestUnit(unittest.TestCase):

    def test_10(self):
        val = isHappy(10)
        assert val == True

    def test_444(self):
        val = isHappy(444)
        assert val == False

if __name__ == "__main__":
    unittest.main()