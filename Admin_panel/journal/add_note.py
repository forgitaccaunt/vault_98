import sqlite3
from datetime import datetime
from GUI.color_decor import get_succes, get_warning


def add_new_note(user_id):
    note = input('ВВЕДИТЕ ТЕКСТ: ')
    date = datetime.today().strftime("%H:%M-%d.%m.%Y")

    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                query = '''INSERT INTO Journal (id_user, note, date)
                VALUES (?, ?, ?)'''
                cursor.execute(query, (user_id, note, date))

        except Exception:
            print(f'{get_warning()} TERMINAL ERROR')

    print()
    input(f'{get_succes()} Запись добавлена... press any key')
