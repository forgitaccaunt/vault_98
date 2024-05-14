import sqlite3
from GUI.color_decor import get_succes, get_warning


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
            print(f'{get_warning()}TERMINAL ERROR')

    for user in user_list:
        if user[1] == user_name and user[2] == user_pass:
            print(f'{get_succes()} ACCESS level: {user[4]}')
            return user
    else:
        print(f'{get_warning()} Неверное ИМЯ ПОЛЬЗОВАТЕЛЯ или ПАРОЛЬ!')
        return user_authorization()
