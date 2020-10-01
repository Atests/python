'''
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. 
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. 
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func().
'''

def int_func(text):    
    my_list = []
    for i in text.lower().split():
        my_list.append( i[0].upper() + i[1:len(i)])
    return ' '.join(my_list)

print(int_func('прОверка текста'))
print(int_func('прОверка'))


# 2-й вариант
def int_func2(text):
    t = text.lower()
    return t[0].upper() + t[1: len(t)]

print(int_func2('прОверка'))


text = 'проверка второй функции'

print(int_func2(text))

text = ' '.join(list(map(lambda x: int_func2(x), text.split())))
print(text)

# 3-й вариант
def int_func3(text):
    return text.title()

print(int_func3('проверка третьего варианта'))