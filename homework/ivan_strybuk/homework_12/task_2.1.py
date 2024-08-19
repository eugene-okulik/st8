def counted(count=1):
    def real_decoration(func):
        def repeats_text(*args):
            for _ in range(0, count):
                func(*args)

        return repeats_text

    return real_decoration


@counted(count=4)
def sample(text):
    print(text)


sample('print me')
