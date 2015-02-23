import thread
import time
 

try:
    from msvcrt import getch
except ImportError:
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class keyin:

    def __init__(self):
        self.char = getch()
        #thread.start_new_thread(self._key, ())

    def key(self, char):
        print 'key:', char

    def _key(self):
        while True:
            self.char = getch()
            if self.char is not None:
                self.key(self.char)
                self.char = None
            time.sleep(0.1)
