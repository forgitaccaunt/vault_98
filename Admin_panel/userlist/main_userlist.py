from Admin_panel.userlist.deluser import persona_el_morta
from Admin_panel.userlist.user_list import get_all_user
from Admin_panel.userlist.userlist_log import get_user_log
from GUI.color_decor import get_warning
from Login.registration import user_registration


# Словарь доступных комманд
command_userlist_menu = {'USERLIST': get_all_user,
                         'ADDUSER': user_registration,
                         'DELUSER': persona_el_morta,
                         'LOGUSER': get_user_log
                         }


# Меню управления персоналом
def get_userlist_menu(user_id):
    print('--------------------------------')
    print('''
\033[1m\033[37m[USERLIST MENU]\033[0m Список доступных комманд:
USERLIST - Список личного состава
ADDUSER - Добавить жителя
DELUSER - Удалить жителя
LOGUSER - Получить логи авторизации
>
RETURN - Назад
          ''')
    try:
        tmp_input = input('COMMAND: ').upper()
        if tmp_input == 'RETURN':
            return None
        else:
            command_userlist_menu[tmp_input](user_id)
            get_userlist_menu(user_id)
    except KeyError:
        print(f'{get_warning()} Неверная команда')
        get_userlist_menu(user_id)
