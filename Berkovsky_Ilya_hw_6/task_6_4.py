"""
*(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
двоеточие и пробел после ФИО:
Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: горные лыжи
"""

from itertools import zip_longest

with open("users_hobby.txt", "a", encoding='utf-8') as f:
    with open("users.csv", encoding='utf-8') as f1, open("hobby.csv", encoding='utf-8') as f2:
        num_lines_users = sum(1 for lines_users in f1)
        num_lines_hobby = sum(1 for lines_hobby in f2)

        if num_lines_users < num_lines_hobby:
            exit(1)

        f1.seek(0)
        f2.seek(0)
        for line_user, line_hobby in zip_longest(f1, f2):
            f.write(f"{line_user.strip()}: "f"{line_hobby.strip() if line_hobby is not None else line_hobby}\n")