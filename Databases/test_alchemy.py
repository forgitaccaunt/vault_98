from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from alchemy import User, Userlogs
from prettytable import PrettyTable

sqlite_database = "sqlite:///Databases/vault98.db"
engine = create_engine(sqlite_database)

with Session(autoflush=False, bind=engine) as db:
    # получение всех объектов
    table = PrettyTable()
    table.field_names = ['id', 'date', 'name', 'note']

    people = db.query(Userlogs).all()
    for p in people:
        table.add_row([p.id, p.date, p.user.name, p.note])

    print(table)
