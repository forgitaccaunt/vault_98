from datetime import date


def age_validator(age: str) -> str:
    if all(map(str.isdigit, age)) and 1888 <= int(age) <= date.today().year:
        return age
    else:
        print('[WARNING] Формат года: ХХХХ начиная с 1888')
        print('# Пример: Моя тётушка родилась в 1965 году')
        age_validator(input('ГОД РОЖДЕНИЯ: '))
