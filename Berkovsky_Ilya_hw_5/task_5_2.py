"""
(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""


def num_generator(max_num):
    num_gen = [random_num for random_num in range(1, max_num + 1, 2)]
    print(num_gen)

user_num = 15
num_generator(user_num)
