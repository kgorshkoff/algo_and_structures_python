# 4.	Определить, какое число в массиве встречается чаще всего.
from random import randint

lst = []
num = 0
cnt = 0

for i in range(10):
    lst.append(randint(1, 10))

for i in lst:
    tmp = 0
    for j in lst:
        if i == j:
            tmp += 1
    if tmp > cnt:
        num = i
        cnt = tmp

print(f'В списке {lst}\n'
      f'Самое частовстречающееся число - {num}, встречается {cnt} раз')