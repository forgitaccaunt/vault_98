import sqlite3


def get_last_note(user_id):

    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                query = '''SELECT date, note FROM Journal
                           ORDER BY id DESC LIMIT 1'''
                note = cursor.execute(query).fetchone()

        except Exception:
            print("TERMINAL ERROR")

    print(note)
    print()

    input("<- RETURN... press any key ")
