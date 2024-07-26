operation_1 = 'результат операции: 42'
operation_2 = 'результат операции: 54'
operation_3 = 'результат работы программы: 209'
operation_4 = 'результат: 2'


def calculate(operation):
    start = operation.index(': ')
    result = int(operation[start:].strip(': ')) + 10
    print(result)


calculate(operation_1)
calculate(operation_2)
calculate(operation_3)
calculate(operation_4)
