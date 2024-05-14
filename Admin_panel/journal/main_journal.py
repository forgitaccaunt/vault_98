from Admin_panel.journal.add_note import add_new_note
from Admin_panel.journal.read import get_all_notes
from Admin_panel.journal.readlast import get_last_note


# Словарь доступных комманд
command_journal_menu = {'ADDNOTE': add_new_note,
                        'READALL': get_all_notes,
                        'READLAST': get_last_note
                        }


# Меню журнала
def get_journal_menu(user_id):
    print('--------------------------------')
    print('''
\033[1m\033[37m[JOURNAL MENU]\033[0m Список доступных комманд:
ADDNOTE - Добавить запись
READALL - Показать все записи
READLAST - показать последнюю запись
>
RETURN - Назад
          ''')
    try:
        tmp_input = input('COMMAND: ').upper()
        if tmp_input == 'RETURN':
            return None
        else:
            command_journal_menu[tmp_input](user_id)
            get_journal_menu(user_id)
    except KeyError:
        print('[WARNING] Неверная команда')
        get_journal_menu(user_id)
