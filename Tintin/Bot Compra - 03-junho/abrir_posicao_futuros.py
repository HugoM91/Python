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
    qnt2 = float("{:.3f}".format(qnt))
    op = int(mkp -(mkp * 0.0035))
    
    open_order = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY, ordertype=OrderType.LIMIT, timeInForce="GTC", quantity= qnt2, price = op)    
    
    
    
def startorder_tp (a):
    
    tp = int(position('BTCUSDT')[0] + (position('BTCUSDT')[0] * 0.008))
    tp1 = int(position('BTCUSDT')[0] + (position('BTCUSDT')[0] * 0.0060))
    
    qnt = int(position('BTCUSDT')[1])/2
    
    take_profit  = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.LIMIT, timeInForce="GTC", quantity= qnt, price = tp) 
    take_profit2 = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.LIMIT, timeInForce="GTC", quantity= qnt, price = tp1)

    return take_profit, take_profit2                         

def startorder_sl (a):
    
    market_price = request_client.get_mark_price(symbol=a)   
    mkp = market_price.markPrice
    
    sl = int(mkp - (mkp * 0.015))
    sl1 = int(mkp - (mkp * 0.012))
    sl2 = int(mkp - (mkp * 0.008))
    
    qnt_10 = float("{:.3f}".format(position('BTCUSDT')[1]  * 0.1))
    qnt_20 = float("{:.3f}".format(position('BTCUSDT')[1]  * 0.2))
    qnt_30 = float("{:.3f}".format(position('BTCUSDT')[1]  * 0.3))
    

    stop_loss = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.STOP, timeInForce="GTC", quantity= qnt_20, price = sl, stopPrice = sl)
    stop_loss1 = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.STOP, timeInForce="GTC", quantity= qnt_10, price = sl1,stopPrice = sl1)    
    stop_loss2 = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.STOP, timeInForce="GTC", quantity= qnt_10, price = sl2,stopPrice = sl2)
    
    
    
startorder_sl
    
    
    
    
    
    
    
    
    
    
    
    
    






















