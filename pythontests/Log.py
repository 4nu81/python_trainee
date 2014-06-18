"""
Diese Klasse realisiert einen Log (log.txt in Programverzeichnis)
"""

import datetime
from MyErrors import UsageError as UE

class log():
    def __init__(self, override = False):
        try:
            kind = 'a'
            if override:
                kind = 'w'
        except:
            raise UE("Falscher Parameter in Methode uebergeben")

        try:
            self.f = open('log.txt', kind)
        except:
            print("open Log-File failed")
            self.f = None
            
    
    def msg(self, log_msg):
        try:
            if not self.f is None:
                msg = str(datetime.datetime.now()) + " : " + str(log_msg) + "\n"
                self.f.write(msg)
        except IOError:
            print("LogMessage failed")        
