'''
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. 
Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, 
а при достижении числа 10 завершаем цикл. 
Во втором также необходимо предусмотреть условие, 
при котором повторение элементов списка будет прекращено.
'''
from itertools import count, cycle

for i in count(start = int(input("Целое число: ")), step=3):
    print(i)
    if i > 215:
        break

colors = cycle(['red', 'greed', 'yellow'])
n = 0
for color in colors:
    n += 1
    print(color)
    if n > 2215:
        break