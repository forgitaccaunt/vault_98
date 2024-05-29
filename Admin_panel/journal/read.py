from functools import lru_cache
from prettytable import PrettyTable
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from Databases.alchemy import Journal
from GUI.color_decor import get_warning


@lru_cache
def get_all_notes(user_id):
    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)

    with Session(autoflush=False, bind=engine) as db:
        # Создаём и печатаем таблицу
        try:
            notes = db.query(Journal).all()
            table = PrettyTable()
            table.field_names = ['DATE', 'USER', 'NOTE']
            for note in notes:
                table.add_row([note.date, note.id_user.name, note.note])
            print(table)
        except Exception:
            print(f'{get_warning()} TERMINLAL ERROR')

    print()
    input("<- RETURN... press any key ")
    return user_id
