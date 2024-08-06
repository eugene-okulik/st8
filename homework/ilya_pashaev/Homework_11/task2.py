PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

split_words = PRICE_LIST.split('\n')
print(split_words)

price_dict = {item.split()[0]: int(item.split()[1][:-1])
              for item in split_words}
print(price_dict)
