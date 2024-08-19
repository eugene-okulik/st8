def repeat_me(func):
    def times(*args, **kwargs):
        times = kwargs.pop('count')
        for _ in range(times):
            func(*args, **kwargs)

    return times


@repeat_me
def example(text):
    print(text)


example('print me', count=12)
