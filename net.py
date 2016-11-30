# -*- coding: utf-8 -*-
# ~/.pyenv/bin/pyenv/versions/2.7.11/bin/python

import time
import sys

INTERFACE = 'eno167'
STATS = []
print 'Interface:', INTERFACE


def NetInfoAndOut():
        ifstat = open('/proc/net/dev').readlines()
        interface  = ifstat[2]
        info = float(interface.split()[1])
        out = float(interface.split()[9])

        infoFormart = round(info / 1024 / 1024, 3)
        outFormart = round(out / 1024 / 1024, 3)
        dicst = {
                "info":str(infoFormart)+"MB",
                "out": str(outFormart) + "MB",
                 }
        return  dicst


netinfo =  NetInfoAndOut()

print netinfo["info"]
