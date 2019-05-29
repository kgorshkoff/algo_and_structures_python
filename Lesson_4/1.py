"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import timeit


def loop(num):
    reverse = 0
    while num > 0:
        reminder = num % 10
        reverse = (reverse * 10) + reminder
        num = num // 10


def recursion(num):
    result = 0
    if num == 0:
        return
    else:
        result += num % 10
        return recursion(num // 10)


print(timeit.timeit("loop(123411)", setup="from __main__ import loop", number=100))
print(timeit.timeit("recursion(123411)", setup="from __main__ import recursion", number=100))


""""
Сделал замеры алгоритма, "разворачивающего" число задом-наперёд.
Скорость работы рекурсии очевидно медленнее, хоть и не принципиально, так как алгоритмы просты.

0.0001439540000000017 - цикл
0.00018295499999999854 - рекурсия

Сложность здесь - линейная O(n)
"""