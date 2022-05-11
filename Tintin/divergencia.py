# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:00:17 2020

@author: hugom
"""

from datetime import datetime



def divrsi (price, ind ,nome, time, velas_atras):
    
    if isinstance(price, list):
        pass
    else:
        price = price.tolist()
        
    p = price[-velas_atras:]
    in1 = ind[-velas_atras:] 
    time = time[-velas_atras:]

    in1 = in1.tolist()

    max_price = max(p)
    max_p_index = p.index(max_price)
    in1_max_price = in1[max_p_index]
    
    t = time[max_p_index]
    t = t/1000
    t = datetime.fromtimestamp(t)
    t = t.strftime('%Y-%m-%d %H:%M')
    
    max_ind = max(in1)
    max_in1_index = in1.index(max_ind)
    price_max_in1 = p[max_in1_index]
    
    preco_zeroquatro =  price_max_in1 + (price_max_in1 * 0.1)
    
    if price_max_in1 < max_price and max_ind > in1_max_price and max_in1_index < max_p_index :
        print( nome , 'sell rsi' , t)
    else:
        print('flop')
        
    min_price = min(p) #preco minimo
    min_p_index = p.index(min_price) # index valor preco minimo
    in1_min_price = in1[min_p_index] # valor indicador preco minimo
    
    t = time[min_p_index]
    t = t/1000
    t = datetime.fromtimestamp(t)
    t = t.strftime('%Y-%m-%d %H:%M')
    
    min_ind = min(in1) # indicador minimo
    min_in1_index = in1.index(min_ind) # index valor minimo indicador
    price_min_in1 = p[min_in1_index]
    
    preco_zeroquatro =  price_min_in1 - (price_min_in1 * 0.1)
    
    if price_min_in1 > min_price and min_ind < in1_min_price and min_in1_index < min_p_index :
        print( nome , 'buy rsi' , t)
    else:
        print('flop')
        
        
def divmacd (price, ind ,nome, time, velas_atras):
   
    if isinstance(price, list):
        pass
    else:
        price = price.tolist()
        
    p = price[-velas_atras:]
    in1 = ind[-velas_atras:] 
    time = time[-velas_atras:]

    in1 = in1.tolist()

    max_price = max(p)
    max_p_index = p.index(max_price)
    in1_max_price = in1[max_p_index]
    
    t = time[max_p_index]
    t = t/1000
    t = datetime.fromtimestamp(t)
    t = t.strftime('%Y-%m-%d %H:%M')
    
    max_ind = max(in1)
    max_in1_index = in1.index(max_ind)
    price_max_in1 = p[max_in1_index]
    
    preco_zeroquatro =  price_max_in1 + (price_max_in1 * 0.1)
    
    if price_max_in1 < max_price and max_ind > in1_max_price and max_in1_index < max_p_index :
        print( nome , 'sell macd' , t)
    else:
        print('flop')
        
    min_price = min(p) #preco minimo
    min_p_index = p.index(min_price) # index valor preco minimo
    in1_min_price = in1[min_p_index] # valor indicador preco minimo
    
    t = time[min_p_index]
    t = t/1000
    t = datetime.fromtimestamp(t)
    t = t.strftime('%Y-%m-%d %H:%M')
    
    min_ind = min(in1) # indicador minimo
    min_in1_index = in1.index(min_ind) # index valor minimo indicador
    price_min_in1 = p[min_in1_index]
    
    preco_zeroquatro =  price_min_in1 - (price_min_in1 * 0.1)
    
    if price_min_in1 > min_price and min_ind < in1_min_price and min_in1_index < min_p_index :
        print( nome , 'buy macd' , t)
    else:
        print('flop')


    
    