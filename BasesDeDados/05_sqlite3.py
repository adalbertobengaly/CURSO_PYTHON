import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# cursor.execute(f'SELECT * FROM {TABLE_NAME} LIMIT 2')
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)

# for row in cursor.fetchall():
#     _id, name, weight = row
#     print(_id, name, weight)

row = cursor.fetchone()
print(row)

cursor.close()
connection.close()
