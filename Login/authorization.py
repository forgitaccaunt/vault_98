import sqlite3


def user_authorization():
    user_name = input('ИМЯ ПОЛЬЗОВАТЕЛЯ: ')
    user_pass = input('ПАРОЛЬ: ')

    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                cursor.execute('SELECT * FROM Users')
                user_list = cursor.fetchall()
        except Exception:
            print("TERMINAL ERROR")

    for user in user_list:
        if user[1] == user_name and user[2] == user_pass:
            print(f'*** ACCESS level: {user[4]}')
            return user
    else:
        print('[WARNING] Неверное ИМЯ ПОЛЬЗОВАТЕЛЯ или ПАРОЛЬ!')
        return user_authorization()
