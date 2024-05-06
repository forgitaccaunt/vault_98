import sqlite3


def get_champion_and_scores(game_id, user_id):
    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                # Вычисляем рекорд
                query = '''
                    SELECT id_user, MAX(score) FROM Scores
                    WHERE id_game = {}
                    ORDER BY id LIMIT 1
                '''. format(game_id)
                champion, record = cursor.execute(query).fetchone()
        except Exception:
            print("Ошибка вычисления рекорда")

        try:
            with connection:
                # Вычисляем имя рекордсмена
                query = 'SELECT name FROM Users WHERE id = {}'.format(champion)
                champion = cursor.execute(query).fetchone()[0]
        except Exception:
            print("Ошибка имени рекордсмена")

        try:
            with connection:
                # Вычисляем рекорд текущего пользователя
                query = '''SELECT score FROM Scores
                WHERE id_user = {}'''.format(user_id)
                my_record = cursor.execute(query).fetchone()[0]

        except Exception:
            print("Ошибка текущего рекорда")

    print(f'РЕКОРД: {record} ({champion})')
    print(f'ТВОЙ РЕКОРД: {my_record}')
