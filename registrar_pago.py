import pyodbc
conexion=pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=.;'
    'DATABASE=prueba;'
    'Trusted_Connection=yes;'
)
cursor=conexion.cursor()

cliente='Corporativo Alfa'
monto=150000.00
fecha='2026-09-15'

sql_sp="{CALL sp_RegistrarPago(?,?,?)}"
cursor.execute(sql_sp, (cliente, monto, fecha))

conexion.commit()

print(f"¡Pago de ${monto} registrado para {cliente} exitosamente!")

cursor.close()
conexion.close()
