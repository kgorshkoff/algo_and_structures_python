# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


num = int(input('Введите трёхзначное число: '))

third = num % 10
second = (num - third) / 10 % 10
first = (num - third - second * 10) / 100 % 10

print(f'Сумма : {first + second + third}')
print(f'Произведение: {first * second * third}')

