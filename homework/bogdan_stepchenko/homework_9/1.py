# Напишите функцию-генератор, которая генерирует список чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число


import sys
sys.set_int_max_str_digits(0)


def fibonacci_generator():
    previous, current = 0, 1
    while True:
        yield previous
        previous, current = current, current + previous


for num, val in enumerate(fibonacci_generator()):
    number = num + 1    # +1 cause enumerate starts from 0
    nums = [5, 200, 1000, 100000]
    for i in nums:
        if number == i:
            print(f"The number №{i} in Fibonacci' list is: {val}")


#   It's possible to do it that way, but speed of progressing is unacceptable

list_fib = list(enumerate(fibonacci_generator()))
print(f"The number №5 in Fibonacci' list is: {list_fib[4][1]}")
print(f"The number №200 in Fibonacci' list is: {list_fib[199][1]}")
print(f"The number №1000 in Fibonacci' list is: {list_fib[999][1]}")
print(f"The number №100.000 in Fibonacci' list is: {list_fib[99999][1]}")
