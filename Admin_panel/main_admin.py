# Словарь доступных комманд
from Admin_panel.communication.main_comm import get_connect_menu
from Admin_panel.journal.main_journal import get_journal_menu
from Admin_panel.userlist.main_userlist import get_userlist_menu
from GUI.color_decor import get_warning
from Login.quit import get_exit


command_admin_panel = {'JOURNAL': get_journal_menu,
                       'PERSONS': get_userlist_menu,
                       'CONNECT': get_connect_menu,
                       '0': get_exit
                       }


# Меню Панели управления
def get_admin_panel(user_id):
    print('--------------------------------')
    print('''
\033[1m\033[37m[ADMIN PANEL MENU]\033[0m Список доступных комманд:
JOURNAL - Журнал записей смотрителя
PERSONS - Работа с личным составом
CONNECT - Связь с другими убежищами
XNAME - [UNSUPPORTED] Изменить имя пользователя
XPASS - [UNSUPPORTED] ИЗменить пароль
>
9 - Назад
0 - KILL TERMINAL
          ''')
    try:
        tmp_input = input('COMMAND: ').upper()
        if tmp_input == '9':
            return user_id
        else:
            command_admin_panel[tmp_input](user_id)
            get_admin_panel(user_id)
    except KeyError:
        print(f'{get_warning()} Неверная команда')
        get_admin_panel(user_id)
