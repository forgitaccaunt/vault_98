import sqlite3


with sqlite3.connect('vault_98/Databases/vault_98.db') as connection:
    cursor = connection.cursor()

    try:
        with connection:
            query = ''
            cursor.execute(query)
    except Exception:
        print("TERMINAL ERROR")
