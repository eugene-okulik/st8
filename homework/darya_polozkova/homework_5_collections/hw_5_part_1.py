my_dict = {'tuple': 'value1', 'list': 'value2', 'dict': 'value3', 'set': 'value4'}
my_dict['tuple'] = (1, 'hi', None, 12.12, False)
my_dict['list'] = [1, 'qa', 11.44, True, 100]
my_dict['dict'] = {'name': 'Dasha', 'age': '34', 'profession': 'qa', 'course': 'python', 'dream': 'True'}
my_dict['set'] = [1, None, 'monday', 12.18, True]

# Для того, что хранится под ключом ‘tuple’:
# выведите на экран последний элемент
print(my_dict['tuple'][-1])
# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
# удалите второй элемент списка
my_dict['list'].append('added')
my_dict['list'].pop(1)
# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент
my_dict['dict'][('i am a tuple',)] = (0.42)
my_dict['set'].append(100.43)
my_dict['set'].remove('monday')
print(my_dict)
