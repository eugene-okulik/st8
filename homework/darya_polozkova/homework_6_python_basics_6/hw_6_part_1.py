operation_1 = 'результат операции: 42'
operation_2 = 'результат операции: 514'
operation_3 = 'результат работы программы: 9'

start_1 = operation_1.index(': ')
result_1 = int(operation_1[start_1:].strip(': ')) + 10

start_2 = operation_2.index(': ')
result_2 = int(operation_2[start_2:].strip(': ')) + 10

start_3 = operation_3.index(': ')
result_3 = int(operation_3[start_3:].strip(': ')) + 10

print(result_1)
print(result_2)
print(result_3)

