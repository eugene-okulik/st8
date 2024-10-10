from faker import Faker
import random


class FakeData:
    fake = Faker()
    RANDOM_FIRST_NAME = fake.first_name()
    RANDOM_LAST_NAME = fake.last_name()
    RANDOM_BOOK_TITLE = fake.sentence(nb_words=3)
    RANDOM_JOB = fake.job()
    RANDOM_WORD = fake.word
    RANDOM_INT = fake.random_int
    FUTURE_DATE = fake.future_date()
    RANDOM_DATE = fake.date


class Generator:

    @staticmethod
    def rand_int_from_to(from_number: int, to_nuber: int):
        number = random.randint(from_number, to_nuber)
        return number

    @staticmethod
    def memory_size_generator():
        sizes = [1, 2, 4, 8, 12, 16, 24, 32, 64, 128, 256, 512, 1024, 2048]
        return random.choice(sizes)

    @staticmethod
    def memory_type_generator():
        memory_type_list = ["GB", "MB", "KB", "TB"]
        memory_type = random.choice(memory_type_list)
        return memory_type


class NegativeCases(FakeData):
    EMPTY_STRING = ""
    VERY_LONG_STRING = "test" * 300
    STRING_SPACE = "    "
    SYMBOL_IN_STRING = "!@#$%^*&^ SELECT *"
    TOO_HEAVY_INTEGER = 99999999999999999999999999999999999999999999
    ZERO = 0
    NEGATIVE_NUMBER = -99999
    FLOAT = 3.14159265
    BOOL_TRUE = True
    BOOL_FALSE = False
    NONE = None
    OBJECT = {}
    LIST = []
