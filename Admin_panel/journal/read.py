from functools import lru_cache
import sqlite3
from GUI.color_decor import get_warning


@lru_cache
def get_all_notes(user_id):

    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                query = '''SELECT id, date,
                    (SELECT name FROM Users
                    WHERE Journal.id_user = Users.id) as named, note
                FROM Journal
                ORDER BY id'''
                notes = cursor.execute(query).fetchall()

        except Exception:
            print(f'{get_warning()} TERMINAL ERROR')

    for note in notes:
        print(f'#{note[0]} [{note[1]}][{note[2]}]: {note[3]}')
    print()

    input("<- RETURN... press any key ")
