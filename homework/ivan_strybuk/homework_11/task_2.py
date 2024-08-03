PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

t = dict(zip(PRICE_LIST.split()[::2], [int(cost.rstrip('р')) for cost in PRICE_LIST.split()[1::2]]))
print(t)  # {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# ---

a1 = dict(zip([key for val, key in enumerate(PRICE_LIST.split()) if val % 2 == 0],
              [int(str(value).rstrip("р")) for val, value in enumerate(PRICE_LIST.split()) if val % 2 != 0]))
print(a1)  # {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}

# ---
key_d = []
value_d = []

for x, y in enumerate(PRICE_LIST.split()):
    if x % 2 == 0:
        key_d.append(y)
    else:
        value_d.append(int(str(y).rstrip("р")))
print(dict(zip(key_d, value_d)))


# ---
def str_convert(a):
    it = iter(a)  # Получим итератор из списка "list" и выведем каждое значение:
    res_dct = dict([k, int(v[:-1])] for k, v in dict(zip(it, it)).items())
    return res_dct


print(str_convert(PRICE_LIST.split()))
