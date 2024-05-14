import sqlite3
from GUI.color_decor import get_warning


# Функция печатает название и описание игры
def get_info(game_id):
    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                query = '''SELECT name, info FROM Games
                    WHERE id = {}'''.format(game_id)
                game_name, game_info = cursor.execute(query).fetchall()[0]
                print(f'>>> {game_name}: {game_info}')
        except Exception:
            print(f'{get_warning()} TERMINAL ERROR')
