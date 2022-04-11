import requests

def currency_rates(User_request):
    """ В tack_4_4 импортировал функцию написанную тут"""
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