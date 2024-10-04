import string
from random import randint, choice


def get_random_str():
    random_len = randint(1, 10)
    random_letters = ''.join(choice(string.ascii_letters) for _ in range(random_len))
    return random_letters


def get_random_int():
    random_len = randint(1, 10)
    random_digits = ''.join(choice('1234567890') for _ in range(random_len))
    return int(random_digits)
