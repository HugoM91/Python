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

    tempo = []
  
    avg_wlc = []
    avgl=[]
    
    for x in close_time:
        t = x
        t = t/1000
        t = datetime.fromtimestamp(t)
        t = t.strftime('%Y-%m-%d %H:%M')
        tempo.append(t)
    
    avg = avg.tolist()    
    for x in avg:    
        avgl.append(x)
    del avgl[0]
    avgl.append(float(0)) 
    
    
        
    for x,y in zip(avg, wlc):
        avg_wlc.append(y - x)
        
    df = pd.DataFrame({'Open' : open1 , 'Close': close, 'High' : high , 'Low':low  , 'Volume':volume,  'Avg':avg, 'Wlc':wlc, 'DifAW' : avg_wlc, 'NextAvgl':avgl } , columns = [ 'Open','High','Low','Close','Volume','Avg', 'Wlc', 'DifAW', 'NextAvgl'])
    
    df.to_csv(r'C:\Users\hugom\Desktop\Projecto\DataFrame\4_mar_15m_24_mar.csv', index=False)
    
chartplot('BTCUSDT')

    