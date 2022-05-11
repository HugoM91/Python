# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 02:14:10 2020

@author: hugom
"""
import pandas as pd


df1 = pd.read_csv('sinalrandom.csv')
df2 = pd.read_csv('sinalrandom2.csv')
df3 = pd.read_csv('sinalvenda.csv')



"""
df3 = pd.read_csv('s3.csv')
df4 = pd.read_csv('s4.csv')
df5 = pd.read_csv('s6.csv')
df6 = pd.read_csv('s7.csv')
df7 = pd.read_csv('s8.csv')
df8 = pd.read_csv('s9.csv')
df9 = pd.read_csv('s10.csv')
df10 = pd.read_csv('s11.csv')
df11 = pd.read_csv('s13.csv')
df12 = pd.read_csv('s14.csv')
df13 = pd.read_csv('s12.csv')
df14 = pd.read_csv('s15.csv')
df15 = pd.read_csv('s16.csv')
df16 = pd.read_csv('s17.csv')
df17 = pd.read_csv('s18.csv')
df18 = pd.read_csv('s19.csv')
df19 = pd.read_csv('s20.csv')
df20 = pd.read_csv('s21.csv')
df21 = pd.read_csv('s22.csv')
df22 = pd.read_csv('s23.csv')
df23 = pd.read_csv('s24.csv')
df24 = pd.read_csv('s25.csv')
df25 = pd.read_csv('s26.csv')
df26 = pd.read_csv('s27.csv')
df27 = pd.read_csv('s28.csv')
df28 = pd.read_csv('s29.csv')
df29 = pd.read_csv('s30.csv')
df30 = pd.read_csv('s31.csv')
df31 = pd.read_csv('s32.csv')
df32 = pd.read_csv('s33.csv')
df33 = pd.read_csv('s34.csv')
df34 = pd.read_csv('s35.csv')
df35 = pd.read_csv('s36.csv')
df36 = pd.read_csv('s37.csv')
df37 = pd.read_csv('s38.csv')
df38 = pd.read_csv('s39.csv')
df39 = pd.read_csv('s40.csv')
df40 = pd.read_csv('s5.csv')
"""
#df_row = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36,df37,df38,df39,df40])
df_row = pd.concat([df1, df2, df3])
df_row.to_csv(r'C:\Users\hugom\Desktop\Projecto\DataFrame\binancedata_venda.csv', index=False)

print(df_row)
