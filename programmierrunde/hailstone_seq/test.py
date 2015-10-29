from hailstone import hailstone
import unittest

class TestHailStone(unittest.TestCase):
    def test_1(self):
        assert hailstone(1) == [1], "False result with 1. Expected [1]. Result %s" % str(h)

    def test_7(self):
        assert hailstone(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], "False result with 7. Expected [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]. Result %s" % str(h)

    def test_0(self):
        h = hailstone(0)
        assert h == [], "False result with 0. Expected []. Result %s" % str(h)

    def test_1_neg(self):
        assert hailstone(-1) == [], "False result with -1. Expected []. Result %s" % str(h)

    def test_27(self):
        h = hailstone(27)
        # element count
        assert len(h)==112
        # first 4 elements
        assert h[:4]==[27, 82, 41, 124]
        # last 4 elements
        assert h[-4:]==[8, 4, 2, 1]

if __name__ == "__main__":
    unittest.main()