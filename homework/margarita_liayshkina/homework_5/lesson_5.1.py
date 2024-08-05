# exercise1

my_dict = {
    "tuple": (1, 2, 3, 4, 5),
    "list": ["monday", "tuesday", "wednesday", "thursday", "friday"],
    "dict_1": {"1": "january", "2": "february", "3": "march", "4": "april", "5": "may"},
    "set": {"apple", "banana", "cherry", "date", "watermelon"}
}

# 1 display the last element
print(my_dict["tuple"][-1])

# 2 added  list element
my_dict["list"].append("saturday")

# 3 delete second  list element
my_dict["list"].pop(1)

# 4 add an element with key ('i am a tuple',) and any value
my_dict["dict_1"]["i am a tuple"] = "value_month"

print(my_dict["dict_1"])

# 5 delete  some dict element
remove_value = my_dict["dict_1"].pop("2")

print(remove_value)

# 6 added new set_element
my_dict["set"].add("melon")
print(my_dict["set"])

# 7 delete set_element
my_dict["set"].remove("melon")
print(my_dict["set"])