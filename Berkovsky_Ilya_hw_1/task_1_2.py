# Задание 2

def list_divided_by_seven(data_list: list):
    sum_divided_by_seven = 0
    for num in data_list:
        sum_number = 0
        divided_number = num
        while (num != 0):
            sum_number += num % 10
            num //= 10
            if sum_number % 7 == 0:
                sum_divided_by_seven += divided_number
    return sum_divided_by_seven


def add_seventeen_to_list_element(data_list: list):
    for i in range(len(data_list)):
        data_list[i] += 17
    return list_divided_by_seven(data_list)

list_of_odd_numbers = [i ** 3 for i in range(1, 1001, 2)]

print(list_divided_by_seven(list_of_odd_numbers))
print(add_seventeen_to_list_element(list_of_odd_numbers))


# Вношу изменения для повторного коммита