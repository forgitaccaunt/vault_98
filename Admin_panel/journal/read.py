import sqlite3


def get_all_notes(user_id):

    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                query = 'SELECT date, note FROM Journal ORDER BY id'
                notes = cursor.execute(query).fetchall()

        except Exception:
            print("TERMINAL ERROR")

    for note in notes:
        print(note)
    print()

    input("<- RETURN... press any key ")
