from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Databases.alchemy import User
from GUI.color_decor import get_warning


def username_validator(name: str) -> str:
    if 3 <= len(name) <= 30 and name.isalnum():
        # Проверка на уникальность
        vault_db = 'sqlite:///Databases/vault98.db'
        engine = create_engine(vault_db)

        with Session(autoflush=False, bind=engine) as db:
            user_name = db.query(User).filter(User.name==name).first()
            if user_name:
                print(f'{get_warning()} Имя занято')
                return username_validator(input('ИМЯ ПОЛЬЗОВАТЕЛЯ: ').upper())
            else:
                return name
    else:
        print(f'{get_warning()} Длина от 3 до 30 символов, ТОЛЬКО буквы и цифры')
        return username_validator(input('ИМЯ ПОЛЬЗОВАТЕЛЯ: ').upper())
