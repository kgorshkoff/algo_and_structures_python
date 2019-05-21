"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

x = int(input('Введите число: '))


def reverse(number):
    if number == 0:
        return number
    else:
        print(number % 10, end='')
        return reverse(number // 10)


reverse(x)