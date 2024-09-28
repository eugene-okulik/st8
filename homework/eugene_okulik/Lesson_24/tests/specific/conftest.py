import pytest


@pytest.fixture()
def for_simple():
    return 'Simple'


@pytest.fixture(scope='session')
def greet():
    print('Hello Spec')
    yield None
    print('Bye Spec')
