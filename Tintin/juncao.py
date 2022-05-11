# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 01:23:04 2020

@author: hugom
"""

from binancedata import velas , ordens
from indicadores import indicadores
from divergencia import divrsi, divmacd
from previousvolumes import volumesantigos, volumesantigos2
from padroes import padroes, padroestime, padroestimeresult
from matplot import chartplot
from datetime import datetime
import time
import numpy as np


l = []
soma= []
        
def start (a):
    close, open1, low, high, volume, nr_trocas, close_time , open_time = velas(a)
    rsi, adx, atr, ma50, ma100, ma200, wlc, macd, macdsignal, macdhist, upperband, middleband, lowerband, avg, fastk, fastd = indicadores (open1 , close , high , low)
    id1 , qty , buy , sell, time , timef = ordens(a)
    dojistar,harami,haramicross,darkcloud,eveningstar,eveningdoji,shootingstar,hangingman,engulfing,invertedhammer,hammer,threesoldiers,threecrows,risefall,piercing = padroes(open1 , close , high , low)
#------------------------------------------------------------------------------
   
    #padroestimeresult(dojistar,open_time, close_time,a,20, volumesantigos2)   
    #volumesantigos2(open_time[30], close_time[30], a, 15)
    #chartplot(a, movingaverage(a)[0], movingaverage(a)[1], movingaverage(a)[2]) #green, blue,red
    
    #divrsi(close, rsi ,a, close_time, 40)
    b = invertedhammer.tolist()
    print(b)

start('BTCUSDT')

    
