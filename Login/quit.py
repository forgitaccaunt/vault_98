import sys
from Logging.user_log import trace_user


def get_exit(user_id):
    # Пишем лог о входе в систему
    trace_user(user_id, 'Выход из системы')
    sys.exit()
