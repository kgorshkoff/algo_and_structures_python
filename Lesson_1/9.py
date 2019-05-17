# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))

if (b < a < c) or (b > a > c):
    result = a
elif (a < b < c) or (a > b > c):
    result = b
else:
    result = c

print(f'Среднее число: {result}')