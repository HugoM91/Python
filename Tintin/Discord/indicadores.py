# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 00:45:52 2020

@author: hugom
"""

import talib
from talib.abstract import  CDLHAMMER, CDLSHOOTINGSTAR, CDL3BLACKCROWS, CDL3WHITESOLDIERS 
import numpy as np


def indicadores (o , c , h , l) : # open, close, high , low
    lista1 = np.array(o)
    lista2 = np.array(c)
    lista3 = np.array(h)
    lista4 = np.array(l)
    
    inputs = {'open' : lista1 , 'close' : lista2 , 'high' : lista3 , 'low' : lista4}
        
    hammer = CDLHAMMER(inputs)
    star = CDLSHOOTINGSTAR(inputs)
    white_soldier = CDL3WHITESOLDIERS(inputs)
    black_crow = CDL3BLACKCROWS(inputs)

    return hammer, star, white_soldier, black_crow

