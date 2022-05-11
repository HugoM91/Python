# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:55:46 2020

@author: hugom
"""

import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt


df = pd.read_csv('4_mar_15m_24_mar.csv')
#plt.figure(figsize=(16,8))
#plt.title('Avg')
#plt.plot(df['Avg'])

avgdf = df.filter(['Avg'])
data = avgdf.values
training_data_len = math.ceil(len(data) * .7)



scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data)
train_data = scaled_data[0:training_data_len, :]



x_train = []
y_train = []
for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])

    
x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))


model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.compile(optimizer='adam',loss='mean_squared_error')
model.fit(x_train, y_train, batch_size=1, epochs=1)


test_data = scaled_data[training_data_len - 60 :, :]

x_test = []
y_test = [data[training_data_len:, :]]

for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0])
    
x_test = np.array(x_test)
x_test = np.reshape(x_test,(x_test.shape[0], x_test.shape[1], 1))

predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

rmse = np.sqrt(np.mean(predictions - y_test)**2)

print(rmse)

train = data[:training_data_len]
valid = data[training_data_len:]

#valid['Predictions'] = predictions

plt.figure(figsize=(16,8))
plt.plot(train['Avg'])
plt.plot(valid[['Avg', predictions]])



























