"""
2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы —
 результат тоже должен быть с заглавной. Например:
#>>> num_translate_adv("One")
"Один"
#>>> num_translate_adv("two")
"два"
"""

from typing import Dict, Any


def num_translate_adv(my_dict):
    for num in my_dict.keys():
        if num == user_num:
            return my_dict.get(num)
        elif num.capitalize() == user_num:
            return (my_dict.get(num, None)).capitalize()

num_dict = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десят"
}

user_num = input("Введите число на английском: ")
print(num_translate_adv(num_dict))
