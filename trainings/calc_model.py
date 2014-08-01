# -*- coding: utf-8 -*-

import math

class term:
    """
    Term base class
    """
    def value(self):
        raise Exception('You called an abstract method','You must inherid from term to implement your term_operation_class')

class val_term(term):
    """
    This class represents an value/operand for other operations
    """
    def __init__(self, val):
        """
        constructor
        @param val: value to be saved in
        """
        self.val = float(val)

    def value(self):
        """
        returns the value represended by the object
        """
        return self.val

class lr_term(term):
    """
    This is a base class for all operations with two operators
    """
    def __init__(self, terms, calc_model_instance):
        """
        constructor
        @param char: the character representing the term
        @param terms: the terms_stack
        @param calc_model_instance: instance of the calc_model class
        """
        i = terms.index(self.char)
        left = calc_model_instance.parse_term(terms[:i])
        right = calc_model_instance.parse_term(terms[i+1:])
        if isinstance(left, term) and isinstance(right, term):
            self.left = left
            self.right = right
        else:
            raise Exception('Invalid Argument', '')

class add_term(lr_term):
    char = '+'
    def value(self):
        """
        Add the left to the right term
        """
        return self.left.value() + self.right.value()

class sub_term(lr_term):
    char = '-'
    def value(self):
        """
        returns value of the left minus the right
        """
        return self.left.value() - self.right.value()

class multi_term(lr_term):
    char = '*'
    def value(self):
        """
        returns value of the left term times the right
        """
        return self.left.value() * self.right.value()

class div_term(lr_term):
    char = '/'
    def value(self):
        """
        returns the value of the left term divided by the right
        """
        return self.left.value() / self.right.value()

class exp_term(lr_term):
    char = '**'
    def value(self):
        """
        returns the value of the left term exponent the right
        """
        return self.left.value() ** self.right.value()

class r_term(term):
    """
    This is a base class for all operations only using one operator
    """
    def __init__(self, terms, calc_model_instance):
        """
        constructor
        @param char: the character representing the term
        @param terms: the terms_stack
        @param calc_model_instance: instance of the calc_model class
        """
        i = terms.index(self.char)
        operand = calc_model_instance.parse_term(terms[i+1:])
        if isinstance(operand, term):
            self.operand = operand
        else:
            raise Exception('Invalid Argument', '')

class sqrt_term(r_term):
    char = 'sqrt'
    def value(self):
        return self.operand.value() ** 0.5

class rt3_term(r_term):
    char = '3rt'
    def value(self):
        return self.operand.value() ** (1.0 / 3.0)

class proz_term(r_term):
    char = '%'
    def value(self):
        return self.operand.value() * 0.01

class rezi_term(r_term):
    char = '1/'
    def value(self):
        return 1.0 / self.operand.value()

# List is unfortunately necessary while dicts are not sorted
# as they are written in source
_valid_operators = ['+','-','/','*','**','sqrt', '%', '1/', '3rt']

_valid_operators_d = {
# 'operational_char' : term_class,
    '+': add_term,
    '-': sub_term,
    '/': div_term,
    '*': multi_term,
    '**': exp_term,
    'sqrt': sqrt_term,
    '%': proz_term,
    '1/': rezi_term,
    '3rt': rt3_term,
}

special_chars = {
    'pi': math.pi,
    'e':math.e
}

################## The Calculations Model ##################

class calc_model:
    """
    calc_model is the modelclass for the calculator.
    It knows how to build the term-tree from the input-stack
    and defines the valid operators. Here happens all the magic.

    Here additional functions can be added and included in the programs logic
    without altering the view.
    """

    def __init__(self):
        self._mem = {}

    def calc_term(self,terms):
        """
        Returns the result build up from the term-stack
        
        @Param terms: This param needs a list with the input to the calculator.
        example: ['2','*','10','**','5','+','sqrt','9']
        result : 200003.0
        """

        for item in self._mem:
            while item in terms:
                i = terms.index(item)
                terms[i] = self._mem[item]

        for item in special_chars:
            while item in terms:
                i = terms.index(item)
                terms[i] = str(special_chars[item])

        term = self.parse_term(terms)
        return term.value()

    def parse_term(self,terms):
        """
        Here the order of operations is beeing defined. Low priority has to be
        prior to high.
        e.g. to do multiplications after addition.
        """
        # if terms has only size 1 there must be a value
        if len(terms) == 1:
            return val_term(terms[0])

        # otherwise it is an operation
        for item in _valid_operators:
            if item in terms:
                return _valid_operators_d[item](terms, self)

