def repeat_me(function):

    def wrapper(count, *args, **kwargs):
        for i in range(0, count):
            function(*args, **kwargs)

    return wrapper


@repeat_me
def example(text):
    print(text)


example(2, "print me")
