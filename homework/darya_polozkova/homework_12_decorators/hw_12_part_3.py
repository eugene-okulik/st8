first = int(input('Enter your first number: '))
second = int(input('Enter your second number: '))


def process(func):
    def wrapper(*args, **kwargs):
        if first == second:
            operation = first + second
        elif first < 0 or second < 0:
            operation = first * second
        elif first > second:
            operation = first - second
        elif first < second:
            operation = first / second
        else:
            print('Sorry, mistake occurs!')
        return operation
    return wrapper


@process
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        print('Sorry, I do not know such operation')

print(calc(first,second))
