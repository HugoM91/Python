
from pandas_fun import create_graph
import telebot
from telebot import types
from data import candles_stock

bot = telebot.TeleBot("")

def run():
    
    @bot.message_handler(commands=['ola'])
    def send_welcome(message):
        user = message.from_user.first_name
        msg_id = message.chat.id
        chat_id1  = msg_id
        markup = types.ReplyKeyboardMarkup()

        crypto = types.KeyboardButton("/crypto_info")
        stock = types.KeyboardButton('/stock_info')
        c1 = types.KeyboardButton('/crypto_chart')
        s1 = types.KeyboardButton('/stock_chart')
        algo = types.KeyboardButton('/lista_c')
        algo2 = types.KeyboardButton('/lista_s')

        markup.row(crypto, stock)
        markup.row(c1,s1)
        markup.row(algo,algo2)

        bot.send_message(chat_id1, "Ola princesa " + user , reply_markup=markup, disable_notification=True)
    
    @bot.message_handler(commands=['stock_info'])
    def send_welcome(message):
        msg_id = message.chat.id
        msg = bot.reply_to(message, "Stock symbol please")
        bot.register_next_step_handler(msg, process_name_step2)

    @bot.message_handler(commands=['crypto_chart'])
    def send_welcome2(message):
        msg_id = message.chat.id
        msg = bot.reply_to(message, "Symbol + candle time \nCandle times - 1d, 4h, 1h, 30m\nexemplo : btc 1d   ou  eth 4h   ou   xrp 1h      ou enj 30m")
        bot.register_next_step_handler(msg, process_name_step)

    @bot.message_handler(commands=['lista_c'])
    def send_welcome(message):
        msg_id = message.chat.id
        msg = bot.reply_to(message, "'BTC', 'ETH', 'BNB', 'BCC', 'NEO', 'LTC', 'QTUM', 'ADA', 'XRP', 'EOS', 'TUSD', 'IOTA', 'XLM', 'ONT', 'TRX', 'ETC', 'ICX', 'VEN', 'NULS', 'VET', 'PAX', 'BCHABC', 'BCHSV', 'USDC', 'LINK', 'WAVES', 'BTT', 'USDS', 'ONG', 'HOT', 'ZIL', 'ZRX', 'FET', 'BAT', 'XMR', 'ZEC', 'IOST', 'CELR', 'DASH', 'NANO', 'OMG', 'THETA', 'ENJ', 'MITH', 'MATIC', 'ATOM', 'TFUEL', 'ONE', 'FTM', 'ALGO', 'USDSB', 'GTO', 'ERD', 'DOGE', 'DUSK', 'ANKR', 'WIN', 'COS', 'NPXS', 'COCOS', 'MTL', 'TOMO', 'PERL', 'DENT', 'MFT', 'KEY', 'STORM', 'DOCK', 'WAN', 'FUN', 'CVC', 'CHZ', 'BAND', 'BUSD', 'BEAM', 'XTZ', 'REN', 'RVN', 'HC', 'HBAR', 'NKN', 'STX', 'KAVA', 'ARPA', 'IOTX', 'RLC', 'MCO', 'CTXC', 'BCH', 'TROY', 'VITE', 'FTT', 'EUR', 'OGN', 'DREP', 'BULL', 'BEAR', 'ETHBULL', 'ETHBEAR', 'TCT', 'WRX', 'BTS', 'LSK', 'BNT', 'LTO', 'EOSBULL', 'EOSBEAR', 'XRPBULL', 'XRPBEAR', 'STRAT', 'AION', 'MBL', 'COTI', 'BNBBULL', 'BNBBEAR', 'STPT', 'WTC', 'DATA', 'XZC', 'SOL', 'CTSI', 'HIVE', 'CHR', 'BTCUP', 'BTCDOWN', 'GXS', 'ARDR', 'LEND', 'MDT', 'STMX', 'KNC', 'REP', 'LRC', 'PNT', 'COMP', 'BKRW', 'SC', 'ZEN', 'SNX', 'ETHUP', 'ETHDOWN', 'ADAUP', 'ADADOWN', 'LINKUP', 'LINKDOWN', 'VTHO', 'DGB', 'GBP', 'SXP', 'MKR', 'DAI', 'DCR', 'STORJ', 'BNBUP', 'BNBDOWN', 'XTZUP', 'XTZDOWN', 'MANA', 'AUD', 'YFI', 'BAL', 'BLZ', 'IRIS', 'KMD', 'JST', 'SRM', 'ANT', 'CRV', 'SAND', 'OCEAN', 'NMR', 'DOT', 'LUNA', 'RSR', 'PAXG', 'WNXM', 'TRB', 'BZRX', 'SUSHI', 'YFII', 'KSM', 'EGLD', 'DIA', 'RUNE', 'FIO', 'UMA', 'EOSUP', 'EOSDOWN', 'TRXUP', 'TRXDOWN', 'XRPUP', 'XRPDOWN', 'DOTUP', 'DOTDOWN', 'BEL', 'WING', 'LTCUP', 'LTCDOWN', 'UNI', 'NBS', 'OXT', 'SUN', 'AVAX', 'HNT', 'FLM', 'UNIUP', 'UNIDOWN', 'ORN', 'UTK', 'XVS', 'ALPHA', 'AAVE', 'NEAR', 'SXPUP', 'SXPDOWN', 'FIL', 'FILUP', 'FILDOWN', 'YFIUP', 'YFIDOWN', 'INJ', 'AUDIO', 'CTK', 'BCHUP', 'BCHDOWN', 'AKRO', 'AXS', 'HARD', 'DNT', 'STRAX', 'UNFI', 'ROSE', 'AVA', 'XEM', 'AAVEUP', 'AAVEDOWN', 'SKL', 'SUSD', 'SUSHIUP', 'SUSHIDOWN', 'XLMUP', 'XLMDOWN', 'GRT', 'JUV', 'PSG', '1INCH', 'REEF', 'OG', 'ATM', 'ASR'")
    
    @bot.message_handler(commands=['crypto_info'])
    def send_welcome(message):
        bot.reply_to(message, " KALINKA ")
    
    @bot.message_handler(commands=['stock_charts'])
    def send_welcome(message):
        bot.reply_to(message, " KALINKA ")
    
    @bot.message_handler(commands=['lista_s'])
    def send_welcome(message):
        bot.reply_to(message, " KALINKA ")



    def process_name_step(message):
        msg = message.text.upper()
        msg = msg.split(" ")
        msg_id = message.chat.id
        create_graph(msg[0], "USDT", msg[1])
        photo = open('test.png', 'rb')
        bot.send_photo(msg_id, photo)
        photo = open('test1.png', 'rb')
        bot.send_photo(msg_id, photo)
        photo = open('test2.png', 'rb')
        bot.send_photo(msg_id, photo)
        photo = open('test3.png', 'rb')
        bot.send_photo(msg_id, photo)
        photo = open('test4.png', 'rb')
        bot.send_photo(msg_id, photo)
        photo = open('test5.png', 'rb')
        bot.send_photo(msg_id, photo)
        
    def process_name_step2(message):

        msg = message.text.upper()
        #msg = msg.split(" ")
        msg_id = message.chat.id
    
        #a = candles_stock(msg, 100)
        
        photo = open('test.png', 'rb')
        bot.send_photo(msg_id, photo)
        photo = open('test1.png', 'rb')
        bot.send_photo(msg_id, photo)
        photo = open('test2.png', 'rb')
        bot.send_photo(msg_id, photo)
        photo = open('test3.png', 'rb')
        bot.send_photo(msg_id, photo)

        #bot.send_message(msg_id, str(a["longBusinessSummary".upper()]))
    
    bot.polling()