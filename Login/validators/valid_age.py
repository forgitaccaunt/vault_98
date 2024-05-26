from datetime import datetime
from GUI.color_decor import get_warning


def age_validator(age: str) -> str:
    try:
        date_object = datetime.strptime(age, "%Y-%m-%d").date()
        return date_object
    except Exception:
        print(f'{get_warning()} Неверная дата')
        return age_validator(input('ДАТА РОЖДЕНИЯ (формат YYYY-MM-DD): '))
