"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def symbols(start, finish):
    if start > finish:
        return
    print(f'{start} - {chr(start)}')
    symbols(start+1, finish)


symbols(32, 127)
