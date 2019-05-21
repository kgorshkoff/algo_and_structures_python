"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

x = int(input('Введите число: '))


def odd_even(number, odd=0, even=0):
    if number == 0:
        print(f'У введеного числа {even} четных цифры и {odd} нечетных')
        return
    elif number % 10 % 2 == 0:
        even += 1
    else:
        odd += 1
    return odd_even(number // 10, odd, even)


odd_even(x)
