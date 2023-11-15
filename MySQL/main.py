# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import pymysql
import dotenv

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # Limpa a tabela
    connection.commit()  # Para criação de tabela não se faz necessário

    # Começo a manipular dados a partir daqui
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES '
            '(%s, %s) '
        )
        value = ('Natália', 25)
        result = cursor.execute(sql, value)
        # print(sql)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES '
            '(%(name)s, %(age)s) '
        )
        valueDict = {
            "name": "Adalberto",
            "age": 26
        }
        result = cursor.execute(sql, valueDict)
        # print(sql)
        # print(valueDict)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES '
            '(%(name)s, %(age)s) '
        )
        valuesDict = (
            {"name": "Jake", "age": 36},
            {"name": "Anderson", "age": 30},
            {"name": "Luiz", "age": 33},
        )
        result = cursor.executemany(sql, valuesDict)  # type:ignore
        # print(sql)
        # print(valuesDict)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES '
            '(%s, %s) '
        )
        valuesTuple = (
            ("Siri", 22),
            ("Helena", 15)
        )
        result = cursor.executemany(sql, valuesTuple)  # type:ignore
        # print(sql)
        # print(valuesTuple)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id > 3'
        )
        result = cursor.execute(sql)
        dados = cursor.fetchall()

        # for row in dados:
        #     print(row)

    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor id: '))
        # maior_id = int(input('Digite o maior id: '))
        menor_id = 2
        maior_id = 4

        # sql = (
        #     f'SELECT * FROM {TABLE_NAME} '
        #     'WHERE id >= %s AND id <= %s'
        # )

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s'
        )

        cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id)))
        data = cursor.fetchall()

        # for row in data:
        #     print(row)

    # 'DELETE' ou 'UPDATE' SEM 'WHERE' terá efeito sobre
    # todos os dados da tabela.
    # 'DELETE' e 'UPDATE', apagam e atualizam todos os dados respectivamente
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )

        cursor.execute(sql, 1)
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # for row in cursor.fetchall():
        #     print(row)

    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id = %s'
        )

        cursor.execute(sql, ('Eleonor', 102, 4))

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        for row in cursor.fetchall():
            print(row)
    connection.commit()
