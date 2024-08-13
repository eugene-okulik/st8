number = 5

while True:
    input_number = int(input("Угадайте цифру: "))
    if input_number == number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("попробуйте снова")
