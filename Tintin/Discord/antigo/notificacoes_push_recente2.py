


from binance.client import Client
import time
from discord_webhook import DiscordWebhook
from indicadores import indicadores
import numpy as np

client = Client('s5jgqnUryEPYD7oCz5uCdAQimuCIHag5OzmSmVkvyRc2pIVPWPZd8mNx3jyDCdbj', '9QWGd9JTXt76ufl9PE3ocW5D1suikdGgylyKPgzecpDYmhXmBCRmX9DgNQ74pxZU')
h = []
trade_id=[]
url_qnt = 'https://discordapp.com/api/webhooks/713723604994490368/cKOQON2_l5kJa0_Lpb2bpADPRSbe2g8lBh5AiUFWle006Fl-iBAEChf0SnL3wIKi-XIS'
url_qnt1 = 'https://discordapp.com/api/webhooks/713899580982427660/u110pz8fa7H_TSO130FbLM4YUGKfICdzrW82WC6Snk5rbT1eeXizZQvmQ8tsax_qMbhC' 
url_var = 'https://discordapp.com/api/webhooks/713841134471872539/a4jZBrxNdBbUEFjj4d0eIqkcbt8_Izme0ZjwAg2c-jKRILwKoByd2y6goJkFcn8zSDya'
url_var24 = 'https://discordapp.com/api/webhooks/715236738125135962/L9tY-mhHUpmxcWkcPGtiqooqI-YlvXbo4SWdNJCXQBMenWMzVvsZevt-h0-G51Bl3SFn'
url_pat = 'https://discordapp.com/api/webhooks/716241164680036402/4uILix2eh8eQIIUek33KiHQHvI3ID2DJJ5H6vsUtIf1YRrgeRgIlkB0yRha3s52c_XNa'

price_qnt = ['BTCUSDT', 'BNBUSDT', 'ETHUSDT', 'XRPUSDT' , 'XMRUSDT' , 'LTCUSDT' , 'EOSUSDT', 'TRXUSDT', 'NEOUSDT', 'IOTAUSDT', 'ZECUSDT', 'DASHUSDT', 'ENJUSDT','MCOUSDT','XLMUSDT' ,'BATUSDT','BTTUSDT', 'ONTUSDT', 'WINUSDT','ENJBTC', 'MCOBTC','BATBTC','NEOBTC', 'XRPBTC' ,'IOSTBTC','ZRXBTC', 'NANOBTC' , 'DOGEBTC', 'ETCBTC', 'XEMBTC', 'QTUMBTC' ,'KNCBTC','SNTBTC'   ]            
price_var = ['BTCUSDT', 'BNBUSDT', 'ETHUSDT', 'XRPUSDT' , 'XMRUSDT' , 'LTCUSDT' , 'EOSUSDT', 'TRXUSDT', 'NEOUSDT', 'IOTAUSDT', 'VETUSDT', 'QTUMUSDT', 'IOSTUSDT', 'ADAUSDT', 'XTZUSDT' , 'ONTUSDT' , 'BATUSDT' ]



def start_qnt(sym):  

    simbolos =  ['BNBUSDT','BTCUSDT']
    simbolos1 = ['ETHUSDT']
    simbolos2 = ['XRPUSDT' , 'XMRUSDT' , 'LTCUSDT' , 'EOSUSDT', 'TRXUSDT']
    simbolos3 = ['NEOUSDT', 'IOTAUSDT', 'ZECUSDT', 'DASHUSDT', 'ENJUSDT','MCOUSDT','XLMUSDT' ,'BATUSDT','BTTUSDT', 'ONTUSDT', 'WINUSDT'] 
    simbolos4 = ['ENJBTC', 'MCOBTC','BATBTC','NEOBTC', 'XRPBTC' ,'IOSTBTC','ZRXBTC', 'NANOBTC' , 'DOGEBTC', 'ETCBTC', 'XEMBTC', 'QTUMBTC' ,'KNCBTC','SNTBTC']
   
    trades2 = client.get_recent_trades(symbol='BTCUSDT')
    btc_price = []            
    for x in trades2[-1:]:
        btc_price.append(float(x['price']))
        
    trades = client.get_recent_trades(symbol=sym)
    for x in trades:
        if x['id'] not in trade_id:
            q = float(x['qty'])
            d = x['isBuyerMaker']
            p = float(x['price'])
            pd = q * p
            q1 = float("{:.3f}".format(q))
            q1 = str(q1)
            pd3 = float("{:.3f}".format(pd))
            pd3 = str(pd3)
            t = float(x['time'])
            
            if sym in simbolos:
                if pd >= 190000 and d == True:
                    webhook = DiscordWebhook(url_qnt1 , content= (':red_circle: ' + '------Sell------  ' + sym + '\n' + pd3 + ' USD' + ' / ' + q1 + ' Coins'))
                    response = webhook.execute()
                    trade_id.append(x['id'])
                if pd >= 190000 and d == False:
                    webhook = DiscordWebhook(url_qnt1 , content= (':green_circle: ' + '------Buy------  ' + sym + '\n' + pd3 + ' USD' + ' / ' + q1 + ' Coins' ))
                    response = webhook.execute()
                    trade_id.append(x['id'])
            
            if sym in simbolos1:
                if pd >= 150000 and d == True:
                    webhook = DiscordWebhook(url_qnt , content= (':red_circle: ' + '------Sell------  ' + sym + '\n' + pd3 + ' USD' + ' / ' + q1 + ' Coins'))
                    response = webhook.execute()
                    trade_id.append(x['id'])
                if pd >= 150000 and d == False:
                    webhook = DiscordWebhook(url_qnt , content= (':green_circle: ' + '------Buy------  ' + sym + '\n' + pd3 + ' USD' + ' \ ' + q1 + ' Coins' ))
                    response = webhook.execute()
                    trade_id.append(x['id'])

            if sym in simbolos2:
                if pd >= 75000 and d == True:
                    webhook = DiscordWebhook(url_qnt , content= (':red_circle: ' + '------Sell------  ' + sym + '\n' + pd3 + ' USD' + ' / ' + q1 + ' Coins'))
                    response = webhook.execute()
                    trade_id.append(x['id'])
                if pd >= 75000 and d == False:
                    webhook = DiscordWebhook(url_qnt , content= (':green_circle: ' + '------Buy------  ' + sym + '\n' + pd3 + ' USD' + ' / ' + q1 + ' Coins' ))
                    response = webhook.execute()
                    trade_id.append(x['id'])

            if sym in simbolos3:
                if pd >= 40000 and d == True:
                    webhook = DiscordWebhook(url_qnt , content= (':red_circle: ' + '------Sell------  ' + sym + '\n' + pd3 + ' USD' + ' / ' + q1 + ' Coins'))
                    response = webhook.execute()
                    trade_id.append(x['id'])
                if pd >= 40000 and d == False:
                    webhook = DiscordWebhook(url_qnt , content= (':green_circle: ' + '------Buy------  ' + sym + '\n' + pd3 + ' USD' + ' / ' + q1 + ' Coins' ))
                    response = webhook.execute()
                    trade_id.append(x['id'])
                    

            if sym in simbolos4:
                bp = btc_price[0]
                pd4 = bp * pd
                pd5 = float("{:.3f}".format(pd4))
                pd5 = str(pd5)
                if pd4 >= 40000 and d == True:
                    webhook = DiscordWebhook(url_qnt , content= (':red_circle: ' + '------Sell------  ' + sym + '\n' + pd5 + ' USD' + ' / ' + q1 + ' Coins'))
                    response = webhook.execute()
                    trade_id.append(x['id'])
                if pd4 >= 40000 and d == False:
                    webhook = DiscordWebhook(url_qnt , content= (':green_circle: ' + '------Buy------  ' + sym + '\n' + pd5 + ' USD' + ' / ' + q1 + ' Coins' ))
                    response = webhook.execute()
                    trade_id.append(x['id'])



def start_var(sym):
    candles = client.get_klines(symbol=sym, interval=Client.KLINE_INTERVAL_1MINUTE, limit = 5)
    candles2 = client.get_klines(symbol=sym, interval=Client.KLINE_INTERVAL_1HOUR, limit = 5)
    
    op = []
    cl = []
    hi = []
    lo = []
    for x in candles[-5:]:
        op.append(float(x[1]))
        cl.append(float(x[4]))
        hi.append(float(x[2]))
        lo.append(float(x[3]))
        
    hammer = indicadores(op, cl, hi, lo)[-2][-1]
    inv_hammer = indicadores(op, cl, hi, lo)[-1][-1]
    hammer = hammer.tolist()
    inv_hammer = inv_hammer.tolist()
        
        
    if hammer == 100:
        webhook = DiscordWebhook(url_pat , content= (':green_circle: ' + sym + '//' + 'Hammer / 1 Minute'))
    if inv_hammer == 100:
        webhook = DiscordWebhook(url_pat , content= (':red_circle: ' + sym + '//' + 'Inverted Hammer / 1 Minute'))

    for x in candles2[-5:]:
        op2 = []
        cl2 = []
        hi2 = []
        lo2 = []
        op2.append(float(x[1]))
        cl2.append(float(x[4]))
        hi2.append(float(x[2]))
        lo2.append(float(x[3]))
        
        hammer = indicadores(op2, cl2, hi2, lo2)[0][-1]
        inv_hammer = indicadores(op2, cl2, hi2, lo2)[1][-1]
        white = indicadores(op2, cl2, hi2, lo2)[2][-1]
        black = indicadores(op2, cl2, hi2, lo2)[3][-1]
        
        hammer = hammer.tolist()
        inv_hammer = inv_hammer.tolist()
        white = white.tolist()
        black = black.tolist()
        
        if hammer == 100:
            webhook = DiscordWebhook(url_pat , content= (':green_circle: ' + sym + '//' + 'Hammer / 1 Hour'))
        if inv_hammer == 100:
            webhook = DiscordWebhook(url_pat , content= (':red_circle: ' + sym + '//' + 'Inverted Hammer / 1 Hour'))      
        if white == 100:
            webhook = DiscordWebhook(url_pat , content= (':green_circle: ' + sym + '//' + 'Three White Soldier / 1 Hour'))
        if black == -100:
            webhook = DiscordWebhook(url_pat , content= (':red_circle: ' + sym + '//' + 'Three Black Crows / 1 Hour'))
            
                       
    open1 = float(candles[-3][1])
    open2 = float(candles[-1][1])
    dif_open = float((open2 * 100 / open1) - 100)
    dif_open2 = float("{:.3f}".format(dif_open))
             
    if dif_open > 1.7:
        dif_open3 = str(dif_open2)
        webhook = DiscordWebhook(url_var , content= (':green_circle: ' + sym + '//' + dif_open3 + '%' + ' Up'))
        response = webhook.execute()
    if dif_open < -1.7:
        dif_open3 = str(dif_open2)
        webhook = DiscordWebhook(url_var , content= (':red_circle: ' + sym + '//' + (dif_open3*-1) + '%' + ' Down'))
        response = webhook.execute()      





while True: 
    for x in price_qnt:
        start_qnt(x)
    for x in price_var:
        start_var(x)

        
    if len(trade_id) > 30000:
        del trade_id[:20000]
    
    
    time.sleep(90)











