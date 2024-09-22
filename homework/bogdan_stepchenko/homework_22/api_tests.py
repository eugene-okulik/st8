import string
from random import randint, choice
from homework.bogdan_stepchenko.homework_21.api_client import APIClient
import pytest


# функция для генерации рандомной строки
def get_random_str():
    random_len = randint(1, 10)
    random_letters = ''.join(choice(string.ascii_letters) for _ in range(random_len))
    return random_letters


# функция для генерации рандомного числа
def get_random_int():
    random_len = randint(1, 10)
    random_digits = ''.join(choice('1234567890') for _ in range(random_len))
    return int(random_digits)


# фикстура для принта текста до и после ВСЕХ автотестов класса
@pytest.fixture(scope='class')
def start_end():
    print('Start testing.....')
    yield
    print('Testing was completed!')


# фикстура для создания клиента
@pytest.fixture(scope='function')
def api_client():
    return APIClient('https://api.restful-api.dev/objects')


# фикстура для создания объекта внутри клиента
@pytest.fixture(scope='function')
def created_object(api_client):
    new_object = api_client.create_object(get_random_str(), get_random_int(), get_random_int(), get_random_str())
    yield new_object
    api_client.delete_object(new_object["id"])


@pytest.mark.usefixtures("start_end")
class TestAPIClient:

    @pytest.mark.smoke
    def test_get_exact_object(self, api_client, created_object):
        fetched_object = api_client.get_exact_object(created_object['id'])
        assert fetched_object['id'] == created_object['id']
        assert fetched_object['name'] == created_object['name']
        assert fetched_object['data'] == created_object['data']

    @pytest.mark.critical
    def test_update_object_with_patch(self, api_client, created_object):
        new_name = get_random_str()
        updated_object = api_client.update_object_with_patch(created_object['id'], new_name)
        assert updated_object['name'] == new_name

    def test_update_object_with_put(self, api_client, created_object):
        new_name = get_random_str()
        new_year = get_random_int()
        new_price = get_random_int()
        new_cpu = get_random_str()
        updated_object = api_client.update_object_with_put(
            created_object['id'], new_name, new_year, new_price, new_cpu)
        assert updated_object['name'] == new_name
        assert updated_object['data']['year'] == new_year
        assert updated_object['data']['price'] == new_price
        assert updated_object['data']['CPU model'] == new_cpu
