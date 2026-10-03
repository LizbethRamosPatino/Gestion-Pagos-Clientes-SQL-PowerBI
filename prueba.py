import pandas as pd
import pyodbc

conexion = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=.;"
    "DATABASE=prueba;"
    "UID=sa;"
    "PWD=9085Uupe;"
)
query = "SELECT * FROM CarteraClientes"
df = pd.read_sql(query, conexion)
conexion.close()

print("---1.TABLA COMPLETA---")
print(df)
print("\n"+"="*40+"\n")

monto_total = df["Monto_Solicitado"].sum()
print("---2.MONTO TOTAL EN CARTERA---")
print(f"${monto_total:,.2f}")
print("\n"+"="*40+"\n")

buenos_clientes = df[df["Historial_Limpio"]==1]
print("---3.CLIENTES CON HISTORIAL LIMPIO---")
print(buenos_clientes)
print("\n"+"="*40+"\n")

conteo = df["Dictamen"].value_counts()
print("--- 4. RESUMEN DE DICTÁMENES---")
print(conteo)
