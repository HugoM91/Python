# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:58:02 2020

@author: hugom
"""

import pandas as pd
import numpy as np

hd = pd.read_csv('binancedata_venda.csv')

x = hd.drop('Pred', axis=1)
y = hd['Pred']



from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators = 100)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split (x, y,test_size = 0.2) #divide a data em data para teste e data para treinar test_size define a percentagem data para treinar
                                                    #x_train = 80% da data, x_test = 20% da data

model = RandomForestClassifier(n_estimators = 100).fit(x_train,y_train)


y_preds = model.score(x_test , y_test)
y_preds2 = model.predict(x_train)

print(y_preds)
print(y_preds2)
