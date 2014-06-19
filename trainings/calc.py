import os, sys, time


_valid_operators = ['+','-','/','*','**','sqrt']
_no_mem_values = ['save', 'exit', 'help', 'clear', 'del', 'res']

WELCOME = """
Hello, this is your terminal calculator.
Hope you get your things done with me.
"""



def welcome(s, clear):
    w = ''
    os.system(clear)
    for c in WELCOME:
        w += c
        os.system(clear)
        print w
        time.sleep(0.001)
    time.sleep(s)

def is_number(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

def is_valid_operator(s):
    if s in _valid_operators:
        return True
    return False

class bcolors:
    RESULT = '\033[92m'
    DEFAULT = '\033[0m'

class calc:

    def __init__(self, clear):
        self.clear_term = clear
        self._stack = []
        self._mem = {}
        self._res = None
        self._help_text = """
            ConsolCalc by am@rcs.de
            
            Howto:
            
            type each element of your term seperated by pressing enter
            
            allowed operations:
                {operations}
            type '=' to calculate the result

            type 'help' for this help
            type 'res' for using last result
            type 'del' to delete last term element
            type 'clear' for deleting buffers
            type 'exit' to exit program
        """.format(operations=', '.join(_valid_operators))

    def clear(self):
        os.system(self.clear_term)

    def calc(self):
        try:
            return eval(' '.join(self._stack))
        except SyntaxError:
            return 'SyntaxError'
        except ZeroDivisionError:
            return 'Zero Division Error'
        except:
            return 'Error'

    def proceed(self, term):
        if is_number(term):
            self._stack.append(term)
        elif is_valid_operator(term):
            self._stack.append('{term}'.format(term=term))
        elif term in self._mem:
            self._stack.append('{term}'.format(term=self._mem[term]))
        else:
            pass

    def _clear(self):
        self._stack = []
        self._res = None
        self._mem = {}
        self.clear()

    def _del(self):
        if len(self._stack) >= 1:
            self._stack = self._stack[:-1]
        self.clear()

    def _result(self):
        s = str(self._res)
        if is_number(s):
            self.proceed(s)
        self.clear()

    def _equals(self):
        self.clear()
        self._res = self.calc()
        print '{term} = {green}{result}{cdefault}'.format(term=' '.join(self._stack), green=bcolors.RESULT, result=self._res, cdefault=bcolors.DEFAULT)
        self._stack = []
        print ''

    def _help(self):
        self.clear()
        print self._help_text

    def _add(self):
        self.proceed(self.term)
        self.clear()

    def _memory(self, i):
        self._mem[i] = self._res
        self.clear()

    def _print_mem(self):
        if self._mem:
            print 'Memory:'
            for key in self._mem:
                print '{key} = {mem}'.format(key=key, mem=str(self._mem[key]))
            print ''

    def _save(self):
        not_done = True
        s = 'Give a name to save to : '
        while not_done:
            nr = raw_input(s)
            if not is_number(nr) and not is_valid_operator(nr) and not nr in _no_mem_values:
                self._memory(nr)
                not_done = False
            else:
                print '{nr} is an invalid save name.'.format(nr=nr)
                s = 'Give another name to save to : '

    def run(self):
        while True:
            self._print_mem()
            print 'Enter your term:'
            print 'term : {term}'.format(term=' '.join(self._stack))
            self.term = raw_input('$ : ')

            if self.term == 'exit':
                return 0
            elif self.term == 'clear':
                self._clear()
            elif self.term == 'del':
                self._del()
            elif self.term == 'res':
                self._result()
            elif self.term == '=':
                self._equals()
            elif self.term == 'help':
                self._help()
            elif self.term == ('save'):
                self._save()
            else:
                self._add()

if __name__ == '__main__':
    clear = ''
    if os.name == "nt":
        clear = 'cls'
    else:
        clear = 'clear'
    #welcome(2, clear)
    os.system(clear)
    c = calc(clear)
    sys.exit(c.run())
