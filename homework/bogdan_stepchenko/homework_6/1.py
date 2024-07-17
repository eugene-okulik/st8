from random import choice

a = 'результат операции: 42'
b = 'результат работы программы: 9'

text_from_return = choice([a, b])

# index_from = text_from_return.index(': ') + 1   # solution with 'index' method

index_from = text_from_return.find(': ') + 2  # solution with 'find' method

number_from_slice = text_from_return[index_from:]
edited_number_from_slice = int(number_from_slice) + 10

print(edited_number_from_slice)
