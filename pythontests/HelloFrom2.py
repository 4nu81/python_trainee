import threading, time, sys


class myThread(threading.Thread):
    def __init__(self, name):
        self.threadname = name
        threading.Thread.__init__(self)


    def run(self):
        print("starting Thread")
        startThread(self.threadname)
        

def hello(threadname):
    print("hello, world " + threadname + " is calling")

def startThread(threadname):
    i = 0
    while i < 20:
        i += 1
        hello(threadname)

def main():
    t1 = myThread("Thread1")
    t2 = myThread("Thread2")
    t1.start()
    t2.start()
    while t1.isAlive() or t2.isAlive():
        pass
    return 0

if __name__ == "__main__":
    sys.exit(main())
