"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


number = int(input("Введите последовательность: "))
digit = int(input("Какую цифру ищем: "))


def func(number, entries=0):
    if number == 0:
        print(f'{entries} вхождений цифры {digit}')
        return
    if number % 10 == digit:
        entries += 1
    func(number // 10, entries)


func(number)
