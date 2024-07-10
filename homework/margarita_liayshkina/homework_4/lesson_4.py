# Напишите программу, которая спрашивает:

# как вас зовут?
# что вы хотите купить?
# сколько это стоит?
# сколько у вас есть?
# сколько можете отложить в месяц?


your_name = input("What is your name?: ")
desired_acquisition = input("What do you want to buy?: ")
cost = float(input("How match does it cost?: "))
your_many = float(input("How match many do you have?: "))
monthly_savings = float(input("How much money can you save per month?: "))
money_need = cost - your_many
months_to_save = money_need / monthly_savings

print(f"Hello, {your_name}. You are short of {money_need} for the purchase to {desired_acquisition} ")
print(f"Possibility of making the purchase now: {money_need <= 0}")
print(f"Months remaining until purchase: {months_to_save} ")
