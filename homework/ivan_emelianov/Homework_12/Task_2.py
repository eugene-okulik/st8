def repeat_me(country):
    def decorator(func):
        def wrapper(*args, **kwargs):
            i = 1
            while i <= country:
                func(*args, **kwargs)
                i += 1
        return wrapper
    return decorator


@repeat_me(country=3)
def example(text):
    print(text)


example('print')
