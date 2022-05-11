
#465446424 - ID Hugo
#-475899940 - ID Grupo Cryptolicious

import telebot
from binancedata import velas
from indicadores import indicadores
from binance.client import Client
import time

client = Client('', '')
bot = telebot.TeleBot("")

def startnoti(sym):
    close, open1, low, high , volume , nr_trocas, close_time, open_time = velas(sym)
    rsi , adx , atr , ma50 , ma100, ma200, wcl, macd, macdsignal, macdhist, upperband, middleband, lowerband, avg, fastk, fastd = indicadores (open1 , close , high , low)

    ma50 = ma50.tolist()
    ma200 = ma200.tolist()
    rsi = rsi.tolist()
    
    # Exponentical Moviong average Crossover 
    for x,y,k,z in zip(ma50[-2:], ma200[-2:], ma50[-1:], ma200[-1:]):
        a = x - y
        b = k - z
        if a < 0 and b > 0:
            bot.send_message(-475899940, text = ('Ma Cross UP' + sym))
        if a > 0 and b < 0 :
            bot.send_message(-475899940, text = ('Ma Cross DOWN' + sym))
            
    
    # Rsi
    for x in rsi[-2:]:
        if x > 86:
            bot.send_message(-475899940, text = ('RSI OverBought' + sym))
        if x < 13:
            bot.send_message(-475899940, text = ('RSI OverSold' + sym))
        
    

while True:
    startnoti('BTCUSDT')
    startnoti('XRPUSDT')
    startnoti('ETHUSDT')
    startnoti('LTCUSDT')
    startnoti('XMRUSDT')
    startnoti('EOSUSDT')
    startnoti('TRXUSDT')
    startnoti('ENJUSDT')
    startnoti('MCOUSDT')
    startnoti('BNBUSDT')
    startnoti('XLMUSDT')
    startnoti('NEOUSDT')
    startnoti('BATUSDT')
    startnoti('BTTUSDT')
    startnoti('ONTUSDT')
    startnoti('IOTAUSDT')
    startnoti('ZECUSDT')
    startnoti('DASHUSDT')
    
    time.sleep(7200)









 









