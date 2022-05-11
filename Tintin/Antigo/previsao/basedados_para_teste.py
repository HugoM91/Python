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


def prever(lista):
    
    df = pd.read_csv('basedados1.csv')
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
    
    x_train = x[x.index < 104]
    x_test = x[x.index >= 105]
    y_train = y[y.index < 104]
    y_test = y[y.index >= 105]
    
    model = RandomForestClassifier(n_estimators = 100).fit(x_train,y_train)
    model2 = RandomForestRegressor(n_estimators = 100).fit(x_train,y_train)
    model3 = LinearRegression().fit(x_train,y_train)
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    
    a = model.predict(x_test)
    b = model2.predict(x_test)
    c = model3.predict(x_test)
    

    if a == 1:
        print(current_time)
        print(a)
        print(b)
        print(c)
        print('----------')
        
    
    











