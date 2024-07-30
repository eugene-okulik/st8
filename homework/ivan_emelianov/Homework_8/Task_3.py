operations = [
    'результат операции: 42',
    'результат операции: 514',
    'результат работы программы: 9',
    'результат: 2'
]

ten = 10


def extract_result(text):
    # Извлекаем результат после ": "
    return int(text.split(': ')[1])


for operation in operations:
    result = extract_result(operation)
    if 'работы программы' in operation:
        label = 'результат работы программы'
    else:
        label = 'результат операции'
    print(f'{label}: {result + ten}')
