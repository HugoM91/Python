from binance.client import Client
import time
from discord_webhook import DiscordWebhook
from binance.websockets import BinanceSocketManager


client = Client('', '')
bm = BinanceSocketManager(client)




price_qnt = ['BTCUSDT', 'BNBUSDT', 'ETHUSDT', 'XRPUSDT' , 'XMRUSDT' , 'LTCUSDT' , 'EOSUSDT', 'TRXUSDT', 'NEOUSDT', 'IOTAUSDT', 'ZECUSDT', 'DASHUSDT', 'ENJUSDT','MCOUSDT','XLMUSDT' ,'BATUSDT','BTTUSDT', 'ONTUSDT', 'WINUSDT','ENJBTC', 'MCOBTC','BATBTC','NEOBTC', 'XRPBTC' ,'IOSTBTC','ZRXBTC', 'NANOBTC' , 'DOGEBTC', 'ETCBTC', 'XEMBTC', 'QTUMBTC' ,'KNCBTC','SNTBTC'   ]            
price_var = ['BTCUSDT', 'BNBUSDT', 'ETHUSDT', 'XRPUSDT' , 'XMRUSDT' , 'LTCUSDT' , 'EOSUSDT', 'TRXUSDT', 'NEOUSDT', 'IOTAUSDT', 'VETUSDT', 'QTUMUSDT', 'IOSTUSDT', 'ADAUSDT', 'XTZUSDT' , 'ONTUSDT' , 'BATUSDT' ]

trade_id=[]

open1 = [0]
close = []
low = []
high = []
volume = []
nrtrades = []

def handlek_message(msg): 
    
    print(msg['k']['o'])
    symb = msg['k']['s']
    if msg['k']['o'] != open1[-1]:
        open1.append(msg['k']['o'])
        print('oila')
    if len(open1) == 4:
        del open1[0]
        a = float(open1[-3])
        b = float(open1[-1])
        c = float((b * 100 / a) - 100)
        d = float("{:.3f}".format(c))   
    
        if c > 0.2:
            e = str(d)
            webhook = DiscordWebhook(url_var , content= (':green_circle: ' + symb + '//' + e + '%' + ' UpNOVO'))
            response = webhook.execute()
        if c < -0.2:
            e = str(d)
            webhook = DiscordWebhook(url_var , content= (':red_circle: ' + symb + '//' + (e*-1) + '%' + ' DownNOVO'))
            response = webhook.execute() 
            

    
    
    
def process_message(msg):
    trades2 = client.get_recent_trades(symbol='BTCUSDT')
    btc_price = []            
    for x in trades2[-1:]:
        btc_price.append(float(x['price']))
        
    a = msg['q']
    b = msg['t']
 
    if a*btc_price[-1] >= 0:
    
    
        
for x in price_var:
    kline = bm.start_kline_socket(x, handlek_message, interval='1m')
    

bm.start() #comeca a websocket


