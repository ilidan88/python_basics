"""
(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи те же, а значения — кортежи вида (<files_quantity>,
[<files_extensions_list>]), например:
{
100: (15, ['txt']),
1000: (3, ['py', 'txt']),
10000: (7, ['html', 'css']),
100000: (2, ['png', 'jpg'])
}
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили
скрипт.

"""

import os
import json

files = []  # в список будем записывать картежи (размер файлов, расширение)

for r, d, f in os.walk('./'):  # os.walk('./') - ходим по всей дериктории
    for file in f:
        file_path = os.path.join(r, file)
        files.append((file_path.split(".")[-1], os.stat(file_path).st_size))
        # Записываем файлв в files, расширение + размер
max_size = max(files, key=lambda x: x[1])[1]
# max_size теперь нажодим по 1 элементу картежа. т.е это будет 2й элемент = размер
i = 1
my_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    my_dict[i] = (0, [])
    # ходим по max_size и заисывем в словарь кллючи умножая на дсять после каждой цифры
    #  в итоге my_dict = {10: (0, []), 100: (0, []), 1000: (0, []), 10000: (0, []), 100000: (0, [])}
    # размер max_size = 99903
for file in files:
    len_file = len(str(file[1]))
    num, ext_list = my_dict[10 ** len_file]
    ext_list.append(file[0])
    ext_list = list(set(ext_list))
    my_dict[10 ** len_file] = (num + 1, ext_list)
print(my_dict)

with open('_summary.json', 'w') as f_json:
    json.dump(my_dict, f_json)
