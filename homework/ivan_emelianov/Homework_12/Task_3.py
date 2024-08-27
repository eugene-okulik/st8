a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = "+"


def operation_manager(calc_func):
    def wrapper(first, second, operation):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'

        return calc_func(first, second, operation)

    return wrapper


@operation_manager
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


print(calc(a, b, c))
