"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections

med = []

corps = collections.defaultdict(list)
n = int(input('Введите количество предприятий: '))

for i in range(n):
    corp_name = input(str(i+1) + "-я компания: ")

    for j in range(4):
        quarter = int(input(f'Прибыль за {j+1}-й квартал: '))
        corps[corp_name].append(quarter)

    corps[corp_name].append(sum(corps[corp_name]) / 4)
    med.append(corps[corp_name][4])

print(f'Средняя прибыль за год для всех предприятий равна {sum(med) / n}')

for k, v in corps.items():
    if v[-1] < sum(med) / n:
        print(f'У компании {k} средняя прибыль ниже среднего')
    if v[-1] > sum(med) / n:
        print(f'У компании {k} средняя прибыль ниже среднего')
