# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:42:15 2020

@author: hugom
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

df = pd.read_csv('basedados1.csv')

dftest = df.drop('Pred' , axis=1)
dfpred = df['Pred']

def prever(df_test , df_train , model):
        
    np.random.seed(54)
    
    x = df_test
    y = df_train
    
    x_train, x_test, y_train, y_test = train_test_split(x , y , test_size = 0.2)

    model2 = model().fit(x_train,y_train)

    y_pred = model2.score(x_test, y_test)

    print(y_pred)

    u = np.array(y_test)

    print(model2.predict(np.array(x_test)))
    print(u)

    print('-----------')

prever (dftest, dfpred, RandomForestRegressor)
prever (dftest, dfpred, RandomForestClassifier)
prever (dftest, dfpred, LinearRegression)

"""
print(y_pred2)

u = np.array(y_test)

print(model2.predict(np.array(x_test)))
print(u)

i_preds = model2.predict(x_test)
print(np.mean(i_preds == y_test))
"""














