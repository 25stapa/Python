"""
Задача 18:
Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

N = int(input('\nEnter the number of list items: '))
list_A = list(range(1, N + 1))
print(*list_A, sep=', ')
x = int(input('Enter number X: '))

for i in list_A:
    if x - 1 == i or x + 1 == i:
        print(f'\nThe closest element to a given number {x} is: {i}')
    else:
        i += 1
