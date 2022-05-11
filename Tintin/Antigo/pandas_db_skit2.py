# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:29:10 2020

@author: hugom
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:11:39 2020

@author: hugom
"""

import pandas as pd
import numpy as np
from binancedata import velas
from indicadores import indicadores
from datetime import datetime
from previousvolumes import volumesantigos , volumesantigos2


def chartplot(a):
    close, open1, low, high, volume, nr_trocas, close_time, open_time = velas(a)
    rsi, adx, atr, ma50, ma100, ma200, wlc, macd, macdsignal, macdhist, upperband, middleband, lowerband, avg = indicadores (open1 , close , high , low)

    #buy = []
    #sell = []
    dirVela = []
    difMacd = []
    rsiover = []

    #for x,y in zip(open_time, close_time):
        #buy.append(volumesantigos(x,y,a)[1])
        #sell.append(volumesantigos(x,y,a)[2])
        
    for x,y in zip(close, open1):
        if x > y:
            dirVela.append(float(1)) #vela subiu
        if x == y :
            dirVela.append(float(0)) #vela ficou igual
        if x < y:
            dirVela.append(float(-1)) #vela desceu
            
    for x, y in zip(macd,macdsignal):
        difMacd.append(x-y)
            
    for x in rsi:       
        if x > 65:
            rsiover.append(float(1))
        elif x < 35:
            rsiover.append(float(-1))
        else:
            rsiover.append(float(0))


    df = pd.DataFrame({'Open':open1, 'Close':close, 'DirVela':dirVela, 'Avg':avg, 'Rsi':rsi, 'RsiOver':rsiover, 'MacdDif':difMacd, 'Atr':atr}, columns = ['Open', 'Close','DirVela', 'Avg', 'Rsi', 'RsiOver', 'MacdDif', 'Atr'])
    
    df.to_csv(r'C:\Users\hugom\Desktop\Projecto\DataFrame\testenovo', index=False)
    
chartplot('BTCUSDT')

    