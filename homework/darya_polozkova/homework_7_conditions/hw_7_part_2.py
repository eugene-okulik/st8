my_range = range(1,101)
for x in my_range:
    if x % 3 == 0 and x % 5 == 0:
        print('FuzzBuzz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0:
        print('Fuzz')
    else:
        print(x)
