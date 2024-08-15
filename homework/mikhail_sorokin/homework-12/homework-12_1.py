"""
Создайте универсальный декоратор, который можно будет применить к любой функции.
 Декоратор должен делать следующее: он должен распечатывать слово "finished"после выполнения декорированной функции.

Код, использующий этот декоратор может выглядеть, например, так:

@finish_me
def example(text):
    print(text)

example('print me')
В результате работы будет такое:

print me

finished
"""


def finish_text(func):
    func()
    print('finished')


@finish_text
def example():
    c = 3 * 3
    print(f"result = {c}")
