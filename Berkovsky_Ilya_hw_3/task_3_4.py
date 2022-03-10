"""
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
#>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам?
"""
from typing import Dict, Any, List


def thesaurus_adv(*args) -> dict:
    last_name_dict = {}
    for last_name in args:
        last_name_key = last_name.split(" ")[1][0].capitalize()
        if last_name_key not in last_name_dict:
            name_dict = {}
            last_name_dict[last_name_key] = name_dict
            for name in args:
                key = name.split(" ")[0][0].capitalize()
                key_1 = name.split(" ")[1][0].capitalize()
                if key not in name_dict and key_1 == last_name_key:
                    name_dict[key] = []
                    name_dict[key].append(name)

    return last_name_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
