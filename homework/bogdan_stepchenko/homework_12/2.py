# Создайте универсальный декоратор, который будет управлять тем,
# сколько раз запускается декорируемая функция


# Решение через указание кол-ва вызовов функции во декораторе, а не во wrapper

def execute_several_times(needed_calls):

    def decorator(func):

        def wrapper(*args, **kwargs):

            result = list(map(lambda x: func(*args, **kwargs), range(needed_calls)))
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
    def wrapper(*args, **kwargs):

        needed_calls = kwargs.pop('needed_calls', 1)
        list(map(lambda x: func(*args, **kwargs), range(needed_calls)))

    return wrapper


@deco
def some_func(text):
    print(text)


some_func('Blabla', needed_calls=4)
