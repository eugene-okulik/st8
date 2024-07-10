name = input("Как вас зовут? ")
dream = input("Что вы хотите купить? ")
price = float(input("Сколько это стоит? "))
money = float(input("Сколько у вас есть? "))
debt = float(input("Сколько можете отложить в месяц? "))

needed = price-money
months = needed/debt

aim = (
    f"Привет, {name}. На твою мечту - {dream} не хватает {price-money}. "
       f"Можно ли купить сейчас? - Ответ: {money == price}. До исполнения мечты осталось месяцев: {needed/debt}"
       )

print(aim)

