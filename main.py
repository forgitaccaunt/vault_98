import logging
import logging.config
import yaml
from Admin_panel.main_admin import get_admin_panel
from Games.main_games import get_games
from Login.authorization import user_authorization
from Login.quit import get_exit
from Info.info_terminal import get_terminal_info


# Загружаем настройки логирования из файла
with open('Logging/config/logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

# Создаём первый логгер
logger = logging.getLogger(__name__)

# Логотип и интерфейсы
with open("GUI/content/logo.txt", "r") as file:
    for line in file:
        print(f'\033[1m\033[32m{line}\033[0m', end='')
    print()

# Словарь доступных комманд
command_dict = {'GAMES': get_games,
                'ADMIN': get_admin_panel,
                'INFO': get_terminal_info,
                'QUIT': get_exit
                }


# Функция авторизации / регистрации
def login():
    print('\033[1m\033[32m*\033[0m' * 37)
    print('\033[1m\033[32m>>> АВТОРИЗАЦИЯ\033[0m')
    return user_authorization()


# Функция, реализующая главное меню
# Аналогичные функции будут реализовывать внутренние меню
def main():
    print('--------------------------------')
    print('''
\033[1m\033[32m[MAIN TERMINAL MENU]\033[0m Список доступных комманд:
GAMES - Игры
ADMIN - Панель управления
INFO - Информация о терминале
>
QUIT - KILL TERMINAL SESSION
          ''')
    try:
        tmp_input = input('COMMAND: ').upper()
        if tmp_input == 'ADMIN':
            if user_session[4] == "ADMIN":
                get_admin_panel(user_session[0])
                main()
            else:
                print('[WARNING] ПАНЕЛЬ УПРАВЛЕНИЯ доступна только Смотрителю')
                main()
        else:
            command_dict[tmp_input](user_session[0])
            main()
    except KeyError:
        print('[WARNING] Неверная команда')
        main()


# Сохраняем кортеж данных пользователя
user_session = login()
main()
