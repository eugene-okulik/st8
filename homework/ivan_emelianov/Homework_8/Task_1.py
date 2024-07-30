hidden_num = 3

while True:
    enter_num = int(input('Введи число: '))
    simile = hidden_num == enter_num
    if simile:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('Попробуйте снова')
