"""
*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей
структурой:
|--my_project
    |--settings
        | |--__init__.py
        | |--dev.py
        | |--prod.py
    |--mainapp
        | |--__init__.py
        | |--models.py
        | |--views.py
        | |--templates
            | |--mainapp
                | |--base.html
                | |--index.html
    |--authapp
        | |--__init__.py
        | |--models.py
        | |--views.py
        | |--templates
            |--authapp
                | |--base.html
                | |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
ситуации, библиотеки использовать нельзя.
"""

import os
import yaml


yaml_docs = {"my_project_1":
            [{'settings_1': [
                '__init__.py', 'dev.py', 'prod.py'
            ],
            },
                {'mainapp_1': [
                    '__init__.py', 'models.py', 'views.py', {'templates': [{
                       'mainapp': ['base.html', 'index.html']}]
                    }]},
                {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{
                    'authapp': ['base.html', 'index.html']}]
                }
                             ]
                 }

            ]
    }

file = open('config.yaml', 'w')
file.write(yaml.dump(yaml_docs))
file.close()

with open('config.yaml') as my_file:
    yaml_docs = yaml.safe_load(my_file)
    # safe_load переводит файл в python обьект


def folder_creation(date):
    for folder, data_tmps in date.items():  # folder - ключ соваря, data_tmps - значение
        if not os.path.exists(folder):  # Проверяем наличие папки
            os.mkdir(folder)  # Если нет, то создаём
        os.chdir(folder)  # При помощи os.chdir переходим в эту папку
        for data_tmp in data_tmps:  # ходим по значению
            if isinstance(data_tmp, dict):  # Если значение является словарем
                folder_creation(data_tmp)   # То применяем функцию folder_creation
            else:  # Если значение не словарь то
                if not os.path.exists(data_tmp):  # проверяем наличие файла
                    if "." in data_tmp:  #Если в названии значения есть .
                        # то создаём файл и записываем туда пустую строку
                        with open(data_tmp, "w") as f:
                            f.write("")
    else:
        os.chdir("../")  # Смена дериктории (выход вверх)

folder_creation(yaml_docs)


