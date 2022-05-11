# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:56:37 2020

@author: hugom
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:42:15 2020

@author: hugom
"""
from datetime import datetime

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import pickle
from indicadores import indicadores
from statistics import mean
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm


def prever(lista):
    
    df = pd.read_csv('com_ad_final.csv')
    
    df_real = pd.concat([df, lista])
    
    dftest = df_real.drop('Pred' , axis=1)
    dfpred = df_real['Pred']
    
    np.random.seed(54)    
    x = dftest
    y = dfpred    
        
    x_train = x[x.index <= 206]
    x_test = x[x.index == 207]
    y_train = y[y.index <= 206]
    y_test = y[y.index == 207]
    
    model = RandomForestClassifier(n_estimators = 100).fit(x_train,y_train)

    a1 = model.predict(x_test)

    print(a1 , ' 1')
    return a1 
        
def prever1(lista):
    
    df = pd.read_csv('sem_ad_final.csv')
    
    df_real = pd.concat([df, lista])
    
    dftest = df_real.drop('Pred' , axis=1)
    dfpred = df_real['Pred']
    
    np.random.seed(54)    
    x = dftest
    y = dfpred    
        
    x_train = x[x.index <= 206]
    x_test = x[x.index == 207]
    y_train = y[y.index <= 206]
    y_test = y[y.index == 207]
    
    model = RandomForestClassifier(n_estimators = 100).fit(x_train,y_train)

    a1 = model.predict(x_test)
    print(a1 , ' 2')
    return a1    


def prever2(lista):
    
    df = pd.read_csv('rsi_macd_final.csv')
    
    df_real = pd.concat([df, lista])
    
    dftest = df_real.drop('Pred' , axis=1)
    dfpred = df_real['Pred']
    
    np.random.seed(54)    
    x = dftest
    y = dfpred    
        
    x_train = x[x.index <= 206]
    x_test = x[x.index == 207]
    y_train = y[y.index <= 206]
    y_test = y[y.index == 207]
    
    model = RandomForestClassifier(n_estimators = 100).fit(x_train,y_train)

    a1 = model.predict(x_test)
    print(a1 , ' 3')
    return a1 








