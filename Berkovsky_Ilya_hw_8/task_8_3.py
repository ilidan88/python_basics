"""
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

#>>> a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции?
Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:
#>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""
#from fractions import wraps


def type_logger(func):  # Функция которая принимает внутрь функцию
   # @wraps(func)  # Скрывает работу декоратора
    def wrapper(*args):     # Эта функция принимает аргументы переданные в функцию выше
        """XAXA"""
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)}', end=", ")
        return func(*args)
    return wrapper

@type_logger
def calc_cube(*args):
    return list(map(lambda x: x ** 3, args))

a = calc_cube(5, 3)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)

# какая-то беда с импортом from fractions import wraps


