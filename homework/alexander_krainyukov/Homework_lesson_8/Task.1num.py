num_program = 77
while True:
    select_num = int(input('Write any number: '))
    if select_num != num_program:
        print('“попробуйте снова”')
        continue
    elif select_num == num_program:
        print('“Поздравляю! Вы угадали!”')
        break
