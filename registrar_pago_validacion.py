import pyodbc
try:
    conexion = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=.;DATABASE=prueba;Trusted_Connection=yes;'
    )
    cursor = conexion.cursor()
    cliente = 'Corporativo Alfa'
    monto = -500.00
    fecha = '2026-09-15'
    sql_sp = "{CALL sp_RegistrarPago(?,?,?)}"
    cursor.execute(sql_sp,(cliente, monto, fecha))
    conexion.commit()
    print("Pago registrado con éxito.")
except pyodbc.DatabaseError as e:
    print(f"⚠ Error capturado desde la Base de Datos:\n{e}")
finally:
    cursor.close()
    conexion.close()
          
