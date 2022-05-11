# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:04:19 2020

@author: hugom
"""

import pandas as pd

df = pd.read_csv('basedados2.csv')


df['p8'] = (df['p8'] * 100 / df['p7'] )-100
df['p7'] = (df['p7'] * 100 / df['p6'] )-100
df['p6'] = (df['p6'] * 100 / df['p5'] )-100
df['p5'] = (df['p5'] * 100 / df['p4'] )-100
df['p4'] = (df['p4'] * 100 / df['p3'] )-100
df['p3'] = (df['p3'] * 100 / df['p2'] )-100
df['p2'] = (df['p2'] * 100 / df['p1'] )-100
df2 = df.drop(['p1'], axis=1)

df2.to_csv(r'C:\Users\hugom\Desktop\Projecto\DataFrame\basedados_alt.csv', index=False)


print (df2)