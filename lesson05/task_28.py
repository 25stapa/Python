"""
Task 28: Дана строка (возможно, пустая), состоящая из букв A-Z:
AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB BBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида:
A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла невалидная строка.
Пояснения: Если символ встречается 1 раз, он остается без изменений;
Если символ повторяется более 1 раза, к нему добавляется количество повторений.

"""

data = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'


def rle(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += prev_char + str(count)
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += prev_char + str(count)
        return encoding


print(rle(data))
