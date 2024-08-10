PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

list = PRICE_LIST.split()
#Check with for cycle
#keys = []
#values = []
#for key, value in enumerate(list):
#    if key % 2 == 0:
#        keys.append(value)
#    else:
#        values.append(int(value.strip('р')))
#print(keys, values)

key = [value for key, value in enumerate(list) if key % 2 == 0]
value = [int(str(value).strip("р")) for key, value in enumerate(list) if key % 2 != 0]
prices = zip(key, value)
dict = dict(prices)
print(dict)
