import pandas as pd
import pyodbc

conexion_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=prueba;"
    "Trusted_Connection=yes;"

)

try:
    conn=pyodbc.connect(conexion_str)
    query="EXEC SP_ObtenerCarteraPorRiesgo @NivelRiesgo = 'Alto Riesgo'"
    df_cartera=pd.read_sql(query, conn)
    conn.close()
    print("--- ¡Conexión exitosa a SQL Server! ---")
    print(df_cartera)
except Exception as e:
    print("Ocurrió un detalle al conectar:",e)
