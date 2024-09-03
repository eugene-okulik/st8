def choose_operation(func):
   def wrapper(first, second):
        if first == second:
            operation = '+'
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
def calc(first, second,operation=None):
   if operation == '+':
        return first + second

   elif operation == '*':
       return first * second
   elif operation == '-':
       return first - second
   elif operation == '/':
       return first / second
   else:
       print('sorry,mistake') 

print(calc(10,10))
print(calc(2,15))