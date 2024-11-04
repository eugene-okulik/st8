import random
import string


def random_name(length=8):
    name = ''.join(random.choices(string.ascii_letters, k=length))
    return name


def random_email(length=8):
    postfix = '@test.com'
    email = ''.join(random.choices(string.ascii_letters, k=length))
    return email + postfix


def random_password(length=8):
    letters = ''.join(random.choices(string.ascii_letters, k=length))
    digits = ''.join(random.choices(string.digits, k=length))
    password = letters.capitalize() + digits
    return password
