import sys

sys.set_int_max_str_digits(0)


def fibonacci():
    fib1, fib2 = 0, 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


nums = [5, 200, 1000, 100000]

num = 0
for num, val in enumerate(fibonacci()):
    if num in nums:
        print(f"This is {num} key in Fibonacci with {val} value")
    num += 1
    if num > 100000:
        break
