# Создайте универсальный декоратор, который можно будет
# применить к любой функции. Декоратор должен делать следующее:
# он должен распечатывать слово "finished" после выполнения декорированной функции.


def finisher(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('finished')
        return result

    return wrapper


@finisher
def some_func(text):
    print(text)


some_func('Hello world')
