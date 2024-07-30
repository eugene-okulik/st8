import sys

sys.set_int_max_str_digits(0)


def f():
    n0 = 0
    n1 = 1
    while True:
        yield n0
        sum_n = n0 + n1
        n0, n1 = n1, sum_n


target_number = [5, 200, 1000, 100_000]

count = 0
for count, num in enumerate(f()):
    if count in target_number:
        print(num)
    count += 1
    if count > 100000:
        break
