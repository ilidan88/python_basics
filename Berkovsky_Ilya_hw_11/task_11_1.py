"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def transform(cls, day_month_year):
        new_date = []
        for i in day_month_year.split():
            if i != "-":
                new_date.append(i)
        return f'{int(new_date[0])} {int(new_date[1])} {int(new_date[2])}'

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 < year <= 2022:
                    return f'Правильная дата'
                else:
                    return 'Неправильный год'
            else:
                return "Неправильный месяц"
        else:
            return 'Неправильняй день'

    def __str__(self):
        return f'Текущая дата {Date.transform(self.day_month_year)}'


date = Date('15 - 4 - 22')
print(date)
print(date.valid(15, 4, 2022))
print(date.valid(15, 22, 2022))
print(date.valid(33, 4, 2022))
print(date.valid(15, 4, 2030))
print(Date.transform('15 - 4 - 22'))