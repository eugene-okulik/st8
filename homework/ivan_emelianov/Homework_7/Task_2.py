seq_num = range(1, 101)

for num in seq_num:
    if num % 3 == 0 and num % 5 == 0:
        print('FuzzBuzz')
    elif num % 3 == 0:
        print('Fuzz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
