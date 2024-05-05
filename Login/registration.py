import sqlite3
from .validators.valid_password import password_validator
from .validators.valid_username import username_validator
from .validators.valid_age import age_validator


def user_registration():
    print('Для регистрации нового USER введите данные...')
    user_name = username_validator(input('ИМЯ ПОЛЬЗОВАТЕЛЯ: '))
    user_pass = password_validator(input('ПАРОЛЬ: '))
    user_age = age_validator(input('ГОД РОЖДЕНИЯ: '))
    # Права доступа по умолчанию 'USER' (при создании БД не предусмотрел)
    user_rank = 'USER'

    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                query = '''INSERT INTO Users (name, pass, age, rank)
                VALUES (?, ?, ?, ?)'''
                cursor.execute(query, (user_name, user_pass, user_age, user_rank))
                print('Пользователь зарегестрирован')
        except Exception:
            print("TERMINAL ERROR")
