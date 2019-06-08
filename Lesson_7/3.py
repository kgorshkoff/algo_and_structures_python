"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""


def cocktail_sort(lst):
    n = len(lst)
    swapped = True
    start = 0
    end = n - 1

    while swapped:

        swapped = False

        for i in range(start, end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True

        if not swapped:
            break

        swapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True

        start = start + 1

    return lst


lst = [63, 9, 70, 11, 38, 12, 76, 63, 95, 35, -18, 8, -3, 21, 81, 56, 35, 50, -31, -88, -99, -60, 91, 81, -98, -45, -22, -8, -56, -34, 30, -61, 73, 65, 35, 24, -50, 81, 23, -93, -19, 7, -22, 46, 36, -52, -87, 2, -89]


print(lst)
cocktail_sort(lst)
print(lst)
med = int(len(lst) / 2)
print(f'Медиана в этом массива находится на позиции {med} и это элемент {lst[med]}')
