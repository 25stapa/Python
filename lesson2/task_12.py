# Task 12: Petya and Katya are brother and sister.
# Petya is a student, and Katya is a schoolgirl.
# Petya helps Katya with math. He conceives two natural numbers
# X and Y (X,Y≤1000), and Katya has to guess them. To do this, Petya makes two clues.
# He calls the sum of these numbers S, and their product P.
# Help Katya guess the numbers Petya has planned.

S = int(input('Enter the sum of two numbers S: '))
P = int(input('Enter the product of two numbers P: '))
for i in range(S):
    for j in range(P):
        if S == i + j and P == i * j:
            print(f'The number X is: {i},\tThe number Y is: {j}.')
