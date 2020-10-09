'''
    Необходимо создать (не программно) текстовый файл, 
    где каждая строка описывает учебный предмет и наличие лекционных, 
    практических и лабораторных занятий по этому предмету и их количество. 
    Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
    Сформировать словарь, содержащий название предмета и общее количество 
    занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

def get_str_sum_of_numbers(s: str) -> int:
    n = 0
    b = ''
    for i in range(len(s)):
        try:
            b = b + str(int(s[i]))
        except:
            if len(b) > 0:
                n = n + int(b)
                b = ''
    if len(b) > 0:
        n = n + int(b)   
    return n 

items = dict('')

with open('file6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        s_split = line.split(': ')
        s_key = str(s_split[0])
        default = get_str_sum_of_numbers(s_split[1]) 
        if s_key in items:
            items[s_key] = items.get(s_key) + default # повторно встречается предмет                   
        else:              
            s_dict = items.setdefault(s_key, default)                      
print(items)