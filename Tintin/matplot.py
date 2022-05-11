# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 02:00:36 2020

@author: hugom
"""

import matplotlib.pyplot as plt
import mplfinance as mpf
from binancedata import velas
from padroes import padroes
import pandas as pd
from datetime import datetime
from indicadores import indicadores




def chartplot(a ):
    close, open1, low, high, volume, nr_trocas, close_time, open_time = velas(a)
    dojistar,harami,haramicross,darkcloud,eveningstar,eveningdoji,shootingstar,hangingman,engulfing,invertedhammer,hammer,threesoldiers,threecrows,risefall,piercing = padroes(open1 , close , high , low)
    rsi , adx , atr , ma50 , ma100, ma200, wcl, macd, macdsignal, macdhist, upperband, middleband, lowerband, avg, fastk, fastd = indicadores (open1 , close , high , low)


    tempo = []
    
    for x in close_time:
        t = x
        t = t/1000
        t = datetime.fromtimestamp(t)
        t = t.strftime('%Y-%m-%d')
        tempo.append(t)

    
    df = pd.DataFrame({'Open' : open1 , 'Close': close, 'High' : high , 'Low':low , 'data':tempo , 'Volume':volume, 'padrao':rsi , 'padrao2':upperband , 'padrao3':lowerband} , columns = ['data' , 'Open','High','Low','Close','Volume','padrao','padrao2','padrao3'])
    df = df.set_index(pd.DatetimeIndex(df['data']))

    apdict = [(mpf.make_addplot(df['padrao'] ,secondary_y=False, color='g' )) ,(mpf.make_addplot(df['padrao2']  ,secondary_y=True,color='b' )),(mpf.make_addplot(df['padrao3'] ,secondary_y=True,color='r' ))]
    mpf.plot(df,  type='line',addplot=apdict)    
    

