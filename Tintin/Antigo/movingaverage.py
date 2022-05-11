# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:56:45 2020

@author: hugom
"""

from indicadores import indicadores
from binancedata import velas 
import talib
from talib.abstract import MA , WCLPRICE, AVGPRICE
import numpy as np


def movingaverage(a):
    
    lista=[]
    
    close, open1, low, high, volume, nr_trocas, close_time , open_time = velas(a)
    lista1 = np.array(open1)
    lista2 = np.array(close)
    lista3 = np.array(high)
    lista4 = np.array(low)
    
    inputs = {'open' : lista1 , 'close' : lista2 , 'high' : lista3 , 'low' : lista4}
    
    wcl = WCLPRICE(inputs)
    avg = AVGPRICE(inputs)
    
    ma50  = MA(inputs, timeperiod=50, matype=0)
    ma100 = MA(inputs, timeperiod=100, matype=0)
    ma200 = MA(inputs, timeperiod=200, matype=0)
    ma300 = MA(inputs, timeperiod=300, matype=0)
    ma500 = MA(inputs, timeperiod=500, matype=0)
    
    inputs2 = {'close':wcl}
    wma50  = MA(inputs2, timeperiod=50, matype=0) 
    wma100 = MA(inputs2, timeperiod=100, matype=0)
    wma200 = MA(inputs2, timeperiod=200, matype=0)
    wma300 = MA(inputs2, timeperiod=300, matype=0)
    wma500 = MA(inputs2, timeperiod=500, matype=0)   

    inputs3 = {'close':avg}
    ama50  = MA(inputs3, timeperiod=50, matype=0) 
    ama100 = MA(inputs3, timeperiod=100, matype=0)
    ama200 = MA(inputs3, timeperiod=200, matype=0)
    ama300 = MA(inputs3, timeperiod=300, matype=0)
    ama500 = MA(inputs3, timeperiod=500, matype=0) 
       
    
    for x,y in zip(wma100 , ma100):
        lista.append(y - x)
    
    return lista , wma50 , wma100

