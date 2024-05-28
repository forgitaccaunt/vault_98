from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Databases.alchemy import User
from GUI.color_decor import get_succes, get_warning


def persona_el_morta(user_id):
    persona = input('ИДЕНТИФИКАТОР гражданина: ')

    vault_db = 'sqlite:///Databases/vault98.db'
    engine = create_engine(vault_db)

    with Session(autoflush=False, bind=engine) as db:
        try:
            if input('ВЫ УВЕРЕНЫ? [YES / NO]: ') == 'YES':
                user = db.query(User).filter(User.id==persona).first()
                db.delete(user)
                db.commit()
                print(f'{get_succes()} Житель мёртв или навсегда покинул убежище.')
            else:
                print(f'{get_warning()} Операция прервана')

        except Exception:
            print(f'{get_warning()} TERMINLAL ERROR')

    print()
    input("<- RETURN... press any key ")
    return user_id
