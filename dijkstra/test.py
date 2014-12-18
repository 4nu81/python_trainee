#! /usr/bin/python

import sys
from dijkstra import *

# Test
class Test:
    def __init__(self):
        self.k1 = Knoten(1)
        self.k2 = Knoten(2)
        self.k3 = Knoten(3)
        self.k4 = Knoten(4)
        self.k5 = Knoten(5)
        self.k6 = Knoten(6)

        self.v1 = Verbindung(self.k1, self.k2, 1)
        self.v2 = Verbindung(self.k1, self.k3, 2)
        self.v3 = Verbindung(self.k2, self.k4, 2)
        self.v4 = Verbindung(self.k4, self.k6, 2)
        self.v5 = Verbindung(self.k4, self.k5, 1)
        self.v6 = Verbindung(self.k3, self.k5, 3)
        self.v7 = Verbindung(self.k5, self.k3, 1)
        self.v8 = Verbindung(self.k5, self.k6, 2)
        self.v9 = Verbindung(self.k6, self.k1, 1)
        self.v10 = Verbindung(self.k6, self.k3, 1)

        verbindungen = [
            self.v1,
            self.v2,
            self.v3,
            self.v4,
            self.v5,
            self.v6,
            self.v7,
            self.v8,
            self.v9,
            self.v10,
        ]
        
        knoten = [
            self.k1,
            self.k2,
            self.k3,
            self.k4,
            self.k5,
            self.k6,
        ]

        self.graph = Graph(knoten, verbindungen)

    def test1(self):
        route = Logik.trace(self.graph, start = self.k1, ende = self.k5)
        route_test = [self.v1, self.v3, self.v5]

        assert len(route) == len(route_test), 'falsche Laenge'
        for i in range(len(route_test)):
            assert route[i] is route_test[i], 'Fehler'
        print 'test1 erfolgreich'

    def test2(self):
        route = Logik.trace(self.graph, self.k1, self.k6)
        route_test = [self.v1, self.v3, self.v4]

        assert len(route) == len(route_test), 'falsche Laenge'
        for i in range(len(route_test)):
            assert route[i] is route_test[i], 'Fehler'
        print 'test2 erfolgreich'

    def run(self):
        self.test1()
        self.test2()


if __name__ == '__main__':
    t = Test()
    t.run()
