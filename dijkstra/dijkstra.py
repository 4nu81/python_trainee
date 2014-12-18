# Model

class Knoten:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

class Verbindung:
    def __init__(self, start, ende, wichtung):
        self.start = start
        self.ende = ende
        self.wichtung = wichtung
    
    def __str__(self):
        return "{start} -> {ende} : {wichtung}".format(start=self.start, ende=self.ende, wichtung=self.wichtung)

class Graph:
    def __init__(self, knoten, verbindungen):
        self.knoten = knoten
        self.verbindungen = verbindungen

class Logik:

    @staticmethod
    def pop_lowest(liste):
        if len(liste) == 0:
            return None

        result = liste[0]
        for item in liste:
            if item.entfernung < result.entfernung:
                result = item
        liste.remove(result)
        return result

    @staticmethod
    def init(graph, start):
        unbesucht = []
        for item in graph.knoten:

            if item is start:
                item.entfernung = 0
            else:
                item.entfernung = float('inf')

            item.link = None
            unbesucht.append(item)
        return unbesucht

    @staticmethod
    def trace(graph, start, ende):

        unbesucht = Logik.init(graph, start)

        while len(unbesucht) > 0:
            this_knoten = Logik.pop_lowest(unbesucht)

            for verbindung in graph.verbindungen:
                if verbindung.start is this_knoten:
                    entf = this_knoten.entfernung + verbindung.wichtung
                    if verbindung.ende.entfernung > entf:
                        verbindung.ende.entfernung = entf
                        verbindung.ende.link = verbindung

        this = ende.link
        result = [this]
        if not this.start.link is None:
            while True:
                this = this.start.link
                result.insert(0, this)

                if this.start.link is None:
                    break
        return result
