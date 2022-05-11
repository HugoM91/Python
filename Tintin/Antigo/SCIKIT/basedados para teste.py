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

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('basedados1.csv')

dftest = df.drop('Pred' , axis=1)
dfpred = df['Pred']
        
np.random.seed(54)
    
x = dftest
y = dfpred
    
x_train, x_test, y_train, y_test = train_test_split(x , y , test_size = 0.2)

model2 = RandomForestClassifier(n_estimators = 100).fit(x_train,y_train)

y_pred = model2.score(x_test, y_test)


pickle.dump(model2, open('model2.pkl', 'wb'))











