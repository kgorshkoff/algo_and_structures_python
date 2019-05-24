#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint

a = int(input('Введите нижнюю границу:  '))
b = int(input('Введите верхнюю границу: '))
x, y = a, b
lst = []

for i in range(10):
    lst.append(randint(a, b))
    num = lst[i]
    if num > x:
        x = num
    elif num < y:
        y = num

print(f'min = {y}, max = {x}')
print(f'Список до замены:       {lst}')
lst[lst.index(x)], lst[lst.index(y)] = lst[lst.index(y)], lst[lst.index(x)]
print(f'Список после замены:    {lst}')
