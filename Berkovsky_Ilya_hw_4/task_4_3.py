

"""
*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса
дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

"""

import requests


def currency_rates(User_request):
    address = "http://www.cbr.ru/scripts/XML_daily.asp"
    currency_str = requests.get(address).text
    date_ind = currency_str.find("Date")
    date = currency_str[date_ind + 6:date_ind + 16]
    currency_code = []
    for currency in currency_str.split('<CharCode>')[1:]:
        currency_code.append(currency.split("</CharCode>")[0])
    exchange_rates = []
    for exchange in currency_str.split('<Value>')[1:]:
        exchange_rates.append(float(exchange.split('</Valugite>')[0].replace(',', '.')))
    currency_dictionary = dict(zip(currency_code, exchange_rates))
    result_from_dict = currency_dictionary.get(User_request.upper())
    result = f"Одни {User_request} равен {result_from_dict} рублей на момент {date}"
    return result

if __name__ == "__main__":
    print(currency_rates("EUR"))
    print(currency_rates("USD"))
    print(currency_rates("usd"))