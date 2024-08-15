# Создайте универсальный декоратор, который будет управлять тем,
# сколько раз запускается декорируемая функция


# Решение через указание кол-ва вызовов функции во декораторе, а не во wrapper

def execute_several_times(needed_calls):

    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            while count < needed_calls:
                count += 1
                print(f'Number of function\' execution: {count}')
                result = func(*args, **kwargs)
                print('-' * 20)
            return result

        return wrapper

    return decorator


@execute_several_times(needed_calls=4)
def some_func(text):
    print(text)


some_func('Hello world')


# Решение через указание кол-ва вызовов функции во wrapper, а не в декораторе - и
# как следствие - в параметрах фунцкции при вызове


def deco(func):
    def wrapper(text, needed_calls):
        for i in range(needed_calls):
            func(text)
    return wrapper


@deco
def some_func(text):
    print(text)


some_func('Blabla', needed_calls=4)
