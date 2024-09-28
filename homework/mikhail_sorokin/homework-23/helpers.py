from faker import Faker


class FakeData:
    fake = Faker()
    RANDOM_FIRST_NAME = fake.first_name()
    RANDOM_LAST_NAME = fake.last_name()
    RANDOM_BOOK_TITLE = fake.sentence(nb_words=3)
    RANDOM_JOB = fake.job()
    RANDOM_WORD = fake.word
    RANDOM_INT = fake.random_int
    FUTURE_DATE = fake.future_date()
    FAKE_DATE = fake.date


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
