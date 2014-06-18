from MyErrors import UsageError as UE

class fReader(object):
    def __init__(self, filename):
        try:
            self.f = open(filename, 'r')
            print("file %s was opened and is ready to be read.\n"%filename)
        except IOError:
            raise UE("File %s could not been open"%filename)
        else:
            return

    def getData(self):
        result = []
        for line in self.f:
            # lösche Zeilenumbrüche
            line = line.replace("\n", "")
            # ignoriere Kommentare
            if not line.startswith("#"):
                result.append(line)
        return result
