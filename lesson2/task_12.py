# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа
# X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

S = int(input('Enter the sum of two numbers S: '))
P = int(input('Enter the product of two numbers P: '))
for i in range(S):
    for j in range(P):
        if S == i + j and P == i * j:
            print(f'The number X is: {i},\tThe number Y is: {j}.')