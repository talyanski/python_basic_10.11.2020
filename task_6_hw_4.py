#  !!!! Для корректной работы скриптов с параметрами (везде внешний ввод) необходимо отключать остальные варианты !!!!

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
# быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

#  -----------------------первый скрипт через randint--------------------------------

from sys import argv
from random import randint

name, start = argv
start = int(start)
try:
    list_61 = [randint(start, 10) for _ in range(11-start)]
    print(f'\nгенерируем целые числа начиная с {start} до 10 {list_61}')
except ValueError as err:
    print('Ошибка ввода')
    print(err)
print("end 6_1_1", '-' * 40, "\n")

#  -----------------------первый скрипт через count--------------------------------

from sys import argv
from itertools import count

name, start = argv
start = int(start)
try:
    for i in count(start):
        if i > 10:
            break
        else:
            print(i)
except ValueError as err:
    print('Ошибка ввода')
    print(err)
print("end 6_1_2", '-' * 40, "\n")

#  -----------------------второй скрипт через cycle--------------------

from sys import argv
from itertools import cycle

name, *arg_1 = argv
count = 0
for item in cycle(arg_1):
    if count > 10:
        break
    print(item)
    count += 1
print("end 6_2", '-' * 40, "\n")
