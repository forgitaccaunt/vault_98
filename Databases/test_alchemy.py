from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from alchemy import Game, Journal, Score
from prettytable import PrettyTable

sqlite_database = "sqlite:///Databases/vault98.db"
engine = create_engine(sqlite_database)

with Session(autoflush=False, bind=engine) as db:

    game_id = 1
    user_id = 1

    champion = db.query(Score).filter(Score.id_game==game_id).order_by(Score.score.desc()).first()
    record = db.query(Score).filter(Score.id_user==user_id, Score.id_game==game_id).first()
    
    print(champion.score, champion.user.name)
    print(record.score)