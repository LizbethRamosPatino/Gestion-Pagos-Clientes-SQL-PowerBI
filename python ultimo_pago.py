import pyodbc

conexion_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.;"
    "DATABASE=prueba;"
    "Trusted_Connection=yes;"
)

with pyodbc.connect(conexion_str)as conn:
    cursor=conn.cursor()

    query = """
WITH PagosOrdenados AS(
SELECT
ID_Pago, Cliente, Monto_Pagado, Fecha_Pago,
ROW_NUMBER() OVER(PARTITION BY Cliente ORDER BY Fecha_Pago DESC) AS Num_Pago
FROM PagosClientes
)
SELECT Cliente, Monto_Pagado, Fecha_Pago
FROM PagosOrdenados
WHERE Num_Pago = 1;
"""
    cursor.execute(query)

    print("\n--- ÚLTIMO PAGO REGISTRADO POR CLIENTE ---")
    for fila in cursor.fetchall():
        print(f"Cliente: {fila.Cliente:<18} | Monto:${fila.Monto_Pagado:,.2f} | Fecha: {fila.Fecha_Pago}")
