from math import ceil

# Напишите программу, которая спрашивает:
#
# как вас зовут?
# что вы хотите купить?
# сколько это стоит?
# сколько у вас есть?
# сколько можете отложить в месяц?
# В результате программа должна распечатать, например, такое:
#
# Привет, Петя. На покупку Ferrari тебе не хватает 1000000
# Возможность совершения покупки: False
# До покупки осталось 200 месяцев

name = input('Представьтесь, пожалуйста. \n')
buy_target = input('Что бы вы хотели купить? \n')
target_price = int(input(f'Сколько стоит {buy_target}? \n'))
your_wallet = int(input('Сколько денег у вас есть? \n'))

if target_price > your_wallet:
    monthly_piggy_bank = int(input('Сколько денег вы можете отложить в месяц? \n'))
    needed_money = target_price - your_wallet
    print(f'Привет, {name}! На покупку {buy_target} тебе не хватает {target_price - your_wallet}')
    print(f'Возможность совершения покупки: {your_wallet > target_price}')
    print(f"До покупки осталось: {ceil(needed_money / monthly_piggy_bank)} месяцев")
else:
    print(f'Привет, {name}! Тебе хватает денег на покупку {buy_target}! '
          f'После покупки у тебя останется {your_wallet - target_price}')
    print(f'Возможность совершения покупки: {your_wallet > target_price}')
