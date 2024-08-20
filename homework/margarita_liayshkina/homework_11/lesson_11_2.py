PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

general_price = PRICE_LIST.split("\n")
# print(general_price)

price_dict = {product_info.split()[0]: int(product_info.split()[1][:-1]) for product_info in general_price}
print(price_dict)
