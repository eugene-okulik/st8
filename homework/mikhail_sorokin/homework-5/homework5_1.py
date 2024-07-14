
my_dict = {
    "tuple": (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,),
    "list": ["black_cat", "white_cat", "orange_Cat", "gray_cat", "bold_cat"],
    "dict": {"odin": 1, "dva": 2, "tri": 3, "chetyre": 4, "pyat": 5},
    "set": {"abbd", 4, 11.11, "333", True, False}
}

print(my_dict['tuple'][-1])

my_dict['list'].append("white_cat")
my_dict['list'].pop(1)

my_dict['dict'].update({tuple('i am a tuple',): 7})
my_dict['dict'].pop("chetyre")

my_dict['set'].add(777)
my_dict['set'].remove(1)

print(my_dict)
