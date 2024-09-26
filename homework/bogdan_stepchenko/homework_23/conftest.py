import pytest
from homework.bogdan_stepchenko.homework_21.api_client import APIClient
from homework.bogdan_stepchenko.homework_22.api_tests import get_random_str, get_random_int


# фикстура для принта текста до и после ВСЕХ автотестов класса
@pytest.fixture(scope='class')
def start_end():
    print('Start testing.....')
    yield
    print('Testing was completed!')


# фикстура для создания клиента и обьекта внутри клиента
@pytest.fixture(scope='function')
def api_client_with_object():
    api_client = APIClient('http://167.172.172.115:52353/object')
    created_object = api_client.create_object(get_random_str(), get_random_int(), get_random_int(), get_random_str())

    assert created_object is not None, "Failed to create the object"

    yield api_client, created_object
    api_client.delete_object(created_object["id"])
