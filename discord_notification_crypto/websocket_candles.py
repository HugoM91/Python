

import websocket, json
from main import symbols, client, url_misc
from utils import  mensagem_compra_venda
import time 
from signals import big_wick, discord_send_message

streams = []
interval = '1m'
for x in symbols:
    streams.append(x.lower()+'@kline_'+ interval)

websocket_link ='/'
websocket_link= websocket_link.join(streams)


def btc_price():
    trades2 = client.get_recent_trades(symbol='BTCUSDT')
    btc_price = trades2[-1]['price']
    return btc_price

def on_message(ws,message):
    #print(message)
    #print(type(message))
    msg = json.loads(message)
    sym = msg['s']
    msg = msg['k']
    if msg['x'] == True:
        v = msg['v']*btc_price #volume 
        v_compras = msg['V']*btc_price #volume de compras
        o = msg['o']  
        h = msg['h'] 
        l = msg['l'] 
        c = msg['c']
        bw = big_wick(o, c, l, h, v, v_compras, sym, interval)
        if bw != '':
            discord_send_message(url_misc, bw)
            

def on_close(ws):
    print('closed')

def start_candles_socket():
    socket = f'wss://stream.binance.com:9443/ws/{websocket_link}'
    #socket = f'wss://stream.binance.com:9443/ws/btcusdt@kline_1m'
    ws = websocket.WebSocketApp(socket, on_message = on_message, on_close=on_close)
    ws.run_forever()


'''
{'e': 'kline', 'E': 1624893120130, 's': 'BTCUSDT', 
'k': 
{'t': 1624893060000, 'T': 1624893119999, 's': 'BTCUSDT', 'i': '1m', 'f': 936908469, 'L': 936909686, 
 'o': '34507.05000000', 'c': '34540.04000000', 'h': '34550.00000000', 'l': '34507.04000000', 
'v': '40.44804800', 'n': 1218, 'x': True, 'q': '1396768.70857690', 'V': '21.86484000', 'Q': '754992.16154884', 'B': '0'}}

  {
  "e": "kline",     // Event type
  "E": 123456789,   // Event time
  "s": "BNBBTC",    // Symbol
  "k": {
    "t": 123400000, // Kline start time
    "T": 123460000, // Kline close time
    "s": "BNBBTC",  // Symbol
    "i": "1m",      // Interval
    "f": 100,       // First trade ID
    "L": 200,       // Last trade ID
    "o": "0.0010",  // Open price
    "c": "0.0020",  // Close price
    "h": "0.0025",  // High price
    "l": "0.0015",  // Low price
    "v": "1000",    // Base asset volume
    "n": 100,       // Number of trades
    "x": false,     // Is this kline closed?
    "q": "1.0000",  // Quote asset volume
    "V": "500",     // Taker buy base asset volume   ***DESCRIPTION BELOW MOTHERTRUCKER
    "Q": "0.500",   // Taker buy quote asset volume
    "B": "123456"   // Ignore
  }
}


*** Taker buy means the buyer is the taker and seller is the maker.
Base asset means the quantity is expressed as the amount of coins that were received by the buyer (as opposed to quote asset which would be the amount paid by the buyer in btc/eth/usdt, depending on the market)
'Volume' is the total amount of traded coins in the timeframe, disregarding which side is the taker
So basically to calculate maker buy volume (or taker sell, which is the same):
'Volume' - ' Taker buy base asset volume' = ' Maker buy base asset volume'
'''