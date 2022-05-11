

import websocket, json
from utils import  mensagem_compra_venda
import time
import requests
import threading

streams = []
symbols = ['BTCUSDT', 'ETHBTC', 'LTCBTC', 'BNBBTC', 'NEOBTC', 'GASBTC', 'QTUMBTC',  'OMGBTC', 'ZRXBTC', 'STRATBTC', 'KNCBTC', 'IOTABTC', 'LINKBTC', 'XVGBTC', 'EOSBTC', 'SNTBTC', 'ETCBTC', 'MTHBTC', 'ENGBTC', 'DNTBTC', 'ZECBTC', 'BNTBTC', 'ASTBTC', 'DASHBTC', 'OAXBTC', 'TRXBTC', 'ARKBTC', 'XRPBTC',  'ENJBTC', 'STORJBTC', 'XMRBTC', 'BATBTC', 'LSKBTC', 'MANABTC', 'ADABTC', 'XLMBTC', 'WAVESBTC', 'IOSTBTC', 'STEEMBTC', 'NANOBTC', 'ONTBTC', 'STORMBTC', 'XEMBTC', 'ZENBTC', 'DATABTC','DENTBTC', 'HOTBTC', 'VETBTC','BTTBTC', 'MATICBTC', 'ATOMBTC','ALGOBTC','DOGEBTC', 'ANKRBTC','XTZBTC','CTSIBTC','COMPBTC','AVABTC', 'JSTBTC','DOTBTC', 'LUNABTC','SUSHIBTC','UNIBTC','AVAXBTC','AAVEBTC', 'AUDIOBTC', 'AKROBTC', 'JUVBTC', 'PSGBTC', '1INCHBTC','CAKEBTC', 'OMBTC', 'SUPERBTC', 'CFXBTC', 'EPSBTC','MIRBTC', 'ICPBTC', 'BAKEBTC', 'KEEPBTC']
#symbols = ['BTCUSDT']

#for x in symbols:
    #streams.append(x.lower()+'@trade')

#websocket_link ='/'
#websocket_link= websocket_link.join(streams)

def get_marketcap(symbol):

    reqs = requests.get('https://www.binance.com/exchange-api/v2/public/asset-service/product/get-products')
    reqs = reqs.json()
    for x in reqs['data']:
        if x['s'] == 'BTCUSDT':
            btc_price = float(x['c'])
        if x['s'] == symbol:
            res = btc_price*float(x['c'])*float(x['cs'])
            
    return res

def btc_price():
    trades2 = client.get_recent_trades(symbol='BTCUSDT')
    btc_price = trades2[-1]['price']
    print(btc_price)
    return btc_price

def on_message(ws,message):
    msg = json.loads(message)
    marketcap = get_marketcap(msg['s'])
    if msg['s'] == 'BTCUSDT':
        price_usd = float(msg['q'])*float(btc_price())
    else :
        price_usd = float(msg['q'])*float(btc_price())*float(msg['p'])
    
    print('symbol ', msg['s'], '  market cap: ', marketcap, '  quantity USD: ', price_usd)
    if marketcap > 5000000000:
        if price_usd > 120000:
            mensagem_compra_venda(msg['m'], msg['s'], price_usd, float(msg['q']))
            time.sleep(1.3)
    elif marketcap > 1000000000:
        if price_usd > 75000:
            mensagem_compra_venda(msg['m'], msg['s'], price_usd, float(msg['q']))
            time.sleep(1.3)
    elif marketcap > 500000000:
        if price_usd > 50000:
            mensagem_compra_venda(msg['m'], msg['s'], price_usd, float(msg['q']))
            time.sleep(1.3)
    elif marketcap > 100000000:
        if price_usd > 10000:
            mensagem_compra_venda(msg['m'], msg['s'], price_usd, float(msg['q']))
            time.sleep(1.3)
    elif marketcap > 50000000:
        if price_usd > 10000:
            mensagem_compra_venda(msg['m'], msg['s'], price_usd, float(msg['q']))
            time.sleep(1.3)
            
def on_close(ws):
    print('closed')

def start_market_orders_socket (symbol):

    socket = f'wss://stream.binance.com:9443/ws/{symbol+'@trade'}'
    ws = websocket.WebSocketApp(socket, on_message = on_message, on_close=on_close)
    ws.run_forever()


for x in symbols:
    thread1 = start_market_orders_socket(x)
    thread1.start()

#start_market_orders_socket()

'''
streams = [
    "ethbtc@trade","bnbbtc@trade","wavesbtc@trade","bchabcbtc@trade",
    "bchsvbtc@trade","xrpbtc@trade","tusdbtc@trade","eosbtc@trade",
    "trxbtc@trade","ltcbtc@trade","xlmbtc@trade","bcptbtc@trade",
    "adabtc@trade","zilbtc@trade","xmrbtc@trade","stratbtc@trade",
    "zecbtc@trade","qkcbtc@trade","neobtc@trade","dashbtc@trade","zrxbtc@trade"
  ]
'''
