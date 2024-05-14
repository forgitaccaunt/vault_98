
from functools import lru_cache
import sqlite3

from GUI.color_decor import get_warning


@lru_cache
def get_user_log(user_id):

    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                query = '''SELECT id, date, (SELECT name FROM Users
                WHERE Userlogs.user_id = Users.id) as named, note
                FROM Userlogs
                ORDER BY id'''
                user_log = cursor.execute(query).fetchall()

        except Exception:
            print(f'{get_warning()} TERMINAL ERROR')

    for note in user_log:
        print(f'#{note[0]} [{note[1]}][{note[2]}]: {note[3]}')
    print()

    input("<- RETURN... press any key ")
