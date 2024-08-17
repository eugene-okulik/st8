def decator(func):
    def inner(*args):
        func(*args)
        print("finished")

    return inner


@decator
def exampl(text):
    print(text)


exampl("print me")
