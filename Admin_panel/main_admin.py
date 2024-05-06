# Словарь доступных комманд
command_admin_panel = {
                'RETURN': None
                }


# Меню Панели управления
def get_admin_panel(user_id):
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
