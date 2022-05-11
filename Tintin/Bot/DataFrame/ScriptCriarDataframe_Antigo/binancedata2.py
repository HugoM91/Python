# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:57:37 2020

@author: hugom
"""

from binance.client import Client
from datetime import datetime

client = Client('s5jgqnUryEPYD7oCz5uCdAQimuCIHag5OzmSmVkvyRc2pIVPWPZd8mNx3jyDCdbj', '9QWGd9JTXt76ufl9PE3ocW5D1suikdGgylyKPgzecpDYmhXmBCRmX9DgNQ74pxZU')



# from time to time "2020-02-01T19:20+01:00" ,"2020-02-02T19:20+01:00"
# "1 day ago UTC"
# "1 hour ago UTC"
# from day to day "1 Dec, 2017", "1 Jan, 2018"
def velas(a):
    klines = client.get_historical_klines(a, Client.KLINE_INTERVAL_5MINUTE , "2020-01-18T06:20" ,"2020-01-18T13:20"  )
    
    close=[]
    open1=[]
    low=[]
    high=[]
    volume=[]
    nr_trocas=[]
    close_time = []
    open_time=[]
    for x in klines:
        open_time.append(float(x[0]))
        open1.append(float(x[1]))
        high.append(float(x[2]))
        low.append(float(x[3]))
        close.append(float(x[4]))
        volume.append(float(x[5]))
        close_time.append(float(x[6]))
        nr_trocas.append(float(x[8]))
            
    return close, open1, low, high , volume , nr_trocas, close_time, open_time