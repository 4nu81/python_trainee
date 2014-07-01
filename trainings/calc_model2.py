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

class sin_term(r_term):
    char = 'sin'
    def value(self):
        print self.operand.value()
        return math.sin(self.operand.value())

class asin_term(r_term):
    char = 'asin'
    def value(self):
        return math.asin(self.operand.value())

class cos_term(r_term):
    char = 'cos'
    def value(self):
        return math.cos(self.operand.value())

class acos_term(r_term):
    char = 'acos'
    def value(self):
        return math.acos(self.operand.value())

class tan_term(r_term):
    char = 'tan'
    def value(self):
        return math.tan(self.operand.value())

class atan_term(r_term):
    char = 'atan'
    def value(self):
        return math.atan(self.operand.value())

class log_term(r_term):
    char = 'log'
    def value(self):
        return math.log(self.operand.value())

class rad_term(r_term):
    char = 'rad'
    def value(self):
        return math.radians(self.operand.value())

class deg_term(r_term):
    char = 'deg'
    def value(self):
        return math.degrees(self.operand.value())

################## The Calculations Model ##################

# List is unfortunately necessary while dicts are not sorted
# as they are written in source
_valid_operators = ['(',')','+','-','/','*','**','sqrt','sin','cos','tan','asin','acos','atan','rad','deg','log']

_valid_operators_d = {
    # 'operational_char' : term_class,
    '(': None,
    ')': None,
    '+': add_term,
    '-': sub_term,
    '/': div_term,
    '*': multi_term,
    '**': exp_term,

    'sqrt': sqrt_term,
    'sin': sin_term,
    'cos': cos_term,
    'tan': tan_term,
    'asin': asin_term,
    'acos': acos_term,
    'atan': atan_term,
    'rad': rad_term,
    'deg': deg_term,
    'log': log_term,
}

special_chars = {
    'pi': math.pi,
    'e':math.e
}

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

    def _check_brackets(self,terms):
        """
        Checks for brackets in 'terms' and tests if there are missing opening or closing ones.
        returns False if no brackets are found
        returns True if brackets are found 
        """
        chk = 0
        exist = False
        for item in terms:
            if item == '(':
                chk += 1
                exist = True
            elif item == ')':
                chk -= 1
            if chk < 0:
                raise Exception('Syntaxfehler','Öffnende Klammer(n) nicht gefunden.')
        if chk > 0:
            raise Exception('Syntaxfehler','Schliessende Klammer(n) nicht gefunden.')
        return exist

    def _find_closing_bracket(self, terms, start):
        i = c = 0
        for i in range(len(terms)):
            item = terms[i]
            if item == '(':
                c += 1
            elif item == ')':
                c -= 1
                if c == 0:
                    return i

    def _solve_brackets(self, terms):
        """
        solves all brackets and replaces them by their values
        """
        while self._check_brackets(terms): # solve all terms inbetween brackets
            start = terms.index('(') # opening bracket
            end = self._find_closing_bracket(terms, start) # closing bracket related to start
            val = self.calc_term(terms[start+1:end]) # Value of term inbetween brackets
            # replace term in bracket by its value.
            new = terms[:start]
            new.append(val)
            new.extend(terms[end+1:])
            terms = new
        return terms

    def parse_term(self,terms):
        """
        Here the order of operations is beeing defined. Low priority has to be
        prior to high.
        e.g. to do multiplications after addition.
        """
        # at first the brackets need to be solved
        terms = self._solve_brackets(terms)
        # if terms has only size 1 there must be a value
        if len(terms) == 1:
            return val_term(terms[0])

        for item in _valid_operators:
            if item in terms:
                return _valid_operators_d[item](terms, self)

