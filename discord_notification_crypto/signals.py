from discord_webhook import DiscordWebhook
import numpy as np
from main import symbols
from PIL import Image
import time

#manda mensagaem para o discord
def discord_send_message(url, content):

    webhook = DiscordWebhook(url, content=content)
    response = webhook.execute()
    time.sleep(2)

#manda imagens para o discord  
def discord_send_image(url, pic_url):

    webhook = DiscordWebhook(url=url, username="Webhook with files")
    # send two images
    with open(pic_url, "rb") as f:
        webhook.add_file(file=f.read(), filename='example.jpg')
    response = webhook.execute()

#descobre o nome da variavel
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

#utility // so funciona para o rsi_overbought_oversold
def rsi_volatility(price_list):
    content = []
    inicial_price = price_list[-9]
    for x in price_list:
        content.append(((inicial_price-x)*100/inicial_price)-100)
    
    content = [np.round(x, 2) for x in content[-10:]]
    return content

#signal
def rsi_overbought_oversold(real,sym, interval, indicator, h, l, c):
    content = None
    if real[-1] >= 77 and real[-2] >= 70:
        if  h[-1] > h[-2] and h[-2] > h[-3] and h[-3] > h[-4] and h[-4] > h[-5] :
            circle = ":red_circle:"
            content = f"\n{circle}  {sym} :candle:  **{interval}** \n```**{indicator}** {real[-8:-1]}\n**Rsi Variation** {rsi_volatility(real)[-8:-1]}\n**Price** {c[-8:-1]}\n**Price Variation** {rsi_volatility(c)[-8:-1]}```"
    elif real[-1] < 23  and real[-2] < 30 and real[-2] > 12 and real[-1] > 12:
        if  l[-1] < l[-2] and l[-2] < l[-3] and l[-3] < l[-4] and l[-4] < l[-5]:
            circle = ":green_circle:"
            content = f"\n{circle}  {sym} :candle:  **{interval}** \n```**{indicator}** {real[-8:-1]}\n**Rsi Variation** {rsi_volatility(real)[-8:-1]}\n**Price** {c[-8:-1]}\n**Price Variation** {rsi_volatility(c)[-8:-1]}```"
    return content

#signal
def macd_crossover(macd,macdsignal, sym, interval, indicator):
    content = None
    if macd[-4] > macdsignal[-4] and macd[-3] < macdsignal[-3] and macd[-2] < macdsignal[-2] and macd[-1] < macdsignal[-1]:
        circle = ":red_circle:"
        content = f"\n{circle}  {sym} :candle:  **{interval}** \n```{indicator} **CROSSOVER**```"
    elif macd[-4] < macdsignal[-4] and macd[-3] > macdsignal[-3] and macd[-2] > macdsignal[-2] and macd[-1] > macdsignal[-1]:
        circle = ":green_circle:"
        content = f"\n{circle}  {sym} :candle:  **{interval}** \n```{indicator} **CROSSOVER**```"
    return content

#signal
def ema_crossover(ema1,ema2, sym, interval):
    content = None
    name1 = namestr(ema1, globals())
    name2 = namestr(ema2, globals())
    if name1 and name2:
        if ema1[-4] > ema2[-4] and ema1[-3] < ema2[-3] and ema1[-2] < ema2[-2] and ema1[-1] < ema2[-1]:
            circle = ":red_circle:"
            content = f"\n{circle}\t{sym} last **{interval}** \n```{name2[0]} **CROSSOVER** {name1[0]}```"
        elif ema1[-4] < ema2[-4] and ema1[-3] > ema2[-3] and ema1[-2] > ema2[-2] and ema1[-1] > ema2[-1]:
            circle = ":green_circle:"
            content = f"\n{circle}\t{sym} last **{interval}** \n```{name1[0]} **CROSSOVER** {name2[0]}```"
    return content
    
#manda report
def send_report(interval, data_store):
    content = None
    rsi = []
    ema = {'14': [],'56': [],'112': [],'224': []}
    close = []
    open1 = []
    
    for x in data_store['simbolos']:
        if data_store[x]['rsi'] != 100:
            if data_store[x]['rsi'] != 0:
                rsi.append(data_store[x]['rsi'])
        if data_store[x]['close'] != 0:
            close.append(data_store[x]['close'])
        if data_store[x]['open'] != 0:
            open1.append(data_store[x]['open'])
        if  data_store[x]['ema14'] != 0:
            ema["14"].append(data_store[x]['ema14'])
        if data_store[x]['ema56'] != 0:
            ema["56"].append(data_store[x]['ema56'])
        if data_store[x]['ema112'] != 0:
            ema["112"].append(data_store[x]['ema112'])
        if data_store[x]['ema224'] != 0:
            ema["224"].append(data_store[x]['ema224'])   

    rsi_print = sum(rsi)/len(rsi)
    ema14_print = sum(ema["14"])/len(ema["14"])
    ema56_print = sum(ema["56"])/len(ema["56"])
    ema112_print = sum(ema["112"])/len(ema["112"])
    ema224_print = sum(ema["224"])/len(ema["224"])
    close_print = sum(close)/len(close)
    open_print = sum(open1)/len(open1)
    ema14_close_print = (sum(close)/len(close))-(ema14_print)
    ema56_close_print = (sum(close)/len(close))-(ema56_print)
    ema112_close_print = (sum(close)/len(close))-(ema112_print)
    ema224_close_print = (sum(close)/len(close))-(ema224_print)
    open_close_print = 100 - (close_print * 100 / open_print)
    
    content = f"\n **Report {interval}** \n```**Open** {open_print}\n**Close** {close_print}\n**Open/Close Variation** {open_close_print}\n**Ema14** {ema14_print}\n**Ema56** {ema56_print}\n**Ema112** {ema112_print}\n**Ema224** {ema224_print}\n**Close - Ema14** {ema14_close_print}\n**Close - Ema56** {ema56_close_print}\n**Close - Ema112** {ema112_close_print}\n**Close - Ema224** {ema224_close_print}\n**Rsi** {rsi_print}\n```"

    return content
    
#signal
def big_wick(o, c, l, h, v, v_compras, sym, interval):
    content = ''
    if o > c and (c-o)*2 < (h-c):
        circle = ":green_circle:"
        content = f"\n{circle}  {sym} :candle:  **{interval}** \n```**Big Wick**\nTotal Volume  = {v}/n Buy Volume % = {v_compras*100/v}% ```"
    elif c < o and (o-c)*2 < (c-l):
        circle = ":red_circle:"
        content = f"\n{circle}  {sym} :candle:  **{interval}** \n```**Big Wick**\nTotal Volume  = {v}/n Buy Volume % = {v_compras*100/v}% ```"
    return content