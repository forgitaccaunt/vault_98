from datetime import datetime
import sqlite3
from GUI.color_decor import get_warning


def trace_user(user_id, msg):
    date = datetime.today().strftime("%H:%M-%d.%m.%Y")

    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                query = '''INSERT INTO Userlogs
                (user_id, date, note)
                VALUES (?, ?, ?)
                '''
                cursor.execute(query, (user_id, date, msg))

        except Exception:
            print(f'{get_warning()} TERMINAL ERROR')
