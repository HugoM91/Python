from indicators import Indicators
from reports import Reports
import threading
from main import symbols, indicators, patterns, client, indicators_webhook
from websocket_market_orders import start_market_orders_socket
from websocket_candles import start_candles_socket

binance_options = {
        'symbols': symbols,
        'client': client,
        'limit': 300
}
settings = {
        'discord_webhook': indicators_webhook,
        'indicators': indicators,
        'patterns': patterns
}
def start_indicators(interval, discord_sleep):
        i = Indicators(interval, discord_sleep,binance_options = binance_options, **settings)
        i.start()
def start_report(interval, discord_sleep):
        r = Reports(interval, discord_sleep,binance_options = binance_options, **settings)
        r.start()


thread1 = threading.Thread(target=start_indicators, args=('1h', 15))
thread2 = threading.Thread(target=start_indicators, args=('4h', 45))
thread3 = threading.Thread(target=start_indicators, args=('1d', 240))
#thread4 = threading.Thread(target=start_report, args=(('1h', 3600)))
#thread5 = threading.Thread(target=start_report, args=(('4h', 14400)))
#thread6 = threading.Thread(target=start_report, args=('1d', 86400))
#thread10 = threading.Thread(target=start_market_orders_socket)
#thread11 = threading.Thread(target=start_candles_socket)

#thread11.start
#thread10.start()
thread1.start()
thread2.start()
thread3.start()
#thread4.start()
#thread5.start()
#thread6.start()

print('All threads started')

