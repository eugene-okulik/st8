name_input = input("Как вас зовут? ")
item_input = input("Что вы хотите купить? ")
price_input = float(input("Cколько это стоит? "))
amount_input = float(input("Cколько у вас есть? "))
save_money_input = float(input("Cколько можете отложить в месяц? "))

lack = price_input - amount_input
purchase = bool(0 >= lack)
left = lack / save_money_input

print(f'Привет {name_input}. На покупку {item_input} тебе не хватает {round(lack)}')
print(f'Возможность совершить покупку {purchase}')
print(f'До покупки осталось {round(left)} месяцев')
