import mysql.connector

midb =mysql.connector.connect(
    host='localhost',
    user='artumarin',
    password='USUARIO2024n-',
    database='prueba'
)

cursor = midb.cursor() 

# LISTAR DATOS 
# cursor.execute('select * from Usuario')
# resultado = cursor.fetchall()
# print(resultado)

# VERR DEFINICIONES DE TABLAS
# cursor.execute('show create table Usuario')

# INSERTAR DATOS
# sql = " insert into Usuario(email, username, edad) values (%s, %s, %s)"
# values =('micorreo@correo.com', 'nombreusuario', 45)

# ACTUALIZA DATOS
# sql = 'update Usuario set email = micorreo@correo.com where id = %s'
# values = ('micorreo@correo.com', 4)
# cursor.execute(sql, values)

# midb.commit()

# print(cursor.rowcount)

# ELIMINAR DATOS
sql = 'delete from Usuario where id = %s'
values = (4, )
cursor.execute(sql, values)
midb.commit()




