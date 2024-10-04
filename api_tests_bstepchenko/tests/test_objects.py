import pytest
import allure
from api_tests_bstepchenko.data import constants
from api_tests_bstepchenko.endpoints.get_object import GetObject
from api_tests_bstepchenko.endpoints.post_object import PostObject
from api_tests_bstepchenko.endpoints.put_object import PutObject
from api_tests_bstepchenko.endpoints.patch_object import PatchObject
from api_tests_bstepchenko.endpoints.del_object import DeleteObject


@allure.feature('Homework #23 tests')
@pytest.mark.usefixtures("start_end")
class TestAPIClient:

    @allure.title('Creation object test')
    @allure.description('That test is about creation object for following tests')
    @allure.severity('Critical')
    def test_creation_object(self):
        post_obj_endpoint = PostObject()
        post_obj_endpoint.post_new_object()
        post_obj_endpoint.check_response_code_is_(200)
        post_obj_endpoint.check_updated_name()
        post_obj_endpoint.check_updated_year()
        post_obj_endpoint.check_updated_price()
        post_obj_endpoint.check_updated_cpu_model()

    @allure.title('Getting exact object test')
    @allure.severity('Minor')
    def test_get_exact_object(self, create_and_delete_object):
        get_obj_endpoint = GetObject()
        get_obj_endpoint.get_object_by_id(create_and_delete_object)
        get_obj_endpoint.check_response_code_is_(200)

    @allure.title('Updating object with PUT test')
    @pytest.mark.parametrize('name', ['ABCdef', '   ', '!@#$%'],
                             ids=['letters', 'spaces', 'symbols']
                             )
    @pytest.mark.parametrize('year', [1993, [2024]], ids=['old', 'new'])
    @pytest.mark.parametrize('price', [1, 100000], ids=['small', 'huge'])
    def test_update_object_with_put(self, create_and_delete_object, name, price, year):
        put_obj_endpoint = PutObject()
        payload = constants.PAYLOAD_FOR_OBJECT
        payload['name'] = name
        payload['data']['price'] = price
        payload['data']['year'] = year
        put_obj_endpoint.update_obj_with_put(create_and_delete_object, payload)
        put_obj_endpoint.check_response_code_is_(200)
        put_obj_endpoint.check_updated_name()
        put_obj_endpoint.check_updated_year()
        put_obj_endpoint.check_updated_price()
        put_obj_endpoint.check_updated_cpu_model()

    @allure.title('Updating object with PATCH test')
    def test_update_object_with_patch(self, create_and_delete_object):
        patch_obj_endpoint = PatchObject()
        patch_obj_endpoint.update_obj_with_patch(create_and_delete_object)
        patch_obj_endpoint.check_response_code_is_(200)
        patch_obj_endpoint.check_updated_name()
        patch_obj_endpoint.check_updated_price()
        patch_obj_endpoint.check_updated_year()
        patch_obj_endpoint.check_updated_cpu_model()

    @allure.title('Deletion object test')
    @allure.severity('Critical')
    def test_deletion_object(self):
        del_obj_endpoint = DeleteObject()
        new_object = del_obj_endpoint.create_new_object()
        del_obj_endpoint.check_response_code_is_(200)
        del_obj_endpoint.delete_created_object(new_object)
        del_obj_endpoint.check_response_code_is_(200)
        del_obj_endpoint.check_obj_absense(new_object)
