from Admin_panel.main_admin import get_admin_panel
from Login.authorization import user_authorization
from Login.registration import user_registration
from Login.quit import get_exit
from Info.info_terminal import get_terminal_info


# Логотип и интерфейсы
with open("GUI/content/logo.txt", "r") as file:
    for line in file:
        print(line, end='')
    print()

# Словарь доступных комманд
command_dict = {'GAMES': 'get_games',
                'ADMIN': get_admin_panel,
                'INFO': get_terminal_info,
                'QUIT': get_exit
                }
# Кортеж с возможными вариантами YES
yes_tpl = ('Y', 'YE', 'YES', 'Д', 'ДА', 'D', 'DA')


# Функция авторизации / регистрации
def login():
    if input('У Вас есть учётная запись? [YES / NO]: ').upper() in yes_tpl:
        return user_authorization()
    else:
        print('Для работы в терминале необходима учётная запись VAULT-TEK...')
        if input('Создать учётную запись? [YES / NO]: ').upper() in yes_tpl:
            user_registration()
        else:
            print('Возврат в меню Авторизации...')
            login()


# Функция, реализующая главное меню
# Аналогичные функции будут реализовывать внутренние меню
def main():
    print('''
[MAIN TERMINAL MENU] Список доступных комманд:
GAMES - Игры
ADMIN - Панель управления
INFO - Информация о терминале
>
QUIT - KILL TERMINAL SESSION
          ''')
    try:
        tmp_input = input('COMMAND: ').upper()
        if tmp_input == 'ADMIN':
            if user_session[0] == 1:
                get_admin_panel()
                main()
            else:
                print('[WARNING] ПАНЕЛЬ УПРАВЛЕНИЯ доступна только Смотрителю')
                main()
        else:
            command_dict[tmp_input]()
            main()
    except KeyError:
        print('[WARNING] Неверная команда')
        main()


user_session = login()
main()
