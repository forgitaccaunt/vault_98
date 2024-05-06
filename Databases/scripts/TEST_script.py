import sqlite3


with sqlite3.connect('Databases/vault_98.db') as connection:
    cursor = connection.cursor()

    try:
        with connection:
            query = 'SELECT name FROM Users WHERE id = {}'.format(1)
            print(cursor.execute(query).fetchone())

    except Exception:
        print("TERMINAL ERROR")
