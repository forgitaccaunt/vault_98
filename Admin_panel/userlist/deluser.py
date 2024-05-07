import sqlite3


def persona_el_morta(user_id):
    persona = input('ИДЕНТИФИКАТОР гражданина: ')

    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                query = 'DELETE FROM Users WHERE id = {}'.format(persona)
                if input('ВЫ УВЕРЕНЫ? [YES / NO]: ') == 'YES':
                    cursor.execute(query)
                    print('Гражданин мёрт или навсегда покинул убежище...')
                else:
                    print("[WARNING] Операция прервана")
        except Exception:
            print("[WARNING] TERMINAL ERROR")

    print()

    input("<- RETURN... press any key ")
