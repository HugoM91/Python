# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:08:07 2020

@author: hugom
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


df = pd.read_csv('testenovo.csv')

df = df.drop(df.index[:33])
df = df.drop('Open', axis = 1)
df = df.drop('Avg' , axis = 1)


df['Rsi2'] = df['Rsi'].shift(1)
df['Rsi3'] = df['Rsi'].shift(2)
df['Atr1'] = df['Atr'].shift(1)
df['Atr2'] = df['Atr'].shift(2)
df['Macd1'] = df['MacdDif'].shift(1)
df['Macd2'] = df['MacdDif'].shift(2)

df = df.drop(df.index[:3])

df_pred = df['Close']
df_pred2 = df_pred.shift(1)
df_pred2[:1].fillna(6000, inplace= True)


np.random.seed(84)

x=df
y=df_pred2

x_train, x_test, y_train, y_test = train_test_split(x , y, test_size=0.2)

model = LinearRegression().fit(x_train, y_train)

y_pred = model.predict(x_test)

u =np.array(y_test)

print(model.score(x_test, y_test))





"""
fig , ax1 = plt.subplots()
ax2 = ax1.twinx()

print(u)
ax1.plot(u[20:60], 'r')
ax2.plot(y_pred[20:60], 'b')

plt.plot()
"""





























