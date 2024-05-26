from Databases.alchemy import User
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from GUI.color_decor import get_succes, get_warning
from .validators.valid_rank import rank_validator
from .validators.valid_password import password_validator
from .validators.valid_username import username_validator
from .validators.valid_age import age_validator


def user_registration(user_id):
    print('Для регистрации нового USER введите данные...')
    user_name = username_validator(input('ИМЯ ПОЛЬЗОВАТЕЛЯ: ').upper())
    user_pass = password_validator(input('ПАРОЛЬ: '))
    user_age = age_validator(input('ДАТА РОЖДЕНИЯ (формат YYYY-MM-DD): '))
    user_rank = rank_validator(input('УРОВЕНЬ ДОСТУПА: ').upper())

    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)
    try:
        with Session(autoflush=False, bind=engine) as db:
            tmp = User(name=user_name, password=user_pass, age=user_age, rank=user_rank)
            db.add(tmp)
            db.commit()
            print(f'{get_succes()} Пользователь зарегестрирован!')
            print(f'DATA: {user_name} {user_pass} {user_age} {user_rank}')
    except Exception:
        print(f'{get_warning()} TERMINAL ERROR')

    print()
    input("<- RETURN... press any key ")
    print()
