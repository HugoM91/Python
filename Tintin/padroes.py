# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:38:02 2020

@author: hugom
"""
#BULLISH PATTERNS
#https://cointelegraph.com/news/5-bullish-candlestick-patterns-every-bitcoin-crypto-trader-must-know  
#BEARISH PATTERNS
#https://cointelegraph.com/news/5-bearish-candlestick-patterns-every-bitcoin-trader-must-know   

from talib.abstract import CDLDOJISTAR , CDLHARAMI , CDLHARAMICROSS, CDLDARKCLOUDCOVER , CDLEVENINGSTAR , CDLEVENINGDOJISTAR , CDLSHOOTINGSTAR
from talib.abstract import CDLHANGINGMAN , CDLENGULFING , CDLINVERTEDHAMMER , CDLHAMMER, CDL3WHITESOLDIERS , CDL3BLACKCROWS , CDLRISEFALL3METHODS , CDLPIERCING
import numpy as np
from datetime import datetime

 
def padroes (o , c , h , l):
    lista1 = np.array(o)
    lista2 = np.array(c)
    lista3 = np.array(h)
    lista4 = np.array(l)
    
    inputs = {'open' : lista1 , 'close' : lista2 , 'high' : lista3 , 'low' : lista4}
    
    dojistar = CDLDOJISTAR(inputs)
    harami = CDLHARAMI(inputs)
    haramicross = CDLHARAMICROSS(inputs)
    darkcloud = CDLDARKCLOUDCOVER(inputs, penetration=0)
    eveningstar = CDLEVENINGSTAR(inputs, penetration=0)
    eveningdoji = CDLEVENINGDOJISTAR(inputs, penetration=0)
    shootingstar = CDLSHOOTINGSTAR(inputs)
    hangingman = CDLHANGINGMAN(inputs)
    engulfing = CDLENGULFING(inputs)
    invertedhammer = CDLINVERTEDHAMMER(inputs)
    hammer = CDLHAMMER(inputs)
    threesoldiers = CDL3WHITESOLDIERS(inputs)
    threecrows = CDL3BLACKCROWS(inputs)
    risefall = CDLRISEFALL3METHODS(inputs)
    piercing = CDLPIERCING(inputs)
    
    return dojistar,harami,haramicross,darkcloud,eveningstar,eveningdoji,shootingstar,hangingman,engulfing,invertedhammer,hammer,threesoldiers,threecrows,risefall,piercing
    
def padroestime(lista,opentime_lista,closetime_lista):
    lista1=[]
    opentime = []
    closetime = []
    
    result = np.where(lista == 100)
    
    l=0
    while len(result[0]) != l :
        lista1.append(result[0][l])
        l+=1
    for x in lista1:
        opentime.append(opentime_lista[x])
        closetime.append(closetime_lista[x])

    return opentime , closetime


def padroestimeresult(padrao, opentime, closetime,a,b,volumesantigos2):
    f = padroestime(padrao, opentime, closetime)[1]

    for y in f:
        g = int(y) - 59999
        h = int(y)
        volumesantigos2(g, h, a, b)
        t = g
        t = t/1000
        t = datetime.fromtimestamp(t)
        t = t.strftime('%Y-%m-%d %H:%M:%S')
        
        print(t)
        t = h
        t = t/1000
        t = datetime.fromtimestamp(t)
        t = t.strftime('%Y-%m-%d %H:%M:%S')
        print(t)

