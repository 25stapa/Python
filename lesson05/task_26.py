"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит
число А в целую степень B с помощью рекурсии.
*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""

a = int(input('Enter number A: '))
b = int(input("Enter degree of a number A: "))


def degree(a, b):
    if b == 1:
        return a
    if b != 1:
        return a * degree(a, b - 1)


print(f'The result of exponentiation is: {degree(a, b)}')
