"""
Программа спрашивает: имя, что хотите купить, стоимость,
доступные средства и количество денег которое возможно отлажить.

В результате программа должна распечатать:
- Привет, Петя. На покупку Ferrari тебе не хватает 1000000
- Возможность совершения покупки: False
- До покупки осталось 200 месяцев
"""

name = input("Как вас зовут? ")
target = input("Что вы хотите купить? ")
cost_target = float(input("Cколько это стоит? "))
available_cash = float(input("Cколько у вас есть? "))
available_cash_for_deposit = float(input("Cколько можете отложить в месяц? "))

calculation = cost_target - available_cash
accumulate_cash = int(calculation / available_cash_for_deposit)
buy = available_cash >= cost_target

print(f"Привет, {name}. На покупку {target} тебе не хватает", calculation)
print(f"Возможность совершения покупки:", buy)
print(f"До покупки осталось", accumulate_cash, "месяцев")
