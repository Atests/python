'''
Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce

def multiplication(num1, num2):
    return num1*num2

my_list = [el for el in range(99, 1001) if el%2 == 0]

print(reduce(multiplication, my_list))