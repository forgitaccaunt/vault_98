from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from alchemy import Journal, Score
from prettytable import PrettyTable

sqlite_database = "sqlite:///Databases/vault98.db"
engine = create_engine(sqlite_database)

with Session(autoflush=False, bind=engine) as db:
    # получение всех объектов
        # Создаём и печатаем таблицу
    user_scores = db.query(Score).filter(Score.id_game==1).first()
    print(user_scores)
