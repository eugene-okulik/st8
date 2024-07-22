for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FuzzBuzz")
    elif i % 3 == 0:
        print("fuzz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
