import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'
)

# cursor.execute(sql, {'nome': 'Joana', 'peso': 4})
values = (
    {'nome': 'Joãozinho', 'peso': 4},
    {'nome': 'Maria', 'peso': 5},
    {'nome': 'Helena', 'peso': 9},
    {'nome': 'Gabriel', 'peso': 7}
)
cursor.executemany(sql, values)
connection.commit()

cursor.close()
connection.close()
