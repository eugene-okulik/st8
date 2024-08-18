def final(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('finish')
        return result

    return wrapper
@final
def example(text):
    print(text)

example('print me')
