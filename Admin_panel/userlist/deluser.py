import sqlite3
from GUI.color_decor import get_succes, get_warning


def persona_el_morta(user_id):
    persona = input('ИДЕНТИФИКАТОР гражданина: ')

    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                query = 'DELETE FROM Users WHERE id = {}'.format(persona)
                if input('ВЫ УВЕРЕНЫ? [YES / NO]: ') == 'YES':
                    cursor.execute(query)
                    print(f'{get_succes()} Житель мёрт или навсегда покинул убежище...')
                else:
                    print(f'{get_warning()} Операция прервана')
        except Exception:
            print(f'{get_warning()} TERMINAL ERROR')

    print()

    input("<- RETURN... press any key ")
