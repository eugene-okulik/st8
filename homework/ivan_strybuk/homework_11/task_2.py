PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

t = dict(zip(PRICE_LIST.split()[::2], PRICE_LIST.split()[1::2]))
print(t)
# ---

a1 = dict(zip([key for val, key in enumerate(PRICE_LIST.split()) if val % 2 == 0],
              [value for val, value in enumerate(PRICE_LIST.split()) if val % 2 != 0]))
print(a1)

# ---
key_d = []
value_d = []

for x, y in enumerate(PRICE_LIST.split()):
    if x % 2 == 0:
        key_d.append(y)
    else:
        value_d.append(y)
print(dict(zip(key_d, value_d)))


# ---
def Convert(a):
    it = iter(a)  # Получим итератор из списка "list" и выведем каждое значение:
    res_dct = dict(zip(it, it))
    return res_dct


print(Convert(PRICE_LIST.split()))
