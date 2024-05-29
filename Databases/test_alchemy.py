from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from alchemy import Journal
from prettytable import PrettyTable

sqlite_database = "sqlite:///Databases/vault98.db"
engine = create_engine(sqlite_database)

with Session(autoflush=False, bind=engine) as db:
    # получение всех объектов
        # Создаём и печатаем таблицу
    notes = db.query(Journal).all()
    table = PrettyTable()
    table.field_names = ['ID', 'DATE', 'USER', 'NOTE']
    for row in notes:
        table.add_row([row.id, row.date, row.id_user, row.note])
    print(table)
