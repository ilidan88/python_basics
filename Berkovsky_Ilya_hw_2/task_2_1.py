"""Выяснить тип результата выражений"""

expression_list = [15 * 3,
                   15 / 3,
                   15 // 2,
                   15 ** 2]

for expression in expression_list:
    print(type(expression))
