# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 00:45:52 2020

@author: hugom
"""

import talib
from talib.abstract import RSI, MACD, ADX, ATR , BBANDS , MA , WCLPRICE, AVGPRICE, STOCHRSI, EMA
import numpy as np


def indicadores (o , c , h , l) : # open, close, high , low
    lista1 = np.array(o)
    lista2 = np.array(c)
    lista3 = np.array(h)
    lista4 = np.array(l)
    
    inputs = {'open' : lista1 , 'close' : lista2 , 'high' : lista3 , 'low' : lista4}
        
    macd, macdsignal, macdhist = MACD(inputs, fastperiod=12, slowperiod=26, signalperiod=9)
    rsi = RSI(inputs, timeperiod=14)    
    adx = ADX(inputs , timeperiod=14)
    atr = ATR(inputs , timeperiod=14)
    upperband, middleband, lowerband = BBANDS(inputs, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    ma50 = MA(inputs, timeperiod=50, matype=0)
    ma100 = MA(inputs, timeperiod=100, matype=0)
    ma200 = EMA(inputs, timeperiod=200, matype=0)
    wcl = WCLPRICE(inputs)
    avg = AVGPRICE(inputs)
    fastk, fastd = STOCHRSI(inputs, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)

    

    
    return rsi , adx , atr , ma50 , ma100, ma200, wcl, macd, macdsignal, macdhist, upperband, middleband, lowerband, avg, fastk, fastd

