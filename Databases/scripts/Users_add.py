import sqlite3


with sqlite3.connect('vault_98/Databases/vault_98.db') as connection:
    cursor = connection.cursor()

    try:
        with connection:
            query = '''INSERT INTO Users (name, pass, age, rank)
            VALUES
            ("AMANDA", "CLOUDY1998", "1998", "USER")
            '''
            cursor.execute(query)
    except Exception:
        print("TERMINAL ERROR")
