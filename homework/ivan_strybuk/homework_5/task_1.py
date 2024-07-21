my_dict = {
    "tuple": (2, 'one', 2.2, True, None, 'try'),
    "list": [2, 'one', 2.2, True, None, 'try'],
    "dict": {"one": 'value', "two": 'value_2', "5": 2, "2.2": '[3]', "ping": 200},
    "set": {2, 'one', 2.2, True, (None,), 'try'}
}

print(my_dict["tuple"][-1])  # выведите на экран последний элемент

my_dict["list"].append(44)  # добавьте в конец списка еще один элемент
pop_list = my_dict["list"].pop(1)  # удалите второй элемент списка. возвращает извлеченный элемент

my_dict["dict"]["i am a tuple"] = 43  # добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict["dict"].pop('one')  # удалите какой-нибудь элемент

my_dict["set"].add(3)  # добавьте новый элемент в множество
my_dict["set"].remove(2.2)  # удалите элемент из множества
