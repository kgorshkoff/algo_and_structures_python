#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
from random import randint

lst = []
low = 0

for i in range(10):
    x = lst.append(randint(-10, 10))

for i in lst:
    if i < low:
        low = i

print(f'В списке {lst} максимальный отрицательный элемент - {low}\n'
      f'находится по индексу {lst.index(low)}')
