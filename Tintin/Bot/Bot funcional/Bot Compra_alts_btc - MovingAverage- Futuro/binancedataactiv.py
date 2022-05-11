# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:57:37 2020

@author: hugom
"""

from binance.client import Client
import pandas as pd
from indicadores import indicadores
from statistics import mean
from learning_model import prever
import time
import telebot
#---------------------------
from abrir_posicao_futuros import startorder_open, position, startorder_tp
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


client = Client('s5jgqnUryEPYD7oCz5uCdAQimuCIHag5OzmSmVkvyRc2pIVPWPZd8mNx3jyDCdbj', '9QWGd9JTXt76ufl9PE3ocW5D1suikdGgylyKPgzecpDYmhXmBCRmX9DgNQ74pxZU')
bot = telebot.TeleBot("1225240806:AAHAn7e8jOZ--ThHRvzw3NHIuEkHcSeGnUY")


u = [1]

tickers = client.get_ticker()

def velas(a):
    klines = client.get_historical_klines(a, Client.KLINE_INTERVAL_5MINUTE , '6 hour ago UTC'  )
    
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

def listapandas(lista):
    if (len(lista)%6) >= 3 :
        print('===ATENCAO===Remainder muito grande')
    else :
        pass
    lista = lista[36:]
    novalista = []    
    a = int(len(lista)/8)

    novalista.append((mean(lista[:a])))
    novalista.append((mean(lista[a:a*2])))
    novalista.append((mean(lista[a*2:a*3])))
    novalista.append((mean(lista[a*3:a*4])))
    novalista.append((mean(lista[a*4:a*5])))
    novalista.append((mean(lista[a*5:a*6])))
    novalista.append((mean(lista[a*6:a*7])))
    novalista.append((mean(lista[a*7:])))
    
    return novalista
 
def datapandas (a):
    close, open1, low, high, volume, nr_trocas, close_time, open_time = velas(a)
    rsi, adx, atr, ma50, ma100, ma200, wlc, macd, macdsignal, macdhist, upperband, middleband, lowerband, avg, fastk, fastd = indicadores (open1 , close , high , low)

    macddif=[]
    stodif=[]
    pred =[0]
    
    for x,y in zip (macd, macdsignal):
        macddif.append(x - y)
    for x,y in zip(fastk, fastd):
        stodif.append(x - y)
    
    df = pd.DataFrame({'p1': listapandas(wlc)[0], 'p2':listapandas(wlc)[1], 'p3':listapandas(wlc)[2],'p4':listapandas(wlc)[3], 'p5':listapandas(wlc)[4], 'p6':listapandas(wlc)[5], 'p7':listapandas(wlc)[6],'p8':listapandas(wlc)[7], 'rsi':listapandas(rsi)[0], 'rsi1':listapandas(rsi)[1],'rsi2':listapandas(rsi)[2], 'rsi3':listapandas(rsi)[3], 'rsi4':listapandas(rsi)[4], 'rsi5':listapandas(rsi)[5], 'rsi6':listapandas(rsi)[6], 'rsi7':listapandas(rsi)[7], 'sto':listapandas(stodif)[0],'sto1':listapandas(stodif)[1],'sto2':listapandas(stodif)[2],'sto3':listapandas(stodif)[3],'sto4':listapandas(stodif)[4],'sto5':listapandas(stodif)[5],'sto6':listapandas(stodif)[6],'sto7':listapandas(stodif)[7] ,'macd':listapandas(macddif)[0],'macd1':listapandas(macddif)[1],'macd2':listapandas(macddif)[2],'macd3':listapandas(macddif)[3] ,'macd4':listapandas(macddif)[4],'macd5':listapandas(macddif)[5],'macd6':listapandas(macddif)[6],'macd7':listapandas(macddif)[7], 'macdl':listapandas(macd)[0],'macd1l':listapandas(macd)[1],'macd2l':listapandas(macd)[2],'macd3l':listapandas(macd)[3] ,'macd4l':listapandas(macd)[4],'macd5l':listapandas(macd)[5],'macd6l':listapandas(macd)[6],'macd7l':listapandas(macd)[7], 'macds':listapandas(macdsignal)[0],'macd1s':listapandas(macdsignal)[1],'macd2s':listapandas(macdsignal)[2],'macd3s':listapandas(macdsignal)[3] ,'macd4s':listapandas(macdsignal)[4],'macd5s':listapandas(macdsignal)[5],'macd6s':listapandas(macdsignal)[6],'macd7s':listapandas(macdsignal)[7], 'stol':listapandas(fastk)[0],'sto1l':listapandas(fastk)[1],'sto2l':listapandas(fastk)[2],'sto3l':listapandas(fastk)[3],'sto4l':listapandas(fastk)[4],'sto5l':listapandas(fastk)[5],'sto6l':listapandas(fastk)[6],'sto7l':listapandas(fastk)[7], 'stos':listapandas(fastd)[0],'sto1s':listapandas(fastd)[1],'sto2s':listapandas(fastd)[2],'sto3s':listapandas(fastd)[3],'sto4s':listapandas(fastd)[4],'sto5s':listapandas(fastd)[5],'sto6s':listapandas(fastd)[6],'sto7s':listapandas(fastd)[7], 'Pred':pred},columns = ['p1','p2', 'p3','p4','p5','p6','p7','p8','rsi','rsi1','rsi2','rsi3','rsi4','rsi5','rsi6','rsi7','sto','sto1','sto2','sto3','sto4','sto5','sto6','sto7' ,'macd','macd1','macd2','macd3','macd4','macd5','macd6','macd7','macdl','macd1l','macd2l','macd3l','macd4l','macd5l','macd6l','macd7l','macds','macd1s','macd2s','macd3s','macd4s','macd5s','macd6s','macd7s','stol','sto1l','sto2l','sto3l','sto4l','sto5l','sto6l','sto7l','stos','sto1s','sto2s','sto3s','sto4s','sto5s','sto6s','sto7s' ,'Pred'], index=[412])
  
    return df



s = {}
k = 0
i = []

def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]
        
    
def run(a):
    close, open1, low, high, volume, nr_trocas, close_time, open_time = velas(a)
    rsi, adx, atr, ma50, ma100, ma200, wlc, macd, macdsignal, macdhist, upperband, middleband, lowerband, avg, fastk, fastd = indicadores (open1 , close , high , low)

    ma = ma200.tolist()
    
    if prever(datapandas(a))[0] == 0:
        set_key(s, str(a) , 0)
    if prever(datapandas(a))[0] == 1:
        set_key(s, str(a) , 1)   
        
    if k >=15:
        print('Lista S = ' ,s[a][-3], s[a][-2] , s[a][-1], '/',  str(a))
        if s[a][-3] == 0 and s[a][-2] == 1 and s[a][-1] == 1 and position(a)[0] == 0 and ma[-1] < open1[-1]:
            bot.send_message(-442907326, text = ('Posicao aberta --- alts/btc com moving average' + str(a)))
            startorder_tp(a)
            startorder_open(a)
    
    
while True:
    
    run('BTCUSDT')
    run('ETHUSDT')
    run('XRPUSDT')
    run('LTCUSDT')
    run('EOSUSDT')
    run('ADAUSDT')
    run('XLMUSDT')
    run('XMRUSDT')
    run('ZECUSDT')
    run('BNBUSDT')
    run('NEOUSDT')
    run('ATOMUSDT')
    run('DASHUSDT')
    run('VETUSDT')
    
    k += 5

    time.sleep(300)


















