import time

import telebot

bot = telebot.TeleBot("1374176915:AAE-PEInK_nyLMOPSLSz7uDdFzYzDs9XC1E") # cod bot

print('ola')

@bot.message_handler(commands=['maldicao80'])
def send_welcome(message):
    bot.register_next_step_handler(message, process_name_step2)
def process_name_step2(message):
    bot.reply_to(message,"ðð¿ââï¸")
    time.sleep(1)
    bot.reply_to(message,"ð¤· ")
    time.sleep(1)
    bot.reply_to(message,"ðð¾ââï¸ ")
    time.sleep(1)
    bot.reply_to(message, "ðð»ââï¸ ")
    time.sleep(1)
    bot.reply_to(message, message.text + "ðð You have ð been âcursedâ  ã mUahahaha â ï¸â ï¸â ï¸ ")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    user = message.from_user.first_name
    msg_id = message.from_user.id
    chatid = message.chat.id

    if user == "Hugo":
        bot.edit_message_text(text="Sou coco", chat_id=message.chat.id, message_id=msg_id)
        bot.reply_to(message, "Sou Coco")

bot.polling()