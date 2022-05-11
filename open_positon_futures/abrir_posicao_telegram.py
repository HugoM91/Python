# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:10:03 2020

@author: hugom
"""

from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
import time
import telebot
from telebot import types


#discord WEBHOOKS
url_pos = ''
url_teste = ''

#Binance API FUTURES
request_client = RequestClient(api_key='', secret_key='')

#TElgeram bit id
bot = telebot.TeleBot("")

    
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
    
    tp = int(position(a)[0] + (position(a)[0] * 0.0021))
    take_profit  = request_client.post_order(symbol=a, side=OrderSide.SELL, ordertype=OrderType.LIMIT, timeInForce="GTC", quantity= qnt, price = tp) 
    
 
def open_short(a):

    qnt = 0.01
    open_order = request_client.post_order(symbol=a, side=OrderSide.SELL, ordertype=OrderType.MARKET, quantity= qnt)   
    
    tp = int(position(a)[0] - (position(a)[0] * 0.0021))
    take_profit  = request_client.post_order(symbol=a, side=OrderSide.BUY, ordertype=OrderType.LIMIT, timeInForce="GTC", quantity= qnt, price = tp) 

    
    


@bot.message_handler(commands=['long'])
def send_welcome(message):
    msg = bot.reply_to(message, "long opened")
    open_long('BTCUSDT')

    
@bot.message_handler(commands=['short'])
def send_welcome(message):
    msg = bot.reply_to(message, "short opened")
    open_short('BTCUSDT')
    
bot.polling()



















