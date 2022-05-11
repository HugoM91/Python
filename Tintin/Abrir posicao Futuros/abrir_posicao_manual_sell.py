
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
import inspect
from discord_webhook import DiscordWebhook
import time

request_client = RequestClient(api_key='qZjzNUgXyuQazOmkvuU1GMAkIjoxDRkvjeHeCLRFwcvCO0fx1kZeU2IdZLvIrzgx', secret_key='uad9STV3faJFfMWDAVvPvdd5e8pVY51ciAgR5Hmiw6gla0vMw3oL2HVEltabvrLB')
url_pos = 'https://discordapp.com/api/webhooks/716716241275977910/GbK-3BZZHr5bYNd-W1_PEEqkPVa67CsKJyhkopNBpdskfW88GGCGNV8Xyl0GAgi1uswB'
url_teste = 'https://discordapp.com/api/webhooks/717350806768189581/bWI72oh5kMEHXBhcgX78fEBP_OmtwZ5Lu7CF7teJyo5HBWkx-pNuLc60fI2CpRnL9qtQ'



def position(a):
    result = request_client.get_position()
    print(result)
    def get_entry_price(result_list, sym):
        for pos_obj in result_list:
           #print(pos_obj.symbol)
           if pos_obj.symbol == sym:
               return pos_obj.entryPrice , pos_obj.positionAmt
                  
    entry_price = get_entry_price(result, a)[0]
    position_size = get_entry_price(result, a)[1]

    return entry_price, position_size



def startorder_open (a):
    result = request_client.get_mark_price(symbol=a)
    entry = int(result.markPrice + (result.markPrice*0.0002))
    qnt = 0.2
    tp = int(entry - (entry * 0.0032))
    tp2 = int(entry - (entry * 0.006))
    sl = int(entry + (entry * 0.0024))
    open_order = request_client.post_order(symbol=a, side=OrderSide.SELL, ordertype=OrderType.LIMIT,  timeInForce="GTC", quantity= qnt, price = entry)    
    webhook = DiscordWebhook(url_pos , content= (':red_circle:' + '---Open Short---' + '\n' +  'Entry:  ' + str(entry) + '\n' + 'Take Profit 1 :  ' + str(tp) + '\n' + 'Take Profit 2 :  ' + str(tp2) + '\n' + 'Stop Loss: ' + str(sl)))
    response = webhook.execute()
    
def tp_stop(a):
    
    qnt = 0.2
    qnt2 = 0.1
    tp = int(position(a)[0] - (position(a)[0] * 0.0032))
    tp2 = int(position(a)[0] - (position(a)[0] * 0.006))
    sl = int(position(a)[0] + (position(a)[0] * 0.0024))

    
    take_profit  = request_client.post_order(symbol=a, side=OrderSide.BUY, ordertype=OrderType.LIMIT, timeInForce="GTC", quantity= qnt2, price = tp) 
    take_profit2  = request_client.post_order(symbol=a, side=OrderSide.BUY, ordertype=OrderType.LIMIT, timeInForce="GTC", quantity= qnt2, price = tp2) 
    stop_loss = request_client.post_order(symbol=a, side=OrderSide.BUY, ordertype=OrderType.STOP, timeInForce="GTC", quantity= qnt, price = sl, stopPrice = sl)
    

    

def run(a):
    #startorder_open(a)
    tp_stop(a)
    
run('BTCUSDT')
    
    
    
    
    























