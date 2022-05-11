
#465446424 - ID Hugo
#-475899940 - ID Grupo Cryptolicious

import telebot
from binancedata import velas
from indicadores import indicadores
from binance.client import Client
import time
from datetime import datetime

client = Client('', '')
bot = telebot.TeleBot("")

h = []
trade_id=[]
chat__id = ""

def startnoti(sym):
    
    trades = client.get_recent_trades(symbol=sym)
    trades2 = client.get_recent_trades(symbol='BTCUSDT')
    
    simbolos =  ['BTCUSDT']
    simbolos1 =  ['BNBUSDT', 'ETHUSDT']
    simbolos2 = ['XRPUSDT' , 'XMRUSDT' , 'LTCUSDT' , 'EOSUSDT', 'TRXUSDT']
    simbolos3 = ['NEOUSDT', 'IOTAUSDT', 'ZECUSDT', 'DASHUSDT', 'ENJUSDT','MCOUSDT','XLMUSDT' ,'BATUSDT','BTTUSDT', 'ONTUSDT', 'WINUSDT'] 
    simbolos4 = ['ENJBTC', 'MCOBTC','BATBTC','NEOBTC', 'XRPBTC' ,'IOSTBTC','ZRXBTC', 'NANOBTC' , 'DOGEBTC', 'ETCBTC', 'XEMBTC', 'QTUMBTC' ,'KNCBTC','SNTBTC'  ]

    
    btc_price = []            
    for x in trades2[-1:]:
        btc_price.append(float(x['price']))
    
    for x in trades:
        
        if x['id'] not in trade_id:
            q = float(x['qty'])
            d = x['isBuyerMaker']
            p = float(x['price'])
            pd = q * p
            q1 = float("{:.3f}".format(q))
            q1 = str(q1)
            pd3 = float("{:.3f}".format(pd))
            pd3 = str(pd3)
            #-------------/USDT
            if sym in simbolos:
                if pd >= 190000 and d == True:
                    bot.send_message(-442907326, text = ('------Sell------' + sym + '\n' + pd3 + ' USD' + '\n' + q1 + ' Coins'))
                    trade_id.append(x['id'])
                if pd >= 190000 and d == False:
                    bot.send_message(chat__id,text = ('------Buy------' + sym + '\n' + pd3 + ' USD' + '\n' + q1 + ' Coins' ))
                    trade_id.append(x['id'])
            #--------------------------------------------
            if sym in simbolos1:
                if pd >= 150000 and d == True:
                    bot.send_message(-442907326, text = ('------Sell------' + sym + '\n' + pd3 + ' USD' + '\n' + q1 + ' Coins'))
                    trade_id.append(x['id'])
                if pd >= 150000 and d == False:
                    bot.send_message(chat__id,text = ('------Buy------' + sym + '\n' + pd3 + ' USD' + '\n' + q1 + ' Coins' ))
                    trade_id.append(x['id'])
            #--------------------------------------------        
            if sym in simbolos2:
                if pd >= 75000 and d == True:
                    bot.send_message(chat__id, text = ('------Sell------' + sym + '\n' + pd3 + ' USD' + '\n' + q1 + ' Coins'))
                    trade_id.append(x['id'])
                if pd >= 75000 and d == False:
                    bot.send_message(chat__id,text = ('------Buy------' + sym + '\n' + pd3 + ' USD' + '\n' + q1 + ' Coins' ))
                    trade_id.append(x['id'])
            #--------------------------------------------        
            if sym in simbolos3:
                if pd >= 40000 and d == True:
                    bot.send_message(chat__id, text = ('------Sell------' + sym + '\n' + pd3 + ' USD' + '\n' + q1 + ' Coins'))
                    trade_id.append(x['id'])
                if pd >= 40000 and d == False:
                    bot.send_message(chat__id,text = ('------Buy------' + sym + '\n' + pd3 + ' USD' + '\n' + q1 + ' Coins' ))
                    trade_id.append(x['id'])
                    
            # --------/BITCOIN        
            if sym in simbolos4:
                bp = btc_price[0]
                pd4 = bp * pd
                pd5 = float("{:.3f}".format(pd4))
                pd5 = str(pd5)
                if pd4 >= 40000 and d == True:
                    bot.send_message(chat__id, text = ('------Sell------' + sym + '\n' + pd5 + ' USD' + '\n' + q1 + ' Coins'))
                    trade_id.append(x['id'])
                if pd4 >= 40000 and d == False:
                    bot.send_message(chat__id,text = ('------Buy------' + sym + '\n' + pd5 + ' USD' + '\n' + q1 + ' Coins' ))
                    trade_id.append(x['id'])
"""                    
            if sym in simbolos5:
                bp = btc_price[0]
                pd3 = bp * pd
                pd4 = str(pd3)
                if pd3 >= 25000 and d == True:
                    bot.send_message(-475899940, text = ('------Sell------' + sym + '\n' + pd4 + ' USD' + '\n' + q1 + ' Coins'))
                    trade_id.append(x['id'])
                if pd3 >= 50000 and d == False:
                    bot.send_message(-475899940,text = ('------Buy------' + sym + '\n' + pd4 + ' USD' + '\n' + q1 + ' Coins' ))
                    trade_id.append(x['id'])
"""        
            
while True:
    #---------/USDT
    #simbolo 1
    startnoti('BTCUSDT')
    startnoti('BNBUSDT')
    startnoti('ETHUSDT')

    #simbolo 2 

    startnoti('XRPUSDT')
    startnoti('LTCUSDT')
    startnoti('XMRUSDT')
    startnoti('EOSUSDT')
    startnoti('TRXUSDT')
    
    #simbolo 3 
    startnoti('NEOUSDT')
    startnoti('IOTAUSDT')           
    
    startnoti('ZECUSDT')
    startnoti('DASHUSDT')
    startnoti('ENJUSDT')
    startnoti('MCOUSDT')
    startnoti('XLMUSDT')
    startnoti('BATUSDT')
    startnoti('BTTUSDT')
    startnoti('ONTUSDT')
    startnoti('WINUSDT')

    
    #---------/BTC
    #simbolo 4
    startnoti('ENJBTC')
    startnoti('MCOBTC')
    startnoti('BATBTC')
    startnoti('NEOBTC')
    startnoti('XRPBTC')
    startnoti('IOSTBTC')
    startnoti('ZRXBTC')
    startnoti('NANOBTC')
    startnoti('DOGEBTC')
    startnoti('ETCBTC')
    startnoti('XEMBTC')
    startnoti('QTUMBTC')
    startnoti('KNCBTC')
    startnoti('SNTBTC')
    

    
    
    if len(trade_id) > 30000:
        del trade_id[:20000]
        
    time.sleep(60)









 









