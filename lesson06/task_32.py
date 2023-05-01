"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
import random

list_1 = [random.randint(-15, 15) for i in range(15)]
print(list_1)
min_number = int(input('Enter minimum: '))
max_number = int(input('Enter maximum: '))

for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i, end=', ')
