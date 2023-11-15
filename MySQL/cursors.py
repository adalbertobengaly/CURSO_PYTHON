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
    cursorclass=pymysql.cursors.SSDictCursor,
    # cursorclass=pymysql.cursors.DictCursor,
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

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # data = cursor.fetchall()

        print('For 1:')
        # for row in cursor.fetchall():
        for row in cursor.fetchall_unbuffered():
            print(row)

            if row['id'] >= 5:
                break

        # SSDictCursor não carrega todos os dados de vez,
        # portanto o scroll não vai funcionar com 'fetchall_unbuffered()'
        # cursor.scroll(-2)
        # cursor.scroll(1)
        # cursor.scroll(0, 'absolute')

        print('\nFor 2:')
        # for row in cursor.fetchall():
        for row in cursor.fetchall_unbuffered():
            print(row)

    connection.commit()
