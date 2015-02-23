class Ausgabe:
    def __init__(self, filename):
        self.f = open(filename, 'w')

    def write(self, line):
        self.f.write(line)

    def close(self):
        self.f.close()
