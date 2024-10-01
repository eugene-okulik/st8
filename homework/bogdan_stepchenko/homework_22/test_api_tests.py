import string
from random import randint, choice
from homework.bogdan_stepchenko.homework_21.api_client import APIClient
import pytest
import allure


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


# фикстура для создания клиента и обьекта внутри клиента
@pytest.fixture(scope='function')
def api_client_with_object():
    api_client = APIClient('http://167.172.172.115:52353/object')
    created_object = api_client.create_object(get_random_str(), get_random_int(), get_random_int(), get_random_str())

    assert created_object is not None, "Failed to create the object"

    yield api_client, created_object
    api_client.delete_object(created_object["id"])


@allure.feature('Homework #22 tests')
@pytest.mark.usefixtures("start_end")
class TestAPIClient:

    @allure.title('API creation object test')
    def test_creation_object(self):
        api_client = APIClient('http://167.172.172.115:52353/object')
        name = get_random_str()
        year = get_random_int()
        price = get_random_int()
        cpu_model = get_random_str()
        created_object = api_client.create_object(name, year, price, cpu_model)

        assert created_object is not None, "Failed to create the object"
        assert created_object['name'] == name
        assert created_object['data']['year'] == year
        assert created_object['data']['price'] == price
        assert created_object['data']['CPU model'] == cpu_model

    @allure.title('API deletion test')
    def test_deletion_object(self):
        api_client = APIClient('http://167.172.172.115:52353/object')
        created_object = api_client.create_object(get_random_str(), get_random_int(),
                                                  get_random_int(), get_random_str())
        created_object_id = created_object['id']
        deleted_response = api_client.delete_object(created_object_id)
        assert deleted_response is True, 'Object was deleted successfully'

        fetch_deleted_object = api_client.get_exact_object(created_object_id)
        assert fetch_deleted_object is None or fetch_deleted_object == {}

    @allure.title('API getting exact object test')
    @pytest.mark.smoke
    def test_get_exact_object(self, api_client_with_object):
        api_client, created_object = api_client_with_object
        fetched_object = api_client.get_exact_object(created_object['id'])
        assert fetched_object['id'] == created_object['id']
        assert fetched_object['name'] == created_object['name']
        assert fetched_object['data'] == created_object['data']

    @allure.title('API updating object with PATCH test')
    @pytest.mark.critical
    def test_update_object_with_patch(self, api_client_with_object):
        api_client, created_object = api_client_with_object
        new_name = get_random_str()
        updated_object = api_client.update_object_with_patch(created_object['id'], new_name)
        assert updated_object['name'] == new_name

    @allure.title('API updating object with PUT')
    def test_update_object_with_put(self, api_client_with_object):
        api_client, created_object = api_client_with_object
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
