from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Databases.alchemy import User
from GUI.color_decor import get_warning


@lru_cache
def get_all_user(user_id):

    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)

    with Session(autoflush=False, bind=engine) as db:
        users = db.query(User).all()
        if users:
            print(f' ID |       NAME       |     AGE     | RANK ')
            print(f'============================================')
            for user in users:
                print(f'{user.id:4}| {user.name:16} | {user.age}  | {user.rank:6}')
        else:
            print(f'{get_warning()} TERMINLAL ERROR')

    print()
    input("<- RETURN... press any key ")
    return user_id
