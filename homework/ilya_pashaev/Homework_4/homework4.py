name = input("Как вас зовут? ")
item = input("Что вы хотите купить? ")
price = float(input("Сколько это стоит? "))
available_money = float(input("Сколько у вас есть? "))
monthly_savings = float(input("Сколько можете отложить в месяц? "))
needed_money = price - available_money
can_buy = needed_money <= 0
months_left = max(0, needed_money / monthly_savings)
print(f"Привет, {name}. На покупку {item} тебе не хватает {needed_money if needed_money > 0 else 0:.2f}")
print(f"Возможность совершения покупки: {can_buy}")
print(f"До покупки осталось {int(months_left)} месяцев")
