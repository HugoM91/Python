# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:23:12 2020

@author: hugom
"""
#465446424 - ID Hugo
#-475899940 - ID Grupo Cryptolicious
#-1001266364263 # grupo benny/joao

import telebot
from binancedata import velas
from indicadores import indicadores
from binance.client import Client
from datetime import datetime
from abrir_posicao_futuros import startorder_sl, position 
import numpy as np 
import heapq

bot = telebot.TeleBot("")
client = Client('', '')


chat__id = -1001266364263

#--------------------------Ticker Notificacoes---------------------------------
tickers = client.get_ticker()

def gogo(sym):
    for x in tickers:
        if x['symbol'] == sym:
            return x['priceChangePercent'] , x['volume'], str(x['count']) 
        

perc_change1 = []
l_sim1 = []
perc_change2 = []
l_sim2 = []
vol1=[]
vol2=[]

for x in  tickers:
    if x['symbol'].endswith("USDT"):
        perc_change1.append(x['priceChangePercent'])
        l_sim1.append(x['symbol'])
        vol1.append(int(float(x['volume']) * float(x['lastPrice'])))
        
    if x['symbol'].endswith("BTC"):
        perc_change2.append(x['priceChangePercent'])
        l_sim2.append(x['symbol'])
        vol2.append(int(float(x['volume']) * float(x['lastPrice'])))

def largest (list_perc , list_tama):
    larg = heapq.nlargest(10, list_perc)
    top1 = [list_tama[list_perc.index(larg[0])] , larg[0]]
    top2 = [list_tama[list_perc.index(larg[1])] , larg[1]]
    top3 = [list_tama[list_perc.index(larg[2])] , larg[2]]
    top4 = [list_tama[list_perc.index(larg[3])] , larg[3]]
    top5 = [list_tama[list_perc.index(larg[4])] , larg[4]]
    top6 = [list_tama[list_perc.index(larg[5])] , larg[5]]
    top7 = [list_tama[list_perc.index(larg[6])] , larg[6]]
    top8 = [list_tama[list_perc.index(larg[7])] , larg[7]]
    top9 = [list_tama[list_perc.index(larg[8])] , larg[8]]
    top10 = [list_tama[list_perc.index(larg[9])] , larg[9]]
    
    return top1, top2, top3, top4, top5, top6, top7, top8, top9, top10

def smallest (list_perc , list_tama):
    larg = heapq.nsmallest(10, list_perc)
    top1 = [list_tama[list_perc.index(larg[0])] , larg[0]]
    top2 = [list_tama[list_perc.index(larg[1])] , larg[1]]
    top3 = [list_tama[list_perc.index(larg[2])] , larg[2]]
    top4 = [list_tama[list_perc.index(larg[3])] , larg[3]]
    top5 = [list_tama[list_perc.index(larg[4])] , larg[4]]
    top6 = [list_tama[list_perc.index(larg[5])] , larg[5]]
    top7 = [list_tama[list_perc.index(larg[6])] , larg[6]]
    top8 = [list_tama[list_perc.index(larg[7])] , larg[7]]
    top9 = [list_tama[list_perc.index(larg[8])] , larg[8]]
    top10 = [list_tama[list_perc.index(larg[9])] , larg[9]]
    
    return top1, top2, top3, top4, top5, top6, top7, top8, top9, top10            


#-------------------------HELP

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(chat__id, text = ('Info Moedas - btc , eth , ltc , xrp , xmr , trx , eos, enj \nFuturos  -  position_btc'))
    
#-------------------------Informacoes das Moedas
@bot.message_handler(commands=['btc'])
def send_welcome(message):
    symb = gogo('BTCUSDT')
    bot.send_message(chat__id, text = ('-----24hours-----' '\n .Price Change% = ' + (symb[0]) + '\n Volume = ' + (symb[1]) + '\n Nr Trades = ' + (symb[2])))
@bot.message_handler(commands=['eth'])
def send_welcome(message):
    symb = gogo('ETHUSDT')
    bot.send_message(chat__id, text = ('-----24hours-----USDT' '\n .Price Change% = ' + (symb[0]) + '\n Volume = ' + (symb[1]) + '\n Nr Trades = ' + (symb[2])))
    symb1 = gogo('ETHBTC')
    bot.send_message(chat__id, text = ('-----24hours-----BTC' '\n .Price Change% = ' + (symb1[0]) + '\n Volume = ' + (symb1[1]) + '\n Nr Trades = ' + (symb1[2])))

@bot.message_handler(commands=['ltc'])
def send_welcome(message):
    symb = gogo('LTCUSDT')
    bot.send_message(chat__id, text = ('-----24hours-----USDT' '\n .Price Change% = ' + (symb[0]) + '\n Volume = ' + (symb[1]) + '\n Nr Trades = ' + (symb[2])))
    symb1 = gogo('LTCBTC')
    bot.send_message(chat__id, text = ('-----24hours-----BTC' '\n .Price Change% = ' + (symb1[0]) + '\n Volume = ' + (symb1[1]) + '\n Nr Trades = ' + (symb1[2])))

@bot.message_handler(commands=['xrp'])
def send_welcome(message):
    symb = gogo('XRPUSDT')
    bot.send_message(chat__id, text = ('-----24hours-----USDT' '\n .Price Change% = ' + (symb[0]) + '\n Volume = ' + (symb[1]) + '\n Nr Trades = ' + (symb[2])))
    symb1 = gogo('XRPBTC')
    bot.send_message(chat__id, text = ('-----24hours-----BTC' '\n .Price Change% = ' + (symb1[0]) + '\n Volume = ' + (symb1[1]) + '\n Nr Trades = ' + (symb1[2])))

@bot.message_handler(commands=['xmr'])
def send_welcome(message):
    symb = gogo('XMRUSDT')
    bot.send_message(chat__id, text = ('-----24hours-----USDT' '\n .Price Change% = ' + (symb[0]) + '\n Volume = ' + (symb[1]) + '\n Nr Trades = ' + (symb[2])))
    symb1 = gogo('XMRBTC')
    bot.send_message(chat__id, text = ('-----24hours-----BTC' '\n .Price Change% = ' + (symb1[0]) + '\n Volume = ' + (symb1[1]) + '\n Nr Trades = ' + (symb1[2])))

@bot.message_handler(commands=['trx'])
def send_welcome(message):
    symb = gogo('TRXUSDT')
    bot.send_message(chat__id, text = ('-----24hours-----USDT' '\n .Price Change% = ' + (symb[0]) + '\n Volume = ' + (symb[1]) + '\n Nr Trades = ' + (symb[2])))
    symb1 = gogo('TRXBTC')
    bot.send_message(chat__id, text = ('-----24hours-----BTC' '\n .Price Change% = ' + (symb1[0]) + '\n Volume = ' + (symb1[1]) + '\n Nr Trades = ' + (symb1[2])))

@bot.message_handler(commands=['eos'])
def send_welcome(message):
    symb = gogo('EOSUSDT')
    bot.send_message(chat__id, text = ('-----24hours-----USDT' '\n .Price Change% = ' + (symb[0]) + '\n Volume = ' + (symb[1]) + '\n Nr Trades = ' + (symb[2])))
    symb1 = gogo('EOSBTC')
    bot.send_message(chat__id, text = ('-----24hours-----BTC' '\n .Price Change% = ' + (symb1[0]) + '\n Volume = ' + (symb1[1]) + '\n Nr Trades = ' + (symb1[2])))

@bot.message_handler(commands=['enj'])
def send_welcome(message):
    symb = gogo('ENJUSDT')
    bot.send_message(chat__id, text = ('-----24hours-----USDT' '\n .Price Change% = ' + (symb[0]) + '\n Volume = ' + (symb[1]) + '\n Nr Trades = ' + (symb[2])))
    symb1 = gogo('ENJBTC')    
    bot.send_message(chat__id, text = ('-----24hours-----BTC' '\n .Price Change% = ' + (symb1[0]) + '\n Volume = ' + (symb1[1]) + '\n Nr Trades = ' + (symb1[2])))



#-------------------------comecar stopLOSS
@bot.message_handler(commands=['stop_loss'])
def send_welcome(message):
    if position('BTCUSDT')[1] > 0:
        startorder_sl('BTCUSDT')
    else:
        bot.send_message(chat__id, text = ( ' Nao existe Posicao ' ))
    
    
#------------------------Informacoes da Posicao
@bot.message_handler(commands=['position_btc'])
def send_welcome(message):
    if position('BTCUSDT')[1] > 0:

        perc_mark =  (position('BTCUSDT')[0] * 100 / position('BTCUSDT')[3]) -100
        perc_liq =  (position('BTCUSDT')[2] * 100 / position('BTCUSDT')[3]) -100
        qnt_usd = position('BTCUSDT')[2] * position('BTCUSDT')[1]
        
        perc_mark1 = str(perc_mark)
        perc_liq1 = str(perc_liq) 
        qnt_usd1 = str(qnt_usd)
        
        p = str(position('BTCUSDT')[1])
        pl = str(position('BTCUSDT')[4])
        mp = str(position('BTCUSDT')[3])
        ep = str(position('BTCUSDT')[0])
        lp =  str(position('BTCUSDT')[2])
        bot.send_message(chat__id, text = ('Posicao Aberta' + '\n' + '--------' + (position('BTCUSDT')[5]) + '--------' ) + '\n' + 'Position Size = '  + p + '// ' + qnt_usd1 + '$' + '\n' +'Profit / Loss = '  +  pl + '$' + '\n' + 'Market Price = '  +  mp  + '$' + '\n' + 'Entry Price = ' +  ep + '$' + '// ' + perc_mark1 + '%'+ '\n' + 'Liquidation Price = '  +  lp + '$' + '// '  + perc_liq1 + '%')

                
        #bot.send_message(message.chat.id, text = ('Position Size = '  + p + '// ' + qnt_usd1 + '$'))
        #bot.send_message(message.chat.id, text = ('Profit / Loss = '  +  pl + '$'))
        #bot.send_message(message.chat.id, text = ('Market Price = '  +  mp  + '$'))
        #bot.send_message(message.chat.id, text = ('Entry Price = '  +  ep + '$' + '// ' + perc_mark1 + '%')) 
        #bot.send_message(message.chat.id, text = ('Liquidation Price = '  +  lp + '$' + '// '  + perc_liq1 + '%')) 
        
    else:
        bot.send_message(chat__id, text = ( ' Nao existe Posicao ' ))
  
      
#-------------------------comecar stopLOSS
        

@bot.message_handler(commands=['top_usdt'])
def send_welcome(message):         
    bot.send_message(chat__id, text = ( ' Top USDT % Change 24h \n' + str(largest(perc_change1,l_sim1)) + '\n'  + '\n' + ' Top USDT Volume  24h \n' + str(largest(vol1,l_sim1))))        
        
        
@bot.message_handler(commands=['top_btc'])
def send_welcome(message):         
    bot.send_message(chat__id, text = ( ' Top BTC % Change 24h \n' + str(largest(perc_change2,l_sim2)) + '\n'  + '\n' +' Top BTC Volume  24h \n' + str(largest(vol2,l_sim2))))        
        
bot.polling()










# Commands
# /btc
# /position_btc









