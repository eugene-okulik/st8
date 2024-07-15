name = input('What is your name: ')
purchase = input('What do you want to buy: ')
cost = float(input('How much does it cost: '))
have = float(input('How much do you have: '))
set_aside = float(input('How much can you set aside each month: '))

remaining = cost - have
can_purchase = have >= cost
months_to_buy = (cost - have) / set_aside

print(f"Привет, {name}. На покупку {purchase} тебе не хватает {remaining: }")
print(f"Возможность совершения покупки: {bool(can_purchase)}")
print(f"До покупки осталось {int(months_to_buy)} месяцев")
