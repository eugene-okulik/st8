my_dict = {'tuple': (1, 2, 3, 4, 5), 'list': [1, 2, 3, 4, 5], 'dict': {'1': 223, '2': 224, '3': 225, '4': 226,
                                                                       '5': 227}, 'set': {1, None, 'text', False, 5}}
print(my_dict['tuple'][-1])
my_dict['list'].append(777)
my_dict['list'].pop(1)
print(my_dict['list'])
my_dict['dict'].pop('1')
my_dict['dict']['i_am_a_tuple'] = 333
my_dict['set'].add(7)
my_dict['set'].pop()
print(my_dict)
