from psycopg2 import connect

connection = connect(
    host ='localhost',
    user ='postgres',
    dbname = 'mydb',
    password ='12345'
)

cursor = connection.cursor()
# sql = 'CREATE TABLE cidade (id SERIAL PRIMARY KEY, nome VARCHAR(100), uf VARCHAR(2))'
# sql = 'DROP TABLE cidade'
# cursor.execute(sql, ("Rio de Janeiro", "RJ"))
# cursor.execute(sql)
# sql = 'INSERT INTO cidade (nome, uf) VALUES (%s, %s)'
# values = [
#     ("Rio de Janeiro", "RJ"),
#     ("São Paulo", "SP"),
#     ("Minas Gerais", "MG"),
#     ("Espírito Santo", "ES"),
#     ("Distrito Federal", "DF")
# ]
# cursor.executemany(sql, values)
# connection.commit()

# sql = "INSERT INTO cidade (nome, uf) VALUES (%s, %s)"
# value = ("Rio Grande do Sul", "RS")
# value = ("Santa Catarina", "SC")
# cursor.execute(sql, value)

# sql = 'SELECT * FROM cidade WHERE id % 2 != 0'
# sql = "SELECT * FROM cidade WHERE nome LIKE '%an%'"
# sql = "SELECT * FROM cidade WHERE nome LIKE '%rito%'"
# sql = "UPDATE cidade SET uf = 'SP' WHERE id = 1"
# sql = "UPDATE cidade SET uf = 'RJ' WHERE nome = 'Rio de Janeiro'"
# sql = "DELETE FROM cidade WHERE id = 8"
# cursor.execute(sql)
# print(cursor.rowcount, 'deletado(s)')
# connection.commit()

sql = 'SELECT * FROM cidade ORDER BY id DESC'
cursor.execute(sql)
resultado = cursor.fetchall()
for x in resultado:
    print(x)

# resultado = cursor.fetchone()
# print(resultado)

# print("type(resultado) é...", type(resultado))

cursor.close()
connection.close()