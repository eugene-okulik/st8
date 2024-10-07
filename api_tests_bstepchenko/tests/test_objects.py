import pytest
import allure
from api_tests_bstepchenko.data import constants


@allure.feature('Homework #23 tests')
@pytest.mark.usefixtures("start_end")
class TestAPIClient:

    @allure.title('Creation object test')
    @allure.description('That test is about creation object for following tests')
    @allure.severity('Critical')
    def test_creation_object(self, post_object_endpoint):
        payload = constants.PAYLOAD_FOR_OBJECT
        post_object_endpoint.post_new_object(payload)
        post_object_endpoint.check_response_code_is_(200)
        post_object_endpoint.check_updated_name(payload)
        post_object_endpoint.check_updated_year(payload)
        post_object_endpoint.check_updated_price(payload)
        post_object_endpoint.check_updated_cpu_model(payload)

    @allure.title('Getting exact object test')
    @allure.severity('Minor')
    def test_get_exact_object(self, create_and_delete_object, get_object_endpoint):
        object_id, payload = create_and_delete_object
        get_object_endpoint.get_object_by_id(object_id)
        get_object_endpoint.check_response_code_is_(200)
        get_object_endpoint.check_name(payload)
        get_object_endpoint.check_year(payload)
        get_object_endpoint.check_price(payload)
        get_object_endpoint.check_cpu_model(payload)

    @allure.title('Updating object with PUT test')
    @pytest.mark.parametrize('name', ['ABCdef', '   ', '!@#$%'],
                             ids=['letters', 'spaces', 'symbols']
                             )
    @pytest.mark.parametrize('year', [1993, 2024], ids=['old', 'new'])
    @pytest.mark.parametrize('price', [1, 100000], ids=['small', 'huge'])
    def test_update_object_with_put(self, create_and_delete_object, put_object_endpoint, name, price, year):
        object_id, payload = create_and_delete_object
        put_object_endpoint.update_obj_with_put(object_id, payload)
        put_object_endpoint.check_response_code_is_(200)
        put_object_endpoint.check_updated_name(payload)
        put_object_endpoint.check_updated_year(payload)
        put_object_endpoint.check_updated_price(payload)
        put_object_endpoint.check_updated_cpu_model(payload)

    @allure.title('Updating object with PATCH test')
    def test_update_object_with_patch(self, create_and_delete_object, patch_object_endpoint):
        object_id, payload = create_and_delete_object
        patch_object_endpoint.update_obj_with_patch(object_id)
        patch_object_endpoint.check_response_code_is_(200)
        payload = constants.PAYLOAD_FOR_OBJECT
        patch_object_endpoint.check_updated_name(payload)
        patch_object_endpoint.check_updated_price(payload)
        patch_object_endpoint.check_updated_year(payload)
        patch_object_endpoint.check_updated_cpu_model(payload)

    @allure.title('Deletion object test')
    @allure.severity('Critical')
    def test_deletion_object(self, delete_object_endpoint):
        new_object = delete_object_endpoint.create_new_object()
        delete_object_endpoint.check_response_code_is_(200)
        delete_object_endpoint.delete_created_object(new_object)
        delete_object_endpoint.check_response_code_is_(200)
        delete_object_endpoint.check_obj_absense(new_object)
