# При помощи генераторов (list и/или dict comprehension)
# превратите этот текст в словарь такого вида:
#
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

list_price_list = PRICE_LIST.split()

names = [list_price_list[x] for x in range(0, len(list_price_list)) if x % 2 == 0]
prices = [list_price_list[x] for x in range(0, len(list_price_list)) if x % 2 != 0]

int_prices = [int(i.rstrip('р')) for i in prices]

zipped_dict = dict(zip(names, int_prices))
print(zipped_dict)
