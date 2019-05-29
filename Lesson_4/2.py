"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import timeit


def wrap_sieve(end, n):
    def eratosthenes(n):
        sieve = list(range(n + 1))
        sieve[1] = 0
        for i in sieve:
            if i > 1:
                for j in range(i + i, len(sieve), i):
                    sieve[j] = 0
        return sieve
    while len(eratosthenes(n)) < end:
        n += 1
    return eratosthenes(n).pop()


def wrap_non_sieve(end, n):
    def non_sieve(n):
        lst = []
        for i in range(2, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                lst.append(i)
        return lst
    while len(non_sieve(n)) < end:
        n += 1
    return non_sieve(n).pop()


print(timeit.timeit("wrap_sieve(100, 2)", setup="from __main__ import wrap_sieve", number=100))
print(timeit.timeit("wrap_non_sieve(100, 2)", setup="from __main__ import wrap_non_sieve", number=100))


'''
Проверил два алгоритма. Решето работает быстрее в любых случаях, как при маленьких, так и при больших числах
Связано это с тем, что решето использует умный алгоритм и не перебирает все возможные комбинации цифр.
Замеры при end = 100, n = 100:
0.18552505600000002 - решето
55.562932067000006 - наивный алгоритм

Сложность здесь линейно-логарифмическая - О(N log N)
'''