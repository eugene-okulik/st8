import collections

# {'Минск': ['мясо', 'молоко'], 'Москва': ['спорт'], 'Брест': ['хлеб','товары']}


with open('shops.txt') as shops_file:
    shops = shops_file.read()


shops_list = shops.splitlines()
print(shops_list)

shops_dict = collections.defaultdict(list)
for line in shops_list:
    categ, shop = line.split(':')  # ['мясо', 'Минск']
    # if not shop in shops_dict:
    #     shops_dict[shop] = [categ]
    #     # shops_dict[shop] = []
    # else:
    shops_dict[shop].append(categ)

print(shops_dict)
