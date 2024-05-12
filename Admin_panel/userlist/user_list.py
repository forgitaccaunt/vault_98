from functools import lru_cache
import sqlite3


@lru_cache
def get_all_user(user_id):

    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                query = 'SELECT id, name, age, rank FROM Users ORDER BY id'
                users = cursor.execute(query).fetchall()

        except Exception:
            print("TERMINAL ERROR")

    for user in users:
        print(f'ID: {user[0]:<3}# NAME: {user[1]:<15} age: {user[2]} [{user[3]}]')
    print()

    input("<- RETURN... press any key ")
