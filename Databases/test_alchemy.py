from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from alchemy import User

sqlite_database = "sqlite:///Databases/vault98.db"
engine = create_engine(sqlite_database, echo=False)

with Session(autoflush=False, bind=engine) as db:
    # получение всех объектов
    people = db.query(User).all()
    for p in people:
        print(f"{p.id}.{p.name} ({p.age})")
