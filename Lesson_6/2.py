"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from memory_profiler import profile
from pympler import asizeof
from dataclasses import dataclass


class Character:
    def __init__(self, level, name):
        self.level = level
        self.name = name


class CharacterSlots:
    __slots__ = ('level', 'name')

    def __init__(self, level, name):
        self.level = level
        self.name = name


@dataclass
class CharacterDataClass:
    level: int
    name: str


char = Character(5, 'Marvin')
char_slots = CharacterSlots(5, 'Marvin')
char_dataclass = CharacterDataClass(5, 'Marvin')


@profile
def foo():
    print(f'Links number: {asizeof.asizeof(char)}')

@profile
def bar():
    print(f'Links number: {asizeof.asizeof(char_slots)}')

@profile
def baz():
    print(f'Links number: {asizeof.asizeof(char_dataclass)}')


foo()
bar()
baz()

'''
Как видно в логе снизу минимальное количество ссылок на переменные приходтся на класс, где используются слоты
data-class - это переиначеный классический класс для данных, просто с более удобной записью.
Тем не менее, согласно потреблению памяти, классический класс для данных использовал меньше всего памяти.


Links number: 368
Filename: /Users/kirill/PycharmProjects/algo_and_structures_python/Lesson_6/2.py

Line #    Mem usage    Increment   Line Contents
================================================
    39     10.8 MiB     10.8 MiB   @profile
    40                             def foo():
    41     10.8 MiB      0.0 MiB       print(f'Links number: {asizeof.asizeof(char)}')


Links number: 144
Filename: /Users/kirill/PycharmProjects/algo_and_structures_python/Lesson_6/2.py

Line #    Mem usage    Increment   Line Contents
================================================
    43     10.8 MiB     10.8 MiB   @profile
    44                             def bar():
    45     10.8 MiB      0.0 MiB       print(f'Links number: {asizeof.asizeof(char_slots)}')


Links number: 368
Filename: /Users/kirill/PycharmProjects/algo_and_structures_python/Lesson_6/2.py

Line #    Mem usage    Increment   Line Contents
================================================
    47     10.8 MiB     10.8 MiB   @profile
    48                             def baz():
    49     10.8 MiB      0.0 MiB       print(f'Links number: {asizeof.asizeof(char_dataclass)}')
'''