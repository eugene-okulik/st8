my_range = range(1,101)
for _ in my_range:
    if _ % 3 == 0 and _ % 5 == 0:
        print('FuzzBuzz')
    elif _ % 5 == 0:
        print('Buzz')
    elif _ % 3 == 0:
        print('Fuzz')
    else:
        print(_)
