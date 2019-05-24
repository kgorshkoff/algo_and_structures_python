"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import randint

lst = []
a = int(input('Введите нижнюю границу : '))
b = int(input('Введите верхнюю границу: '))
y, x = b, b

for i in range(10):
    lst.append(randint(a, b))
    num = lst[i]
    if num < x:
        x = num


for i in range(len(lst)):
    if lst.index(x) == i:
        continue
    num = lst[i]
    if num < y:
        y = num

print(f'{lst}\n'
      f'Минимальными являются значения: {x} и {y}')