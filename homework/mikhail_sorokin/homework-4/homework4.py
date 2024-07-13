
name = input("What is you're name ? ")

goods = input("What do you want to buy ? ")

price = float(input("how much it cost ? "))

wallet_amount = float(input("how much money do you hove ? "))

saved_money = float(input(" how much do you can save money per months ? "))

not_enough = price - wallet_amount

left_months = not_enough / saved_money

opportunity = f"Possibility of making a purchase: {price <= wallet_amount}"

greeting = f"Hello, {name}. You don't have {not_enough} to buy a {goods}"

needed = f"{int(left_months + 0.999)} months left until purchase"

print(opportunity)
print(greeting)
print(needed)
