"""
Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
 (числа и операция передаются в аргументы функции). Функция выглядит примерно так:

def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif .....
Программа спрашивает у пользователя 2 числа (вне функции)

Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:

если числа равны, то функция calc вызывается с операцией сложения этих чисел
если первое больше второго, то происходит вычитание второго из певрого
если второе больше первого - деление первого на второе
если одно из чисел отрицательное - умножение
"""

"""декоратор запрашивает числа, затем сравнивает их и выбирает операцию"""

#### ВНИМАНИЕ!!!!!!!
"""
Я все сам реализовал но долго не мог понять почему была жалоба на тип данных пока не пошел спрашивать  чат gpt
и он не подсказал, что wrapper нельзя вызывать как функцию внутри wrapper(). 
Но я теперь не понимаю до конца как это работает. Ведь раньше возвращался результат, а сейчас вся функция, которая,
 по идее без предварительного вызова не может подставить аргументы в calc, вместо чего вроде как подставляется как
  ссылка на переменную в памяти... Вместо 3 аргументов, а cal 3 ждет - я запутался и теперь не понимаю че оно работает
"""


def operations(func):
    input1, input2 = int(input("Input the first number: ")), int(input("input the second number: "))
    operations_list = ["+", "-", "/", "*"]

    def wrapper():
        if input1 == input2:
            return func(input1, input2, operations_list[0])
        elif input1 > input2:
            return func(input1, input2, operations_list[1])
        elif input1 < input2 and "-" not in str(input1) and str(input2):
            return func(input1, input2, operations_list[2])
        elif "-" in str(input1) or "-" in str(input2):
            return func(int(input1), int(input2), operations_list[3])

    return wrapper


@operations
def calc(first, second, operation):
    print(first, second, operation)
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == "/":
        return first / second
    elif operation == "*":
        return first * second


print(calc())
