def finish_me(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("finished")
        return result

    return wrapper


@finish_me
def example(text):
    print(text)


example("print me")
