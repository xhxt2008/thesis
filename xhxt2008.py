#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 00:32:23 2018

@author: xhxt2008
"""

import pandas as pd
import numpy as np


def classes2(increace_rate):
    Y_class =[]
    for values in increace_rate:
        if values<0:
            Y_class.append(0)
        elif values>=0:
            Y_class.append(1)
        else:
            print('ok')
    return Y_class         

def classes3(increace_rate):
    Y_class =[]
    for values in increace_rate:
        if values<-0.005:
            Y_class.append(-1)
        elif values>=-0.005 and values<=0.005:
            Y_class.append(0)
        elif values>0.005:
            Y_class.append(1)    
        else:
            print('ok')
    return Y_class 
def classes5(increace_rate):
    Y_class =[]
    for values in increace_rate:
        if values>=-0.003 and values<=0.003:
            Y_class.append(0)
        elif values>0.003 and values<=0.01:
            Y_class.append(1)
        elif values>=-0.01 and values<-0.003:
            Y_class.append(-1)
        elif values> 0.01:
            Y_class.append(2)
        elif values<-0.01:
            Y_class.append(-2)
       # print('highDown')
        else:
           print('ok')
    return Y_class 