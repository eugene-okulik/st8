words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

key = words.keys()
val = words.values()

list_key = list(key)
list_val = list(val)

numb = 0

while numb <= 3:
    mult = list_key[numb] * list_val[numb]
    numb += 1
    print(mult)
