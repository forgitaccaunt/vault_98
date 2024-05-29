
from prettytable import PrettyTable
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Databases.alchemy import Journal
from GUI.color_decor import get_warning


def get_last_note(user_id):
    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)

    with Session(autoflush=False, bind=engine) as db:
        # Создаём и печатаем таблицу
        try:
            note = db.query(Journal).order_by(Journal.id.desc()).first()
            table = PrettyTable()
            table.field_names = ['DATE', 'USER', 'NOTE']
            table.add_row([note.date, note.user.name, note.note])
            print(table)
        except Exception:
            print(f'{get_warning()} TERMINLAL ERROR')

    print()
    input("<- RETURN... press any key ")
    return user_id
