def datei_einlesen(filename):
    f = file(filename, 'r')
    result = f.readlines()
    f.close()
    return result
