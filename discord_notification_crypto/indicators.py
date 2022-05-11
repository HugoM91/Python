from binance.client import Client
from discord_webhook import DiscordWebhook
import numpy as np
import time
import yaml
from main import client, patterns_webhook
from utils import talib_indicator, talib_pattern

class Indicators:

    def __init__(self, interval, discord_sleep, binance_options, **kwargs):
        self.discord_webhook = kwargs['discord_webhook']
        self.discord_sleep = discord_sleep/2
        self.indicators = kwargs['indicators']
        self.patterns = kwargs['patterns']

        self.symbols = binance_options['symbols']
        self.interval = interval.lower()
        self.limit = binance_options['limit']

        self.load_config('config/indicators_config.yaml')
        self.client = binance_options['client']


    def load_config(self, config_path):
        with open(config_path) as file:
            self.indicators_config = yaml.load(file, Loader=yaml.FullLoader)

    def start(self):
        while True:
            for sym in self.symbols:
                candles = client.get_klines(symbol=sym, interval=self.interval, limit=self.limit)
                # candle: [1624190400000, '0.00936400', '0.00939200', '0.00928300', '0.00934100', '15934.56000000', 1624193999999, '148.61589299', 7071, '8633.40000000', '80.51476709', '0']
                # Candle example:
                # [
                #     [
                #         1499040000000,      // Open time
                #         "0.01634790",       // Open
                #         "0.80000000",       // High
                #         "0.01575800",       // Low
                #         "0.01577100",       // Close
                #         "148976.11427815",  // Volume
                #         1499644799999,      // Close time
                #         "2434.19055334",    // Quote asset volume
                #         308,                // Number of trades
                #         "1756.87402397",    // Taker buy base asset volume
                #         "28.46694368",      // Taker buy quote asset volume
                #         "17928899.62484339" // Ignore.
                #     ]
                # ]

                ohlcv = [candle[1:6] for candle in candles]

                indicators = talib_indicator(self.indicators, ohlcv, sym, self.interval, **self.indicators_config)
                patterns = talib_pattern(self.patterns, ohlcv)


                for indicator, content in indicators.items():
                    if content:
                        webhook = DiscordWebhook(self.discord_webhook, content=content)
                        response = webhook.execute()
                        time.sleep(2)
                time.sleep(self.discord_sleep)
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
  
