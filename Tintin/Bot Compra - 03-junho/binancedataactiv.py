# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:57:37 2020

@author: hugom
"""

from binance.client import Client
import pandas as pd
from indicadores import indicadores
from statistics import mean
from learning_model import prever, prever1, prever2
import time
from abrir_posicao_futuros import startorder_open, position, startorder_tp
import telebot
from discord_webhook import DiscordWebhook

url_teste = 'https://discordapp.com/api/webhooks/717350806768189581/bWI72oh5kMEHXBhcgX78fEBP_OmtwZ5Lu7CF7teJyo5HBWkx-pNuLc60fI2CpRnL9qtQ'
client = Client('s5jgqnUryEPYD7oCz5uCdAQimuCIHag5OzmSmVkvyRc2pIVPWPZd8mNx3jyDCdbj', '9QWGd9JTXt76ufl9PE3ocW5D1suikdGgylyKPgzecpDYmhXmBCRmX9DgNQ74pxZU')
bot = telebot.TeleBot("1225240806:AAHAn7e8jOZ--ThHRvzw3NHIuEkHcSeGnUY")

s = []
s1=[]
s2=[]
r = [0,1]
u = [1]
k = []

def velas(a):
    klines = client.get_historical_klines(a, Client.KLINE_INTERVAL_1MINUTE , '2 hour ago UTC' )
    
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
    lista = lista[60:]
    novalista = []    
    a = int(len(lista)/16)

    novalista.append((mean(lista[:a])))
    novalista.append((mean(lista[a:a*2])))
    novalista.append((mean(lista[a*2:a*3])))
    novalista.append((mean(lista[a*3:a*4])))
    novalista.append((mean(lista[a*4:a*5])))
    novalista.append((mean(lista[a*5:a*6])))
    novalista.append((mean(lista[a*6:a*7])))
    novalista.append((mean(lista[a*7:a*8])))
    novalista.append((mean(lista[a*8:a*9])))
    novalista.append((mean(lista[a*9:a*10])))
    novalista.append((mean(lista[a*10:a*11])))
    novalista.append((mean(lista[a*11:a*12])))
    novalista.append((mean(lista[a*12:a*13])))
    novalista.append((mean(lista[a*13:a*14])))
    novalista.append((mean(lista[a*14:a*15])))
    novalista.append((mean(lista[a*15:])))
    
    return novalista
 
def datapandas (a):
    close, open1, low, high, volume, nr_trocas, close_time, open_time = velas(a)
    rsi, adx, atr, ma50, ma100, ma200, wlc, macd, macdsignal, macdhist, upperband, middleband, lowerband, avg, fastk, fastd, ad = indicadores (open1 , close , high , low, volume)
    macddif=[]
    stodif=[]
    pred =[0]
    for x,y in zip (macd, macdsignal):
        macddif.append(x - y)
    for x,y in zip(fastk, fastd):
        stodif.append(x - y)
        
    df = pd.DataFrame({'p1': listapandas(wlc)[0], 'p2':listapandas(wlc)[1], 'p3':listapandas(wlc)[2],
                       'p4':listapandas(wlc)[3], 'p5':listapandas(wlc)[4], 'p6':listapandas(wlc)[5], 
                       'p7':listapandas(wlc)[6],'p8':listapandas(wlc)[7],'p9':listapandas(wlc)[8],'p10':listapandas(wlc)[9],
                       'p11':listapandas(wlc)[10],'p12':listapandas(wlc)[11],'p13':listapandas(wlc)[12],'p14':listapandas(wlc)[13],
                       'p15':listapandas(wlc)[14],'p16':listapandas(wlc)[15], 'rsi':listapandas(rsi)[0], 
                       'rsi1':listapandas(rsi)[1],'rsi2':listapandas(rsi)[2], 'rsi3':listapandas(rsi)[3], 
                       'rsi4':listapandas(rsi)[4], 'rsi5':listapandas(rsi)[5], 'rsi6':listapandas(rsi)[6], 
                       'rsi7':listapandas(rsi)[7], 'rsi8':listapandas(rsi)[8],'rsi9':listapandas(rsi)[9],'rsi10':listapandas(rsi)[10],
                       'rsi11':listapandas(rsi)[11],'rsi12':listapandas(rsi)[12],'rsi13':listapandas(rsi)[13],'rsi14':listapandas(rsi)[14],
                       'rsi15':listapandas(rsi)[15], 'sto':listapandas(stodif)[0],'sto1':listapandas(stodif)[1],
                       'sto2':listapandas(stodif)[2],'sto3':listapandas(stodif)[3],'sto4':listapandas(stodif)[4],
                       'sto5':listapandas(stodif)[5],'sto6':listapandas(stodif)[6],'sto7':listapandas(stodif)[7] ,
                       'sto8':listapandas(stodif)[8] ,'sto9':listapandas(stodif)[9] ,'sto10':listapandas(stodif)[10] ,
                       'sto11':listapandas(stodif)[11] ,'sto12':listapandas(stodif)[12] ,'sto13':listapandas(stodif)[13] ,
                       'sto14':listapandas(stodif)[14] ,'sto15':listapandas(stodif)[15],
                       'macd':listapandas(macddif)[0],'macd1':listapandas(macddif)[1],'macd2':listapandas(macddif)[2],
                       'macd3':listapandas(macddif)[3] ,'macd4':listapandas(macddif)[4],'macd5':listapandas(macddif)[5],
                       'macd6':listapandas(macddif)[6],'macd7':listapandas(macddif)[7],'macd8':listapandas(macddif)[8],
                       'macd9':listapandas(macddif)[9],'macd10':listapandas(macddif)[10],'macd11':listapandas(macddif)[11],
                       'macd12':listapandas(macddif)[12],'macd13':listapandas(macddif)[13],'macd14':listapandas(macddif)[14],
                       'macd15':listapandas(macddif)[15], 'macdl':listapandas(macd)[0],
                       'macd1l':listapandas(macd)[1],'macd2l':listapandas(macd)[2],'macd3l':listapandas(macd)[3] ,
                       'macd4l':listapandas(macd)[4],'macd5l':listapandas(macd)[5],'macd6l':listapandas(macd)[6],
                       'macd7l':listapandas(macd)[7],'macd8l':listapandas(macd)[8],'macd9l':listapandas(macd)[9],'macd10l':listapandas(macd)[10],
                       'macd11l':listapandas(macd)[11],'macd12l':listapandas(macd)[12],'macd13l':listapandas(macd)[13],'macd14l':listapandas(macd)[14],
                       'macd15l':listapandas(macd)[15], 'macds':listapandas(macdsignal)[0],'macd1s':listapandas(macdsignal)[1],
                       'macd2s':listapandas(macdsignal)[2],'macd3s':listapandas(macdsignal)[3] ,'macd4s':listapandas(macdsignal)[4],
                       'macd5s':listapandas(macdsignal)[5],'macd6s':listapandas(macdsignal)[6],'macd7s':listapandas(macdsignal)[7], 
                       'macd8s':listapandas(macdsignal)[8], 'macd9s':listapandas(macdsignal)[9], 'macd10s':listapandas(macdsignal)[10],
                       'macd11s':listapandas(macdsignal)[11], 'macd12s':listapandas(macdsignal)[12], 'macd13s':listapandas(macdsignal)[13], 
                       'macd14s':listapandas(macdsignal)[14], 'macd15s':listapandas(macdsignal)[15], 
                       'macdh':listapandas(macdhist)[0],'macd1h':listapandas(macdhist)[1],
                       'macd2h':listapandas(macdhist)[2],'macd3h':listapandas(macdhist)[3] ,'macd4h':listapandas(macdhist)[4],
                       'macd5h':listapandas(macdhist)[5],'macd6h':listapandas(macdhist)[6],'macd7h':listapandas(macdhist)[7], 
                       'macd8h':listapandas(macdhist)[8], 'macd9h':listapandas(macdhist)[9], 'macd10h':listapandas(macdhist)[10],
                       'macd11h':listapandas(macdhist)[11], 'macd12h':listapandas(macdhist)[12], 'macd13h':listapandas(macdsignal)[13], 
                       'macd14h':listapandas(macdhist)[14], 'macd15h':listapandas(macdhist)[15],
                       'stol':listapandas(fastk)[0],'sto1l':listapandas(fastk)[1],'sto2l':listapandas(fastk)[2],
                       'sto3l':listapandas(fastk)[3],'sto4l':listapandas(fastk)[4],'sto5l':listapandas(fastk)[5],
                       'sto6l':listapandas(fastk)[6],'sto7l':listapandas(fastk)[7],'sto8l':listapandas(fastk)[8],
                       'sto9l':listapandas(fastk)[9],'sto10l':listapandas(fastk)[10],'sto11l':listapandas(fastk)[11],
                       'sto12l':listapandas(fastk)[12],'sto13l':listapandas(fastk)[13],'sto14l':listapandas(fastk)[14],
                       'sto15l':listapandas(fastk)[15], 'stos':listapandas(fastd)[0],
                       'sto1s':listapandas(fastd)[1],'sto2s':listapandas(fastd)[2],'sto3s':listapandas(fastd)[3],
                       'sto4s':listapandas(fastd)[4],'sto5s':listapandas(fastd)[5],'sto6s':listapandas(fastd)[6],
                       'sto7s':listapandas(fastd)[7],'sto8s':listapandas(fastd)[8],'sto9s':listapandas(fastd)[9],
                       'sto10s':listapandas(fastd)[10],'sto11s':listapandas(fastd)[11],'sto12s':listapandas(fastd)[12],
                       'sto13s':listapandas(fastd)[13],'sto14s':listapandas(fastd)[14],'sto15s':listapandas(fastd)[15],
                       'ad':listapandas(ad)[0],'ad1':listapandas(ad)[1],'ad2':listapandas(ad)[2],
                       'ad3':listapandas(ad)[3] ,'ad4':listapandas(ad)[4],'ad5':listapandas(ad)[5],
                       'ad6':listapandas(ad)[6],'ad7':listapandas(ad)[7],'ad8':listapandas(ad)[8],
                       'ad9':listapandas(ad)[9],'ad10':listapandas(ad)[10],'ad11':listapandas(ad)[11],
                       'ad12':listapandas(ad)[12],'ad13':listapandas(ad)[13],'ad14':listapandas(ad)[14],
                       'ad15':listapandas(ad)[15], 
                       'Pred':pred},columns = ['p1','p2', 'p3','p4','p5','p6','p7',
                                                                              'p8','p9','p10', 'p11','p12','p13','p14','p15',
                                                                              'p16','rsi','rsi1','rsi2','rsi3','rsi4',
                                                                              'rsi5','rsi6','rsi7','rsi8','rsi9','rsi10','rsi11','rsi12',
                                                                              'rsi13','rsi14','rsi15','sto','sto1','sto2',
                                                                              'sto3','sto4','sto5','sto6','sto7' ,'sto8','sto9','sto10',
                                                                              'sto11','sto12','sto13','sto14','sto15' ,'macd',
                                                                              'macd1','macd2','macd3','macd4','macd5','macd6',
                                                                              'macd7','macd8','macd9','macd10','macd11','macd12','macd13','macd14',
                                                                              'macd15','macdl','macd1l','macd2l','macd3l','macd4l'
                                                                              ,'macd5l','macd6l','macd7l','macd8l','macd9l','macd10l','macd11l','macd12l'
                                                                              ,'macd13l','macd14l','macd15l','macds','macd1s','macd2s',
                                                                              'macd3s','macd4s','macd5s','macd6s','macd7s','macd8s','macd9s','macd10s',
                                                                              'macd11s','macd12s','macd13s','macd14s','macd15s','macdh' ,'macd1h'
                                                                              ,'macd2h' ,'macd3h' ,'macd4h' ,'macd5h' ,'macd6h' ,'macd7h' ,'macd8h' ,
                                                                              'macd9h' ,'macd10h' ,'macd11h' ,'macd12h' ,'macd13h' ,'macd14h', 'macd15h'
                                                                              ,'stol','sto1l','sto2l','sto3l','sto4l','sto5l','sto6l','sto7l'
                                                                              ,'sto8l','sto9l','sto10l','sto11l','sto12l','sto13l','sto14l','sto15l'
                                                                              ,'stos','sto1s','sto2s','sto3s','sto4s','sto5s','sto6s',
                                                                              'sto7s' ,'sto8s','sto9s','sto10s','sto11s','sto12s','sto13s','sto14s',
                                                                              'sto15s' ,'ad' ,'ad1' ,'ad2' ,'ad3' ,'ad4' ,'ad5' ,'ad6' ,'ad7' ,'ad8' ,'ad9' ,
                                                                              'ad10' ,'ad11' ,'ad12' ,'ad13' ,'ad14' ,'ad15' ,'Pred'] ,index = [207])

    return df                                            
                                               
                                               
def datapandas2 (a):
    close, open1, low, high, volume, nr_trocas, close_time, open_time = velas(a)
    rsi, adx, atr, ma50, ma100, ma200, wlc, macd, macdsignal, macdhist, upperband, middleband, lowerband, avg, fastk, fastd, ad = indicadores (open1 , close , high , low, volume)
    macddif=[]
    stodif=[]
    pred =[0]
    for x,y in zip (macd, macdsignal):
        macddif.append(x - y)
    for x,y in zip(fastk, fastd):
        stodif.append(x - y)
        
    df = pd.DataFrame({'p1': listapandas(wlc)[0], 'p2':listapandas(wlc)[1], 'p3':listapandas(wlc)[2],
                       'p4':listapandas(wlc)[3], 'p5':listapandas(wlc)[4], 'p6':listapandas(wlc)[5], 
                       'p7':listapandas(wlc)[6],'p8':listapandas(wlc)[7],'p9':listapandas(wlc)[8],'p10':listapandas(wlc)[9],
                       'p11':listapandas(wlc)[10],'p12':listapandas(wlc)[11],'p13':listapandas(wlc)[12],'p14':listapandas(wlc)[13],
                       'p15':listapandas(wlc)[14],'p16':listapandas(wlc)[15], 'rsi':listapandas(rsi)[0], 
                       'rsi1':listapandas(rsi)[1],'rsi2':listapandas(rsi)[2], 'rsi3':listapandas(rsi)[3], 
                       'rsi4':listapandas(rsi)[4], 'rsi5':listapandas(rsi)[5], 'rsi6':listapandas(rsi)[6], 
                       'rsi7':listapandas(rsi)[7], 'rsi8':listapandas(rsi)[8],'rsi9':listapandas(rsi)[9],'rsi10':listapandas(rsi)[10],
                       'rsi11':listapandas(rsi)[11],'rsi12':listapandas(rsi)[12],'rsi13':listapandas(rsi)[13],'rsi14':listapandas(rsi)[14],
                       'rsi15':listapandas(rsi)[15], 'sto':listapandas(stodif)[0],'sto1':listapandas(stodif)[1],
                       'sto2':listapandas(stodif)[2],'sto3':listapandas(stodif)[3],'sto4':listapandas(stodif)[4],
                       'sto5':listapandas(stodif)[5],'sto6':listapandas(stodif)[6],'sto7':listapandas(stodif)[7] ,
                       'sto8':listapandas(stodif)[8] ,'sto9':listapandas(stodif)[9] ,'sto10':listapandas(stodif)[10] ,
                       'sto11':listapandas(stodif)[11] ,'sto12':listapandas(stodif)[12] ,'sto13':listapandas(stodif)[13] ,
                       'sto14':listapandas(stodif)[14] ,'sto15':listapandas(stodif)[15],
                       'macd':listapandas(macddif)[0],'macd1':listapandas(macddif)[1],'macd2':listapandas(macddif)[2],
                       'macd3':listapandas(macddif)[3] ,'macd4':listapandas(macddif)[4],'macd5':listapandas(macddif)[5],
                       'macd6':listapandas(macddif)[6],'macd7':listapandas(macddif)[7],'macd8':listapandas(macddif)[8],
                       'macd9':listapandas(macddif)[9],'macd10':listapandas(macddif)[10],'macd11':listapandas(macddif)[11],
                       'macd12':listapandas(macddif)[12],'macd13':listapandas(macddif)[13],'macd14':listapandas(macddif)[14],
                       'macd15':listapandas(macddif)[15], 'macdl':listapandas(macd)[0],
                       'macd1l':listapandas(macd)[1],'macd2l':listapandas(macd)[2],'macd3l':listapandas(macd)[3] ,
                       'macd4l':listapandas(macd)[4],'macd5l':listapandas(macd)[5],'macd6l':listapandas(macd)[6],
                       'macd7l':listapandas(macd)[7],'macd8l':listapandas(macd)[8],'macd9l':listapandas(macd)[9],'macd10l':listapandas(macd)[10],
                       'macd11l':listapandas(macd)[11],'macd12l':listapandas(macd)[12],'macd13l':listapandas(macd)[13],'macd14l':listapandas(macd)[14],
                       'macd15l':listapandas(macd)[15], 'macds':listapandas(macdsignal)[0],'macd1s':listapandas(macdsignal)[1],
                       'macd2s':listapandas(macdsignal)[2],'macd3s':listapandas(macdsignal)[3] ,'macd4s':listapandas(macdsignal)[4],
                       'macd5s':listapandas(macdsignal)[5],'macd6s':listapandas(macdsignal)[6],'macd7s':listapandas(macdsignal)[7], 
                       'macd8s':listapandas(macdsignal)[8], 'macd9s':listapandas(macdsignal)[9], 'macd10s':listapandas(macdsignal)[10],
                       'macd11s':listapandas(macdsignal)[11], 'macd12s':listapandas(macdsignal)[12], 'macd13s':listapandas(macdsignal)[13], 
                       'macd14s':listapandas(macdsignal)[14], 'macd15s':listapandas(macdsignal)[15], 
                       'macdh':listapandas(macdhist)[0],'macd1h':listapandas(macdhist)[1],
                       'macd2h':listapandas(macdhist)[2],'macd3h':listapandas(macdhist)[3] ,'macd4h':listapandas(macdhist)[4],
                       'macd5h':listapandas(macdhist)[5],'macd6h':listapandas(macdhist)[6],'macd7h':listapandas(macdhist)[7], 
                       'macd8h':listapandas(macdhist)[8], 'macd9h':listapandas(macdhist)[9], 'macd10h':listapandas(macdhist)[10],
                       'macd11h':listapandas(macdhist)[11], 'macd12h':listapandas(macdhist)[12], 'macd13h':listapandas(macdsignal)[13], 
                       'macd14h':listapandas(macdhist)[14], 'macd15h':listapandas(macdhist)[15],
                       'stol':listapandas(fastk)[0],'sto1l':listapandas(fastk)[1],'sto2l':listapandas(fastk)[2],
                       'sto3l':listapandas(fastk)[3],'sto4l':listapandas(fastk)[4],'sto5l':listapandas(fastk)[5],
                       'sto6l':listapandas(fastk)[6],'sto7l':listapandas(fastk)[7],'sto8l':listapandas(fastk)[8],
                       'sto9l':listapandas(fastk)[9],'sto10l':listapandas(fastk)[10],'sto11l':listapandas(fastk)[11],
                       'sto12l':listapandas(fastk)[12],'sto13l':listapandas(fastk)[13],'sto14l':listapandas(fastk)[14],
                       'sto15l':listapandas(fastk)[15], 'stos':listapandas(fastd)[0],
                       'sto1s':listapandas(fastd)[1],'sto2s':listapandas(fastd)[2],'sto3s':listapandas(fastd)[3],
                       'sto4s':listapandas(fastd)[4],'sto5s':listapandas(fastd)[5],'sto6s':listapandas(fastd)[6],
                       'sto7s':listapandas(fastd)[7],'sto8s':listapandas(fastd)[8],'sto9s':listapandas(fastd)[9],
                       'sto10s':listapandas(fastd)[10],'sto11s':listapandas(fastd)[11],'sto12s':listapandas(fastd)[12],
                       'sto13s':listapandas(fastd)[13],'sto14s':listapandas(fastd)[14],'sto15s':listapandas(fastd)[15], 
                       'Pred':pred},columns = ['p1','p2', 'p3','p4','p5','p6','p7',
                                                                              'p8','p9','p10', 'p11','p12','p13','p14','p15',
                                                                              'p16','rsi','rsi1','rsi2','rsi3','rsi4',
                                                                              'rsi5','rsi6','rsi7','rsi8','rsi9','rsi10','rsi11','rsi12',
                                                                              'rsi13','rsi14','rsi15','sto','sto1','sto2',
                                                                              'sto3','sto4','sto5','sto6','sto7' ,'sto8','sto9','sto10',
                                                                              'sto11','sto12','sto13','sto14','sto15' ,'macd',
                                                                              'macd1','macd2','macd3','macd4','macd5','macd6',
                                                                              'macd7','macd8','macd9','macd10','macd11','macd12','macd13','macd14',
                                                                              'macd15','macdl','macd1l','macd2l','macd3l','macd4l'
                                                                              ,'macd5l','macd6l','macd7l','macd8l','macd9l','macd10l','macd11l','macd12l'
                                                                              ,'macd13l','macd14l','macd15l','macds','macd1s','macd2s',
                                                                              'macd3s','macd4s','macd5s','macd6s','macd7s','macd8s','macd9s','macd10s',
                                                                              'macd11s','macd12s','macd13s','macd14s','macd15s','macdh' ,'macd1h'
                                                                              ,'macd2h' ,'macd3h' ,'macd4h' ,'macd5h' ,'macd6h' ,'macd7h' ,'macd8h' ,
                                                                              'macd9h' ,'macd10h' ,'macd11h' ,'macd12h' ,'macd13h' ,'macd14h', 'macd15h'
                                                                              ,'stol','sto1l','sto2l','sto3l','sto4l','sto5l','sto6l','sto7l'
                                                                              ,'sto8l','sto9l','sto10l','sto11l','sto12l','sto13l','sto14l','sto15l'
                                                                              ,'stos','sto1s','sto2s','sto3s','sto4s','sto5s','sto6s',
                                                                              'sto7s' ,'sto8s','sto9s','sto10s','sto11s','sto12s','sto13s','sto14s',
                                                                              'sto15s' ,'Pred'],  index = [207])
    return df

def datapandas3 (a):
    
    close, open1, low, high, volume, nr_trocas, close_time, open_time = velas(a)
    rsi, adx, atr, ma50, ma100, ma200, wlc, macd, macdsignal, macdhist, upperband, middleband, lowerband, avg, fastk, fastd, ad = indicadores (open1 , close , high , low, volume)
    macddif=[]
    stodif=[]
    pred =[0]
    for x,y in zip (macd, macdsignal):
        macddif.append(x - y)
    for x,y in zip(fastk, fastd):
        stodif.append(x - y)
        
    df = pd.DataFrame({'p1': listapandas(wlc)[0], 'p2':listapandas(wlc)[1], 'p3':listapandas(wlc)[2],
                       'p4':listapandas(wlc)[3], 'p5':listapandas(wlc)[4], 'p6':listapandas(wlc)[5], 
                       'p7':listapandas(wlc)[6],'p8':listapandas(wlc)[7],'p9':listapandas(wlc)[8],'p10':listapandas(wlc)[9],
                       'p11':listapandas(wlc)[10],'p12':listapandas(wlc)[11],'p13':listapandas(wlc)[12],'p14':listapandas(wlc)[13],
                       'p15':listapandas(wlc)[14],'p16':listapandas(wlc)[15], 'rsi':listapandas(rsi)[0], 
                       'rsi1':listapandas(rsi)[1],'rsi2':listapandas(rsi)[2], 'rsi3':listapandas(rsi)[3], 
                       'rsi4':listapandas(rsi)[4], 'rsi5':listapandas(rsi)[5], 'rsi6':listapandas(rsi)[6], 
                       'rsi7':listapandas(rsi)[7], 'rsi8':listapandas(rsi)[8],'rsi9':listapandas(rsi)[9],'rsi10':listapandas(rsi)[10],
                       'rsi11':listapandas(rsi)[11],'rsi12':listapandas(rsi)[12],'rsi13':listapandas(rsi)[13],'rsi14':listapandas(rsi)[14],
                       'rsi15':listapandas(rsi)[15], 
                       'macd':listapandas(macddif)[0],'macd1':listapandas(macddif)[1],'macd2':listapandas(macddif)[2],
                       'macd3':listapandas(macddif)[3] ,'macd4':listapandas(macddif)[4],'macd5':listapandas(macddif)[5],
                       'macd6':listapandas(macddif)[6],'macd7':listapandas(macddif)[7],'macd8':listapandas(macddif)[8],
                       'macd9':listapandas(macddif)[9],'macd10':listapandas(macddif)[10],'macd11':listapandas(macddif)[11],
                       'macd12':listapandas(macddif)[12],'macd13':listapandas(macddif)[13],'macd14':listapandas(macddif)[14],
                       'macd15':listapandas(macddif)[15], 'macdl':listapandas(macd)[0],
                       'macd1l':listapandas(macd)[1],'macd2l':listapandas(macd)[2],'macd3l':listapandas(macd)[3] ,
                       'macd4l':listapandas(macd)[4],'macd5l':listapandas(macd)[5],'macd6l':listapandas(macd)[6],
                       'macd7l':listapandas(macd)[7],'macd8l':listapandas(macd)[8],'macd9l':listapandas(macd)[9],'macd10l':listapandas(macd)[10],
                       'macd11l':listapandas(macd)[11],'macd12l':listapandas(macd)[12],'macd13l':listapandas(macd)[13],'macd14l':listapandas(macd)[14],
                       'macd15l':listapandas(macd)[15], 'macds':listapandas(macdsignal)[0],'macd1s':listapandas(macdsignal)[1],
                       'macd2s':listapandas(macdsignal)[2],'macd3s':listapandas(macdsignal)[3] ,'macd4s':listapandas(macdsignal)[4],
                       'macd5s':listapandas(macdsignal)[5],'macd6s':listapandas(macdsignal)[6],'macd7s':listapandas(macdsignal)[7], 
                       'macd8s':listapandas(macdsignal)[8], 'macd9s':listapandas(macdsignal)[9], 'macd10s':listapandas(macdsignal)[10],
                       'macd11s':listapandas(macdsignal)[11], 'macd12s':listapandas(macdsignal)[12], 'macd13s':listapandas(macdsignal)[13], 
                       'macd14s':listapandas(macdsignal)[14], 'macd15s':listapandas(macdsignal)[15], 
                       'macdh':listapandas(macdhist)[0],'macd1h':listapandas(macdhist)[1],
                       'macd2h':listapandas(macdhist)[2],'macd3h':listapandas(macdhist)[3] ,'macd4h':listapandas(macdhist)[4],
                       'macd5h':listapandas(macdhist)[5],'macd6h':listapandas(macdhist)[6],'macd7h':listapandas(macdhist)[7], 
                       'macd8h':listapandas(macdhist)[8], 'macd9h':listapandas(macdhist)[9], 'macd10h':listapandas(macdhist)[10],
                       'macd11h':listapandas(macdhist)[11], 'macd12h':listapandas(macdhist)[12], 'macd13h':listapandas(macdsignal)[13], 
                       'macd14h':listapandas(macdhist)[14], 'macd15h':listapandas(macdhist)[15],
                        
                       'Pred':pred},columns = ['p1','p2', 'p3','p4','p5','p6','p7',
                                                                              'p8','p9','p10', 'p11','p12','p13','p14','p15',
                                                                              'p16','rsi','rsi1','rsi2','rsi3','rsi4',
                                                                              'rsi5','rsi6','rsi7','rsi8','rsi9','rsi10','rsi11','rsi12',
                                                                              'rsi13','rsi14','rsi15','macd',
                                                                              'macd1','macd2','macd3','macd4','macd5','macd6',
                                                                              'macd7','macd8','macd9','macd10','macd11','macd12','macd13','macd14',
                                                                              'macd15','macdl','macd1l','macd2l','macd3l','macd4l'
                                                                              ,'macd5l','macd6l','macd7l','macd8l','macd9l','macd10l','macd11l','macd12l'
                                                                              ,'macd13l','macd14l','macd15l','macds','macd1s','macd2s',
                                                                              'macd3s','macd4s','macd5s','macd6s','macd7s','macd8s','macd9s','macd10s',
                                                                              'macd11s','macd12s','macd13s','macd14s','macd15s','macdh' ,'macd1h'
                                                                              ,'macd2h' ,'macd3h' ,'macd4h' ,'macd5h' ,'macd6h' ,'macd7h' ,'macd8h' ,
                                                                              'macd9h' ,'macd10h' ,'macd11h' ,'macd12h' ,'macd13h' ,'macd14h', 'macd15h'
                                                                              ,'Pred'] , index = [207] )
                                                                              
    return df




def run(a):
    print(s, 'lista')
    if len(s) == 2:
        if s[0] == r[0] and s[1] == r[1] and position(a)[0] == 0:
            webhook = DiscordWebhook(url_teste , content= ('Abrir posicao com ad')))
            response = webhook.execute()
    if prever(datapandas(a))[0] == 0:
        if len(s) == 2:
            del s[0]
        s.append(0)
    if prever(datapandas(a))[0] == 1:
        if len(s) == 2:
            del s[0]
        s.append(1)
    
def run1(a):
    print(s1, 'listas1')
    if len(s1) == 2:
        if s1[0] == r[0] and s1[1] == r[1] and position(a)[0] == 0:
            webhook = DiscordWebhook(url_teste , content= ('Abrir posicao sem ad')))
            response = webhook.execute()
    if prever1(datapandas2(a))[0] == 0:
        if len(s1) == 2:
            del s1[0]
        s1.append(0)
    if prever1(datapandas2(a))[0] == 1:
        if len(s1) == 2:
            del s1[0]
        s1.append(1)
        
def run2(a):
    print(s2, 'listas2')
    if len(s2) == 2:
        if s2[0] == r[0] and s2[1] == r[1] and position(a)[0] == 0:
            webhook = DiscordWebhook(url_teste , content= ('Abrir posicao macd e rsi'))
            response = webhook.execute()
    if prever2(datapandas3(a))[0] == 0:
        if len(s2) == 2:
            del s2[0]
        s2.append(0)
        
    if prever2(datapandas3(a))[0] == 1:
        if len(s2) == 2:
            del s2[0]
        s2.append(1)
        


while True:
    
    run('BTCUSDT')
    run1('BTCUSDT')
    run2('BTCUSDT')
    time.sleep(300)




















