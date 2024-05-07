import sqlite3


with sqlite3.connect('Databases/vault_98.db') as connection:
    cursor = connection.cursor()

    try:
        with connection:
            query = '''INSERT INTO Users (name, pass, age, rank)
            VALUES
            ("BRADWIS", "EPTMEMN", "1990", "USER")
            '''
            cursor.execute(query)
    except Exception:
        print("TERMINAL ERROR")
