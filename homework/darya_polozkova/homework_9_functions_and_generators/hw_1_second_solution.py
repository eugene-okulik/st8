import sys

sys.set_int_max_str_digits(0)


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        c = a + b
        a = b
        b = c


print_numbers = [5, 200, 1000, 10000]

count = 0
for count, num in enumerate(fibonacci()):
    if count in print_numbers:
        print(f'Finally I got {count} element in Fibonacci with {num} value')
    count += 1
    if count > 100000:
        break
