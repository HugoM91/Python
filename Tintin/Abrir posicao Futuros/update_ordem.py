



from binance_f import RequestClient
from binance_f import SubscriptionClient
from binance_f.constant.test import *
from binance_f.model import *
from binance_f.exception.binanceapiexception import BinanceApiException
from binance_f.base.printobject import *
from discord_webhook import DiscordWebhook

url_teste = 'https://discordapp.com/api/webhooks/717350806768189581/bWI72oh5kMEHXBhcgX78fEBP_OmtwZ5Lu7CF7teJyo5HBWkx-pNuLc60fI2CpRnL9qtQ'
url_pos = 'https://discordapp.com/api/webhooks/716716241275977910/GbK-3BZZHr5bYNd-W1_PEEqkPVa67CsKJyhkopNBpdskfW88GGCGNV8Xyl0GAgi1uswB'

request_client = RequestClient(api_key='qZjzNUgXyuQazOmkvuU1GMAkIjoxDRkvjeHeCLRFwcvCO0fx1kZeU2IdZLvIrzgx', secret_key='uad9STV3faJFfMWDAVvPvdd5e8pVY51ciAgR5Hmiw6gla0vMw3oL2HVEltabvrLB')
listen_key = request_client.start_user_data_stream()
result = request_client.keep_user_data_stream()
sub_client = SubscriptionClient(api_key='qZjzNUgXyuQazOmkvuU1GMAkIjoxDRkvjeHeCLRFwcvCO0fx1kZeU2IdZLvIrzgx', secret_key='uad9STV3faJFfMWDAVvPvdd5e8pVY51ciAgR5Hmiw6gla0vMw3oL2HVEltabvrLB')
    


def position(a):
    result = request_client.get_position()
        
    def get_entry_price(result_list, sym):
        for pos_obj in result_list:
           #print(pos_obj.symbol)
           if pos_obj.symbol == sym:
               return pos_obj.entryPrice , pos_obj.positionAmt
                  
    entry_price = get_entry_price(result, a)[0]
    position_size = get_entry_price(result, a)[1]

    return entry_price, position_size


    
def callback(data_type: 'SubscribeMessageType', event: 'any'):
    
    if data_type == SubscribeMessageType.RESPONSE:
        print("Event ID: ", event)
    elif  data_type == SubscribeMessageType.PAYLOAD:
        if(event.eventType == "ORDER_TRADE_UPDATE"):  
            a = str(event.type)
            
            if  event.orderStatus == 'FILLED' and a == 'LIMIT':
            
                result = request_client.get_mark_price(symbol='BTCUSDT')
                e = result.markPrice
                e = str(e)
                
                webhook = DiscordWebhook(url_pos , content= ('TAKE PROFIT  at : ' + e))
                response = webhook.execute()
                
                result = request_client.cancel_all_orders(symbol="BTCUSDT")
                
                if position('BTCUSDT')[0] > 0:
                    tp = int(position('BTCUSDT')[0] + (position(a)[0] * 0.0052))
                    sl = int(position('BTCUSDT')[0])
                    qnt = position('BTCUSDT')[1]
                    stop_loss = request_client.post_order(symbol=a, side=OrderSide.BUY, ordertype=OrderType.STOP, timeInForce="GTC", quantity= qnt, price = sl, stopPrice = sl)
                    take_profit  = request_client.post_order(symbol=a, side=OrderSide.BUY, ordertype=OrderType.LIMIT, timeInForce="GTC", quantity= qnt, price = tp) 
                    webhook = DiscordWebhook(url_teste , content= ('Stop moved to entry'))
                    response = webhook.execute()
                
            if event.orderStatus == 'FILLED' and a == 'STOP_MARKET':
                result = request_client.get_mark_price(symbol=a)
                e = result.markPrice
                e = str(e)
                webhook = DiscordWebhook(url_teste , content= ('Position Closed - STOP LOSS' + e ))
                response = webhook.execute()
                result = request_client.cancel_all_orders(symbol="BTCUSDT")

                
    
        elif(event.eventType == "listenKeyExpired"):
            print("CAUTION: YOUR LISTEN-KEY HAS BEEN EXPIRED!!!")
            print("CAUTION: YOUR LISTEN-KEY HAS BEEN EXPIRED!!!")
            print("CAUTION: YOUR LISTEN-KEY HAS BEEN EXPIRED!!!")
    else:
        print("Unknown Data:")
    print()
    
    
def error(e: 'BinanceApiException'):
   print(e.error_code + e.error_message)
    
sub_client.subscribe_user_data_event(listen_key, callback, error)