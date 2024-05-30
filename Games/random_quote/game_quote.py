import requests
from GUI.color_decor import get_warning
from Games.get_game_info import get_info
from Games.get_record import get_champion_and_scores
from Games.user_add_scores import add_scores


def get_random_quote(user_id, game_id):
    get_info(game_id)

    # Запрос к API, чтение json, вывод на экран
    try:
        response = requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&format=json')
        if response.status_code == 200:
            json_data = response.json()
            print(f"# {json_data['quoteText']} [{json_data['quoteAuthor']}]")
    except Exception:
        print(f'{get_warning()} TERMINAL ERROR')

    # Добавлем очки в таблицу Score
    add_scores(game_id, user_id)

    # Выводим рекорд игры и личный рекорд
    get_champion_and_scores(game_id, user_id)

    input('<- RETURN')
