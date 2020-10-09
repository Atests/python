'''
    Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
    Необходимо написать программу, открывающую файл 
    на чтение и считывающую построчно данные. 
    При этом английские числительные должны заменяться на русские. 
    Новый блок строк должен записываться в новый текстовый файл.
'''

score ={'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('file4-2.txt', 'w', encoding='utf-8') as fw:
    with open('file4-1.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            rez = line.split()
            rez[0] = score[rez[0]]        
            print(' '.join(rez), file=fw)