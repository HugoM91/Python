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
    
    qnt = 12/mkp
    
    if qnt < 1:
        qnt2 = float("{:.3f}".format(qnt))
    if qnt > 10:
        qnt2 = int(q)
    else:
        qnt2 = float("{:.1f}".format(qnt))
    
    
    open_order = request_client.post_order(symbol=a, side=OrderSide.BUY, ordertype=OrderType.MARKET, quantity= qnt2)    
    
def startorder_tp (a):
    
    if position(a)[0] > 1000:
        tp = "{:.1f}".format(position(a)[0] + (position(a)[0] * 0.0042))
    elif 1000 > position(a)[0] > 10:
        tp = "{:.2f}".format(position(a)[0] + (position(a)[0] * 0.0042))                    
    elif 10 > position(a)[0] > 1:
        tp = "{:.3f}".format(position(a)[0] + (position(a)[0] * 0.0042))
    elif 1 > position(a)[0] > 0.1:
        tp = "{:.4f}".format(position(a)[0] + (position(a)[0] * 0.0042))
    elif 0.1 > position(a)[0] > 0.01:
        tp = "{:.5f}".format(position(a)[0] + (position(a)[0] * 0.0042))

    qnt = position(a)[1]
    
    take_profit  = request_client.post_order(symbol=a, side=OrderSide.SELL, ordertype=OrderType.LIMIT, timeInForce="GTC", quantity= qnt, price = tp) 


    
    
    
    
    
    
    
    
    
    
    






















