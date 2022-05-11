from binance.client import Client
from indicadores import indicadores
from discord_webhook import DiscordWebhook
import numpy as np

client = Client('s5jgqnUryEPYD7oCz5uCdAQimuCIHag5OzmSmVkvyRc2pIVPWPZd8mNx3jyDCdbj', '9QWGd9JTXt76ufl9PE3ocW5D1suikdGgylyKPgzecpDYmhXmBCRmX9DgNQ74pxZU')
url_teste = 'https://discordapp.com/api/webhooks/717350806768189581/bWI72oh5kMEHXBhcgX78fEBP_OmtwZ5Lu7CF7teJyo5HBWkx-pNuLc60fI2CpRnL9qtQ'


def teste(sym):
    candles = client.get_klines(symbol=sym, interval=Client.KLINE_INTERVAL_1MINUTE, limit = 1)
    
       

          
    
       
teste('BTCUSDT')