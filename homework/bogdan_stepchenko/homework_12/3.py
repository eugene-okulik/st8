# Напишите программу: Есть функция которая делает одну из
# арифметических операций с переданными ей числами (числа и операция
# передаются в аргументы функции). Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение


def choose_operation(func):

    def wrapper(first, second):
        if first == second:
            operation = "+"
        elif second < 0 or first < 0:
            operation = '*'
        elif first > second:
            operation = '-'
        else:
            operation = '/'
        result = func(first, second, operation)
        return result

    return wrapper


@choose_operation
def some_func(first, second, operation=None):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second == 0:
            print('Error: it is not possible to divide by 0')
        return first / second
    else:
        print('Error: operation is unknown')


print(some_func(10, 10))
print(some_func(10, 2))
print(some_func(10, 40))
print(some_func(10, -10))
