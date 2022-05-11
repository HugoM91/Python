from binance.client import Client
import time
from datetime import datetime
import sqlite3
import talib
import numpy as np
import pandas as pd
from talib.abstract import RSI
from talib.abstract import OBV
from talib.abstract import MACD
from talib.abstract import ATR
import math



client = Client('s5jgqnUryEPYD7oCz5uCdAQimuCIHag5OzmSmVkvyRc2pIVPWPZd8mNx3jyDCdbj', '9QWGd9JTXt76ufl9PE3ocW5D1suikdGgylyKPgzecpDYmhXmBCRmX9DgNQ74pxZU')
klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Nov, 2019", "1 Mar, 2020")


#--------------------------Listas----------------------------------------------
close=[]
volume=[]
open1=[]
high=[]
low=[]
#--------------------------Sqlite----------------------------------------------

conn = sqlite3.connect('candlesteste', check_same_thread=False)
c = conn.cursor()    
c.execute("""CREATE TABLE IF NOT EXISTS candlesteste (time REAL, open REAL, close REAL, low REAL, high REAL 
                                                      ,rsi REAL, volume REAL, nr_trades REAL, trades_volume REAL,
                                                      obv REAL, macd REAL, macdsignal REAL, macdhist REAL, atr REAL, dir_preco REAL, dir_rsi REAL, obv_dir REAL, macd_dir REAL, macdsignal_dir REAL, macd_cruza REAL)""" )
conn.commit()

#---------------------------Kline listas---------------------------------------
for x in klines:
    open1.append (x[1])
    close.append (x[4])
    volume.append(x[5])
    high.append(x[2])
    low.append(x[3])

#-------------------------------Indicadores------------------------------------
#-------Conversao para os indicadores lerem
close2 = np.array(close, dtype='f8')
volume2 = np.array(volume, dtype='f8')
open2 = np.array(open1, dtype='f8')
high2 = np.array(high, dtype='f8')
low2 = np.array(low, dtype='f8')

inputs = {'close': close2, 'volume' :volume2, 'open':open2, 'high':high2, 'low':low2}

#---------RSI--------    
output = RSI(inputs, timeperiod=14)
rsi3 = output.tolist()


#--------OBV----------

real = OBV(inputs)
obv = real.tolist()

#------MACD---------

macd, macdsignal, macdhist = MACD(inputs, fastperiod=12, slowperiod=26, signalperiod=9)
macd2 = macd.tolist()
macds = macdsignal.tolist()
macdh = macdhist.tolist()

#-----ATR-----------

real = ATR(inputs, timeperiod=14)
atr = real.tolist()

#-------------------------------Tabela Sqlite----------------------------------
for x,y,k,ma,mas,mah,at,x_1,y_1,k_1,ma_1,mas_1,mah_1,at_1 in zip(klines[1:],rsi3[1:],obv[1:],macd2[1:], macds[1:],macdh[1:],atr[1:],klines,rsi3,obv,macd2, macds,macdh,atr):
    v = float(x[5])
    t = float(x[8]) 
    if v > 0 and t > 0:
        vt = v/t
    else:
        vt = 0
    t = x[0]/1000
    t = datetime.fromtimestamp(t)
    t1 = t.strftime('%Y-%m-%d')
    
    openv = float(x[1])
    closev = float(x[4])
    
#---------------           
    if openv - closev > 0:
        dir = 'down'
    else:
        dir = 'up'
#--------------- 
    if y > y_1:
        rsidir = 'up'
    else:
        rsidir = 'down'
#---------------       
    if k > k_1:
        obvdir = 'up'
    else:
        obvdir = 'down'
#---------------       
    if ma > ma_1 :
        macddir = 'up'
    else:
        macddir = 'down'
#---------------           
    if mas > mas_1:
        macdsdir = 'up'
    else:
        macdsdir = 'down'
#---------------
#new low (close) = nlp
    g = ma - mas
    h = ma_1 - mas_1 
    
    if math.copysign(1, g) != math.copysign(1, h):
        crz = "cruzou"
    else:
        crz = "bola"
    

#---------------

    c.execute('INSERT INTO candlesteste (time, open, close, low, high, rsi, volume, nr_trades, trades_volume, obv, macd, macdsignal, macdhist, atr, dir_preco, dir_rsi, obv_dir, macd_dir, macdsignal_dir, macd_cruza) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
              (t1, x[1], x[4], x[3], x[2],y, x[5], x[8],vt, k, ma, mas, mah, at, dir, rsidir, obvdir, macddir, macdsdir, crz))

conn.commit()
conn.close()



#new low
#new high
#cross macd
#dif between macd and macdsignal if macd > macd signal = up, if dif keeps incrising high chance going up







