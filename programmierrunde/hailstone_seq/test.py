from hailstone import hailstone, hailstoneRecursive
import unittest

class TestHailStone(unittest.TestCase):
    def test_1(self):
        h = hailstone(1)
        hr = hailstoneRecursive(1)
        assert h == hr
        assert h == [1], "False result with 1. Expected [1]. Result %s" % str(h)

    def test_7(self):
        h = hailstone(7)
        hr = hailstoneRecursive(7)
        assert h == hr
        assert h == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], "False result with 7. Expected [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]. Result %s" % str(h)

    def test_0(self):
        h = hailstone(0)
        hr = hailstoneRecursive(0)
        assert h == hr
        assert h == [], "False result with 0. Expected []. Result %s" % str(h)

    def test_1_neg(self):
        h = hailstone(-1)
        hr = hailstoneRecursive(-1)
        assert h == hr
        assert h == [], "False result with -1. Expected []. Result %s" % str(h)

    def test_27(self):
        h = hailstone(27)
        hr = hailstoneRecursive(27)
        assert h == hr
        # element count
        assert len(h)==112
        # first 4 elements
        assert h[:4]==[27, 82, 41, 124]
        # last 4 elements
        assert h[-4:]==[8, 4, 2, 1]

if __name__ == "__main__":
    unittest.main()