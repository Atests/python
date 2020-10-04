'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета 
заработной платы сотрудника. 
В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия. Для выполнения 
расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv
print(argv)
param = argv[1:]

def payroll_accounting(output_in_hours: float, rate_per_hour: float, prize: float )->float:
    try:
        return output_in_hours*rate_per_hour + prize
    except:
        print('Не ошибайтесь, вводите правильно значения!')
        return None

def float_new(value):    
    try:
        return float(value)
    except:
        return value

if 'help' in param or 'h' in param:
    print('Расчет заработной платы сотрудника.\n',
            'Вводим три значения: <output_in_hours>, <rate_per_hour>, <prize>')   # для консоли cmd
else:
    if 3==len(param):    
        print('Заработная плата: ', 
                payroll_accounting(
                                    float_new(param[0]), 
                                    float_new(param[1]), 
                                    float_new(param[2])
                                  )
            )
    else:
        print('Вводить надо три значения: <output_in_hours>, <rate_per_hour>, <prize>')

# print(payroll_accounting(23,12,78))