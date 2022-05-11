# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 02:32:43 2020

@author: hugom
"""
from binance.client import Client
from statistics import mean
from binancedata import velas
from indicadores import indicadores
import pandas as pd

client = Client('s5jgqnUryEPYD7oCz5uCdAQimuCIHag5OzmSmVkvyRc2pIVPWPZd8mNx3jyDCdbj', '9QWGd9JTXt76ufl9PE3ocW5D1suikdGgylyKPgzecpDYmhXmBCRmX9DgNQ74pxZU')
 

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
    
    for x,y in zip (macd, macdsignal):
        macddif.append(x - y)
    for x,y in zip(fastk, fastd):
        stodif.append(x - y)
    
    
    df = pd.DataFrame({'p1': listapandas(wlc)[0], 'p2':listapandas(wlc)[1], 'p3':listapandas(wlc)[2],'p4':listapandas(wlc)[3], 'p5':listapandas(wlc)[4], 'p6':listapandas(wlc)[5], 'p7':listapandas(wlc)[6],'p8':listapandas(wlc)[7], 'rsi':listapandas(rsi)[0], 'rsi1':listapandas(rsi)[1],'rsi2':listapandas(rsi)[2], 'rsi3':listapandas(rsi)[3], 'rsi4':listapandas(rsi)[4], 'rsi5':listapandas(rsi)[5], 'rsi6':listapandas(rsi)[6], 'rsi7':listapandas(rsi)[7], 'sto':listapandas(stodif)[0],'sto1':listapandas(stodif)[1],'sto2':listapandas(stodif)[2],'sto3':listapandas(stodif)[3],'sto4':listapandas(stodif)[4],'sto5':listapandas(stodif)[5],'sto6':listapandas(stodif)[6],'sto7':listapandas(stodif)[7] ,'macd':listapandas(macddif)[0],'macd1':listapandas(macddif)[1],'macd2':listapandas(macddif)[2],'macd3':listapandas(macddif)[3] ,'macd4':listapandas(macddif)[4],'macd5':listapandas(macddif)[5],'macd6':listapandas(macddif)[6],'macd7':listapandas(macddif)[7]},columns = ['p1','p2', 'p3','p4','p5','p6','p7','p8','rsi','rsi1','rsi2','rsi3','rsi4','rsi5','rsi6','rsi7','sto','sto1','sto2','sto3','sto4','sto5','sto6','sto7' ,'macd','macd1','macd2','macd3','macd4','macd5','macd6','macd7'], index=[0])
    print(df)
    df.to_csv(r'C:\Users\hugom\Desktop\Projecto\DataFrame\seraqueedesta2.csv', index=False)
    
datapandas('BTCUSDT')

        
        
        
        
        
        
        
        
        
        
        
        
        
        