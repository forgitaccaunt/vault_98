from datetime import datetime
import requests
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Databases.alchemy import User
from GUI.color_decor import get_inform, get_warning


def get_terminal_info(user_id):
    print(f'{get_inform()}:')

    # Получаем имя админа (смотрителя) терминала
    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)
    with Session(autoflush=False, bind=engine) as db:
        try:
            tmp = db.query(User).filter(id==1).first()
            admin_name = tmp.name
        except Exception:
            print(f'{get_warning()} LOST ADMIN NAME')

    # Получаем IP машины для строчки CONNECT_PORT
    try:
        response = requests.get('https://api.ipify.org/?format=json')
        if response.status_code == 200:
            json_data = response.json()
    except Exception:
        print(f'{get_warning()} LOST IP')

    # Ищем геолокацию по IP запросом к другому API
    try:
        response = requests.get('https://ipwho.is/8.8.4.4?fields=latitude,longitude')
        if response.status_code == 200:
            location = response.json()
    except Exception:
        print(f'{get_warning()} LOST GEOLOCATION')

    # Получаем файл json с информацией о терминале
    with open("Info/terminal_info.json") as file:
        info = json.load(file)

    # Подставляем в файл IP и ADMIN и выводим
    info['SYSTEM_TIME'] = datetime.today().strftime("%H:%M of %d.%m.%Y")
    info['LOCATION'] = (location['latitude'], location['longitude'])
    info['SYSTEM_PORT'] = json_data['ip']
    info['OVERSEER'] = admin_name
    info['IDS_USER'] = user_id

    for key, value in info.items():
        print(f'{key}: {value}')

    print()
    input("<- RETURN... press any key ")
