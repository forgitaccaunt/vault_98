
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from Databases.alchemy import Journal
from GUI.color_decor import get_succes, get_warning


def add_new_note(user_id):
    note = input('ВВЕДИТЕ ТЕКСТ: ')
    date = datetime.today()

    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)
    try:
        with Session(autoflush=False, bind=engine) as db:
            tmp = Journal(note=note, date=date, id_user=user_id)
            db.add(tmp)
            db.commit()
            print(f'{get_succes()} Запись добавлена')
    except Exception:
        print(f'{get_warning()} TERMINAL ERROR')

    print()
    return user_id
