"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

lst = []
a = int(input('Введите нижнюю границу:  '))
b = int(input('Введите верхнюю границу: '))
y, x = a, b
result = 0

for i in range(10):
    lst.append(randint(a, b))
    num = lst[i]
    if num > y:
        y = num
    elif num < x:
        x = num

if lst.index(x) < lst.index(y):
    pos_low, pos_high = lst.index(x), lst.index(y)
else:
    pos_low, pos_high = lst.index(y), lst.index(x)

print(f'lst = {lst}\n'
      f'min = {x}    index = {pos_low}\n'
      f'max = {y}    index = {pos_high}\n')

for i in range(len(lst)):
    if i > pos_low and i < pos_high:
        result += lst[i]

print(f'Сумма элементов между минимальным и максимальным значением: {result}')
