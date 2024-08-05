numbers = []

for x in range(1, 101):
    if x % 15 == 0:
        numbers.append('FuzzBuzz')
    elif x % 5 == 0:
        numbers.append('Buzz')
    elif x % 3 == 0:
        numbers.append('Fuzz')
    else:
        numbers.append(x)
print(numbers)
