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
    
    df = pd.read_csv('binancedata_venda.csv')
    #print(df)
    df_real = pd.concat([df, lista])

    #print(df_real)
    
    dftest = df_real.drop('Pred' , axis=1)
    dfpred = df_real['Pred']

    
    np.random.seed(54)    
    x = dftest
    y = dfpred    
    
    #x_train, x_test, y_train, y_test = train_test_split(x , y , test_size = 0.2)
    #model2 = RandomForestClassifier(n_estimators = 100).fit(x_train,y_train)
    #y_pred = model2.score(x_test, y_test)
    
    x_train = x[x.index <= 141]
    x_test = x[x.index == 142]
    y_train = y[y.index <= 141]
    y_test = y[y.index == 142]
    
    model = RandomForestClassifier(n_estimators = 100).fit(x_train,y_train)
    model2 = RandomForestRegressor(n_estimators = 100).fit(x_train,y_train)
    #model3 = LinearRegression().fit(x_train,y_train)
    #model4 = KNeighborsClassifier().fit(x_train, y_train)
    #model5 = svm.SVC(kernel='rbf' , C=1, gamma = 'auto' ).fit(x_train, y_train)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    
    #a = model.score(x_test, y_test)
    #b = model2.score(x_test, y_test)
    #c = model3.score(x_test, y_test)
    #d = model4.score(x_test, y_test)
    
    a1 = model.predict(x_test)
    b1 = model2.predict(x_test)
    #c1 = model3.predict(x_test)
    #d1 = model4.predict(x_test) #nao funciona
    #e1 = model5.predict(x_test)
    
    #print(current_time)
    #print(a1)
    #print(b1)
    #print(c1)
    #print(d1)
    #print(e1)
    #print('----------')
    
    if b1 <= -0.9:
        print ('-------B maior que 0.92--------')
        print(current_time)
        
    return a1 , b1
        
    











