import mysql.connector

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'flask_app'

personas_db = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE, )

#Ejecutar sentencia select

cursor = personas_db.cursor()
# cursor.execute('SELECT*FROM users')
# resultado = cursor.fetchall()
#
# for p in resultado:
#     print(p)
# cursor.close()
# personas_db.close()

# INSERTAR UN REGISTRO
# sentencia_sql = 'INSERT INTO users(id,name,email) VALUES (%s, %s, %s)'
# valores = (4,'Victor Ramos','victor@gmail.com')
#
# cursor.execute(sentencia_sql, valores)
# personas_db.commit()
# print(f'Se ha agregado un nuevo registro {valores}')
# cursor.close()
# personas_db.close()

# Update (actualizar un registro

# sentencia_sql = 'UPDATE users SET name = %s, email = %s WHERE id = %s'
# valores = ('Victoria', 'Flores',4)
#
# cursor.execute(sentencia_sql,valores)
# personas_db.commit()
# print(f'Se ha modificado el registro {valores[2]} {valores}')
# cursor.close()
# personas_db.close()


#Eliminar (Delete)
sentencia_sql = 'DELETE FROM users WHERE id=%s'
valores = (4,)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print(f'Se ha eliminado el id {valores[0]} ')

cursor.close()
personas_db.close()