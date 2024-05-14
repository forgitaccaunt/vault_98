import sqlite3

from GUI.color_decor import get_warning


def username_validator(name: str) -> str:
    if 3 <= len(name) <= 30:
        # Проверка уникальности:
        with sqlite3.connect('Databases/vault_98.db') as connection:
            cursor = connection.cursor()

            try:
                with connection:
                    query = 'SELECT COUNT(*) FROM Users WHERE name = ?'
                    tmp = cursor.execute(query, (name,))
                    if tmp.fetchone()[0] == 0:
                        return name
                    else:
                        print(f'{get_warning()} ИМЯ занято')
                        username_validator(input('ИМЯ ПОЛЬЗОВАТЕЛЯ: ').upper())
            except Exception:
                print(f'{get_warning()} TERMINAL ERROR')
    else:
        print(f'{get_warning()} Имя не менше 3 символов')
        print(f'{get_warning()} Имя не больше 30 символов')
        username_validator(input('ИМЯ ПОЛЬЗОВАТЕЛЯ: ').upper())
