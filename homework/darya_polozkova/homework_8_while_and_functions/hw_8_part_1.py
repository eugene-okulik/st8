user_number = int(input('Угадай, что я загадала?: '))

while True:
    number = 111
    if user_number != number:
        print('Попробуй снова!')
        user_number = int(input('Введи новое число: '))
    else:
        print('Поздравляю! Вы угадали!')
        break
