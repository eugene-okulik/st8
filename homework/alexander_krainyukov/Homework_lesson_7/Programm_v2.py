my_range = range(1, 101)
for num in my_range:
    if num % 3 == 0 and num % 5 == 0:
        print('FuzzBuzz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0:
        print('Fuzz')
    else:
        print(num)
