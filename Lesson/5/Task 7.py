'''
Создать (не программно) текстовый файл, 
в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, 
вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. 
Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json
profit = {}
prof_sum = 0
prof_count = 0
prof_aver = 0
aver_dict = {}
list_profit = []
with open('file7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, ownership, revenue, costs = line.split()
        profit[name] = int(revenue) -int(costs)
        if profit.get(name) >= 0:
            prof_sum += profit.get(name)
            prof_count += 1
    list_profit.append(profit)
    if prof_count != 0:
        prof_aver = prof_sum / prof_count
        aver_dict = {'average_profit': round(prof_aver)}
        list_profit.append(aver_dict)

with open('file7.json', 'w', encoding='utf-8')  as f:
    json.dump(list_profit, f)  

