import math


class term:
    """
    Term base class
    """
    def value(self):
        raise Exception('You called an abstract method','Please inherid from term to implement your own version')

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
    def __init__(self, left, right):
        """
        constructor
        @param left: the left operator
        @param right: the right operator
        """
        if isinstance(left, term) and isinstance(right, term):
            self.left = left
            self.right = right
        else:
            raise Exception('Invalid Argument', '')

class add_term(lr_term):
    def value(self):
        """
        Add the left to the right term
        """
        return self.left.value() + self.right.value()

class sub_term(lr_term):
    def value(self):
        """
        returns value of the left minus the right
        """
        return self.left.value() - self.right.value()

class multi_term(lr_term):
    def value(self):
        """
        returns value of the left term times the right
        """
        return self.left.value() * self.right.value()

class div_term(lr_term):
    def value(self):
        """
        returns the value of the left term divided by the right
        """
        return self.left.value() / self.right.value()

class exp_term(lr_term):
    def value(self):
        """
        returns the value of the left term exponent the right
        """
        return self.left.value() ** self.right.value()

class r_term(term):
    """
    This is a base class for all operations only using one operator
    """
    def __init__(self, operand):
        if isinstance(operand, term):
            self.operand = operand
        else:
            raise Exception('Invalid Argument', '')

class sqrt_term(r_term):
    def value(self):
        return self.operand.value() ** 0.5

class sin_term(r_term):
    def value(self):
        print self.operand.value()
        return math.sin(self.operand.value())

class asin_term(r_term):
    def value(self):
        return math.asin(self.operand.value())

class cos_term(r_term):
    def value(self):
        return math.cos(self.operand.value())

class acos_term(r_term):
    def value(self):
        return math.acos(self.operand.value())

class tan_term(r_term):
    def value(self):
        return math.tan(self.operand.value())

class atan_term(r_term):
    def value(self):
        return math.atan(self.operand.value())

################## The Calculations Model ##################

class calc_model:
    """
    calc_model is the modelclass for the calculator.
    It knows how to build the term-tree from the input-stack
    and defines the valid operators. Here happens all the magic.

    Here additional functions can be added and included in the programs logic
    without altering the view.
    """

    _valid_operators = ['+','-','/','*','**','sqrt','(',')','sin','cos','tan','asin','acos','atan']

    def calc_term(self,terms):
        """
        Returns the result build up from the term-stack
        
        @Param terms: This param needs a list with the input to the calculator.
        example: ['2','*','10','**','5','+','sqrt','9']
        result : 200003.0
        """
        term = self.parse_term(terms)
        return term.value()

    def check_brackets(self,terms):
        chk = 0
        exist = False
        for item in terms:
            if item == '(':
                chk += 1
                exist = True
            elif item == ')':
                chk -= 1
            if chk < 0:
                raise Exception('Syntaxfehler','Oeffnende Klammer(n) nicht gefunden.')
        if chk > 0:
            raise Exception('Syntaxfehler','Schliessende Klammer(n) nicht gefunden.')
        return exist

    def find_closing(self, terms, start):
        i = 0
        c = 0
        for i in range(len(terms)):
            item = terms[i]
            if item == '(':
                c += 1
            elif item == ')':
                c -= 1
                if c == 0:
                    return i

    def build_lr_term(self, char, terms, _class):
        i = terms.index(char)
        left = self.parse_term(terms[:i])
        right = self.parse_term(terms[i+1:])
        return _class(left, right)

    def build_r_term(self, char, terms, _class):
        i = terms.index(char)
        operand = self.parse_term(terms[i+1:])
        return _class(operand)

    def solve_brackets(self, terms)
        while self.check_brackets(terms):
            start = terms.index('(')
            end = self.find_closing(terms, start)
            val = self.calc_term(terms[start+1:end])
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
        terms = self.solve_brackets(terms)
        # if terms has only size 1 there must be a value
        if len(terms) == 1:
            return val_term(terms[0])
        # Operartionen mit 2 Operatoren
        elif '+' in terms:
            return self.build_lr_term('+', terms, add_term)
        elif '-' in terms:
            return self.build_lr_term('-', terms, sub_term)
        elif '*' in terms:
            return self.build_lr_term('*', terms, multi_term)
        elif '/' in terms:
            return self.build_lr_term('/', terms, div_term)
        elif '**' in terms:
            return self.build_lr_term('**', terms, exp_term)
        # Operartionen mit 1 Operator
        elif 'sqrt' in terms:
            return self.build_r_term('sqrt', terms, sqrt_term)
        elif 'sin' in terms:
            return self.build_r_term('sin', terms, sin_term)
        elif 'cos' in terms:
            return self.build_r_term('cos', terms, cos_term)
        elif 'tan' in terms:
            return self.build_r_term('tan', terms, tan_term)
        elif 'asin' in terms:
            return self.build_r_term('asin', terms, asin_term)
        elif 'acos' in terms:
            return self.build_r_term('acos', terms, acos_term)
        elif 'atan' in terms:
            return self.build_r_term('atan', terms, atan_term)
