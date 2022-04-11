"""
Task 3
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в
файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с
кодом «1». При решении задачи считать, что объём данных в файлах во много
раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби  (hobby.csv):
скалолазание,охота
горные лыжи
"""
from itertools import zip_longest
import json

text_users = """Иванов,Иван,Иванович
Петров,Петр,Петрович"""

text_hobby = """скалолазание,охота
горные лыжи"""

#with open("users.csv", "w+", encoding='utf-8') as f:
    #f.write(text_users)


#with open("hobby.csv", "w+", encoding='utf-8') as f:
    #f.write(text_hobby)

users_hobby = {}
with open("users.csv", encoding='utf-8') as f1, open("hobby.csv", encoding='utf-8') as f2:
    num_lines_users = sum(1 for lines_users in f1)  # Считаем строки документа
    num_lines_hobby = sum(1 for lines_hobby in f2)

    if num_lines_users < num_lines_hobby:
        exit(1)
    f1.seek(0)  # Возвращяем курсор в начало дока
    f2.seek(0)
    for line_user, line_hobby in zip_longest(f1, f2):
        users_hobby[line_user.strip()] = line_hobby.strip() if line_hobby is not None else line_hobby
        # Собираем словарь с ключом line_user и значением line_hobby, если line_hobby None, то возвращаем line_hobby
        # .strip() убирает \n
with open('task3.json', 'w', encoding='utf-8') as f:
    json.dump(users_hobby, f, ensure_ascii=False)
# передаём обьект в формате json. Методом dump передаёб обьеке (users_hobby),
# ensure_ascii=False - символы будут записаны как есть, без экранирования
