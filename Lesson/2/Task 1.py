'''
    Создать список и заполнить его элементами различных типов данных. 
    Реализовать скрипт проверки типа данных каждого элемента. 
    Использовать функцию type() для проверки типа. 
    Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

my_list = []
my_list.append('Мир')  # str
my_list.append(12)  # int
my_list.append(45.04)  # float
my_list.append(['1', 2])  # list
my_list.append({1, 3, 4})  # множество
my_list.append(('Кортеж', 'молоко'))  # tuple
my_list.append(True)  # boolean
my_list.append({'day': 26, 'month': 9, 'yaer': 2020})  # словарь

for i in my_list:
    print(type(i), '=> ', i)
