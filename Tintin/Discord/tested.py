"""
if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

"""

from binancedata import velas
from indicadores import indicadores
import discord
from binance.client import Client
            

client = Client('s5jgqnUryEPYD7oCz5uCdAQimuCIHag5OzmSmVkvyRc2pIVPWPZd8mNx3jyDCdbj', '9QWGd9JTXt76ufl9PE3ocW5D1suikdGgylyKPgzecpDYmhXmBCRmX9DgNQ74pxZU')

bot = discord.Client()

def velas(a):
    klines = client.get_historical_klines(a, Client.KLINE_INTERVAL_5MINUTE , "2 day ago UTC" )
    
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
        
        
    


velas('BTCUSDT')


last_trades = []

trades = client.get_recent_trades(symbol='BNBBTC')
{
        "id": 28457,
        "price": "4.00000100",
        "qty": "12.00000000",
        "time": 1499865549590,
        "isBuyerMaker": true,
        "isBestMatch": true
    }

for x in trades
#average trades incrising



avg_price = client.get_avg_price(symbol='BNBBTC')



candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)
    
        [
            1499040000000,      # Open time
            "0.01634790",       # Open
            "0.80000000",       # High
            "0.01575800",       # Low
            "0.01577100",       # Close
            "148976.11427815",  # Volume
            1499644799999,      # Close time
            "2434.19055334",    # Quote asset volume
            308,                # Number of trades
            "1756.87402397",    # Taker buy base asset volume
            "28.46694368",      # Taker buy quote asset volume
            "17928899.62484339" # Can be ignored
        ]
]


if a = 2:








"""
@bot.event
async def on_message(message):
    
    
    
bot.run('NzExNTc1Mjc3NDkwNDA1Mzk2.XsJpQg.1A0sZTAe30b-ZoNVxUnO6fD6gAo')
"""