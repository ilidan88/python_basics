"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно.
Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
"""


class Matrix:
    def __init__(self, list_of_lists):
        self.lists = list_of_lists

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.lists])

    def __add__(self, other):
        new_list = []
        if len(self.lists) == len(other.lists):
            for line_1, line_2 in zip(self.lists, other.lists):
                if len(line_1) != len(line_2):
                    return "Problem"
                sum_line = [x + y for x, y in zip(line_1, line_2)]
                new_list.append(sum_line)
        else:
            return "problem 2"
        return Matrix(new_list)


matrix_1 = Matrix([[1, 2, 8], [3, 4, 6], [5, 6, 7], [7, 8, 9]])
matrix_2 = Matrix([[9, 10, 11], [11, 12, 13], [13, 14, 15], [15, 16, 17]])
print(matrix_1)
print('_' * 30)
print(matrix_2)
print('_' * 30)
print(matrix_1 + matrix_2)