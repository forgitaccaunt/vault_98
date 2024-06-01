
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Databases.alchemy import Score
from GUI.color_decor import get_warning


def get_champion_and_scores(game_id, user_id):
    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)

    with Session(autoflush=False, bind=engine) as db:
        try:
            champion = db.query(Score).filter(Score.id_game==game_id).order_by(Score.score.desc()).first()
            record = db.query(Score).filter(Score.id_user=user_id, Score.id_game==game_id).first()
        except Exception:
            print(f'{get_warning()} TERMINAL ERROR')

    print(f'РЕКОРД: {champion.score} ({champion.user.name})')
    print(f'ТВОЙ РЕКОРД: {record.user.name}')
