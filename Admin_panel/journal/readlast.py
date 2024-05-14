import sqlite3
from GUI.color_decor import get_warning


def get_last_note(user_id):

    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                query = '''SELECT id, date,
                    (SELECT name FROM Users
                    WHERE Journal.id_user = Users.id) as named, note
                FROM Journal
                ORDER BY id DESC
                LIMIT 1'''
                note = cursor.execute(query).fetchone()

        except Exception:
            print(f'{get_warning()} TERMINAL ERROR')

    print(f'#{note[0]} [{note[1]}][{note[2]}]: {note[3]}')
    print()

    input("<- RETURN... press any key ")
