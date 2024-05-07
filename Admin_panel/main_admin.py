from Admin_panel.journal.add_note import add_new_note
from Admin_panel.journal.read import get_all_notes
from Admin_panel.journal.readlast import get_last_note
from Admin_panel.userlist.deluser import persona_el_morta
from Admin_panel.userlist.user_list import get_all_user
from Login.registration import user_registration


# Словарь доступных комманд
command_admin_panel = {'ADDNOTE': add_new_note,
                       'READ': get_all_notes,
                       'READLAST': get_last_note,
                       'USERLIST': get_all_user,
                       'ADDUSER': user_registration,
                       'DELUSER': persona_el_morta
                       }


# Меню Панели управления
def get_admin_panel(user_id):
    print('--------------------------------')
    print('''
[ADMIN PANEL MENU] Список доступных комманд:
>>> Журнал записей смотрителя:
ADDNOTE  - Добавить запись
READ     - Показать все записи
READLAST - Показать последнюю запись
>>> Личный состав:
USERLIST - Список личного состава
ADDUSER  - Добавить гражданина
DELUSER  - Удалить гражднина
>>> [UNSUPPORTED] Протокол событий:
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
