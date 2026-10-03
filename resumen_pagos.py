import pandas as pd
import pyodbc
conexion_str=(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=prueba;"
    "Trusted_Connection=yes;"
)

try:
    conn = pyodbc.connect(conexion_str)
    query="SELECT * FROM V_ResumenPagos"
    df_resumen=pd.read_sql(query, conn)
    conn.close()
    print("--- Resumen de Pagos Traído de SQL ---")
    print(df_resumen)

except Exception as e:
    print("Ocurrió un detalle al conectar:",e)
