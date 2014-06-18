"""
Prueft Programmrelevante Eingaben und notwendige Bedingungen. Gibt eine Exception falls Bedingungen nicht erfuellt.
"""

import sys, os
from MyErrors import UsageError as UE

class check(object):
    def __init__(self):        
        return
    
    def CheckArgCount(self, args):
        if len(args) != 2:
            sys.stderr.write("Benutze: %s <Dateiname>\n" % (args[0],))
            raise UE("Laenge passt nicht\n")
        print("Number of Args is fine")
        return
