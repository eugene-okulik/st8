import sys

sys.set_int_max_str_digits(0)

def fibonacci():
    fib1, fib2 = 0, 1
    while True:
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1

for num, val in enumerate(fibonacci()):
    number = num + 1
    nums = [5, 200, 1000, 100000]
    for i in nums:
        if number == i:
            print(f"This is {num} key in Fibonacci with {val} value")
            break
