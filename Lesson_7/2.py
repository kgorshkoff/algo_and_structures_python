"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""


def merge_sort(lst):
    if len(lst) > 1:
        center = len(lst) // 2
        left = lst[:center]
        right = lst[center:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
        return lst


lst = [-64, -6, -60, 38, -91, 68, -100, -69, -75, 15, 85, -60, 28, -19, 86, 79, 33, -76, 86, 29, 64, -80, -1, 13, 46, 1, 1, -46, 25, -39, 83, -35, -48, -22, -82, -2, 33, -80, 2, -60, 26, 61, 52, 38, -14, 52, -79, 71, -36, 6]
print(lst)
print(merge_sort(lst))




