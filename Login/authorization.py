from Databases.alchemy import User
from GUI.color_decor import get_succes, get_warning
from Logging.user_log import trace_user
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def user_authorization():
    user_name = input('ИМЯ ПОЛЬЗОВАТЕЛЯ: ')
    user_pass = input('ПАРОЛЬ: ')

    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)

    with Session(autoflush=False, bind=engine) as db:
        user_session = db.query(User).filter(User.name==user_name and User.password==user_pass).first()
        if user_session:
            print(f'{get_succes()} ACCESS level: {user_session.rank}')
            trace_user(user_session.id, 'Вход в систему')
            return user_session.id, user_session.rank
        else:
            print(f'{get_warning()} Неверное ИМЯ ПОЛЬЗОВАТЕЛЯ или ПАРОЛЬ!')
            return user_authorization()
