"""
Задача 10: На столе лежат n монеток.
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повёрнуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
"""
n = int(input('Enter the number of coins: '))
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input('If the coin lies obverse up - enter the number 1, if not - the number 0: '))
    if x == 1:
        count_one += 1
    else:
        count_zero += 1
if count_one > count_zero:
    print(f'Minimum number of coins to flip: {count_zero}')
else:
    print(f'Minimum number of coins to flip: {count_one}')
