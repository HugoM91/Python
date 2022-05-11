import pandas 
import mysql.connector 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches




def make_plot_facturacao():
    try:
        mydb = mysql.connector.connect(
                host="",
                user="",
                password="",
                database=""
            )
        query = "Select * from <>;"
        result_dataFrame = pandas.read_sql(query,mydb)
        
        

        dia = [1,2,3,4] # trocar por result_dataFrame['dia'].astype(int)
        
        plt.plot(dia, result_dataFrame['facturacao_total'].astype(int), color="red")
        plt.plot(dia,result_dataFrame['facturacao_comida'].astype(int), color="green")
        plt.plot(dia,(result_dataFrame['facturacao_cocktail'].astype(int)+result_dataFrame['facturacao_vinhos'].astype(int)), color="blue")
        plt.ylabel('some numbers')
        plt.savefig("testeplot.png", dpi=100)
        red_patch = mpatches.Patch(color='red', label='Facturação Total')
        green_patch = mpatches.Patch(color='green', label='Facturação Comida')
        blue_patch = mpatches.Patch(color='blue', label='Facturação Bebida')
        plt.legend(handles=[red_patch,green_patch ,blue_patch ])
        plt.xlim(1, 15)
        plt.ylim(1, 5000)

        plt.savefig("facturacao_dia_mes_ano.png", dpi=100)
        #plt.show()


        
        mydb.close() #close the connection

    except Exception as e:
        mydb.close()
        print(str(e))

def make_plot_reservas():
    try:
        mydb = mysql.connector.connect(
                host="",
                user="",
                password="",
                database=""
            )
        query = "Select * from relatorio;"
        result_dataFrame = pandas.read_sql(query,mydb)
        
        

        dia = [1,2,3,4] # trocar por result_dataFrame['dia'].astype(int)
        
        plt.plot(dia, result_dataFrame['nr_reservas'].astype(int), color="red")
        plt.plot(dia,result_dataFrame['nr_noshow'].astype(int), color="green")
        plt.plot(dia,result_dataFrame['nr_cancelamentos'].astype(int), color="blue")
        plt.plot(dia,(result_dataFrame['nr_reservas'].astype(int)-result_dataFrame['nr_noshow'].astype(int)-result_dataFrame['nr_cancelamentos'].astype(int)), color="black")
        plt.savefig("testeplot.png", dpi=100)
        red_patch = mpatches.Patch(color='red', label='Reservas')
        green_patch = mpatches.Patch(color='green', label='NoShow')
        blue_patch = mpatches.Patch(color='blue', label='Cancelamentos')
        black_patch = mpatches.Patch(color='black', label='Nr de Jantares')
        plt.legend(handles=[red_patch,green_patch ,blue_patch, black_patch])
        plt.xlim(1, 15)
        plt.ylim(1, 200)

        plt.savefig("reservas_dia_mes_ano.png", dpi=100)
        #plt.show()


        
        mydb.close() #close the connection

    except Exception as e:
        mydb.close()
        print(str(e))

make_plot_reservas()