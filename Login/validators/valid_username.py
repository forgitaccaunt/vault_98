import sqlite3


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
                        print('[WARNING] ИМЯ занято')
                        username_validator(input('ИМЯ ПОЛЬЗОВАТЕЛЯ: ').upper())
            except Exception:
                print("TERMINAL ERROR")
    else:
        print('[WARNING] Имя не менше 3 символов')
        print('[WARNING] Имя не больше 30 символов')
        username_validator(input('ИМЯ ПОЛЬЗОВАТЕЛЯ: ').upper())
