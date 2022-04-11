"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>,
<requested_resource>). Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

"""

import requests

# url = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
# my_file = open("nginx_logs.txt", "w+", encoding='utf-8')
# my_file.write(requests.get(url).text)
# my_file.close()


with open("nginx_logs.txt", "r", encoding='utf-8') as f:
    my_log = []
    for line in f:
        split_line = line.split()  # Разделяем строку по пробелам
        my_log.append((split_line[0], split_line[5].replace('"', ''), split_line[6]))  # тянем по индекссам .replace('"', '') - убирает " перед GET
print(*my_log, sep="\n")  # параметр sep="\n", делает вывод каждого элемента с новой строки
