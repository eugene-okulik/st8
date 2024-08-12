my_dict = {'tuple': ('tuple', 5, False, 4.7, 10), 'list': [1, 'text', 8, 'abra', 'cadabra'],
           'dict': {'morning': 'coffee', 'launch': 'soup', 'dinner': 'meet', 'weekend': 'cake'},
           'set': {1, 2, 3, 4, 5}}
my_tuple = my_dict['tuple']
print(my_tuple[-1])
my_list = list(my_dict['list'])
my_list.append('add to the end')
print(my_list)
deleted_element = my_list.pop(1)
print(my_list)
my_dict['dict'][('i am a tuple',)] = 'any value'
print(type(['dict']))
print(my_dict['dict'])
my_dict['dict'].pop('morning')
print(my_dict['dict'])
my_dict['set'].add(33)
my_dict['set'].pop()
my_dict['set'].remove(2)
print(my_dict['set'])
print('The final result: ', my_dict)
