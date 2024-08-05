PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_dict = {line.split()[0]: int(line.split()[1][:-1]) for line in PRICE_LIST.split('\n')}
print(new_dict)
