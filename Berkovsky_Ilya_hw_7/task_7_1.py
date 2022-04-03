"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""
import os
list_dir = ['settings', "mainapp", "adminapp", "authapp"]
dir_path = os.path.join('my_project')
if os.path.exists(dir_path):
    print("Папка my_project уже существует")
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    for i in list_dir:
        if not os.path.exists(i):
            os.makedirs(f"my_project/{i}")
