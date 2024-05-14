import sqlite3


with sqlite3.connect('Databases/vault_98.db') as connection:
    cursor = connection.cursor()

    try:
        with connection:
            query = '''SELECT * FROM Userlogs
            '''
            cursor.execute(query)
            tmp = cursor.fetchall()

    except Exception:
        print("TERMINAL ERROR")
