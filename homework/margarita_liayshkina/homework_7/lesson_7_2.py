for i in range(1, 101):
    x1 = i % 3
    x2 = i % 5

    if x2 == 0 and x1 == 0:
        print("FUZZBUZZ")
    elif x1 == 0:
        print("FUZZ")
    elif x2 == 0:
        print("BUZZ")

    else:
        print(i)
