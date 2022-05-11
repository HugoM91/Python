# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:06:50 2020

@author: hugom
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


df = pd.read_csv('testeRecente.csv')
df.drop(df.index[:14], inplace =True)


df['Rsi2'] = df['Rsi'].shift(1)
df['Rsi3'] = df['Rsi'].shift(2)
df['MacdDif2'] = df['MacdDif'].shift(1)
df['MacdDif3'] = df['MacdDif'].shift(2)
df['Atr2'] = df['Atr'].shift(1)
df['Atr3'] = df['Atr'].shift(2)


df.drop(df.index[:3], inplace =True)


df_prediction = df[['Avg']].shift(1)
df_prediction[:1].fillna(0, inplace=True)


x = df.drop('Avg', axis = 1)
y = df_prediction

np.random.seed(65)

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2)

model = LinearRegression().fit(x_train, y_train)

model.score(x_test,y_test)
y_pred = model.predict(x_test)


print(model.score(x_test,y_test))
#print(y_pred)
#print(y_test)

y2 = []
u = np.array(y_test)
#print(u)
#plt.plot(y_pred)
#plt.plot(u, 'r', secondary_axis=True)


fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

ax1.plot(y_pred[:], 'g-')
ax2.plot(u[:], 'r-')



plt.show()



