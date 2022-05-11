# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 12:43:47 2021

@author: Admin
"""
from binance.client import Client
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
from talib import MACD, STOCHRSI
import numpy as np
import time

api_key=''
secret_key=''
client = Client(api_key, secret_key)
request_client = RequestClient(api_key='', secret_key='')

    
def get_entry_price(result_list, sym):
    for pos_obj in result_list:
        if pos_obj.symbol == sym:
            return pos_obj.entryPrice , pos_obj.positionAmt
        
        
def position(a):
    result = request_client.get_position()
        
    
    entry_price = get_entry_price(result, a)[0]
    position_size = get_entry_price(result, a)[1]

    return entry_price, position_size


def open_long(a):

    qnt = 0.01
    open_order = request_client.post_order(symbol=a, side=OrderSide.BUY, ordertype=OrderType.MARKET, quantity= qnt)   
    
    tp = int(position(a)[0] + (position(a)[0] * 0.0011))
    take_profit  = request_client.post_order(symbol=a, side=OrderSide.SELL, ordertype=OrderType.LIMIT, timeInForce="GTC", quantity= qnt, price = tp) 
    
 
def open_short(a):

    qnt = 0.01
    open_order = request_client.post_order(symbol=a, side=OrderSide.SELL, ordertype=OrderType.MARKET, quantity= qnt)   
    
    tp = int(position(a)[0] - (position(a)[0] * 0.0011))
    take_profit  = request_client.post_order(symbol=a, side=OrderSide.BUY, ordertype=OrderType.LIMIT, timeInForce="GTC", quantity= qnt, price = tp) 


o = []
h = []
l = []
c = []
v = []

def get_candles():
    candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1MINUTE, limit=120)

    for x in candles:
        o.append(x[1])
        h.append(x[2])
        l.append(x[3])
        c.append(x[4])
        v.append(x[5])


def indicators(o,h,l,c):
    c = np.array([float(x) for x in c])
    macd, macdsignal, macdhist = MACD(c, fastperiod=12, slowperiod=26, signalperiod=9)
    fastk, fastd = STOCHRSI(c, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    process(macdsignal,macd,fastk,fastd)


def diference(lista, direction):
    
    i = 0
    flag = 0
    while (i <= 5):
        if direction == 'UP':
            if lista[-i] > lista[-i-1]:
                flag += 1
        elif direction == 'DOWN':
            if lista[-i] < lista[-i-1]:
                flag += 1
        i += 1
        
    if flag == 5:
        return 'True'

    return 'False'
    


def process(macdsignal,macd,fastk,fastd):
    macdsignal = macdsignal[-9:]
    macd = macd[-9:]
    macddif = []
    long = 0
    short = 0
    
    
    for x, y in zip(macdsignal, macd):
        if y > x:
            long+=1
        if x > y:
            short+=1
        macddif.append(y-x)
    
        
    if long >= 8  and diference(macddif, 'UP') == 'True' and sum(macd)/len(macd) > 0:
        if position('BTCUSDT')[1] == 0.0:
            open_short('BTCUSDT')
            print('Short Opened')
            time.sleep(2400)
    if short >= 8 and diference(macddif, 'DOWN') == 'True' and sum(macd)/len(macd) < 0:
        if position('BTCUSDT')[1] == 0.0:
            open_long('BTCUSDT')
            print('Long Opened')
            
            time.sleep(2400)

i = 0
while True:
    get_candles()
    indicators(o, h, l, c)
    
    i += 1
    print('LOOP : ' , i)
    time.sleep(60)


