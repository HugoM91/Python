# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 02:14:10 2020

@author: hugom
"""
import pandas as pd


df1 = pd.read_csv('sem_ad_buy.csv')

df2 = pd.read_csv('sem_ad_random.csv')
df3 = pd.read_csv('sem_ad_random2.csv')
"""

df4 = pd.read_csv('alt_random_final4.csv')
df5 = pd.read_csv('alt_random_final5.csv')

df6 = pd.read_csv('ab7.csv')
df7 = pd.read_csv('ab8.csv')
df8 = pd.read_csv('ab9.csv')
df9 = pd.read_csv('ab10.csv')
df10 = pd.read_csv('ab11.csv')
df = pd.read_csv('ab5.csv')
df11 = pd.read_csv('ab13.csv')
df12 = pd.read_csv('ab14.csv')
df13 = pd.read_csv('ab12.csv')
df14 = pd.read_csv('ab15.csv')
df15 = pd.read_csv('ab16.csv')
df16 = pd.read_csv('ab17.csv')
df17 = pd.read_csv('ab18.csv')
df18 = pd.read_csv('ab19.csv')
df19 = pd.read_csv('ab20.csv')
df20 = pd.read_csv('ab21.csv')
df21 = pd.read_csv('ab22.csv')
df22 = pd.read_csv('ab23.csv')
df23 = pd.read_csv('ab24.csv')
df24 = pd.read_csv('ab25.csv')
df25 = pd.read_csv('ab26.csv')
df26 = pd.read_csv('ab27.csv')
df27 = pd.read_csv('ab28.csv')
df28 = pd.read_csv('ab29.csv')
df29 = pd.read_csv('ab30.csv')
df30 = pd.read_csv('ab31.csv')
df31 = pd.read_csv('ab32.csv')
df32 = pd.read_csv('ab33.csv')
df33 = pd.read_csv('ab34.csv')
df34 = pd.read_csv('ab35.csv')
df35 = pd.read_csv('ab36.csv')
df36 = pd.read_csv('ab37.csv')
df37 = pd.read_csv('ab38.csv')
df38 = pd.read_csv('ab39.csv')
df39 = pd.read_csv('ab40.csv')


df_row = pd.concat([df , df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15 ,  df16, df17 ,df18, df19, df20, df21, df22, df23, df24, df25, df26, df27, df28, df29, df30, df31, df32, df33, df34, df35, df36, df37, df38, df39])
"""
df_row = pd.concat([df1, df2, df3])
df_row.to_csv(r'C:\Users\hugom\Desktop\Projecto\DataFrame\sem_ad_final.csv', index=False)

print(df_row)

