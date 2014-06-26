
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

################## The Calculations Model ##################

class calc_model:
    """
    calc_model is the modelclass for the calculator.
    It knows how to build the term-tree from the input-stack
    and defines the valid operators. Here happens all the magic.

    Here additional functions can be added and included in the programs logic
    without altering the view.
    """

    _valid_operators = ['+','-','/','*','**','sqrt']

    def calc_term(self,terms):
        """
        Returns the result build up from the term-stack
        
        @Param terms: This param needs a list with the input to the calculator.
        example: ['2','*','10','**','5','+','sqrt','9']
        result : 200003.0
        """
        term = self.parse_term(terms)
        return term.value()

    def parse_term(self,terms):
        """
        Here the order of operations is beeing defined. Low priority has to be
        prior to high.
        e.g. to do multiplications after addition.
        """
        if len(terms) == 1:
            return val_term(terms[0])
        elif '+' in terms:
            i = terms.index('+')
            left = self.parse_term(terms[:i])
            right = self.parse_term(terms[i+1:])
            return add_term(left, right)
        elif '-' in terms:
            i = terms.index('-')
            left = self.parse_term(terms[:i])
            right = self.parse_term(terms[i+1:])
            return sub_term(left, right)
        elif '*' in terms:
            i = terms.index('*')
            left = self.parse_term(terms[:i])
            right = self.parse_term(terms[i+1:])
            return multi_term(left, right)
        elif '/' in terms:
            i = terms.index('/')
            left = self.parse_term(terms[:i])
            right = self.parse_term(terms[i+1:])
            return div_term(left, right)
        elif '**' in terms:
            i = terms.index('**')
            left = self.parse_term(terms[:i])
            right = self.parse_term(terms[i+1:])
            return exp_term(left, right)
        elif len(terms) > 2:
            raise Exception('Invalid Syntax')
        elif 'sqrt' == terms[0]:
            operand = self.parse_term(terms[1])
            return sqrt_term(operand)
