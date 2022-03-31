
"""
*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

from collections import Counter

with open("nginx_logs.txt", "r", encoding='utf-8') as f:
    my_log = []
    spammer = {}
    for line in f:
        split_line = line.split()
        my_log.append((split_line[0], split_line[5].replace('"', ''), split_line[6]))
        spammer.setdefault(split_line[0], 0)
        spammer[split_line[0]] += 1
#  print(sorted(spammer.values(), reverse=True)[:3])выводит только значение(
print((Counter(spammer).most_common(5)))
# spam_max = sorted(spammer.items(), key=lambda x: x[1], reverse=True) Сравнивал с вашим
# print(spam_max[:5])
