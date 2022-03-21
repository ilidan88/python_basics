

"""
 Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
str, решить поставленную задачу? Функция должна возвращать результат числового типа,
например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
выведите курсы доллара и евро.

"""

import requests


def currency_rates(User_request):
    address = "http://www.cbr.ru/scripts/XML_daily.asp"
    currency_str = requests.get(address).text
    currency_code = []
    for currency in currency_str.split('<CharCode>')[1:]:
        currency_code.append(currency.split("</CharCode>")[0])
    exchange_rates = []
    for exchange in currency_str.split('<Value>')[1:]:
        exchange_rates.append(float(exchange.split('</Value>')[0].replace(',', '.')))
    currency_dictionary = dict(zip(currency_code, exchange_rates))
    result_from_dict = currency_dictionary.get(User_request.upper())
    result = f"Одни {User_request} равен {result_from_dict} рублей"
    return result

if __name__ == "__main__":
    print(currency_rates("EUR"))
    print(currency_rates("USD"))
    print(currency_rates("usd"))


