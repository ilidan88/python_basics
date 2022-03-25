"""
Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_num = set()
src_set = set()

for num in src:
    if num not in src_set:
        unique_num.add(num)
    else:
        unique_num.discard(num)
    src_set.add(num)

Correct_order = [num for num in src if num in unique_num]
print(Correct_order)