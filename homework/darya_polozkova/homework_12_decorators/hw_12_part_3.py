def process(func):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first < 0 or second < 0:
            operation = '*'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        else:
            print('Sorry, mistake occurs!')
        action = func(first, second, operation)
        return action
    return wrapper


@process
def calc(first, second, operation=None):
    if operation == '+':
        return first + second
    elif operation == '*':
        return first * second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    else:
        print('Sorry, mistake occurs!')

print(calc(3,3))
print(calc(1,2))
