import sys
sys.set_int_max_str_digits(0)

def fibonachi():
    a = 0
    b = 1
    while True:
        fib = a + b
        a = b
        b = fib
        yield fib


wanted_numbers = [5, 200, 1000, 100000]
last_number = wanted_numbers[len(wanted_numbers) - 1]
print(f"last number: {last_number}")
counter = 0
for number in fibonachi():
    if counter in wanted_numbers:
        print(number)
    counter += 1
    if counter >= last_number:
        break
