"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections

hex_string = '0123456789ABCDEF'

col = collections.defaultdict(list)

for i in range(2):
    n = input(f'Введите {i+1}-е шестнадцатиричное число: ')
    for j in n:
        col[i].append(j.upper())

# перевод значений в десятичный формат
integers = []
for i in col:
    n = 0
    for j in col[i]:
        n += hex_string.find(j) * (16 ** (len(col[i]) - col[i].index(j) - 1))
    integers.append(n)

# операции сложения и умножения
a = []
a.append(integers[0] + integers[1])
a.append(integers[0] * integers[1])

# перевод десятичных чисел в шестнадцатеричный формат
for i in a:
    tmp = []
    while i > 1:
        tmp.append(hex_string[int(i % 16)])
        i /= 16
    tmp.reverse()
    col['answers'].append(list(tmp))


print(f'Для чисел {col[0]} и {col[1]}\n'
      f'{col["answers"][0]} - сумма\n'
      f'{col["answers"][1]} - произведение')
