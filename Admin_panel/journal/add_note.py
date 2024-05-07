import sqlite3
from datetime import datetime


def add_new_note(user_id):
    note = input('ВВЕДИТЕ ТЕКСТ: ')
    date = datetime.today().strftime("%H:%M-%d.%m.%Y")

    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                query = '''INSERT INTO Journal (id_user, note, date)
                        VALUES ({}, {}, {})'''.format(user_id, note, date)
                cursor.execute(query)

        except Exception:
            print("TERMINAL ERROR")

    print()
    input("[УСПЕХ] Запись добавлена... press any key")
