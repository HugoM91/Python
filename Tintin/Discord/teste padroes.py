from binance.client import Client
from indicadores import indicadores
from discord_webhook import DiscordWebhook
import numpy as np

client = Client('', '')
url_teste = ''


def teste(sym):
    candles = client.get_klines(symbol=sym, interval=Client.KLINE_INTERVAL_1MINUTE, limit = 1)
    
       

          
    
       
teste('BTCUSDT')
