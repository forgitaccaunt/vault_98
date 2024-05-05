def password_validator(password):
    digits = '1234567890'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '!@#$%^&*()-+_=`~/|\\'
    acceptable = digits+upper_letters+lower_letters+symbols

    set_password = set(password)
    if any(char not in acceptable for char in set_password):
        print('[WARNING] Запрещенный спецсимвол')
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
            print("[WARNING] Рекомендации:", ", ".join(recommendations))
            password_validator(input('ПАРОЛЬ: '))
        else:
            print('*** Password has been verified...')
            return password
