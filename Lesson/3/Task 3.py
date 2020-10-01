'''
    Реализовать функцию my_func(), которая принимает три позиционных 
    аргумента, и возвращает сумму наибольших двух аргументов.
'''

def my_max(x, y):
    if x > y:
        return x
    else:
        return y



def my_func(x, y, z):
    return my_max(my_max(x,y),z)


print(my_func(14, 12, 25))
