def repeat_me(func):
    def wrapper(*args):
        i = 1
        while i <= 2:
            func(*args)
            i += 1
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print')
