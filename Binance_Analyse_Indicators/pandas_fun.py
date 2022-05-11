import pandas as pd

#import tkinter
#import matplotlib
#matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from data import candles



def create_graph(b, c, d):

    a = candles(b, c, d)
    ######    dicionary convert to DataFrame
    df = pd.DataFrame(a, columns=['time_open',  "high/low"])
    df1 = pd.DataFrame(a, columns=['time_open', "volume"])
    df2 = pd.DataFrame(a, columns=['time_open', "volume/trades"])
    df3 = pd.DataFrame(a, columns=['time_open', "rsi"])
    df4 = pd.DataFrame(a, columns=['time_open', "macd"])
    df5 = pd.DataFrame(a, columns=['time_open', "high", "close", "low"])

    #######    save graph
    fig = df.plot(x ='time_open', kind='line', secondary_y = True).get_figure()
    fig1 = df1.plot(x ='time_open', kind='line', secondary_y = True).get_figure()
    fig2 = df2.plot(x ='time_open', kind='line', secondary_y = True).get_figure()
    fig3 = df3.plot(x ='time_open', kind='line', secondary_y = True).get_figure()
    fig4 = df4.plot(x ='time_open', kind='line', secondary_y = True).get_figure()
    fig5 = df5.plot(x ='time_open', kind='line', secondary_y = True).get_figure()

    fig.savefig('test.png')
    fig1.savefig('test1.png')
    fig2.savefig('test2.png')
    fig3.savefig('test3.png')
    fig4.savefig('test4.png')
    fig5.savefig('test5.png')

    

    #######    show graph
    #df.plot(x ='time_open', kind='line', secondary_y = True)
    #plt.show()

#create_graph()
