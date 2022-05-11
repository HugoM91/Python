# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:44:36 2020

@author: hugom
"""
from binance.client import Client
from datetime import datetime


def volumesantigos(opentime, closetime , a):
    client = Client('s5jgqnUryEPYD7oCz5uCdAQimuCIHag5OzmSmVkvyRc2pIVPWPZd8mNx3jyDCdbj', '9QWGd9JTXt76ufl9PE3ocW5D1suikdGgylyKPgzecpDYmhXmBCRmX9DgNQ74pxZU')
    trades = client.get_aggregate_trades(symbol=a, startTime = int(opentime), endTime= int(closetime))
        
    soma =[]
    buy= []
    sell= []

    for x in trades:
        soma.append(float(x['q']))
        if x['m'] == True:
            sell.append(float(x['q']))
        else:
            buy.append(float(x['q']))
        
    t = opentime 
    t = t/1000
    t = datetime.fromtimestamp(t)
    t = t.strftime('%Y-%m-%d %H:%M:%S')
    
    #print(t)
    lista = [sum(soma), sum(buy), sum(sell)]
    
    return lista

def volumesantigos2(closetime, a, minutos):
    minutos = -minutos -1
    total = []
    soma=[]
    buy=[]
    sell=[]
    l = -1
    l2=0
    minu = 0
    opentime = closetime - 59999.0
    
    while l != minutos:
        total.append(volumesantigos(opentime - (minu*l2), closetime - (minu*l2), a))

        l-=1
        soma.append(total[l2][0])
        buy.append(total[l2][1])
        sell.append(total[l2][2])
        l2+=1
        minu = 59999.0
        
        
    return sum(buy), sum(sell)
        
        
"""
    terco = len(soma)/3
    terco = int(terco)

    print('soma =' , sum(soma))
    print(sum(buy)-sum(sell))
    print(sum(buy[:terco])-sum(sell[:terco]))
    print(sum(buy[terco:terco*2])-sum(sell[terco:terco*2]))
    print(sum(buy[terco*2:])-sum(sell[terco*2:]))
    print('----------------')
"""   
    











