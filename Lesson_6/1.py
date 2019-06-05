"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
from memory_profiler import profile


@profile
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


@profile
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


wrap_sieve(20, 2)
wrap_non_sieve(20, 2)

'''
macOS x64 10.14.3, python 3.7.2
Несмотря на гораздо более длительное выполнение "решета Эратосфена" наивным алгоритмом, 
согласно профилировщику памяти оба алгоритма используют одинаковое количество памяти, 
а именно - 10.7 мибибайт


Filename: /Users/kirill/PycharmProjects/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    14     10.7 MiB     10.7 MiB   @profile
    15                             def wrap_sieve(end, n):
    16     10.7 MiB      0.0 MiB       def eratosthenes(n):
    17     10.7 MiB      0.0 MiB           sieve = list(range(n + 1))
    18     10.7 MiB      0.0 MiB           sieve[1] = 0
    19     10.7 MiB      0.0 MiB           for i in sieve:
    20     10.7 MiB      0.0 MiB               if i > 1:
    21     10.7 MiB      0.0 MiB                   for j in range(i + i, len(sieve), i):
    22     10.7 MiB      0.0 MiB                       sieve[j] = 0
    23     10.7 MiB      0.0 MiB           return sieve
    24     10.7 MiB      0.0 MiB       while len(eratosthenes(n)) < end:
    25     10.7 MiB      0.0 MiB           n += 1
    26     10.7 MiB      0.0 MiB       return eratosthenes(n).pop()


Filename: /Users/kirill/PycharmProjects/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    29     10.7 MiB     10.7 MiB   @profile
    30                             def wrap_non_sieve(end, n):
    31     10.7 MiB      0.0 MiB       def non_sieve(n):
    32     10.7 MiB      0.0 MiB           lst = []
    33     10.7 MiB      0.0 MiB           for i in range(2, n + 1):
    34     10.7 MiB      0.0 MiB               for j in range(2, i):
    35     10.7 MiB      0.0 MiB                   if i % j == 0:
    36     10.7 MiB      0.0 MiB                       break
    37                                         else:
    38     10.7 MiB      0.0 MiB                   lst.append(i)
    39     10.7 MiB      0.0 MiB           return lst
    40     10.7 MiB      0.0 MiB       while len(non_sieve(n)) < end:
    41     10.7 MiB      0.0 MiB           n += 1
    42     10.7 MiB      0.0 MiB       return non_sieve(n).pop()
'''