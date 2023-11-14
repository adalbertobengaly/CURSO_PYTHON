import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read   Update Delete
# SQL  - INSERT SELECT UPDATE DELETE

cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET name="QUALQUER", weight=67.89 '
    'WHERE id = 1'
)
connection.commit()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

for row in cursor.fetchall():
    _id, nome, peso = row
    print(_id, nome, peso)

connection.commit()


cursor.close()
connection.close()
