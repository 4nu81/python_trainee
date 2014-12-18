#! /usr/bin/python
# -*- coding: utf-8 -*-

from dijkstra import *
import sys

knoten = [
    'Frankfurt',
    'Manheim',
    'Würzburg',
    'Stuttgart',
    'Kassel',
    'Karlsruhe',
    'Erfurt',
    'Nürnberg',
    'Augsburg',
    'München',
]

verbindungen = [
    ('Frankfurt', 'Manheim', 85),
    ('Frankfurt', 'Kassel', 173),
    ('Frankfurt', 'Würzburg', 217),
    ('Mannheim', 'Karlsruhe', 80),
    ('Würzburg', 'Erfurt', 186),
    ('Würzburg', 'Nürnberg', 103),
    ('Kassel', 'München', 502),
    ('Karlsruhe', 'Augsburg', 250),
    ('Nürnberg', 'Stuttgart', 183),
    ('Nürnberg', 'München', 167),
    ('Augsburg', 'München', 84),
]

class Netz:
    def __init__(self):
        self.knoten = []
        self.verbindungen = []

    def find_knot(self, name):
        for knot in self.knoten:
            if knot.name == name:
                return knot

    def read(self):
        for name in knoten:
            self.knoten.append(Knoten(name))

        for item in verbindungen:
            start = self.find_knot(item[0])
            end = self.find_knot(item[1])
            dist = item[2]
            if start and end:
                self.verbindungen.append(Verbindung(start = start, ende = end, wichtung = dist))
                self.verbindungen.append(Verbindung(start = end, ende = start, wichtung = dist))

        self.graph = Graph(self.knoten, self.verbindungen)

    def get_route(self, start_name, end_name):
        start = self.find_knot(start_name)
        ende = self.find_knot(end_name)
        return Logik.trace(self.graph, start, ende)

if __name__ == '__main__':
    n = Netz()
    n.read()

    routes = [
        ('Frankfurt', 'München'),
        ('München', 'Frankfurt'),
        ('Erfurt','Kassel'),
        ('Augsburg','Stuttgart'),
    ]
    for route in routes:
        trace = n.get_route(route[0], route[1])
        print "\nRoute {start} -> {ende}".format(start= route[0], ende = route[1])
        length = 0
        for item in trace:
            print item
            length += item.wichtung
        print "Länge: {length}\n".format(length = length)
