user_name = input('Как вас зовут?\n')
user_goal = input('Что вы хотите купить?\n')
goal_price = float(input('Cколько это стоит?\n'))
user_money = float(input('Cколько у вас есть?\n'))
monthly_reserve = float(input('Сколько можете отложить в месяц?\n'))
insufficient = float(goal_price - user_money)
deal = user_money >= goal_price
end_goal_date = goal_price / monthly_reserve
text_result = ('Привет, {0}. На покупку {1} тебе не хватает {2}.'
               'Возможность совершения покупки: {3}.'
               'До покупки осталось {4} месяцев')
print(text_result.format(user_name, user_goal, insufficient, deal, end_goal_date))