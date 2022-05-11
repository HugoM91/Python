


from binance.client import Client
import time
from discord_webhook import DiscordWebhook
from indicadores import indicadores
import numpy as np

client = Client('', '')
h = []
trade_id=[]
url_qnt = 'https://discordapp.com/api/webhooks/713723604994490368/cKOQON2_l5kJa0_Lpb2bpADPRSbe2g8lBh5AiUFWle006Fl-iBAEChf0SnL3wIKi-XIS'
url_qnt1 = 'https://discordapp.com/api/webhooks/713899580982427660/u110pz8fa7H_TSO130FbLM4YUGKfICdzrW82WC6Snk5rbT1eeXizZQvmQ8tsax_qMbhC' 
url_var = 'https://discordapp.com/api/webhooks/713841134471872539/a4jZBrxNdBbUEFjj4d0eIqkcbt8_Izme0ZjwAg2c-jKRILwKoByd2y6goJkFcn8zSDya'
url_var24 = 'https://discordapp.com/api/webhooks/715236738125135962/L9tY-mhHUpmxcWkcPGtiqooqI-YlvXbo4SWdNJCXQBMenWMzVvsZevt-h0-G51Bl3SFn'
url_pat = 'https://discordapp.com/api/webhooks/716241164680036402/4uILix2eh8eQIIUek33KiHQHvI3ID2DJJ5H6vsUtIf1YRrgeRgIlkB0yRha3s52c_XNa'
url_vol = 'https://discordapp.com/api/webhooks/718214126500839474/qHgtNjCPALrLOSQ8S9Mm6ChcQkxFlc5ymbz_5yDRPc_YdJrZ0-xL8eUUSw0OnyaDQQb0'



price_qnt = ['BTCUSDT', 'BNBUSDT', 'ETHUSDT', 'XRPUSDT' , 'XMRUSDT' , 'LTCUSDT' , 'EOSUSDT', 'TRXUSDT', 'NEOUSDT', 'IOTAUSDT', 'ZECUSDT', 'DASHUSDT', 'ENJUSDT','MCOUSDT','XLMUSDT' ,'BATUSDT','BTTUSDT', 'ONTUSDT', 'WINUSDT','ENJBTC', 'MCOBTC','BATBTC','NEOBTC', 'XRPBTC' ,'IOSTBTC','ZRXBTC', 'NANOBTC' , 'DOGEBTC', 'ETCBTC', 'XEMBTC', 'QTUMBTC' ,'KNCBTC','SNTBTC'   ]            
price_var = ['BTCUSDT', 'BNBUSDT', 'ETHUSDT', 'XRPUSDT' , 'XMRUSDT' , 'LTCUSDT' , 'EOSUSDT', 'TRXUSDT', 'NEOUSDT', 'IOTAUSDT', 'VETUSDT', 'QTUMUSDT', 'IOSTUSDT', 'ADAUSDT', 'XTZUSDT' , 'ONTUSDT' , 'BATUSDT' ]


vol = {}
i = 0 

def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]
 
        
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
    candles = client.get_klines(symbol=sym, interval=Client.KLINE_INTERVAL_1MINUTE, limit = 6)

    op = []
    hi = []
    lo = []
    cl = []
    vp = []
      
    for x in candles:
        op.append(float(x[1]))
        hi.append(float(x[2]))
        lo.append(float(x[3]))
        cl.append(float(x[4]))
        vo.append(float(x[5]))
#---------------------------
    op_dif = (op[5] * 100 / op[1]) - 100
        
    if op[1] < cl[1] and op[2] < cl[2] and op[3] < cl[3] and op[4] < cl[4] and op[5] < cl[5] and op_dif > 0.35:
        webhook = DiscordWebhook(url_pat , content= (':green_circle' + ' Five White Soldiers - 1 minute // ' + sym))
        response = webhook.execute()
    if op[1] > cl[1] and op[2] > cl[2] and op[3] > cl[3] and op[4] > cl[4] and op[5] > cl[5] and op_dif > 0.35:
        webhook = DiscordWebhook(url_pat , content= (':red_circle' + ' Five Black Crows - 1 minute // ' + sym))
        response = webhook.execute()   
#------------------------    
    set_key(vol, sym, vo[-2])

    if i >= 1 and op[-2] > cl[-2] :
        if vo > ((sum(vol[sym])/len(vol[sym])) * 8):
            webhook = DiscordWebhook(url_vol , content= (':red_circle' + ' High Volume // ' + sym))
            response = webhook.execute()
    if i >= 1 and op[-2]  < cl[-2] :
        if vo > ((sum(vol[sym])/len(vol[sym])) * 8):
            webhook = DiscordWebhook(url_vol , content= (':green_circle' + ' High Volume // ' + sym))
            response = webhook.execute()   
#---------------------------        
    hi_lo = (hi[-2]  - lo[-2] ) * 0.9
    hi_lo_p = (hi[-2]  * 100 / lo[-2] ) - 100
    
    if op[-2]  > (hi_lo + lo[-2] ) and cl[-2]  > (hi_lo + lo[-2] ) and hi_lo_p > 0.1:
        webhook = DiscordWebhook(url_pat , content= (':green_circle: ' + sym + '//' + ' Hammer - 1 minute '))
        response = webhook.execute()
    if op[-2]  < (hi[-2]  - hi_lo) and cl[-2]  < (hi[-2]  - hi_lo) and hi_lo_p > 0.1:
        webhook = DiscordWebhook(url_pat , content= (':red_circle: ' + sym + '//' + ' Shooting Star - 1 minute'))
        response = webhook.execute()
               
#---------------------------         
    open1 = float(op[-3])
    open2 = float(op[-1])
    dif_open = float((open2 * 100 / open1) - 100)
    dif_open2 = float("{:.3f}".format(dif_open))
             
    if dif_open > 1.7:
        dif_open3 = str(dif_open2)
        webhook = DiscordWebhook(url_var , content= (':green_circle: ' + sym + '//' + dif_open3 + '%' + ' Up'))
        response = webhook.execute()
    if dif_open < -1.7:
        dif_open3 = str(dif_open2)
        webhook = DiscordWebhook(url_var , content= (':red_circle: ' + sym + '//' + dif_open3 + '%' + ' Down'))
        response = webhook.execute()      


while True: 
    for x in price_qnt:
        start_qnt(x)
    for x in price_var:
        start_var(x)

        
    if len(trade_id) > 30000:
        del trade_id[:20000]
    
    i += 1 
    time.sleep(90)











