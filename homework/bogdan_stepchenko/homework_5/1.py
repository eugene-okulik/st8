my_dict = {'tuple': ("tuple_1", "tuple_2", "tuple_3", "tuple_4", "tuple_5"),
           'list': ["list_1", "list_2", "list_3", "list_4", "list_5"],
           'dict': {1: "dict_1", 2: "dict_2", 3: "dict_3", 4: "dict_4", 5: "dict_5"},
           'set': {"set_1", "set_2", "set_3", "set_4", "set_5"}
           }

print(my_dict.get('tuple')[-1])     # printing last element from values of 'tuple'

my_dict.get('list').append('list_6')    # adding one more element to 'list'
my_dict.get('list').pop(1)  # removing 2nd element from 'list

my_dict.get('dict').update({tuple('i am a tuple',): 'dict_6'})  # adding key-value to 'dict
del my_dict.get('dict')[1]  # deleting key:value from 'dict' with key = 1

my_dict.get('set').add("set_6")    # adding element to 'set'
my_dict.get('set').remove('set_2')    # removing element from 'set

print(my_dict)
