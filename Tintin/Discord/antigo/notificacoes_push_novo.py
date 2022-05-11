from binance.client import Client
import time
from discord_webhook import DiscordWebhook
from binance.websockets import BinanceSocketManager


client = Client('s5jgqnUryEPYD7oCz5uCdAQimuCIHag5OzmSmVkvyRc2pIVPWPZd8mNx3jyDCdbj', '9QWGd9JTXt76ufl9PE3ocW5D1suikdGgylyKPgzecpDYmhXmBCRmX9DgNQ74pxZU')
bm = BinanceSocketManager(client)


url_qnt = 'https://discordapp.com/api/webhooks/713723604994490368/cKOQON2_l5kJa0_Lpb2bpADPRSbe2g8lBh5AiUFWle006Fl-iBAEChf0SnL3wIKi-XIS'
url_qnt1 = 'https://discordapp.com/api/webhooks/713899580982427660/u110pz8fa7H_TSO130FbLM4YUGKfICdzrW82WC6Snk5rbT1eeXizZQvmQ8tsax_qMbhC' 
url_var = 'https://discordapp.com/api/webhooks/713841134471872539/a4jZBrxNdBbUEFjj4d0eIqkcbt8_Izme0ZjwAg2c-jKRILwKoByd2y6goJkFcn8zSDya'
url_var24 = 'https://discordapp.com/api/webhooks/715236738125135962/L9tY-mhHUpmxcWkcPGtiqooqI-YlvXbo4SWdNJCXQBMenWMzVvsZevt-h0-G51Bl3SFn'

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


