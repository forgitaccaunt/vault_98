import sqlite3


def add_scores(game_id, user_id):
    # Добавлем в таблицу Scores очко Пользователю (каждый запрос - плюс очко)
    with sqlite3.connect('Databases/vault_98.db') as connection:
        cursor = connection.cursor()

        try:
            with connection:
                # Есть ли запись этого пользователя в этой игре
                # Если есть, то добавляем очко, если нет - создаем запись
                query = '''
                        SELECT * FROM Scores WHERE id_game = ? AND id_user = ?
                        '''
                cursor.execute(query, (game_id, user_id))
                if not cursor.fetchall():
                    query = '''
                            INSERT INTO Scores (id_game, id_user, score)
                            VALUES (?, ?, ?)
                            '''
                    cursor.execute(query, (game_id, user_id, 1))
                else:
                    query = '''
                            UPDATE Scores SET score = score + 1
                            WHERE id_game = ? AND id_user = ?
                            '''
                    cursor.execute(query, (game_id, user_id))
        except Exception:
            print("TERMINAL ERROR")
