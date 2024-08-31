from typing import Any, Literal, List, Tuple


def calc(x: int, y: int) -> float:
    return x / y


result = calc(4, 2)


def make_dict(key: str | int | tuple | bool | float, value: Any) -> dict:
    return {key: value}


my_dict = make_dict((1, 4, 6), 'werwer')


class Flower:
    def __init__(self, price, color):
        self.price = price
        self.color = color


def show_flower_price(some_flower: Flower):
    print(some_flower.color)


rose = Flower(12, 'white')
tulip = Flower(5, 'Black')

show_flower_price(rose)


def hi_or_bye(word: Literal['hi', 'by']):
    if word == 'hi':
        print('Hello')
    elif word == 'bye':
        print('good bye')
    else:
        print('give me hi or bye')


hi_or_bye('hi')


def sum_all(list_of_int: List[int] | Tuple[int, int, int]):
    return sum(list_of_int)


sum_all((1, 4, 6))
sum_all([1, 4, 6])
