# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:29:19 2020

@author: hugom
"""

from binance.client import Client
from datetime import datetime

client = Client('', '')



# from time to time "2020-02-01T19:20+01:00" ,"2020-02-02T19:20+01:00"
# "1 day ago UTC"
# "1 hour ago UTC"
# from day to day "1 Dec, 2017", "1 Jan, 2018"
def velas(a):
    klines = client.get_historical_klines(a, Client.KLINE_INTERVAL_5MINUTE , "30 day ago UTC" )
    
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


def ordens(a):
    trades = client.get_recent_trades(symbol= a , limit = 500)
    
    id1 = []
    qty = []
    sell = []
    buy = []
    timef = [] #formatado para a data real
    time = []
    
    for x in trades:
        id1.append(float(x['id']))
        qty.append(float(x['qty']))
        time.append(float(x['time']))
        if x['isBuyerMaker'] == True:
            sell.append(float(x['qty']))
        else:
            buy.append(float(x['qty']))
        
        t = float(x['time'])/1000
        t = datetime.fromtimestamp(t)
        t = t.strftime('%H:%M:%S')
        timef.append(t)
      
        
    return id1 , qty , buy , sell , time ,timef






























