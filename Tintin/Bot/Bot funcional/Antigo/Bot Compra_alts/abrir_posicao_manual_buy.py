# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:10:03 2020

@author: hugom
"""

from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
import inspect


request_client = RequestClient(api_key='qZjzNUgXyuQazOmkvuU1GMAkIjoxDRkvjeHeCLRFwcvCO0fx1kZeU2IdZLvIrzgx', secret_key='uad9STV3faJFfMWDAVvPvdd5e8pVY51ciAgR5Hmiw6gla0vMw3oL2HVEltabvrLB')

def position(a):
    result = request_client.get_position()
        
    def get_entry_price(result_list, sym):
        for pos_obj in result_list:
           #print(pos_obj.symbol)
           if pos_obj.symbol == sym:
               return pos_obj.entryPrice , pos_obj.positionAmt
                  
    entry_price = get_entry_price(result, a)[0]
    position_size = get_entry_price(result, a)[1]

    return entry_price, position_size



def startorder_open (a):
    
    market_price = request_client.get_mark_price(symbol=a)   
    mkp = market_price.markPrice
    qnt = 0.2
    qnt2 = float("{:.3f}".format(qnt))
    
    open_order = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY, ordertype=OrderType.MARKET, quantity= qnt2)    
    
    
    
def startorder_tp (a):
    
    tp = int(position('BTCUSDT')[0] + (position('BTCUSDT')[0] * 0.0027))
    qnt = position('BTCUSDT')[1]
    take_profit  = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.LIMIT, timeInForce="GTC", quantity= qnt, price = tp) 



startorder_open('BTCUSDT')
startorder_tp('BTCUSDT')
    
    
    
    
    
    
    
    
    
    
    
    
    






















