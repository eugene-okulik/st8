# Задание №1 - "Угадайка"
# Создайте такую программу:
# Программа хранит какую-либо цифру в переменной.
# Программа просит пользователя угадать цифру. Пользователь вводит цифру.
# Программа сравнивает цифру с той, что хранится в переменной.
# Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
# Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
# Т.е. программа не завершается пока пользователь не угадает цифру.
#
# Подсказка: задание выполняется с помощью цикла while


def guess_number():
    target = 30
    user_choice = int(input('Please, enter your number: '))

    while user_choice != target:
        print('You didn\'t guess right! Please, try again.')
        user_choice = int(input('Please, enter your number: '))
    print(f'Finally! You guess right! Hidden number was: {target}!')


guess_number()
