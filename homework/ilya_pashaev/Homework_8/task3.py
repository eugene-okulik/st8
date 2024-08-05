lines = ['результат операции: 42',
         'результат операции: 54',
         'результат работы программы: 209',
         'результат: 2']


def fund_number(line):
    number = int(line.split(':')[-1].strip()) + 10
    return number


for line in lines:
    print(fund_number(line))
