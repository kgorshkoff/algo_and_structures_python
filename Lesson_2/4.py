"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def func(depth, x=1, result=0):
    if depth == 0:
        print(f'{result}')
        return
    result += x
    x /= -2
    func(depth-1, x, result)


func(int(input("Введите глубину действия: ")))
