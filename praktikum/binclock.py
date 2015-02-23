import time, datetime
from dec2bin import *
import os


while True:
    _time = time.strftime('%H:%M:%S').split(':')
    h = int(_time[0])
    m = int(_time[1])
    s = int(_time[2])
    
    base = 2
    
    hb = dec2nbr(h,base)
    mb = dec2nbr(m,base)
    sb = dec2nbr(s,base)
    os.system('clear')
    print("{h} : {m} : {s}".format(h=hb, m=mb, s=sb))
    time.sleep(1)
