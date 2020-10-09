'''
    Создать (программно) текстовый файл, 
    записать в него программно набор чисел, разделенных пробелами. 
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
from random import randint 
my_str = [str(randint(1, 365)) for i in range(1, 200)]
with open('file5.txt', 'r+', encoding='utf-8') as f:
    f.write(' '.join(my_str))
    f.seek(0)
    print(f'Сумма чисел из файла: {sum(map(int,f.read().split()))}')