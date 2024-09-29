from pydantic import Field, BaseModel, ValidationError
from homework.bogdan_stepchenko.homework_21.api_client import APIClient
from homework.bogdan_stepchenko.homework_22.test_api_tests import get_random_str, get_random_int
import pytest
import allure


class DataModel(BaseModel):
    year: int
    price: str
    CPU_model: str = Field(alias='CPU model')


class ObjectModel(BaseModel):
    name: str
    data: DataModel


class DeletionResponseModel(BaseModel):
    success: bool


@allure.feature('Homework #23 tests')
@pytest.mark.usefixtures("start_end")
class TestAPIClient:

    @allure.title('Creation object test')
    @allure.description('That test is about creation object for following tests')
    @allure.severity('Critical')
    def test_creation_object(self):
        api_client = APIClient('http://167.172.172.115:52353/object')
        name = get_random_str()
        year = get_random_int()
        price = get_random_int()
        cpu_model = get_random_str()
        created_object = api_client.create_object(name, year, price, cpu_model)
        try:
            validated_object = ObjectModel(**created_object)
            assert created_object is not None, "Failed to create the object"
            assert validated_object.name == name
            assert validated_object.data.year == year
            assert validated_object.data.price == price
            assert validated_object.data.CPU_model == cpu_model
        except ValidationError as error:
            pytest.fail(f'Validation failed: {error}')

    @allure.title('Deletion object test')
    @allure.severity('Critical')
    def test_deletion_object(self):
        api_client = APIClient('http://167.172.172.115:52353/object')
        created_object = api_client.create_object(get_random_str(), get_random_int(),
                                                  get_random_int(), get_random_str())
        created_object_id = created_object['id']
        deleted_response = api_client.delete_object(created_object_id)
        try:
            validated_response = DeletionResponseModel(**{'success': deleted_response})
            assert validated_response.success is True, 'Object was deleted successfully'
        except ValidationError as error:
            pytest.fail(f'Validation failed: {error}')
        fetch_deleted_object = api_client.get_exact_object(created_object_id)
        assert fetch_deleted_object is None or fetch_deleted_object == {}

    @allure.title('Getting exact object test')
    @allure.severity('Minor')
    @pytest.mark.smoke
    def test_get_exact_object(self, api_client_with_object):
        api_client, created_object = api_client_with_object
        fetched_object = api_client.get_exact_object(created_object['id'])
        assert fetched_object['id'] == created_object['id']
        assert fetched_object['name'] == created_object['name']
        assert fetched_object['data'] == created_object['data']

    @allure.title('Updating object with PATCH test')
    @pytest.mark.critical
    def test_update_object_with_patch(self, api_client_with_object):
        api_client, created_object = api_client_with_object
        new_name = get_random_str()
        updated_object = api_client.update_object_with_patch(created_object['id'], new_name)
        assert updated_object['name'] == new_name

    @allure.title('Updating object with PUT test')
    @pytest.mark.parametrize('name, expected_status', [('ABCdef', 200), ('   ', 200), ('!@#$%', 200)],
                             ids=['letters', 'spaces', 'symbols']
                             )
    @pytest.mark.parametrize('year, expected_status_year', [(1993, 200), [2024, 200]], ids=['old', 'new'])
    @pytest.mark.parametrize('price', [1, 100000], ids=['small', 'huge'])
    def test_update_object_with_put(self, api_client_with_object, name, year, price,
                                    expected_status, expected_status_year):
        api_client, created_object = api_client_with_object
        new_name = name
        new_year = year
        new_price = price
        new_cpu = get_random_str()
        updated_object = api_client.update_object_with_put(
            created_object['id'], new_name, new_year, new_price, new_cpu)
        assert updated_object['name'] == new_name
        assert updated_object['data']['year'] == new_year
        assert updated_object['data']['price'] == new_price
        assert updated_object['data']['CPU model'] == new_cpu
