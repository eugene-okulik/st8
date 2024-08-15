import sys
sys.set_int_max_str_digits(0)


def fibonachi(max_n):
    a = 0
    b = 1
    wanted_numbers = [5, 200, 1000, 100000]
    for n in range(max_n):
        fib = a + b
        a = b
        b = fib

        fib_number = n + 3
        if fib_number in wanted_numbers:
            yield fib

list_fib = fibonachi(100001)
print(list(list_fib))
