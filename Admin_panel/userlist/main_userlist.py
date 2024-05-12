from Admin_panel.userlist.deluser import persona_el_morta
from Admin_panel.userlist.user_list import get_all_user
from Login.registration import user_registration


# Словарь доступных комманд
command_userlist_menu = {'USERLIST': get_all_user,
                         'ADDUSER': user_registration,
                         'DELUSER': persona_el_morta
                         }


# Меню управления персоналом
def get_userlist_menu(user_id):
    print('--------------------------------')
    print('''
[USER LIST MENU] Список доступных комманд:
USERLIST - Список личного состава
ADDUSER - Добавить жителя
DELUSER - удалить жителя
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
        print('[WARNING] Неверная команда')
        get_userlist_menu(user_id)
