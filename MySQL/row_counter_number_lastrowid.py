# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
        connection.commit()

        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES '
            '(%s, %s) '
        )
        valuesTuple = (
            ("Adalberto", 26),
            ("Natália", 25),
            ("Siri", 22),
            ("Helena", 15),
            ("Jake", 32),
            ("Anderson", 15),
            ("Luiz", 23)
        )
        result = cursor.executemany(sql, valuesTuple)  # type:ignore
        # print(sql)
        # print(valuesTuple)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id = %s'
        )

        cursor.execute(sql, ('Eleonor', 102, 4))
        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        data = cursor.fetchall()
        for row in data:
            print(row)

        print('resultFromSelect', resultFromSelect)
        print('len(data)', len(data))
        print('rowcount', cursor.rowcount)
        print('rownumber', cursor.rownumber)

        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES '
            '(%s, %s) '
        )
        cursor.execute(sql, ("Jason", 17))
        print('lastowid', cursor.lastrowid)

        cursor.execute(
            f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        )
        lastIdFromSelect = cursor.fetchone()
        print('lastowid na mão', lastIdFromSelect)
        print('rownumber', cursor.rownumber)
        print('rownumber', cursor.rownumber)

    connection.commit()
