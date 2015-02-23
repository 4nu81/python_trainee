#! /usr/bin/python

class ValidationError(Exception):
    pass

class tree:
    def __init__(self, num, char):
        if not type(num) == int:
            raise ValidationError('{num} is not an integer'.format(num=num))
        if (not type(char) == str):
            raise ValidationError('{char} is not of type str'.format(char=char))
        if len(char) != 1:
            raise ValidationError('{char} is not a single character'.format(char=char))
        self.tree = []
        for i in range(num):
            self.tree.append(' ' * (num - i - 1) + char * (1 + 2 * i))
        self.tree.append(' ' * (num - 1) + char)

    def print_me(self):
        for row in self.tree:
            print row


import unittest
from test import test_support

class TestTreeInit(unittest.TestCase):
    def test_tree_init_1x(self):
        tree(num=1, char='x')
    def test_tree_init_3x(self):
        tree(3,'x')
    def test_tree_init_4o(self):
        tree(4,char='o')

# unittest
class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree_4x = tree(4, 'x').tree
        self.tree_1o = tree(1, 'o').tree
        self.test_1o = ['o','o',]
        self.test_4x = [' '*3 + 'x',' '*2 + 'xxx',' ' + 'xxxxx','xxxxxxx',' '*3 + 'x',]

    def test_tree_num_validation(self):
        try:
            a = tree(num='a', char='x')
        except ValidationError:
            pass
        else:
            assert False, "Number Validation doesn't work"

    def test_tree_char_len_validation(self):
        try:
            a = tree(num=2, char='xx')
        except ValidationError:
            pass
        except:
            raise
        else:
            assert False, "Char Length Validation doesn't work"

    def test_tree_char_type_validation(self):
        try:
            a = tree(num=2, char=1)
        except ValidationError:
            pass
        except:
            raise
        else:
            assert False, "Char Type Validation doesn't work"

    def test_tree_len(self):
        assert len(self.tree_4x) == 5, 'Error, wrong length'
        assert len(self.tree_1o) == 2, 'Error, wrong length'

    def test_tree_content(self):
        for i in range(len(self.test_4x)):
            assert self.test_4x[i] == self.tree_4x[i], 'Error, wrong items'
        for i in range(len(self.test_1o)):
            assert self.test_1o[i] == self.tree_1o[i], 'Error, wrong items'

def test_main():
    test_support.run_unittest(TestTreeInit)
    test_support.run_unittest(TestTree)

import sys

if __name__=='__main__':

    if 'test' in sys.argv:
        test_main()
    else:
        num = 5
        char = 'x'
        for item in sys.argv:
            try:
                num = int(item)
                item = False
            except:
                pass
            if type(item) == str and len(item) == 1:
                char = item
        a = tree(num, char)
        a.print_me()
