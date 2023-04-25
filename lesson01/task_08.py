"""Задача 8: Требуется определить, можно ли от шоколадки размером
n × m долек отломить k долек, если разрешается сделать один разлом
по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""

print('Enter the size of the chocolate n x m')
n = int(input('size n: '))
m = int(input('size m: '))
k = int(input('Enter the number of slices you want to break off: '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
    