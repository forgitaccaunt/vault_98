def username_validator(name):
    digits = '1234567890'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    acceptable = digits+upper_letters

    set_name = set(name)
    if any(char not in acceptable for char in set_name):
        print('[WARNING] Запрещенный спецсимвол')
    else:
        recommendations = []
        if len(name) < 3:
            recommendations.append(f'увеличить число символов - {3-len(name)}')
        for what, message in ((digits,        'цифру'),
                              (upper_letters, 'заглавную букву')):
            if all(char not in what for char in set_name):
                recommendations.append(f'добавить 1 {message}')

        if recommendations:
            print("[WARNING] Рекомендации:", ", ".join(recommendations))
            username_validator(input('ИМЯ ПОЛЬЗОВАТЕЛЯ: '))
        else:
            print('Password has been verified...')
            return name
