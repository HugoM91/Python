import datetime
from key import client
from indicators import rsi, a_d, macd, obv,sto, true_range, true_avg, ema, sma
import pyti
from binance.client import Client
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


# cria um dicionario
def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]

# cria imagens yahoo stocks
def candles_stock(symbol,nr_dias):

    ret = {} # dicionary onde os dados sao processados [0]

    tick = yf.Ticker(symbol)
    hist = tick.history(period = str(nr_dias) + "d")

    set_key(ret,"hist",hist)
    set_key(ret,"sustainability",tick.sustainability)
    set_key(ret,"recommendations",tick.recommendations[-10:])
    set_key(ret,"calendar",tick.calendar)
    set_key(ret,"institutional_holders",tick.institutional_holders)
    set_key(ret,"major_holders",tick.major_holders)
    set_key(ret,"mutualfund_holders",tick.mutualfund_holders)
    set_key(ret,"actions",tick.actions)

    for x, y in tick.info.items():
        f = ["sector","fullTimeEmployees","longBusinessSummary","country","industry",
        "marketCap","fiftyDayAverage","twoHundredDayAverage","regularMarketOpen",
        "averageDailyVolume10Day","averageVolume","shortName"]
        if x in f:
            set_key(ret, x.upper(), y)

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    df = tick.sustainability
    ax.table(cellText=df.values, rowLabels=df.index, cellLoc='center',
                 colColours=['gainsboro'] * len(df), colLabels=df.columns, loc='center',)
    fig.tight_layout()
    fig.savefig('test.png')

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    df = tick.major_holders
    ax.table(cellText=df.values, rowLabels=df.index, cellLoc='center',
                 colColours=['gainsboro'] * len(df), colLabels=df.columns, loc='center',)
    fig.tight_layout()
    fig.savefig('test1.png')

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    df = tick.institutional_holders
    ax.table(cellText=df.values, rowLabels=df.index, cellLoc='center',
                 colColours=['gainsboro'] * len(df), colLabels=df.columns, loc='center',)
    fig.tight_layout()
    fig.savefig('test2.png')

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    df = tick.mutualfund_holders
    ax.table(cellText=df.values, rowLabels=df.index, cellLoc='center',
                 colColours=['gainsboro'] * len(df), colLabels=df.columns, loc='center',)

    fig.tight_layout()
    fig.savefig('test3.png')

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    return ret


def symbols():
    d_sym = {}
    prices = client.get_all_tickers()

    for x in prices:
        if x["symbol"].endswith("BTC"):
            set_key(d_sym, "BTC", x["symbol"][:-3])
        if x["symbol"].endswith("USDT"):
            set_key(d_sym, "USDT", x["symbol"][:-4])
        if x["symbol"].endswith("ETH"):
            set_key(d_sym, "ETH", x["symbol"][:-3])
        if x["symbol"].endswith("BNB"):
            set_key(d_sym, "BNB", x["symbol"][:-3])

    return d_sym

# return um dicionario crypto com (open, close, rsi, volume etc...)
def candles(symbol, symbol2, candle_time):
    d_candle = {}
    error = {"candle time" : "incorrect"}

    if candle_time != '1D' and candle_time != '4H' and candle_time != '1H' and candle_time != '30M':
        return error
    if candle_time == '1D':
        candles2 = client.get_klines(symbol= (symbol + symbol2), interval=client.KLINE_INTERVAL_1DAY, limit = 250) #limit = 500 = default
    elif candle_time == '4H':
        candles2 = client.get_klines(symbol= (symbol + symbol2), interval=client.KLINE_INTERVAL_4HOUR, limit = 250) #limit = 500 = default
    elif candle_time == '1H':
        candles2 = client.get_klines(symbol= (symbol + symbol2), interval=client.KLINE_INTERVAL_1HOUR, limit = 300) #limit = 500 = default
    else:
        candles2 = client.get_klines(symbol= (symbol + symbol2), interval=client.KLINE_INTERVAL_30MINUTE, limit = 500) #limit = 500 = default

    for x in candles2:
        i = 0
        while (i < len(x)):
            x[i] = float(x[i])
            if x[i] == 0:
                x[i] = 1
            i+=1

        set_key(d_candle, "time_open", datetime.datetime.fromtimestamp(x[0]/1000))
        set_key(d_candle, "open", x[1])
        set_key(d_candle, "high", x[2])
        set_key(d_candle, "low", x[3])
        set_key(d_candle, "close", x[4])
        set_key(d_candle, "volume", x[5])
        set_key(d_candle, "nr_trades", x[8])
        set_key(d_candle, "high/open", (1 - x[1]/x[2]))
        set_key(d_candle, "high/close", (1 - x[4]/x[2]))
        set_key(d_candle, "high/low", (1 - x[3]/x[2]))
        set_key(d_candle, "low/open", (1 - x[1]/x[3]))
        set_key(d_candle, "low/close", (1 - x[4]/x[3]))
        set_key(d_candle, "open/close", (1 - x[4]/x[1]))
        set_key(d_candle, "volume/trades", x[5]/x[8])

    set_key(d_candle, "sma", sma(d_candle['close'], 10))
    set_key(d_candle, "ema", ema(d_candle['close'], 10))
    set_key(d_candle, "rsi", rsi(d_candle["close"], 14))
    set_key(d_candle, "macd", macd(d_candle['close'], 12, 26))
    set_key(d_candle, "obv", obv(d_candle['close'], d_candle['volume']))
    set_key(d_candle, "sto", sto(d_candle['close'], 14))
    set_key(d_candle, "true_range",true_range(d_candle['close'], 14))
    set_key(d_candle, "true_avg", true_avg(d_candle['close'], 14))

    return d_candle



