"""Создать список, содержащий цены на товары (10–20 товаров), например:
Вывести на экран эти цены через запятую в одну строку,
цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию,
новый список не создавать (доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?"""

price_list = [57.8, 46.51, 97, 62.35, 54.56, 98.12, 20, 87.20, 25.05, 12]


def return_list(my_list):
    ordered_price_list = []
    for price in price_list:
        price_rub = int(price)
        price_kop = int((price * 100) % 100)
        ordered_price_list.append(f'{price_rub:02} руб {price_kop:02} коп')
    return ordered_price_list

print(",".join(return_list(price_list)), "\n", id(return_list(price_list)))

print(",".join(return_list(price_list.sort())), "\n", id(return_list(price_list.sort())))

new_list = return_list(price_list.sort(reverse=True))
print(",".join(new_list))

list_max_5 = []
for i in range(5):
    list_max_5.append(new_list[i])
print(",".join(list_max_5))

#fff