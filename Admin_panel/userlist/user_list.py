from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Databases.alchemy import User
from GUI.color_decor import get_warning
from prettytable import PrettyTable


@lru_cache
def get_all_user(user_id):
    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)

    with Session(autoflush=False, bind=engine) as db:
        # Создаём и печатаем таблицу
        try:
            users = db.query(User).all()
            table = PrettyTable()
            table.field_names = ['ID', 'NAME', 'AGE', 'RANK']
            for user in users:
                table.add_row([user.id, user.name, user.age, user.rank])
            print(table)
        except Exception:
            print(f'{get_warning()} TERMINLAL ERROR')

    print()
    input("<- RETURN... press any key ")
    return user_id
