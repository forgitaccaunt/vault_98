from GUI.color_decor import get_warning


def rank_validator(rank: str) -> str:
    if rank in ('ADMIN', 'USER', 'AGENT'):
        return rank
    else:
        print(f'{get_warning()} ДОСТУПНЫЕ РАНГИ: ADMIN, USER, AGENT')
        return rank_validator(input('УРОВЕНЬ ДОСТУПА: ').upper())
