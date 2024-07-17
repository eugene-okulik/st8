operation_1 = 'результат операции: 42'
operation_2 = 'результат операции: 514'
app = 'результат работы программы: 9'

search = operation_1.find(': ')
search_app = app.find(': ')

result_operation_1 = operation_1[search:]
result_operation_2 = operation_2[search:]
result_app = app[search_app:]

result_operation_1 = result_operation_1.lstrip(' :')
result_operation_2 = result_operation_2.lstrip(' :')
result_app = result_app.lstrip(' :')

print(
    f'результат операции: {int(result_operation_1) + 10} \n'
    f'результат операции: {int(result_operation_2) +10} \n'
    f'результат работы программы: {int(result_app) + 10}'
)
