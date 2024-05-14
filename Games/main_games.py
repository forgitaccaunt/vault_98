from GUI.color_decor import get_warning
from Games.quiz.game_quiz import get_quiz
from Games.random_quote.game_quote import get_random_quote


# Словарь доступных комманд
command_game_panel = {
                'GAME01': (get_random_quote, 1),
                'GAME02': (get_quiz, 2)
                }


# Меню с играми
def get_games(user_id):
    print('--------------------------------')
    print('''
\033[1m\033[37m[GAME MENU]\033[0m Список доступных комманд:
GAME01 - Случайная цитата VAULT-Quote
GAME02 - [UNSUPPORTED] Викторина VAULT-Quiz
GAME03 - [UNSUPPORTED] ARCADA
>
RETURN - Назад
          ''')
    try:
        tmp_input = input('COMMAND: ').upper()
        if tmp_input == 'RETURN':
            return None
        else:
            # Получаю из command_game_panel{} функцию игры и id игры
            # Вызываю функцию игры и передаю в нее user_id и game_id
            get_game_from_dict, game_id = command_game_panel[tmp_input]
            get_game_from_dict(user_id, game_id)
            get_games(user_id)
    except KeyError:
        print(f'{get_warning()} Неверная команда')
        get_games(user_id)
