import requests
import json
import sqlite3


def get_terminal_info(user_id):
    print('>>> TERMINAL INFORMATION:')

    # Получаем имя админа (смотрителя) терминала
    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                cursor.execute('SELECT name FROM Users WHERE id == 1')
                admin_name = cursor.fetchone()[0]
        except Exception:
            print("TERMINAL ERROR")

    # Получаем IP машины для строчки CONNECT_PORT
    try:
        response = requests.get('https://api.ipify.org/?format=json')
        if response.status_code == 200:
            json_data = response.json()
    except Exception:
        print("TERMINAL ERROR")

    # Получаем файл json с информацией о терминале
    with open("Info/terminal_info.json") as file:
        info = json.load(file)

    # Подставляем в файл IP и ADMIN и выводим
    info['CONNECT_PORT'] = json_data['ip']
    info['OVERSEER'] = admin_name
    info['ID_USER'] = user_id

    for key, value in info.items():
        print(f'{key}: {value}')
    input("<- RETURN ")
