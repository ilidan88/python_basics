

duration = [53, 153, 4153, 400153]
for i in duration:
    if i <= 60:
        print(f'{i} сек')
    elif i > 60 and i < 3600:
        print(f"{i // 60} мин {i % 60} сек")
    elif i > 3600 and i < 86400:
        print(f'{i // 3600} час {i % 3600 // 60} мин {i % 60} сек')
    else:
        print(f'{i // 86400 } дн {i % 86400 // 3600 } час {i % 3600 // 60} мин {i % 60} сек')