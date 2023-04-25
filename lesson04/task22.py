"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.

"""
n = int(input('Enter the amount elements of the first set: '))
m = int(input('Enter the amount elements of the second set: '))

set_1 = set()
set_2 = set()
list_1 = list()

a = [int(i) for i in input('Enter the first set: ').split()]
temp = set(a)
for i in temp:
    set_1.add(i)

b = [int(i) for i in input('Enter the second set : ').split()]
temp = set(b)
for i in temp:
    set_2.add(i)
print(set_1)
print(set_2)
summ = set_1 & set_2
print(*summ)
