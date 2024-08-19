first_num, second_num = int(input("Ведите число first: ")), int(input("Ведите число second: "))


def decators(func):
    def compare_number(num_a, num_b):
        if num_a < 0 or num_b < 0:
            return func(num_a, num_b, "*")  # если одно из чисел отрицательное - умножение
        elif num_a == num_b:
            return func(num_a, num_b, "+")  # если числа равны - сложения
        elif num_a > num_b:
            return func(num_a, num_b, "-")  # если первое больше второго - вычитание
        elif num_a < num_b:
            return func(num_a, num_b, "/")  # если второе больше первого - деление

    return compare_number


@decators
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second
    elif operation == "*":
        return first * second


print(calc(first_num, second_num))

assert calc(1, 1) == 2  # если числа равны - сложения
assert calc(4, 2) == 2  # если первое больше второго - вычитание
assert calc(5, 10) == 0.5  # если второе больше первого - деление
assert calc(3, -1) == -3  # если одно из чисел отрицательное - умножение
assert calc(-3, 4) == -12  # если одно из чисел отрицательное - умножение
assert calc(-3, -3) == 9  # если одно из чисел отрицательное - умножение
