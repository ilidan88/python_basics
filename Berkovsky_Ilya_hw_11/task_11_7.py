"""
 Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
 Реализуйте перегрузку методов сложения и умножения комплексных чисел.
 Проверьте работу проекта.
 Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
 Проверьте корректность полученного результата.
"""

class ComplexNumber:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __add__(self, other):
        print('Сумма чисел равна: ')
        return f'{self.y + other.y} + {self.x + other.x}'

    def __mul__(self, other):
        print("Произведение чискл равно : ")
        return f'{self.y * other.y - (self.x * other.x)} + {self.x * other.y}'

    def __str__(self):
        return f'{self.y} + {self.x}'

result_1 = ComplexNumber(2, 5)
result_2 = ComplexNumber(6, -2)
print(result_1)
print(result_2)
print(result_1 + result_2)
print(result_1 * result_2)