# Словарь доступных комманд
from Admin_panel.communication.main_comm import get_connect_menu
from Admin_panel.journal.main_journal import get_journal_menu
from Admin_panel.loglist.main_log import get_loglist_menu
from Admin_panel.userlist.main_userlist import get_userlist_menu


command_admin_panel = {'JOURNAL': get_journal_menu,
                       'USERLIST': get_userlist_menu,
                       'LOGLIST': get_loglist_menu,
                       'CONNECT': get_connect_menu
                       }


# Меню Панели управления
def get_admin_panel(user_id):
    print('--------------------------------')
    print('''
[ADMIN PANEL MENU] Список доступных комманд:
JOURNAL  - Журнал записей смотрителя
USERLIST - Личный состав
LOGLIST  - Журнал событий
CONNECT  - Связь с другими убежищами
>
RETURN - Назад
          ''')
    try:
        tmp_input = input('COMMAND: ').upper()
        if tmp_input == 'RETURN':
            return None
        else:
            command_admin_panel[tmp_input](user_id)
            get_admin_panel(user_id)
    except KeyError:
        print('[WARNING] Неверная команда')
        get_admin_panel(user_id)
