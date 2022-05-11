from binance.client import Client
from discord_webhook import DiscordWebhook
import numpy as np
import time
import yaml

from main import client, reports_webhook, symbols
from utils import talib_indicator, talib_store
from signals import send_report

class Reports:

    def __init__(self, interval, discord_sleep, binance_options, **kwargs):
        self.discord_webhook = kwargs['discord_webhook']
        self.discord_sleep = discord_sleep
        self.indicators = kwargs['indicators']

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
            flag = 0
            data_store = {'simbolos':[]}
            for sym in self.symbols:
                candles = client.get_klines(symbol=sym, interval=self.interval, limit=self.limit)

                ohlcv = [candle[0:-1] for candle in candles]
                if len(ohlcv) > 250:
                    data_store[sym] = talib_store(self.indicators, ohlcv, sym, self.interval, **self.indicators_config)
                    flag = 1
                    data_store['simbolos'].append(sym)
                
            if flag == 1:
                webhook = DiscordWebhook(reports_webhook, content=send_report(self.interval, data_store))
                response = webhook.execute()
            time.sleep(self.discord_sleep)
  