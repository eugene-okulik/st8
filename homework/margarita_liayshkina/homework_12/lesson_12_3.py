def operation_decor(function):

    def wrapper(first, second, operation=None):
        if first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        elif second > first:
            operation = "/"
        elif  first < 0 or second < 0:
            operation = "*"
        return function(first,second,operation)
        
    return wrapper


@operation_decor
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second
    elif operation == "*":
        return  first * second
    else:
        return "Unknown operation"


first = float(input("Enter you number:"))
second = float(input("Enter you number:"))


result = calc(first, second )
print(f"Result operation: {result}")
