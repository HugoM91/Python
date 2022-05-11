import requests
import time
import json
import os
import pandas


class register:

    # --- construtor
    def __init__(self, console, name, id_console, idt_user, idt_chat):
        self.msg7 = ""  # mensgame soma dos last 20 jogos individuais
        self.msg6 = ""  # mensagem dos stats overall
        self.msg5 = ""  # mensagem last 20 todos os jogos
        self.msg4 = ""  # mensagem last 20 jogos individuais
        self.msg3 = ""  # mensagem do ranking
        self.msg2 = "\nOverall  \n"
        self.msg1 = "Last 20 \n"
        self.r_last20 = {}
        self.r_overall = {}
        self.console = console
        self.name = name
        self.member_type = 0
        self.id_console = id_console  # id usado no caso de ser um jogador de pc / pode ser battlenet ou activision
        self.over_updated = {}
        self.l20_updated = {}
        self.l20_stats_matches = []
        self.over_stats = []
        self.idt_user = idt_user  # id do user no telegram quando se regista
        self.idt_chat = idt_chat  # id do chat no telegram quando o user se regista
        self.id_programa = 0

    # --- fazer print bonito
    def regist(self):
        print("Consola : {} \nUsername: {} \nID: {} \nID username telegram: {} \nID chat telegram: {}".format(
            self.console, self.name, self.id_programa, self.idt_user, self.idt_chat))
        lista = {"name": self.name, "id_programa": self.id_programa, "member_type": self.member_type,
                 "console": self.console, "id_console": self.id_console, "idt_chat": self.idt_chat,
                 "idt_user": self.idt_user}
        return lista

    # ---trocar o tipo de membership
    def apply_membership(self, var):
        self.member_type = var

    # ---atribuir o id. FALTA COMPLETAR COM A LOGICA CERTA
    def apply_id(self):
        self.id_programa = 1

    # ---Ir buscar as stats do jogador e meter num json
    def download_stats(self):

        if self.console == "ps4":
            url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone-matches/" + self.name + "/psn"
            url2 = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/" + self.name + "/psn"
        elif self.console == "pc":
            url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone-matches/" + self.name + "%" + self.id_console + "/battle"
            url2 = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/" + self.name + "%" + self.id_console + "/battle"
        else:
            print("      Not a valid console")
            url = 0

        if url == 0:
            print("!!!  Register did not work  !!!")

        else:
            headers = {
                'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com",
                'x-rapidapi-key': "18334bf943msh0fb9fcacb717d1ap16a96bjsn6f8a046d4125"
            }

            if os.path.isfile('basedados/' + self.name + '_l20.json'):
                os.remove('basedados/' + self.name + '_l20.json')
            if os.path.isfile('basedados/' + self.name + '_over.json'):
                os.remove('basedados/' + self.name + '_over.json')

            response = requests.request("GET", url, headers=headers)

            if len(response.text) < 500:

                return 0

            else:
                res = json.loads(response.text)
                with open('basedados/' + self.name + '_l20.json', 'w') as json_file:
                    json.dump(res, json_file)
                time.sleep(1)

                response2 = requests.request("GET", url2, headers=headers)
                res2 = json.loads(response2.text)
                with open('basedados/' + self.name + '_over.json', 'w') as json_file:
                    json.dump(res2, json_file)
                time.sleep(1)

                print("!!! File Created !!!")

                return 1

    # ---cria dicionario
    def set_key(self, dictionary, key, value):
        if key not in dictionary:
            dictionary[key] = value
        elif type(dictionary[key]) == list:
            dictionary[key].append(value)
        else:
            dictionary[key] = [dictionary[key], value]

        # --- Cria as listas com as stats. Retorna dicionarios <l20>[0] e <over>[1]

    # ---abre o ficheiro json
    def open(self):
        with open('basedados/' + self.name + '_l20.json') as json_file:
            self.l20 = json.load(json_file)
        with open('basedados/' + self.name + '_over.json') as json_file:
            self.over = json.load(json_file)

        return self.l20, self.over

        # --- Filtra as listas iniciais. Retorna dicionarios <l20_up>[0] e <over_up>

    # ---filtra as stats
    def filter(self):

        self.open()
        # --- Last20 // l20_stats_summary = []
        self.l20_stats_matches = ["mode", "playerStats", "kills", "headshots", "assists", "scorePerMinute", "deaths",
                                  "kdRatio", "executions", "percentTimeMoving", "longestStreak", "teamPlacement",
                                  "damageDone", "damageTaken"]

        i = 0
        while i != len(self.l20['matches']):
            for x, y in self.l20['matches'][i].items():
                if x == "mode":
                    self.set_key(self.l20_updated, x, y + '\n')

            for x, y in self.l20['matches'][i]["playerStats"].items():
                if x in self.l20_stats_matches:
                    self.set_key(self.l20_updated, x, float("{:.2f}".format(y)))

            self.set_key(self.l20_updated, "damage_dif",
                         float("{:.2f}".format((self.l20['matches'][i]["playerStats"]['damageDone'] -
                                                self.l20['matches'][i]["playerStats"]['damageTaken']))))

            i += 1

        # --- Overall // #self.wz_total = self.over["br_all"]  //  #self.plunder_total = self.over["br_dmz"]

        self.br_total = self.over["br"]

        self.over_stats = ["wins", "topFive", "topTen", "gamesPlayed", "kills", "kdRatio", "downs",
                           "contracts", "score", "scorePerMinute", "deaths"]

        i2 = 0
        for x in self.over_stats:
            if i2 == 0:
                winp = self.br_total['wins'] * 100 / self.br_total['gamesPlayed']
                top5p = self.br_total['topFive'] * 100 / self.br_total['gamesPlayed']
                top10p = self.br_total['topTen'] * 100 / self.br_total['gamesPlayed']
                self.set_key(self.over_updated, "winp", float("{:.2f}".format(winp)))
                self.set_key(self.over_updated, "top5p", float("{:.2f}".format(top5p)))
                self.set_key(self.over_updated, "top10p", float("{:.2f}".format(top10p)))
                i2 += 1

            self.set_key(self.over_updated, x, float("{:.2f}".format(self.br_total[x])))


        print(self.over_updated)
        print('-------------')
        print(self.l20_updated)

    # --- converte as stats em ponstos do ranking
    def ranking(self):
        # ---- Overall

        winp = self.over_updated['winp'] / 15 * 25
        top5p = self.over_updated['top5p'] / 40 * 10
        top10p = self.over_updated['top10p'] / 65 * 5
        kdRatio = self.over_updated['kdRatio'] / 6 * 35
        scorePerMinute = self.over_updated['scorePerMinute'] / 800 * 25

        total = (winp + top5p + top10p + kdRatio + scorePerMinute) * 0.65

        self.set_key(self.r_last20, "total", float("{:.2f}".format(total)))
        self.set_key(self.r_last20, "winp", float("{:.2f}".format(winp)))
        self.set_key(self.r_last20, "top5p", float("{:.2f}".format(top5p)))
        self.set_key(self.r_last20, "top10p", float("{:.2f}".format(top10p)))
        self.set_key(self.r_last20, "kdRatio", float("{:.2f}".format(kdRatio)))
        self.set_key(self.r_last20, "scorePerMinute", float("{:.2f}".format(scorePerMinute)))

        # ---- Last 20

        ["mode", "playerStats", "kills", "deaths","assists", "kdRatio", "damageDone" ,"damageTaken" ,"headshots"
            ,"executions","longestStreak", "percentTimeMoving", "scorePerMinute",  "teamPlacement"]

        kdRatio = sum(self.l20_updated['kdRatio']) / len(self.l20_updated['kdRatio']) / 2 * 3

        damage_dif = (sum(self.l20_updated['damageDone']) / sum(self.l20_updated['damageTaken'])) / 20 * 15
        teamPlacement = (100 - sum(self.l20_updated['teamPlacement']) / len(self.l20_updated['teamPlacement'])) / 90 * 3

        longestStreak = max(self.l20_updated['longestStreak']) / 20 * 5
        scorePerMinute = sum(self.l20_updated['scorePerMinute']) / len(self.l20_updated['scorePerMinute']) / 350 * 5
        assists = sum(self.l20_updated['assists']) / 30 * 5
        executions = sum(self.l20_updated['executions']) / 10 * 5
        headshots = sum(self.l20_updated['headshots']) / 30 * 5
        deaths = sum(self.l20_updated['deaths']) / len(self.l20_updated['deaths']) / 4 * (-3)

        total2 = kdRatio + damage_dif + teamPlacement + longestStreak + scorePerMinute + assists + executions + headshots + deaths

        self.set_key(self.r_overall, 'total', float("{:.2f}".format(total2)))
        self.set_key(self.r_overall, 'kdRatio', float("{:.2f}".format(kdRatio)))
        self.set_key(self.r_overall, 'damage_dif', float("{:.2f}".format(damage_dif)))
        self.set_key(self.r_overall, 'teamPlacement', float("{:.2f}".format(teamPlacement)))
        self.set_key(self.r_overall, 'longestStreak', float("{:.2f}".format(longestStreak)))
        self.set_key(self.r_overall, 'scorePerMinute', float("{:.2f}".format(scorePerMinute)))
        self.set_key(self.r_overall, 'assists', float("{:.2f}".format(assists)))
        self.set_key(self.r_overall, 'executions', float("{:.2f}".format(executions)))
        self.set_key(self.r_overall, 'headshots', float("{:.2f}".format(headshots)))
        self.set_key(self.r_overall, 'deaths', float("{:.2f}".format(deaths)))

        for x, y in self.r_overall.items():
            self.msg1 = self.msg1 + str(x) + ": " + str(y) + '\n'

        for x, y in self.r_last20.items():
            self.msg2 = self.msg2 + str(x) + ": " + str(y) + '\n'

        self.msg3 = "Ranking Final: " + str(
            self.r_overall['total'] * 0.7 + self.r_last20['total']) + "\n \n" + self.msg1 + self.msg2

        return self.r_overall['total'] * 0.7 + self.r_last20['total']

    # --- funcao para criar mensagens
    def mensagem(self):

        passa = ["scorePerMinute", "percentTimeMoving", "damageDone", "damageTaken", "longestStreak", "headshots",
                 'executions', 'assists', 'kdRatio']

        passa3 = ["topFive", "topTen", "gamesPlayed", "kills", "score"]

        i = 0
        i2 = 0
        i3 = 0
        i3 = 0

        while i <= len(self.l20_updated):
            for x, y in self.l20_updated.items():
                if x in passa:
                    pass
                else:
                    try:
                        #  if x['mode'] == 'br_brduos':
                           #   self.set_key(self.last20games, x , y)
                        self.msg4 = self.msg4 + str(x) + ": " + str(y[i]) + " // "
                    except IndexError as e:
                        print(e)

            self.msg4 = self.msg4 + '\n'
            i += 1

        for x, y in self.l20_updated.items():
            if type(y[0]) == int or type(y[0]) == float:
                if x == 'scorePerMinute' or x == 'kdRatio' or x == 'percentTimeMoving':
                    k = sum(y)/len(y)
                elif x == 'longestStreak':
                    k = max(y)
                else:
                    k = sum(y)
                if x == 'teamPlacement':
                    pass
                else:
                    self.msg5 = self.msg5 + x + ": " + str(float("{:.2f}".format(k))) + " || "
            i2 += 1
            if i2 == 4 or i2 == 6 or i2 == 8 or i2 == 11 or i2 == 13 or i2 == 18 or i2 == 21:
                self.msg5 = self.msg5 + '\n'


        self.msg5 = self.msg5 + "\n\nAvg Placement: " + str(
            float("{:.2f}".format(sum(self.l20_updated['teamPlacement']) / (len(self.l20_updated['teamPlacement']))))) + '\n' + str(self.l20_updated['teamPlacement'])

        for x, y in self.over_updated.items():

            if x in passa3:
                pass
            else:
                self.msg6 = self.msg6 + str(x) + ": " + str(y) + " || "
                i3 += 1

            if i3 == 3 or i3 == 6 or 13 == 9 or i3 == 12 or i3 == 15 or i3 == 18:
                self.msg6 = self.msg6 + '\n'


class login():
    def __init__(self, login_file):
        self.login_file = login_file
        print(self.login_file)
        self.user = register(login_file['console'], login_file['name'], login_file['id_console'],
                             login_file['idt_user'], login_file['idt_chat'])
