#  Игра угадай число.

import random

user_value = input("Загадано число от 1 до 10. Попробуй угадать что за число я загадал:\n")
hidden_number = random.randint(1, 10)

while True:
    if int(user_value) == hidden_number:
        print(f"Поздравляю! Вы угадали {hidden_number} правильный ответ.\n")
        break
    else:
        user_value = input("Не угодал. Попробуй снова:\n")
        continue

#  version_2 с моржами пока pass
