def fibonaci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


generator = fibonaci()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
