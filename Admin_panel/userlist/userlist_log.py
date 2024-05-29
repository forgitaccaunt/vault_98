from functools import lru_cache
from prettytable import PrettyTable
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from Databases.alchemy import Userlogs
from GUI.color_decor import get_warning


@lru_cache
def get_user_log(user_id):
    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)

    with Session(autoflush=False, bind=engine) as db:
        # Создаём и печатаем таблицу
        try:
            logs = db.query(Userlogs).all()
            table = PrettyTable()
            table.field_names = ['id', 'DATE', 'USER', 'NOTE']
            for row in logs:
                table.add_row([row.id, row.date, row.user.name, row.note])
            print(table)
        except Exception:
            print(f'{get_warning()} TERMINLAL ERROR')

    print()
    input("<- RETURN... press any key ")
    return user_id
