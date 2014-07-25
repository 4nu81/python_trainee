#!/usr/bin/python
# -*- coding: utf-8 -*-

def decorator(orig_function):
    def new_func(*args, **kwargs):
        print '\n** decoration starts **\n'
        orig_function(*args,**kwargs)
        print '\n** decoration ends **'
    return new_func

class myClass:

    @decorator #passes write() to decorator
    def write(self, mytext):
        print mytext

if __name__ == '__main__':

    c = myClass()
    c.write('The output has been decorated ')
