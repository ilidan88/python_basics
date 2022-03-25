"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
#>>> odd_to_15 = odd_nums(15)
#>>> next(odd_to_15)
1
#>>> next(odd_to_15)
3
...
#>>> next(odd_to_15)
15
#>>> next(odd_to_15)
...StopIteration...
"""


def num_generator(max_num):
    for random_num in range(1, max_num + 1, 2):
        yield random_num

#user_num = int(input("введите число: "))
user_num = 15
gen = num_generator(user_num)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

