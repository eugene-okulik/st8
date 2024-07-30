import sys

sys.set_int_max_str_digits(0)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()

fifth_number = None
for i in range(5):
    fifth_number = next(fib_gen)
print(f'Пятое число Фибоначчи: {fifth_number}')

fib_gen = fibonacci_generator()
for i in range(200):
    two_hundredth_number = next(fib_gen)
print(f'Двухсотое число Фибоначчи: {two_hundredth_number}')

fib_gen = fibonacci_generator()
for i in range(1000):
    thousandth_number = next(fib_gen)
print(f'Тысячное число Фибоначчи: {thousandth_number}')

fib_gen = fibonacci_generator()
for i in range(100000):
    hundred_thousandth_number = next(fib_gen)
print(f'Стотысячное число Фибоначчи: {hundred_thousandth_number}')


# На счет второго варианта не уверен, но умещается в меньшее количество строк)


def fib(f):
    a, b = 0, 1
    for __ in range(f):
        yield a
        a, b = b, a + b


result = list(fib(100001))
# print(result[4], '\n', result[199], '\n', result[999], '\n', result[99999])
