import os, sys

system = 'linux'


def is_number(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

class calc:
    def __init__(self, clear):
        self.clear_term = clear
        self._stack = []

    def clear(self):
        os.system(self.clear_term)

    def calc(self):
        pass

    def proceed(self, term):
        if is_number(term):
            self._stack.append(term)
        else:
            self._stack.append('({term})'.format(term=term)

    def run(self):
        while True:
            print 'Hello Buddy'
            print 'Enter your function:'
            print ' '.join(self._stack)
            term = raw_input('$ : ')
            if term == 'exit':
                return 0
            elif term == 'clear':
                self._stack = []
                self.clear()
            elif term == '=':
                self.clear()
                print '{term} = {result}'.format(term=' '.join(self._stack), result=self.calc())
                self._stack = []
                print ''
                print ''
            else:
                self.proceed(term)
                self.clear()

if __name__ == '__main__':
    clear = ''
    if os.name == "nt":
        clear = 'cls'
    else:
        clear = 'clear'
    os.system(clear)
    c = calc(clear)
    sys.exit(c.run())
