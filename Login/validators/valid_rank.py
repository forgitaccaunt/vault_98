def rank_validator(rank: str) -> str:
    if rank in ('ADMIN', 'USER', 'AGENT'):
        return rank
    else:
        print('[WARNING] ДОСТУПНЫЕ РАНГИ:')
        print('ADMIN, USER, AGENT')
        rank_validator(input('УРОВЕНЬ ДОСТУПА: ').upper())
