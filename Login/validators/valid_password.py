from GUI.color_decor import get_warning


def password_validator(password: str) -> str:
    digits = '1234567890'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '!@#$%^&*()-+_=`~/|\\'
    acceptable = digits+upper_letters+lower_letters+symbols

    set_password = set(password)
    if any(char not in acceptable for char in set_password):
        print(f'{get_warning()} Запрещенный спецсимвол')
    else:
        recommendations = []
        if len(password) < 8:
            recommendations.append(f'увеличить число символов - {8-len(password)}')
        for what, message in ((digits,        'цифру'),
                              (symbols,       'спецсимвол'),
                              (upper_letters, 'заглавную букву'),
                              (lower_letters, 'строчную букву')):
            if all(char not in what for char in set_password):
                recommendations.append(f'добавить 1 {message}')

        if recommendations:
            print(f'{get_warning()} Рекомендации:', ', '.join(recommendations))
            password_validator(input('ПАРОЛЬ: '))
        else:
            return password
