__author__ = 'am'

from collections import namedtuple

Color = namedtuple('Color', ['hue', 'saturation', 'luminosity'])

p = Color(170, 0.1, 0.6)
if p.saturation >= 0.5:
    print 'Whew, that is bright!'
if p.luminosity >= 0.5:
    print 'Wow, that is light'


class myClass(object):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        print value

    def __repr__(self):
        return self._name

    def __enter__(self):
        #set Up
        self._name = 'Name'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #tear down
        self._name = None
        print 'tear down'
        return True

with myClass() as mc:
    print mc
    mc.name = 'Mein Name'
    print mc.name