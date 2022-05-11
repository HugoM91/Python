import discord
from binance.client import Client
from indicadores import indicadores
        
client = Client('', '')
channel =['commands']
bot = discord.Client()
id = bot.get_guild()

def velas(a, b, c):
    klines = client.get_historical_klines(a, b, c)
    
    close=[]
    open1=[]
    low=[]
    high=[]
    volume=[]
    nr_trocas=[]
    close_time = []
    open_time=[]
    for x in klines:
        open_time.append(float(x[0]))
        open1.append(float(x[1]))
        high.append(float(x[2]))
        low.append(float(x[3]))
        close.append(float(x[4]))
        volume.append(float(x[5]))
        close_time.append(float(x[6]))
        nr_trocas.append(float(x[8]))
            
    return close, open1, low, high , volume , nr_trocas, close_time, open_time


"""

@bot.event
async def on_message(message):
    if message.content.startswith('1'):
        a = velas('BTCUSDT', Client.KLINE_INTERVAL_1HOUR)[0][-1]
        b = velas('BTCUSDT', Client.KLINE_INTERVAL_1HOUR)[0][-2]
        c = velas('BTCUSDT', Client.KLINE_INTERVAL_1HOUR)[0][-3]
        ai = 
        bi =
        ci = 
        
        y = str(a)
        await message.channel.send(a)

               
    if message.content.startswith('2'):
        a = velas('BTCUSDT', Client.KLINE_INTERVAL_2HOUR)[0][-1]
        y = str(a)
        await message.channel.send('10')
           
       
    if message.content.startswith('3'):
        a = velas('BTCUSDT', Client.KLINE_INTERVAL_2HOUR)[0][-1]
        y = str(a)
        await message.channel.send('100')
        
        
bot.run('NzExNTc1Mjc3NDkwNDA1Mzk2.XsJpQg.1A0sZTAe30b-ZoNVxUnO6fD6gAo')
"""

