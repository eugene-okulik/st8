def repeat_me(func):
    def repeat_text(*args, count=1):
        for _ in range(0, count):
            func(*args)

    return repeat_text


@repeat_me
def example(text):
    print(text)


example('print me', count=3)
