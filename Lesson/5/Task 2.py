'''
    Создать текстовый файл (не программно), 
    сохранить в нем несколько строк, 
    выполнить подсчет количества строк, 
    количества слов в каждой строке.
'''

with open('file2.txt', 'r', encoding='utf-8') as f:
    lines  = f.readlines()
    print(f'Количество строк: {len(lines)}')
    f.seek(0) 
    for i, line in enumerate(lines):
        words =line.split()
        print(f'{i+1} - строка, {len(words)} слов =>{words}')