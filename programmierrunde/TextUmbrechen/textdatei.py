class textdatei:
    def textLesen(self, filename):
        f = open(filename, 'r')
        text = f.readlines()
        f.close()
        return ' '.join(text)

    def dateiSpeichern(self, filename, text, length):
        filename = str(length) + filename
        f = open(filename, 'w')
        f.write(text)
        f.close()
        return filename
