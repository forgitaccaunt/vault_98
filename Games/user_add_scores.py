from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from Databases.alchemy import Score
from GUI.color_decor import get_warning


def add_scores(game_id, user_id):
    # Добавлем в таблицу Scores очко Пользователю (каждый запрос - плюс очко)
    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)

    with Session(autoflush=False, bind=engine) as db:
        try:
            user_scores = db.query(Score).filter(Score.id_game==game_id, Score.id_user==user_id).first()
            if user_scores:
                user_scores.score += 1
            else:
                tmp = Score(id_game=game_id, id_user=user_id, score=1)
                db.add(tmp)
            db.commit()
        except Exception:
            print(f'{get_warning()} TERMINAL ERROR')
