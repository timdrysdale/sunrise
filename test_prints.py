#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 18:19:53 2020

@author: Timothy D Drysdale <timothy.d.drysdale@gmail.com>
"""

import time
import dmx
import numpy as np
from datetime import datetime as dt  

sender = dmx.DMX_Serial(port="/dev/ttyUSB0")
sender.start()
uni = bytes((0,)*512)
ua = bytearray(uni)

sender.set_data(uni)

print("%s test run of light"%dt.now().strftime('%Y-%m-%d %H:%M:%S'))

tpr = [0,0.1,0.5,1]
rp  = [0,20,255,255]
    
tpg = [0,0.1,0.5,1]
gp = [0,1,50,175]
    
tpb = [0,0.8,1]
bp = [0,0,255]
    
tpw = [0,0.9,1]
wp = [0,0,255]

for t in np.linspace(0,1,30):

    r = int(np.interp(t,tpr,rp))
    g = int(np.interp(t,tpg,gp))
    b = int(np.interp(t,tpb,bp))
    w = int(np.interp(t,tpw,wp))

    ua[0] = r
    ua[1] = g
    ua[2] = b
    ua[3] = w

    uni = bytes(ua)
    sender.set_data(uni)

    time.sleep(0.1)




waiting = True

while True:
    
    uni = bytes((0,)*512)

    sender.set_data(uni)
    print("%s waiting for dawn"%dt.now().strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)
    
    print("%s dawn begins"%dt.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    for t in np.linspace(0,1,30):
        
        r = int(np.interp(t,tpr,rp))
        g = int(np.interp(t,tpg,gp))
        b = int(np.interp(t,tpb,bp))
        w = int(np.interp(t,tpw,wp))
        
        ua[0] = r
        ua[1] = g
        ua[2] = b
        ua[3] = w
        
        uni = bytes(ua)

        sender.set_data(uni)
        
        time.sleep(0.1)
    print("%s day begins"%dt.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    time.sleep(1)
            
    print("%s end of the daily show"%dt.now().strftime('%Y-%m-%d %H:%M:%S'))
           
           

