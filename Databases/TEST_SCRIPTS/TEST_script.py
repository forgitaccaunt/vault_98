import sqlite3


with sqlite3.connect('Databases/vault_98.db') as connection:
    cursor = connection.cursor()

    try:
        with connection:
            query = '''INSERT INTO Journal (id_user, note, date)
            VALUES (?, ?, ?)'''
            cursor.execute(query, (1, 'Проверка', 'date'))

    except Exception:
        print("TERMINAL ERROR")
