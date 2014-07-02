#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
import calc_model2 as calc_model
from calc_model2 import calc_model as model

_no_mem_values = ['save', 'exit', 'help', 'clear', 'del', 'res', 'mem']

class bcolors:
    """
    Defines Colors for output on terminal
    """
    RESULT = '\033[92m'
    CHARS = '\033[91m'
    WELCOME = '\033[93m'
    OPERATORS = '\033[96m'
    DEFAULT = '\033[0m'

help_text = """

    ****************************
    * {WELCOME}ConsoleCalc by am@rcs.de{DEFAULT} *
    ****************************

    Howto:

    type each element of your term seperated by pressing enter

    special characters:
        {OPERATORS}{chars}{DEFAULT}
    known operations:
        {OPERATORS}{operations}{DEFAULT}
    type {RESULT}'='{DEFAULT} to calculate the result

    type {RESULT}'help'{DEFAULT} for this help
    type {RESULT}'res'{DEFAULT} for using last result
    type {RESULT}'save'{DEFAULT} to save last result to a key of your choice exept:
        * {OPERATORS}numbers{DEFAULT}
        * {OPERATORS}{operations}{DEFAULT}
        * {OPERATORS}{no_mem_vals}{DEFAULT}
    type {RESULT}'mem'{DEFAULT} to show the memory
    type {RESULT}'del'{DEFAULT} to delete last term element
    type {RESULT}'clear'{DEFAULT} for deleting buffers
    type {RESULT}'exit'{DEFAULT} to exit program
""".format(
        chars=', '.join(calc_model.special_chars),
        operations=', '.join(calc_model._valid_operators),
        no_mem_vals=', '.join(_no_mem_values),
        WELCOME=bcolors.WELCOME,
        DEFAULT=bcolors.DEFAULT,
        OPERATORS=bcolors.OPERATORS,
        RESULT=bcolors.CHARS
    )


def welcome(s, clear):
    """
    This will be called on programs startup and is a kind of intro
    """
    os.system(clear)
    print help_text
    time.sleep(s)

def is_number(s):
    """
    Checks if s can be converted to a number
    """
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

def is_valid_operator(s):
    """
    Checks if s is a valid operator
    """
    if s in calc_model._valid_operators:
        return True
    return False

class Calculator:
    """
    The Calculators Main Class
    """

    def __init__(self, clear):
        """
        Constructor initializez the Calculator
        
        param 'clear': defines the phrase needet to clear the screen. ('cls' in windows; 'clear' in others)
        """
        self.clear_term = clear
        self._stack = []
        self._res = None
        self._model = model()

    def clear(self):
        """
        Clears the console screen using the clear_term of Calculator
        """
        os.system(self.clear_term)

    def calc(self):
        """
        Calculates the term and returns the calculated value and True if the
        calculation was successful
        """

        try:
            return self._model.calc_term(self._stack[:]), True
        except SyntaxError:
            return 'SyntaxError', False
        except ZeroDivisionError:
            return 'Zero Division Error', False
        except Exception as e:
            msg, txt = e.args
            if txt:
                return '{msg} - {txt}'.format(msg=msg, txt=txt), False
            else:
                return '{msg}'.format(msg=msg), False

    def proceed(self, item):
        """
        Checks if entered Value is a Number or valid Operator. If not it checks if there is a
        key in memory to return the corresponding value.

        param 'item': string to be checked
        """
        if is_number(item):
            self._stack.append(item)
        elif is_valid_operator(item):
            self._stack.append('{item}'.format(item=item))
        elif item in self._model._mem:
            self._stack.append('{item}'.format(item=item))
        elif item in calc_model.special_chars:
            self._stack.append(item)
        else:
            pass

    def _clear(self):
        """
        reinitializez the Calculator
        """
        self._stack = []
        self._res = None
        self._model._mem = {}
        self.clear()

    def _del(self):
        """
        removes last item from entered term
        """
        if len(self._stack) >= 1:
            self._stack = self._stack[:-1]
        self.clear()

    def _result(self):
        """
        adds the last result to the term
        """
        s = str(self._res)
        if is_number(s):
            self.proceed(s)
        self.clear()

    def _equals(self):
        """
        prints the result of the entered term
        if calculation was successful the stack will be cleared
        """
        self.clear()
        self._res, del_stack = self.calc()
        if del_stack:
            color = bcolors.RESULT
        else:
            color = bcolors.CHARS
        print ''
        print '    {term} = {green}{result}{cdefault}'.format(
            term=' '.join(self._stack),
            green=color,
            result=self._res,
            cdefault=bcolors.DEFAULT
        )
        if del_stack:
            self._stack = []
        print ''

    def _help(self):
        """
        shows the helpmessage
        """
        self.clear()
        print help_text

    def _add(self, item):
        """
        attemps to add the entered item to the term
        """
        self.proceed(item)
        self.clear()

    def _memory(self, key):
        """
        saves last result to the memory using key
        
        param 'key': key where res is saved as value
        """
        self._model._mem[key] = self._res
        self.clear()

    def _print_mem(self):
        """
        prints the memory to the terminal
        """
        self.clear()
        if self._model._mem:
            print '    Memory:'
            for k, v in sorted(self._model._mem.items()):
                print '      {key} = {mem}'.format(key=k, mem=str(v))
            print ''

    def _save(self):
        """
        routine to save the last result to the memory. here we try to find a valid key to save to.
        """
        if self._res:
            not_done = True
            s = '    Enter a name to save to (exit to cancel) : '
            while not_done:
                nr = raw_input(s)
                if nr == 'exit':
                    break
                if not is_number(nr) \
                    and not is_valid_operator(nr) \
                    and not nr in _no_mem_values \
                    and not nr in calc_model.special_chars:
                    self._memory(nr)
                    not_done = False
                else:
                    print '        {o_color}{nr} is an invalid save name.{default}'.format(nr=nr, o_color=bcolors.CHARS, default=bcolors.DEFAULT)
                    s = '    Enter another name to save to (exit to cancel): '
        self.clear()

    def _shutdown(self):
        """
        closes the Calculator and exits the program
        """
        self._clear()
        sys.exit(0)

    def proceed_input(self, value):
        """
        This method defines how to proceed the input
        """
        if value == 'exit':
            self._shutdown()
        elif value == 'clear':
            self._clear()
        elif value == 'del':
            self._del()
        elif value == 'res':
            self._result()
        elif value == '=':
            self._equals()
        elif value == 'help':
            self._help()
        elif value == 'save':
            self._save()
        elif value == 'mem':
            self._print_mem()
        else:
            self._add(value)

    def run(self):
        """
        The Main procedure of the Calculator. If this loop ends the program will exit
        """
        while True:
            #self._print_mem()
            print '  Enter your term:'
            print '    term : {term}'.format(term=' '.join(self._stack))
            value = raw_input('  $ : ')
            self.proceed_input(value)


if __name__ == '__main__':
    """
    The main method of the program
    """
    clear = ''
    if os.name == "nt":
        clear = 'cls'
    else:
        clear = 'clear'
    welcome(0, clear)
    c = Calculator(clear)
    sys.exit(c.run())
