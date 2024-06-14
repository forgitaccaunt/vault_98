from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from Databases.alchemy import Game
from GUI.color_decor import get_warning


# Функция печатает название и описание игры
def get_info(game_id):
    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)

    with Session(autoflush=False, bind=engine) as db:
        try:
            tmp = db.query(Game).filter(Game.id==game_id).first()
            print(f'{tmp.name}: {tmp.info}')
        except Exception:
            print(f'{get_warning()} TERMINAL ERROR')
