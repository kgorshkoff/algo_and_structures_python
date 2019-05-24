# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

a = int(input('Введите нижнюю границу:  '))
b = int(input('Введите верхнюю границу: '))
mtx = [[randint(a, b) for x in range(5)] for i in range(5)]
mins = []

print('В матрице: ')
for row in mtx:
    print(row, end=' ')
    low = b
    for i in row:
        if i < low:
            low = i
    mins.append(low)
    print(low)

biggest = 0
for i in mins:
    if i > biggest:
        biggest = i

print(f'Самое большое минимальное число - {biggest}')
