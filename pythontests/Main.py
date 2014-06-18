"""
Python Main-Method file
Usage: Main.py [filename to open]
"""

import sys
from Log import log
from CheckData import check
from MyErrors import UsageError as UE
from FileReader import fReader
from Convert import Convert
from Sort import Sort
from datetime import datetime, timedelta


def getArgs():
    result = []
    try:        
        for arg in sys.argv:
            s = arg
            result.append(s)
    except:
        print("irgend so ein scheiss Fehler mit argv")
        pass
    else:
        return result

def main():
    try:
        #Programm der Mainmethode
        l = log(True)

        args = getArgs()

        c = check()
        c.CheckArgCount(args)

        f = fReader(args[1])
        data = f.getData()

        c = Convert()
        data = c.str2Num(data)
        
        c = Sort()
                
        b = data.copy()
        m = data.copy()
        q = data.copy()

        msg = "sortet to: " + str(c.Bubblesort(b)) + " by Bubblesort"
        print(msg)
        l.msg(msg)
        msg = "sortet to: " + str(c.Mergesort(m)) + " by Mergesort"
        print(msg)
        l.msg(msg)
        msg = "sortet to: " + str(c.Quicksort(q)) + " by Quicksort"
        print(msg)
        l.msg(msg)

        
     
    # Fehlerbehandlung der UsageErrors (eigen angelegte Errors)
    except UE as e:
        msg = 'Benutzerfehler: ' + e.msg        
        print(msg)
        l.msg(msg)
        return 1
    else:
        return 0

if __name__ == "__main__":
    sys.exit(main())
