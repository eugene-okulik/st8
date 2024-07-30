secret_number = 7

while (guess := int(input("Угадайте цифру: "))) != secret_number:
    print("Попробуйте снова")

print("Поздравляю! Вы угадали!")