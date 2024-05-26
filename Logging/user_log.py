from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Databases.alchemy import Userlogs


def trace_user(user_id, msg):
    date = datetime.today()

    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)

    with Session(autoflush=False, bind=engine) as db:
        tmp = Userlogs(id_user=user_id, date=date, note=msg)
        db.add(tmp)
        db.commit()
