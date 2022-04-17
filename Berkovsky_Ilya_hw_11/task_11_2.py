"""
 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
 Проверьте его работу на данных, вводимых пользователем.
 При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
 dividend
 divider
"""
# class DivisionError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# def division(arg_1, arg_2):
#     if arg_2 == 0:
#         raise DivisionError("Делить на 0 нельзя")
#     result = arg_1 / arg_2
#     return result
#
# print(division(16, 2))
# print(division(16, 0))


class DivisionByNoll:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def division_by_noll(dividend, divider):
        try:
            return dividend / divider
        except:
            return "Делить на 0 нельзя"
divis = DivisionByNoll
print(divis.division_by_noll(10, 2))
print(divis.division_by_noll(10, 0))

