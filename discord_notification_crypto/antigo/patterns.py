from binance.client import Client
from discord_webhook import DiscordWebhook
import numpy as np
import time
from main import client, patterns_webhook
from utils import talib_pattern


# Implement all patterns
class Patterns():

    def __init__(self,interval, discord_sleep, binance_options, **kwargs):
        self.discord_webhook = kwargs['discord_webhook']
        self.discord_sleep = discord_sleep
        self.patterns = kwargs['patterns']

        self.client = binance_options['client']
        self.limit = binance_options['limit']
        self.symbols = binance_options['symbols']
        self.interval = interval.lower()


    def start(self):
        while True:
            for sym in self.symbols:
                candles = client.get_klines(symbol=sym, interval=self.interval, limit=self.limit)

                ohlcv = [candle[1:6] for candle in candles]
                patterns = talib_pattern(self.patterns, ohlcv)
                
                for k, v in patterns.items():
                    if any([x == 100 for x in v]):
                        content = f":green_circle: {sym} at **{self.interval}** - Pattern **{k.title()}**" #+ "\n\t{v}\n"
                    if any([x == -100 for x in v]):
                        content = f":red_circle: {sym} at **{self.interval}** - Pattern **{k.title()}**" #+ "\n\t{v}\n"
                    if content:
                        webhook = DiscordWebhook(patterns_webhook, content=content)
                        response = webhook.execute()
                        time.sleep(2)
                    time.sleep(self.discord_sleep)

