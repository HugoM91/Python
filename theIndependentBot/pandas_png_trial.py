

import pandas as pd
import numpy as np
import dataframe_image as dfi
import pandas 
import mysql.connector 


mydb = mysql.connector.connect(
                host="",
                user="",
                password="",
                database=""
            )

            
try:
                
    query = "Select * from relatorio;"
    df = pandas.read_sql(query,mydb)

    mydb.close() #close the connection

except Exception as e:
    mydb.close()
    print(str(e))




df_styled = df.style.background_gradient() #adding a gradient based on values in cell


dfi.export(df_styled,"mytable.png")
