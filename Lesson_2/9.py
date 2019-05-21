"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

max_sum = 0
max_num = 0
nums = input("Введите числа через запятую: ")


def sum_digits(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sum_digits(num // 10)


for num in nums.split(','):
    s = sum_digits(int(num))
    if s > max_sum:
        max_sum = s
        max_num = num

print(f'Наибольшее число - {max_num} с суммой {max_sum}')