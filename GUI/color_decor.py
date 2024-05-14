# Сообщение - предупреждение
def get_warning():
    return '\033[1m\033[31m[WARNING]\033[0m'


# Сообщение - подтверждение
def get_succes():
    return '\033[1m\033[32m[SUCCESS]\033[0m'


# Сообщение - информация
def get_inform():
    return '\033[1m\033[33m[TERMINAL INFORMATION]\033[0m'


# Шаблон оформления меню
# print('\033[1m\033[37m[MAIN TERMINAL MENU]\033[0m Список доступных комманд:')
