



def stream():

    from binance_f import RequestClient
    from binance_f import SubscriptionClient
    from binance_f.constant.test import *
    from binance_f.model import *
    from binance_f.exception.binanceapiexception import BinanceApiException
    from binance_f.base.printobject import *
    from discord_webhook import DiscordWebhook
    
    url_pos = ''
    request_client = RequestClient(api_key='', secret_key='')
    listen_key = request_client.start_user_data_stream()
    result = request_client.keep_user_data_stream()
    sub_client = SubscriptionClient(api_key='', secret_key='')
    
    
    def callback(data_type: 'SubscribeMessageType', event: 'any'):
        if data_type == SubscribeMessageType.RESPONSE:
            print("Event ID: ", event)
        elif  data_type == SubscribeMessageType.PAYLOAD:
            if(event.eventType == "ORDER_TRADE_UPDATE"):  
                a = str(event.type)
                print(a)
                
                if event.orderStatus == 'FILLED' and a == 'LIMIT':
                    webhook = DiscordWebhook(url_pos , content= ('Position Closed - TAKE PROFIT'))
                    response = webhook.execute()
                    result = request_client.cancel_all_orders(symbol="BTCUSDT")
                if event.orderStatus == 'FILLED' and a == 'STOP_MARKET':
                    webhook = DiscordWebhook(url_pos , content= ('Position Closed - STOP LOSS'))
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
