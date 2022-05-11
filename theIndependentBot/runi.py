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
                host="",
                user="",
                password="",
                database=""
            )
mydb2 = mysql.connector.connect(
                host="",
                user="",
                password="",
                database=""
            )
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

make_plot_reservas()
make_plot_facturacao()