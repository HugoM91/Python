from email import encoders
from email.mime.base import MIMEBase
import json
import operator
import time
import telebot
from telebot import types
import xlsxwriter
#import excel2img
import smtplib
import imghdr 
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid
import pandas 
import mysql.connector 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time
from datetime import date
import win32com.client
from PIL import ImageGrab
import os
import pythoncom
import threading
from threading import Thread



mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="decadente"
            )
mydb2 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="decadente"
            )

#mydb = mysql.connector.connect(
 #               host="localhost",
  #              user="licious",
   #             password="1991",
    #            database="decadente"
     #       )


lista_vinho_tinto = ["Pacto","Capela","Andreza","Qnt Convento", "Rebuscado", "Sabicos", "Javali", "Grifo" ]
lista_vinho_branco = ["Paterna", "Golpe", "Docil", "Xisto", "Casa Clara", "Respiro", "Capitão", "Dona Berta"]
lista_espumante = ["Pedreira Brut", "Pedreira Rose", "Uivo", "Conceito", "Vertice"]
lista_portos = ["Terra Prima", "San. LBV", "Javali", "Vallado 20y", "San. 40y"]

lista_bebidas_brancas = []
lista_material_limpeza = []

sender_email = ""
password= ""
rec_email = ""


class telegram:

    def __init__(self, bot):
        self.bot = telebot.TeleBot(bot)
        self.msg_id = 0
        self.data_servico = ""
        self.estabelecimento = ""
        self.nr_reservas = ""
        self.nr_no_shows = ""
        self.nr_cancelamentos = ""
        self.facturacao_total = ""
        self.facturacao_comida = ""
        self.facturacao_vinhos = ""
        self.facturacao_cocktail = ""
        self.facturacao_eventos = ""
        self.tpa_total = ""
        self.tpa_comissoes = ""
        self.cash = ""
        self.descriçao = ""
        self.faltas_cozinha = ""
        self.faltas_sala = ""
        self.reclamacoes = ""
        self.stock_vinhos = {}
        self.email = "hugo.malaquias@hotmail.com"
        self.staff_sala = ""
        self.staff_cozinha = ""
        self.manutencao = ""
        self.contagem_vinho = {} 
        self.encomendar_vinho = {}
        self.nr_walk_in = ""
        self.identificacao_encomendas_vinhos = ""
        self.email_message_vinho = ""
        self.transferencia_de = ""
        self.transferencia_oque = ""
        self.transferencia_para = ""
        self.transferencia_qnt = ""
        self.msg_id_erro = ""
        self.desperdicio_de = ""
        self.desperdicio_oque = ""
        self.desperdicio_qnt = ""

    def run (self):

        def save_db_relatorio():
            
            mycursor = mydb.cursor()
            d_dia = self.data_servico[0]+self.data_servico[1]
            d_mes = self.data_servico[3]+self.data_servico[4]
            d_ano = self.data_servico[6]+self.data_servico[7] + self.data_servico[8]+self.data_servico[9]
            nr_total_clientes = int(self.nr_reservas) + int(self.nr_walk_in) - int(self.nr_cancelamentos) - int(self.nr_no_shows)
            conta_media = str(float(self.facturacao_total) / float(nr_total_clientes))
            conta_media_comida = str(float(self.facturacao_comida) / float(nr_total_clientes))
            conta_media_vinho = str(float(self.facturacao_vinhos) / float(nr_total_clientes))
            conta_media_cocktail =  str(float(self.facturacao_cocktail) / float(nr_total_clientes))
            sql = "INSERT INTO relatorio (data,conta_media_comida,conta_media_vinho,conta_media_cocktail,nr_walkin, nr_total_clientes, conta_media, facturacao_eventos, estabelecimento,nr_reservas,nr_noshow,nr_cancelamentos,facturacao_total,facturacao_comida,facturacao_vinhos,facturacao_cocktail,tpa_total,tpa_comissoes,cash,descricao,faltas_cozinha,faltas_sala,reclamacoes) VALUES (%s,%s, %s,%s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)"
            val = (self.data_servico,conta_media_comida,conta_media_vinho,conta_media_cocktail,self.nr_walk_in, nr_total_clientes, conta_media, self.facturacao_eventos, self.estabelecimento,self.nr_reservas,self.nr_no_shows,self.nr_cancelamentos,self.facturacao_total,self.facturacao_comida,self.facturacao_vinhos,self.facturacao_cocktail,self.tpa_total,self.tpa_comissoes,self.cash,self.descriçao,self.faltas_cozinha,self.faltas_sala,self.reclamacoes)
            mycursor.execute(sql, val)
            mydb.commit()
        
        def make_plot_facturacao():
            try:
                
                query = "Select * from relatorio;"
                result_dataFrame = pandas.read_sql(query,mydb)
                i = 1
                # trocar por result_dataFrame['dia'].astype(int)
                dia = []
                while i != result_dataFrame['facturacao_total'].shape[0] + 1:
                    dia.append(i)
                    i = i + 1 
                
                plt.plot(dia, result_dataFrame['facturacao_total'].astype(int), color="red")
                plt.plot(dia,result_dataFrame['facturacao_comida'].astype(int), color="green")
                plt.plot(dia,(result_dataFrame['facturacao_cocktail'].astype(int)+result_dataFrame['facturacao_vinhos'].astype(int)), color="blue")
                plt.ylabel('some numbers')
                red_patch = mpatches.Patch(color='red', label='Facturação Total')
                green_patch = mpatches.Patch(color='green', label='Facturação Comida')
                blue_patch = mpatches.Patch(color='blue', label='Facturação Bebida')
                plt.legend(handles=[red_patch,green_patch ,blue_patch ])
                plt.xlim(1, 31)
                plt.ylim(1, 5000)
                plt.savefig("facturacao_dia_mes_ano.png", dpi=100)
                    
                mydb.close() #close the connection
            except Exception as e:
                mydb.close()
                print(str(e))
                
        def make_plot_reservas():
            try:
                
                query = "Select * from relatorio;"
                result_dataFrame = pandas.read_sql(query,mydb2)
                
                
                i = 1
                # trocar por result_dataFrame['dia'].astype(int)
                dia = []
                while i != result_dataFrame['facturacao_total'].shape[0] + 1:
                    dia.append(i)
                    i = i + 1 
                
                plt.plot(dia, result_dataFrame['nr_reservas'].astype(int), color="red")
                plt.plot(dia,result_dataFrame['nr_noshow'].astype(int), color="green")
                plt.plot(dia,result_dataFrame['nr_cancelamentos'].astype(int), color="blue")
                plt.plot(dia,(result_dataFrame['nr_reservas'].astype(int)-result_dataFrame['nr_noshow'].astype(int)-result_dataFrame['nr_cancelamentos'].astype(int)), color="black")
                red_patch = mpatches.Patch(color='red', label='Reservas')
                green_patch = mpatches.Patch(color='green', label='NoShow')
                blue_patch = mpatches.Patch(color='blue', label='Cancelamentos')
                black_patch = mpatches.Patch(color='black', label='Nr de Jantares')
                plt.legend(handles=[red_patch,green_patch ,blue_patch, black_patch])
                plt.xlim(1, 31)
                plt.ylim(1, 200)
                plt.savefig("reservas_dia_mes_ano.png", dpi=100)
            
                mydb2.close() #close the connection

            except Exception as e:
                mydb.close()
                print(str(e))
        
        def create_exel():
            total_jantares = str(int(self.nr_reservas)+int(self.nr_walk_in)-int(self.nr_cancelamentos)-int(self.nr_no_shows))
            #workbook = xlsxwriter.Workbook('relatorio_'+self.estabelecimento+'_'+self.data_servico+'.xlsx')
            workbook = xlsxwriter.Workbook('relatorio.xlsx')
            worksheet = workbook.add_worksheet()
            merge_titulo = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#C6E0B4',})
            merge_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#C6E0B4',})
            merge_format2 = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'white',
            })
            merge_left_bot = workbook.add_format({
            'bottom': 5,
            'left' : 5,
            'right' : 1,
            'align': 'left',
            'valign': 'left',
            'fg_color': 'white',})
            merge_left = workbook.add_format({
            'left' : 5,
            'right' : 1,
            'bottom' : 1,
            'top' : 1,
            'align': 'left',
            'valign': 'left',
            'fg_color': 'white',})
            merge_left_top = workbook.add_format({
            'top': 5,
            'left' : 5,
            'right' : 1,
            'align': 'left',
            'valign': 'left',
            'fg_color': 'white',})
            merge_right_bot = workbook.add_format({
            'bottom': 5,
            'right' : 5,
            'align': 'center',
            'valign': 'center',
            'fg_color': 'white',})
            merge_right_top = workbook.add_format({
            'top': 5,
            'right' : 5,
            'align': 'center',
            'valign': 'center',
            'fg_color': 'white',})
            merge_right = workbook.add_format({
            'right' : 5,
            'bottom' : 1,
            'top' : 1,
            'align': 'center',
            'valign': 'center',
            'fg_color': 'white',})

        
            worksheet.merge_range('A2:H2', 'Decadente', merge_titulo)

            worksheet.write('A3', 'Data',merge_format)
            worksheet.merge_range('B3:H3', self.data_servico, merge_format)
            worksheet.merge_range('A4:D4', ' ', merge_format)
            worksheet.merge_range('E4:H4', 'Relatorio', merge_format)
            worksheet.write('A5', 'MOD', merge_left_top)
            worksheet.merge_range('B5:D5', ' ', merge_right_top)
            worksheet.write('A6', 'Staff Sala', merge_left)
            worksheet.merge_range('B6:D6', self.staff_sala, merge_right)
            worksheet.write('A7', 'Staff Cozinha', merge_left_bot)
            worksheet.merge_range('B7:D7', self.staff_cozinha, merge_right_bot)
            worksheet.write('A8', 'Reservas Jantar', merge_left)
            worksheet.merge_range('B8:D8', self.nr_reservas, merge_right)
            worksheet.write('A9', 'Walk-ins',merge_left)
            worksheet.merge_range('B9:D9', self.nr_walk_in, merge_right)
            worksheet.write('A10', 'Cancelamentos',merge_left)
            worksheet.merge_range('B10:D10', self.nr_cancelamentos, merge_right)
            worksheet.write('A11', 'No-shows', merge_left_bot)
            worksheet.merge_range('B11:D11', self.nr_no_shows, merge_right_bot)
            worksheet.write('A12', 'Jantares Servidos',merge_left)
            worksheet.merge_range('B12:D12', total_jantares, merge_right)
            worksheet.write('A13', 'Comidas', merge_left)
            worksheet.merge_range('B13:D13', self.facturacao_comida, merge_right)
            worksheet.write('A14', 'Bebidas S/ Alcool',merge_left)
            worksheet.merge_range('B14:D14', ' ', merge_right)
            worksheet.write('A15', 'Bebidas C/ Alcool',merge_left)
            worksheet.merge_range('B15:D15', self.facturacao_cocktail, merge_right)
            worksheet.write('A16', 'Vinhos',merge_left)
            worksheet.merge_range('B16:D16', self.facturacao_vinhos, merge_right)
            worksheet.write('A17', 'Eventos', merge_left)
            worksheet.merge_range('B17:D17', self.facturacao_eventos, merge_right)
            worksheet.write('A18', 'Total Vendas', merge_left_bot)
            worksheet.merge_range('B18:D18', self.facturacao_total, merge_right_bot)
            worksheet.write('A19', 'TM Comidas', merge_left)
            worksheet.merge_range('B19:D19', str("{:.2f}".format(int(self.facturacao_comida)/int(total_jantares))), merge_right)
            worksheet.write('A20', 'TM Bebidas', merge_left)
            worksheet.merge_range('B20:D20', str("{:.2f}".format((int(self.facturacao_cocktail)+int(self.facturacao_vinhos))/int(total_jantares))), merge_right)
            worksheet.write('A21', 'Ticket Médio Geral', merge_left_bot)
            worksheet.merge_range('B21:D21', str("{:.2f}".format(int(self.facturacao_total)/int(total_jantares))) , merge_right_bot)
            worksheet.write('A22', 'Nr pax',merge_left)
            worksheet.merge_range('B22:D22', ' ', merge_right)
            worksheet.write('A23', 'Total Facturado',merge_left)
            worksheet.merge_range('B23:D23', ' ', merge_right)
            worksheet.write('A24', 'Ticket Médio Evento',merge_left_bot)
            worksheet.merge_range('B24:D24', ' ', merge_right_bot)
            worksheet.write('A25', 'Transferências',merge_left)
            worksheet.merge_range('B25:D25', ' ', merge_right)
            worksheet.write('A26', 'MB',merge_left)
            worksheet.merge_range('B26:D26', self.tpa_total, merge_right)
            worksheet.write('A27', 'Cash',merge_left)
            worksheet.merge_range('B27:D27', self.cash, merge_right)
            worksheet.write('A28', 'Comissões',merge_left)
            worksheet.merge_range('B28:D28', self.tpa_comissoes, merge_right)
            worksheet.write('A29', 'Total Vendas',merge_left_bot)
            worksheet.merge_range('B29:D29', str(int(self.cash) + int(self.tpa_total)), merge_right_bot)
            worksheet.write('A30', 'Budget Diário', merge_left_bot)
            worksheet.merge_range('B30:D30', ' ', merge_right_bot)
            worksheet.set_column('A5:B30', 21)
            worksheet.set_column('B:D', 15)
            worksheet.merge_range('E5:H14', self.descriçao, merge_format2)
            worksheet.merge_range('E15:H17', ('Reclamações : ' + self.reclamacoes), merge_format2)
            worksheet.merge_range('E18:H19', ('Faltas sala : ' + self.faltas_sala), merge_format2)
            worksheet.merge_range('E20:H21', ('Faltas cozinha : ' + self.faltas_cozinha), merge_format2)
            worksheet.merge_range('E22:H25', '     ', merge_format)
            worksheet.merge_range('E26:H26', 'Manutenção', merge_format)
            worksheet.merge_range('E27:H31', self.manutencao, merge_format2)
            worksheet.merge_range('A32:H32', '' , merge_format)


            workbook.set_size(800, 600)

            workbook.close()
            #thread = Thread(target = excel2imagem)
            #thread.start()
            #thread.join()

        def excel2imagem(): 

            #o = win32com.client.gencache.EnsureDispatch("Excel.Application")
            o = win32com.client.Dispatch("Excel.Application",pythoncom.CoInitialize())

            wb = o.Workbooks.Open("C:/Users/Chefe/Desktop/theIndependentBot/relatorio.xlsx")
            ws = wb.Worksheets("Sheet1")
            ws.Range(ws.Cells(2,1),ws.Cells(32,8)).CopyPicture(Format= win32com.client.constants.xlBitmap)  
            img = ImageGrab.grabclipboard()
            imgFile = os.path.join(os.getcwd(),"relatorio.jpg")
            img.save(imgFile)
            wb = o.Workbooks.Close()
            

        def send_email():
            #time.sleep(30)
            message= "Ola"
                    
            msg = EmailMessage()
            msg['Subject'] = "Relatorio " + self.estabelecimento + " " + self.data_servico
            msg['From'] = sender_email
            msg['To'] = rec_email
            msg.set_content("""\
            Boa Noite
            Segue em anexo o relatorio.
            Hugo
            """)
            asparagus_cid = make_msgid()
            msg.add_alternative("""\
            <html>
            <head></head>
            <body>
                <p>Boa Noite</p>
                <p>Segue em anexo o relatorio.</p>
                #<img src="cid:{asparagus_cid}" />
                <p>Hugo</p>
            </body>
            </html>
            """.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
            with open("relatorio.jpg", 'rb') as img:
                msg.get_payload()[1].add_related(img.read(), 'image', 'png',cid=asparagus_cid)
            files = ['facturacao_dia_mes_ano', 'reservas_dia_mes_ano']
            for x in files:
                with open(x+'.png', 'rb') as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    file_name = f.name
                msg.add_attachment(file_data, maintype='image', subtype='file_type', filename=file_name)
            # Make a local copy of what we are going to send.
            with open('outgoing.msg', 'wb') as f:
                f.write(bytes(msg))

            part = MIMEBase('application', "octet-stream")
            part.set_payload(open("relatorio.xlsx", "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="relatorio.xlsx"')
            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            print('email sent')
            server.send_message(msg)     
                
        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            user = message.from_user.first_name
            msg_id = message.chat.id
            self.msg_id_erro = msg_id
            chat_id1  = msg_id
            markup = types.ReplyKeyboardMarkup()
            relatorio = types.KeyboardButton("/Relatorio", )
            encomendas = types.KeyboardButton('/Encomendas')
            horario = types.KeyboardButton('/Horario')
            reservas = types.KeyboardButton('/Desperdicios')
            eventos = types.KeyboardButton('/Eventos')
            markup.row(horario, reservas)
            markup.row(relatorio, encomendas, eventos)
            self.bot.send_message(chat_id1, "Ola " + user, reply_markup=markup, disable_notification=True)  
###- Comeca as perguntas para o relatorio
        @self.bot.message_handler(commands=['Relatorio'])
        def send_welcome(message):
            msg_id = message.chat.id
            self.msg_id_erro = msg_id
            chat_id1  = msg_id
            msg = self.bot.send_message(msg_id, "Data (23-01-2022)?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_data)
        def relatorio_data(message):
            self.data_servico = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Restaurante?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_estabelecimento)    
        def relatorio_estabelecimento(message):
            self.estabelecimento = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Nr Reservas?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_nr_reservas)
        def relatorio_nr_reservas(message):
            self.nr_reservas = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Nr Walk In's?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_walk_in)
        def relatorio_walk_in(message):
            self.nr_walk_in = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Nr No-Shows?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_nr_no_shows)
        def relatorio_nr_no_shows(message):
            self.nr_no_shows = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Nr Cancelamentos?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_nr_cancelamentos)
        def relatorio_nr_cancelamentos(message):
            self.nr_cancelamentos = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Facturação Total?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_facturação_total)
        def relatorio_facturação_total(message):
            self.facturacao_total = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Facturação Comidas?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_facturação_comida)
        def relatorio_facturação_comida(message):
            self.facturacao_comida = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Facturação Vinhos?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_facturação_vinhos)
        def relatorio_facturação_vinhos(message):
            self.facturacao_vinhos = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Facturação Cocktail?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_facturação_cocktails)
        def relatorio_facturação_cocktails(message):
            self.facturacao_eventos = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Facturação Eventos?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_facturação_eventos)
        def relatorio_facturação_eventos(message):
            self.facturacao_cocktail = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Pagamentos TPA (total)?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_pagamentos_tpa)
        def relatorio_pagamentos_tpa(message):
            self.tpa_total = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Comissôes TPA?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_comissoes_tpa)
        def relatorio_comissoes_tpa(message):
            self.tpa_comissoes = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Pagamentos Cash?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_cash)
        def relatorio_cash(message):
            self.cash = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Faltas na Cozinha", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_faltas_cozinha)
        def relatorio_faltas_cozinha(message):
            self.faltas_cozinha = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Faltas na Sala", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_faltas_sala)
        def relatorio_faltas_sala(message):
            self.faltas_sala = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Reclamações" , disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_reclamacoes)
        def relatorio_reclamacoes(message):
            self.reclamacoes = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Staff Sala?", disable_notification=True)
            self.bot.register_next_step_handler(msg, staff_sala)     
        def staff_sala(message):
            self.staff_sala = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Staff Cozinha?", disable_notification=True)
            self.bot.register_next_step_handler(msg, staff_cozinha)
        def staff_cozinha(message):
            self.staff_cozinha = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Manutencao?", disable_notification=True)
            self.bot.register_next_step_handler(msg, manutencao)
        def manutencao(message):
            self.manutencao = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Descrição do serviço?", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_descriçao)
###Devolve as respostsa e pergunta se quer mandar
        def relatorio_descriçao(message):
            self.descriçao = message.text
            msg_id = message.chat.id
            self.bot.send_message(msg_id, "Data : " + self.data_servico + "\nEstabelecimento : " + self.estabelecimento + "\n-----Reservas" + "\nReservas : " + self.nr_reservas + "\nNo-Shows : " + self.nr_no_shows + "\nCancelamentos : " + self.nr_cancelamentos + "\n-----Facturação" + "\nTotal: " + self.facturacao_total + "\nComida : " + self.facturacao_comida + "\nVinhos : " + self.facturacao_vinhos + "\nCocktails : " + self.facturacao_cocktail + "\n-----Pagamentos" + "\nTpa total : " + self.tpa_total + "\nTpa Comissões : " + self.tpa_comissoes + "\nCash : " + self.cash + "\n-----" + "\nDescrição da Noite : \n" + self.descriçao + "\nReclamações : \n" + self.reclamacoes + "\nFaltas Cozinha : \n" + self.faltas_cozinha + "\nFaltas Sala : \n" + self.faltas_sala+ "\Staff Sala : \n" + self.staff_sala+ "\nStaff Cozinha : \n" + self.staff_cozinha+ "\nManutenção : \n" + self.manutencao, disable_notification=True)
            msg = self.bot.send_message(msg_id, "Enviar? (sim)", disable_notification=True)
            self.bot.register_next_step_handler(msg, relatorio_final)
        def relatorio_final(message):
            msg_id = message.chat.id
            if message.text == "sim" or message.text == "Sim":
                
                save_db_relatorio()
                make_plot_reservas()
                make_plot_facturacao()
                create_exel()
                excel2imagem()
                send_email()
                print("--- email enviado ---")
            else:
                print("parabens a voce")
###guardar basedados relatorio // cria os matplot// criar exel // mandar email //    
        


        @self.bot.message_handler(commands=['Encomendas'])
        def send_welcome(message):
            user = message.from_user.first_name
            msg_id = message.chat.id
            chat_id1  = msg_id
            markup = types.ReplyKeyboardMarkup()
            vinhos_tinto = types.KeyboardButton("/Vinhos")
            vinhos_branco = types.KeyboardButton("/Vinhos_Brancos")
            bebidas_brancas = types.KeyboardButton("/Bebidas_Brancos" )
            limpeza_e = types.KeyboardButton('/Limpeza')
            markup.row(vinhos_tinto,vinhos_branco)
            markup.row(bebidas_brancas, limpeza_e)
            self.bot.send_message(chat_id1, "Encomenda de Vinhos Tintos", reply_markup=markup, disable_notification=True) 
        @self.bot.message_handler(commands=['Vinhos'])
        def send_welcome(message):
            msg_id = message.chat.id
            self.msg_id_erro = msg_id
            
            msg_vinho = ""
            for x in lista_vinho_tinto:
                msg_vinho = msg_vinho + x + " ,"
            
            msg_vinho = msg_vinho + "\nQuantidades?\nexemplo 5,1,0,5"
            
            self.bot.send_message(msg_id, msg_vinho, disable_notification=True)            
            self.bot.register_next_step_handler(message, juntar_vinho_tinto)
        def juntar_vinho_tinto(message):
            msg_id = message.chat.id
            string_list = message.text.split(" ,")
            i = 0
            email_message = ""
            for x in string_list:
                self.contagem_vinho[lista_vinho_tinto[i]] = x
                i+=1
            
            parse_vinhos_tinto = pandas.read_excel('parse_vinhos_tintos.xlsx',index_col=None, na_values=['NA'], usecols = "A,B")
                    
        
            products_list = parse_vinhos_tinto.values.tolist()
            print((self.contagem_vinho))
            for x in products_list:
                x.append(self.contagem_vinho[x[0]])
            
            for x in products_list:
                if int(x[2])-int(x[1]) < 0:
                    self.encomendar_vinho[x[0]] = str( (int(x[2])-int(x[1])) *-1)
            for x,y in self.encomendar_vinho.items():
                email_message = email_message + x + ' - ' + y + '\n'
            self.email_message_vinho = email_message
            msg = self.bot.send_message(msg_id, "Quem es tu?", disable_notification=True)
            self.bot.register_next_step_handler(msg, juntar_vinho_branco1)
            #send_email_vinhos(email_message)
            #save_db_encomendas_vinhos()

        def juntar_vinho_branco1(message):
            msg_id = message.chat.id
            self.msg_id_erro = msg_id
            
            msg_vinho = ""
            for x in lista_vinho_branco:
                msg_vinho = msg_vinho + x + " ,"
            
            msg_vinho = msg_vinho + "\nQuantidades?\nexemplo 5,1,0,5"
            
            self.bot.send_message(msg_id, msg_vinho, disable_notification=True)            
            self.bot.register_next_step_handler(message, juntar_vinho_branco2)

        def juntar_vinho_branco2(message):
            msg_id = message.chat.id
            string_list = message.text.split(",")
            i = 0
            email_message = ""
            for x in string_list:
                self.contagem_vinho[lista_vinho_branco[i]] = x
                i+=1
            
            parse_vinhos_brancos = pandas.read_excel('parse_vinhos_brancos.xlsx',index_col=None, na_values=['NA'], usecols = "A,B")
                    
        
            products_list = parse_vinhos_brancos.values.tolist()
            for x in products_list:
                x.append(self.contagem_vinho[x[0]])
            
            for x in products_list:
                if int(x[2])-int(x[1]) < 0:
                    self.encomendar_vinho[x[0]] = str( (int(x[2])-int(x[1])) *-1)
            for x,y in self.encomendar_vinho.items():
                email_message = email_message + x + ' - ' + y + '\n'
            self.email_message_vinho = email_message
            msg = self.bot.send_message(msg_id, "Quem es tu?", disable_notification=True)
            self.bot.register_next_step_handler(msg, identificacao_encomendas_vinhos)
            #send_email_vinhos(email_message)
            #save_db_encomendas_vinhos()
        
        def juntar_vinhos_espumante(message):
            msg_id = message.chat.id
            self.msg_id_erro = msg_id
            
            msg_vinho = ""
            for x in lista_portos:
                msg_vinho = msg_vinho + x + " ,"
            
            msg_vinho = msg_vinho + "\nQuantidades?\nexemplo 5,1,0,5"
            
            self.bot.send_message(msg_id, msg_vinho, disable_notification=True)            
            self.bot.register_next_step_handler(message, juntar_vinhos_espumante2)
        def juntar_vinhos_espumante2(message):
            msg_id = message.chat.id
            string_list = message.text.split(",")
            i = 0
            email_message = ""
            for x in string_list:
                self.contagem_vinho[lista_espumante[i]] = x
                i+=1
            
            parse_espumantes = pandas.read_excel('parse_espumantes.xlsx',index_col=None, na_values=['NA'], usecols = "A,B")
                    
        
            products_list = parse_espumantes.values.tolist()
            for x in products_list:
                x.append(self.contagem_vinho[x[0]])
            
            for x in products_list:
                if int(x[2])-int(x[1]) < 0:
                    self.encomendar_vinho[x[0]] = str( (int(x[2])-int(x[1])) *-1)
            for x,y in self.encomendar_vinho.items():
                email_message = email_message + x + ' - ' + y + '\n'
            self.email_message_vinho = email_message
            msg = self.bot.send_message(msg_id, "Quem es tu?", disable_notification=True)
            self.bot.register_next_step_handler(msg, juntar_portos)
            #send_email_vinhos(email_message)
            #save_db_encomendas_vinhos()
        
        def juntar_portos(message):
            msg_id = message.chat.id
            self.msg_id_erro = msg_id
            
            msg_vinho = ""
            for x in lista_espumante:
                msg_vinho = msg_vinho + x + " ,"
            
            msg_vinho = msg_vinho + "\nQuantidades?\nexemplo 5,1,0,5"
            
            self.bot.send_message(msg_id, msg_vinho, disable_notification=True)            
            self.bot.register_next_step_handler(message, juntar_portos1)
        def juntar_portos1(message):
            msg_id = message.chat.id
            string_list = message.text.split(",")
            i = 0
            email_message = ""
            for x in string_list:
                self.contagem_vinho[lista_vinho_tinto[i]] = x
                i+=1
            
            parse_vinhos_tinto = pandas.read_excel('parse_vinhos_tintos.xlsx',index_col=None, na_values=['NA'], usecols = "A,B")
                    
        
            products_list = parse_vinhos_tinto.values.tolist()
            for x in products_list:
                x.append(self.contagem_vinho[x[0]])
            
            for x in products_list:
                if int(x[2])-int(x[1]) < 0:
                    self.encomendar_vinho[x[0]] = str( (int(x[2])-int(x[1])) *-1)
            for x,y in self.encomendar_vinho.items():
                email_message = email_message + x + ' - ' + y + '\n'
            self.email_message_vinho = email_message
            msg = self.bot.send_message(msg_id, "Quem es tu?", disable_notification=True)
            self.bot.register_next_step_handler(msg, identificacao_encomendas_vinhos)
            send_email_vinhos(email_message)
            #save_db_encomendas_vinhos()
########            
        def save_db_encomendas_vinhos():
        
            mycursor = mydb.cursor()
            for x,y in self.encomendar_vinho.items():
                today = date.today()
                # dd/mm/YY
                d1 = today.strftime("%d/%m/%Y")
                sql = "INSERT INTO encomendas_vinho (nome_vinho, quantidade,data) VALUES (%s,%s,%s)"
                val = (x,y,d1)
                mycursor.execute(sql, val)
                    
                mydb.commit()
        def send_email_vinhos(mensagem):
            
        
            msg = EmailMessage()
            msg['Subject'] = "sujeito"
            msg['From'] = sender_email
            msg['To'] = rec_email
            msg.set_content("Bom dia,\n Seguem as encomendas.\n\n"+mensagem+"\n\n "+self.identificacao_encomendas_vinhos)
            #msg['CC'] = 'hugo.malaquias@hotmail.com', 'dehu170691@shms-mail.ch'
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        def identificacao_encomendas_vinhos(message):
            print(message.text)
            self.identificacao_encomendas_vinhos = message.text
            #send_email_vinhos(self.email_message_vinho)
            save_db_encomendas_vinhos()
### Transferencias
        @self.bot.message_handler(commands=['Transferencias'])
        def send_welcome(message):           
            msg_id = message.chat.id
            self.msg_id_erro = msg_id
            chat_id1  = msg_id
            msg = self.bot.send_message(msg_id, "Queres fazer uma transferencia? (sim)", disable_notification=True)
            self.bot.register_next_step_handler(msg, valida1)
        def valida1(message):
            if message.text == 'sim' or message.text == "Sim":
                msg_id = message.chat.id
                msg = self.bot.send_message(msg_id, "De?", disable_notification=True)
                self.bot.register_next_step_handler(msg, transferencia_de)  
        def transferencia_de(message):
            self.transferencia_de = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Para?", disable_notification=True)
            self.bot.register_next_step_handler(msg, transferencia_para)    
        def transferencia_para(message):
            self.transferencia_para = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "O que?", disable_notification=True)
            self.bot.register_next_step_handler(msg, transferencia_oque)
        def transferencia_oque(message):
            self.transferencia_oque = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Quanto?", disable_notification=True)
            self.bot.register_next_step_handler(msg, transferencia_qnt)
        def transferencia_qnt(message):
            self.transferencia_qnt = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Confirma? (sim)", disable_notification=True)
            self.bot.register_next_step_handler(msg, valida2)
        def valida2(message):
            if message.text == 'sim' or message.text == "Sim":
                msg_id = message.chat.id
                msg = self.bot.send_message(msg_id, "Obrigado", disable_notification=True)
                save_db_encomendas_transferencia()
            else :
                msg = self.bot.send_message(msg_id, "Não funcionou", disable_notification=True)
        def save_db_encomendas_transferencia():
            today = date.today()

            # dd/mm/YY
            d1 = today.strftime("%d/%m/%Y")
            mycursor = mydb.cursor()
            sql = "INSERT INTO transferencias (De, Para, o_que, quanto,data) VALUES (%s,%s,%s,%s,%s)"
            val = (self.transferencia_de, self.transferencia_para,self.transferencia_oque,self.transferencia_qnt,d1)
            mycursor.execute(sql, val)        
            mydb.commit()

        
### Desperdicio        
        @self.bot.message_handler(commands=['Desperdicios'])
        def send_welcome(message):           
            msg_id = message.chat.id
            self.msg_id_erro = msg_id
            chat_id1  = msg_id
            msg = self.bot.send_message(msg_id, "Restaurante?", disable_notification=True)
            self.bot.register_next_step_handler(msg, desperdicio_de)  
        def desperdicio_de(message):
            self.desperdicio_de = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "O que?", disable_notification=True)
            self.bot.register_next_step_handler(msg, desperdicio_oque)    
        def desperdicio_oque(message):
            self.desperdicio_oque = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Quanto?", disable_notification=True)
            self.bot.register_next_step_handler(msg, desperdicio_qnt)
        def desperdicio_qnt(message):
            self.desperdicio_qnt = message.text
            msg_id = message.chat.id
            msg = self.bot.send_message(msg_id, "Confirma (sim)?", disable_notification=True)
            self.bot.register_next_step_handler(msg, valida2)
        def valida2(message):
            if message.text == 'sim' or message.text == "Sim":
                msg_id = message.chat.id
                msg = self.bot.send_message(msg_id, "Obrigado", disable_notification=True)
                save_db_encomendas_desperdicio()
            else :
                msg = self.bot.send_message(msg_id, "Não funcionou", disable_notification=True)
        def save_db_encomendas_desperdicio():
            today = date.today()

            # dd/mm/YY
            d1 = today.strftime("%d/%m/%Y")
            mycursor = mydb.cursor()
            sql = "INSERT INTO transferencias (de, o_que, quanto,data) VALUES (%s,%s,%s,%s)"
            val = (self.desperdicio_de, self.desperdicio_oque,self.desperdicio_qnt,self.transferencia_qnt,d1)
            mycursor.execute(sql, val)        
            mydb.commit()



 

        self.bot.polling()(none_stop=True)
        #self.bot.polling()
"""
        def create_exel():
            workbook = xlsxwriter.Workbook('relatorio_'+self.estabelecimento+'_'+self.data_servico+'.xlsx')
            worksheet = workbook.add_worksheet()
            worksheet.write('A1', 'Data')
            worksheet.write('B1', self.data_servico)
            worksheet.write('A2', 'Estabelecimento')
            worksheet.write('B2', self.estabelecimento)
            worksheet.write('A3', 'Nr Reservas')
            worksheet.write('B3', self.nr_reservas)
            worksheet.write('A4', 'Nr No-Shows')
            worksheet.write('B4', self.nr_no_shows)
            worksheet.write('A5', 'Nr Cancelamentos')
            worksheet.write('B5', self.nr_cancelamentos)
            worksheet.write('H12', 'Facturacao total')
            worksheet.write('I12', self.facturacao_total)
            worksheet.write('H13', 'Facturacao comida')
            worksheet.write('I13', self.facturacao_comida)
            worksheet.write('H14', 'Facturacao Vinhos')
            worksheet.write('I14', self.facturacao_vinhos)
            worksheet.write('J11', "% da Facturação")
            worksheet.write('J13', str(int(self.facturacao_comida)*100/int(self.facturacao_total)))
            worksheet.write('J14', str(int(self.facturacao_vinhos)*100/int(self.facturacao_total)))
            
            workbook.close()
            #excel2img.export_img('relatorio_'+self.estabelecimento+'_'+self.data_servico+'.xlsx',"image.png/image.bmp","sheet!A1:B5")
        def send_email_vinhos(message):
            
            message= "Ola"
           
            msg = EmailMessage()
            print(type(msg))
            print(msg.keys())
            msg['Subject'] = "sujeito"
            msg['From'] = sender_email
            msg['To'] = rec_email
            #msg['CC'] = 'hugo.malaquias@hotmail.com', 'dehu170691@shms-mail.ch'
            msg.set_content('Image attached...')

            #file = ['imagem1', 'imagem2']
            #for x in files:
            #with open('relatorio_'+self.estabelecimento+'_'+self.data_servico+'.xlsx', 'rb') as f:
            with open('Untitled.png', 'rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name

            msg.add_attachment(file_data, maintype='image', subtype='file_type', filename=file_name)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            print('Login sucess')
            server.send_message(msg)

        def make_plot():
            



        @self.bot.message_handler(commands=['Encomendas'])
        def send_welcome(message):
            user = message.from_user.first_name
            msg_id = message.chat.id
            chat_id1  = msg_id
            markup = types.ReplyKeyboardMarkup()

            vinhos_e = types.KeyboardButton("/Vinhos_E", )
            bar_e = types.KeyboardButton('/Bar_E')
            limpeza_e = types.KeyboardButton('/Limpeza_')


            markup.row(vinhos_e, bar_e, limpeza_e)

            self.bot.send_message(chat_id1, "Encomendas para onde? ", reply_markup=markup, disable_notification=True)
        @self.bot.message_handler(commands=['email'])
        def send_email(message):
            
            message= "Ola"
           
            msg = EmailMessage()
            print(type(msg))
            print(msg.keys())
            msg['Subject'] = "sujeito"
            msg['From'] = sender_email
            msg['To'] = rec_email
            #msg['CC'] = 'hugo.malaquias@hotmail.com', 'dehu170691@shms-mail.ch'
            msg.set_content('Image attached...')

            #file = ['imagem1', 'imagem2']
            #for x in files:
            #with open('relatorio_'+self.estabelecimento+'_'+self.data_servico+'.xlsx', 'rb') as f:
            with open('Untitled.png', 'rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name

            msg.add_attachment(file_data, maintype='image', subtype='file_type', filename=file_name)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            print('Login sucess')
            server.send_message(msg)
"""
        

