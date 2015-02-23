import sys

def cmdln_poll():
    return sys.argv[1]

def cmdln_starten():
    dateiname = sys.argv[2]
    email = sys.argv[3]
    return dateiname, email
