
my_dict = {'tuple': (1, 'some', False, True, 55),
           'list': ['text', 52, True, 'make', 66],
           'dict': {'one': 'value1', 'two': 'value2', 'three': 'value3', 'four': 'value4', 'five': 'value5', },
           'set': {52, 'text', True, '665', 'mark'}
           }
# ‘tuple’: вывести последний элемент
print(my_dict['tuple'][-1])

# ‘list’: добавить в конец списка элемент, удалить второй элемент списка
my_dict['list'].append('hello')
my_dict['list'].pop(1)

# ‘dict’: добавить элемент с ключом ('i am a tuple',) и любым значением, удалить какой-нибудь элемент
my_dict['dict']['i am a tuple'] = 'new'
my_dict['dict'].pop('one')

# ‘set’: добавьте новый элемент в множество, удалите элемент из множества
my_dict['set'].add(53)
my_dict['set'].pop()

print(my_dict)
