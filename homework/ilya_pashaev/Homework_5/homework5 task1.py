

my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 11, 12, 13, 14],
    'dict': {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500},
    'set': {1, 2, 3, 4, 5}
}
print('Before')
print(my_dict['tuple'])
print(my_dict['list'])
print(my_dict['dict'])
print(my_dict['set'])
print('After')
print('Last tuple element: ', my_dict['tuple'][-1])
my_dict['list'].append(16)
del my_dict['list'][1]
my_dict['dict'][('i am a tuple')] = 1000
del my_dict['dict']['a']
my_dict['set'].add(6)
my_dict['set'].remove(3)
print(my_dict['list'])
print(my_dict['dict'])
print(my_dict['set'])
