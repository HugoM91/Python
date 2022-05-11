import json
import operator
import time
import telebot
from telebot import types
from register import register, login


chat_id1 = 0 # grupo cod

user_id = "" # usado para ver se o user responde a quem chamou o metodo. Ex se bernardo chamou registar a proxima mensagem (input) so funciona se for do bernardo

msg_id_del = [] # Id of the messages you want to delete


class telegram:

    def __init__(self, bot):
        self.bot = telebot.TeleBot(bot)
        self.msg_id = 0
        self.nome_castigo = "Lollipop"

    def set_key(self, dictionary, key, value):
        if key not in dictionary:
           dictionary[key] = value
        elif type(dictionary[key]) == list:
            dictionary[key].append(value)
        else:
            dictionary[key] = [dictionary[key], value]

    def ranking(self):
        users = {}  #TELEGRAM USER AND ACTIVION IDS
        final = {}
        mensagem = ''

        for x,y in users.items():
            with open('basedados/' + x + '_regist_' + str(y) + '.json') as json_file:
                j = json.load(json_file)

                if j != 0:
                    user2 = login(j)
                    user2.user.open()
                    user2.user.filter()
                    ranking = user2.user.ranking()

                self.set_key(final, x, ranking)

        a = dict(sorted(final.items(), key=operator.itemgetter(1),reverse=True))


        i = 0
        emoji = ['👑','🤘','😿','☔','🐫','🐭']


        for x,y in a.items():
            mensagem = mensagem + emoji[i] + ' - ' + str(x) + " : " + str(float("{:.2f}".format(y))) + '\n'
            i += 1


        return mensagem




    def username(self, user_name, user_id):

        # PERSONALIZED MESSAGES FOR DIFFERENT USERS
        if user_name == "":
            with open('basedados/' + str(user_id) + '.json') as json_file:
                j = json.load(json_file)
        if user_name == "":
            with open('basedados/' + str(user_id) + '.json') as json_file:
                j = json.load(json_file)
        if user_name == "":
            with open('basedados/' + str(user_id) + '.json') as json_file:
                j = json.load(json_file)
        if user_name == "":
            with open('basedados/' + str(user_id) + '.json') as json_file:
                j = json.load(json_file)
        if user_name == "":
            with open('basedados/' + str(user_id) + '.json') as json_file:
                j = json.load(json_file)
        if user_name == "":
            with open('basedados/' + str(user_id) + '.json') as json_file:
                j = json.load(json_file)
        if user_name == "":
            with open('basedados/' + str(user_id) + '.json') as json_file:
                j = json.load(json_file)

        return j



    def run (self):



        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            user = message.from_user.first_name
            msg_id = message.chat.id
            chat_id1  = msg_id
            markup = types.ReplyKeyboardMarkup()

            registar = types.KeyboardButton("/Registar", )
            update = types.KeyboardButton('/Update')
            stats = types.KeyboardButton('/Stats')
            last20 = types.KeyboardButton('/Last20')
            rank = types.KeyboardButton('/Rank')
            ranking = types.KeyboardButton('/Ranking')
            procurar = types.KeyboardButton('/Procurar')
            eggs = types.KeyboardButton('/Timer')

            markup.row(stats, last20, rank)
            markup.row(update, ranking)
            markup.row(registar, procurar, eggs)

            if user == "Manuel":
                self.bot.send_message(chat_id1, "Fodasse ", reply_markup=markup,disable_notification=True)
            else:
                self.bot.send_message(chat_id1, "Ola princesa " + user + ", ufa!!!  nao e o Ma***", reply_markup=markup, disable_notification=True)



        @self.bot.message_handler(commands=['Registar'])
        def send_welcome(message):
            msg_id = message.chat.id

            msg = self.bot.reply_to(message, "Input your data: \nexemplo ps4 = ps4/Tugalicious7/0\nexemplo battlenet = pc/username/batlenet id")
            msg_id_del.append(self.msg_id + 1)
            self.bot.register_next_step_handler(msg, process_name_step)

        def process_name_step(message):
            msg_id_del.append(self.msg_id + 1)

            msg = message.text.split("/")

            if (msg[0] == "pc" or msg[0] == "ps4"):
                if len(msg) == 3:
                    user = register(msg[0], msg[1], msg[2], message.from_user.id, message.chat.id)
                    user.apply_id()
                    if (user.download_stats() == 1):
                        user.filter()
                        user.ranking()
                        with open('basedados/' + str(user.name) + '_regist_' + str(user.idt_user) + '.json', 'w') as json_file:
                            json.dump(user.regist(), json_file)
                        msg_id_del.append(message.chat.id + 1)
                        self.bot.reply_to(message,"Registation Completed \nConsole: " + msg[0] + '\nUsername ' + msg[1] + '\nPC ID: ' + msg[2])
                        time.sleep(3)
                    else:
                        bot_error = open('gif/bot_error.gif', 'rb')
                        self.bot.send_animation(message.chat.id, bot_error,reply_to_message_id=message.message_id)
                        bot_error.close()
                else:
                    self.bot.reply_to(message, "I NEED MORE DATA!!!!! or maybe I have to much of it ????")
            else:
                 self.bot.reply_to(message, "что за херня <" + str(msg[0] + "> ???"))




            #Menu do telegram que indica as opcoes que o user pode tomar// CORE //
        @self.bot.message_handler(commands=['Stats', 'Ranking', 'Rank', 'Procurar', 'Last20', 'Update', 'eggs', 'bunker', 'Timer'])
        def send_welcome(message):
            msg_id = message.chat.id
            chat_id1 = msg_id
            user_name = message.from_user.first_name
            user_id = message.from_user.id
            msg = message.text
            self.msg_id = message.message_id


            j = self.username(user_name, user_id)

            if j != 0:
                user2 = login(j)
                user2.user.open()
                user2.user.filter()
                user2.user.ranking()
                user2.user.mensagem()


                if msg == '/Stats':
                    self.bot.send_message(chat_id1, "Last20\n" + str(user2.user.msg5) + '\n\nOverall\n' + str(user2.user.msg6), disable_notification=True)
                    msg_id_del.append(self.msg_id + 1)
                elif msg == "/Last20":
                    self.bot.send_message(chat_id1, "Last20 detailed\n\n" + str(user2.user.msg4), disable_notification=True)
                    msg_id_del.append(self.msg_id + 1)
                elif msg == "/Rank":
                    self.bot.send_message(chat_id1, "Ranking Breakdown\n\n" + str(user2.user.msg3), disable_notification=True)
                    msg_id_del.append(self.msg_id + 1)
                elif msg == "/Update":
                    user2.user.download_stats()
                    self.bot.send_message(chat_id1, "Updated Completed", disable_notification=True)
                elif msg == "/Ranking":
                    self.bot.send_message(chat_id1, str(self.ranking()))
                    msg_id_del.append(self.msg_id + 1)
                elif msg == "/Procurar":
                    self.bot.send_message(chat_id1, "Under construction")
                    msg_id_del.append(self.msg_id + 1)
                elif msg == "/eggs":
                    bot_error = open('eggs/1.png', 'rb')
                    self.bot.send_photo(message.chat.id, bot_error, reply_to_message_id=message.message_id)
                elif msg == "/bunker":
                    bot_error = open('eggs/2.png', 'rb')
                    self.bot.send_photo(message.chat.id, bot_error, reply_to_message_id=message.message_id)
                    self.bot.reply_to(message, "Red Card Only - 0; 4; 5; 6; 9\nClosed - 2; 7; 8;  //  Easter Egg - 11\nCode -\n1:  97264138   //  3:  87624851\n10:  60274513  //  Farmland:  49285163\nTvShack: 27495810  //  PrisonShack: 72948531")
                elif msg == "/Timer":
                    self.bot.reply_to(message, 'GOGOGO !!!')
                    time.sleep(120)
                    self.bot.reply_to(message, '1/2 tic tok')
                    time.sleep(120)
                    self.bot.reply_to(message, 'You Shall Not Play')











        self.bot.polling()



