my_dict = {
    'tuple': (12, 234, 44, 6, "qw", 1),
    'list': [45, 80, 34, "rt", 12],
    'set': {1, 3, 54, "add", 0},
    'dist': {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5'
    }
}

# Взаимодействие с тем, что хранится под ключом ‘tuple’
print(my_dict['tuple'][-1])

# Взаимодействие с тем, что хранится под ключом ‘list’
my_dict['list'].append(18)
my_dict['list'].pop(1)

# Взаимодействие с тем, что хранится под ключом ‘set’
my_dict['set'].add(15)
my_dict['set'].remove("add")

# Взаимодействие с тем, что хранится под ключом ‘dict’
my_dict['dist'][('i am a tuple',)] = "qwe"
del my_dict['dist']['two']

print(my_dict)
