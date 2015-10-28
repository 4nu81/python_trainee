from hailstone import hailstone
import unittest

class TestHailStone(unittest.TestCase):
    def test_1(self):
        assert hailstone(1) == [1], "False result with 1"

    def test_7(self):
        assert hailstone(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], "False result with 7"

    def test_0(self):
        assert hailstone(0) == [], "False result with 0"

    def test_1_neg(self):
        assert hailstone(-1) == [], "False result with -1"

if __name__ == "__main__":
    unittest.main()