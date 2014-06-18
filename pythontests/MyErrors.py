"""
Eigene Exceptionklasse
Ermoeglich erkennen selbst ausgeloester Exceptions
"""

class UsageError(Exception):    
    def __init__(self, msg):
        self.msg = msg
