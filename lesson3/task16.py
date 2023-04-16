# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

N = int(input('\nEnter the number of list items: '))
print()
some_list = list(range(1, N + 1))
print(some_list)
num_from_list = int(input('\nEnter a number from the list: '))

print(f'The number {num_from_list} appears in the list {some_list.count(num_from_list)} time')

# second solution
print('\nsecond solution')
count = 0
for i in some_list:
    if num_from_list == i:
        count += 1
print(f'\nThe number {num_from_list} appears in the list {count} time')
