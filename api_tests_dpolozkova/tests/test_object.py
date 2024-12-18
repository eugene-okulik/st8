import allure
import pytest

from api_tests_dpolozkova.data import test_data


@allure.feature("Objects")
@allure.story("Get object by id")
@allure.title("Object by id")
@pytest.mark.smoke
def test_get_object_by_id(set_up, start_end, get_object_by_id):
    get_object_by_id.get_object_by_id(set_up)
    get_object_by_id.check_response_code_is_(200)
    get_object_by_id.check_fields_of_object(test_data.DEFAULT_PAYLOAD)
    get_object_by_id.check_object_id_is_(set_up)


@allure.feature("Objects")
@allure.story("Update object")
@allure.title("Update object with method put")
@pytest.mark.critical
def test_update_object_with_put(set_up, start_end, update_object_with_put):
    update_object_with_put.update_object_with_put(set_up, test_data.UPDATE_PAYLOAD)
    update_object_with_put.check_response_code_is_(200)
    update_object_with_put.check_name_is_updated(test_data.UPDATE_PAYLOAD['name'])
    update_object_with_put.check_year_is_updated(test_data.UPDATE_PAYLOAD['data']['year'])
    update_object_with_put.check_price_is_updated(test_data.UPDATE_PAYLOAD['data']['price'])


@allure.feature("Objects")
@allure.story("Update object")
@allure.title("Update object name with method patch")
@pytest.mark.parametrize(
    'name', [
        "Param-pam Pro 16",
        "$&*%!#%@",
        "   "],
    ids=['letters', 'symbols', 'spaces']
)
def test_update_object_with_patch(set_up, start_end, name, update_object_with_patch):
    payload = test_data.DEFAULT_PAYLOAD
    payload['name'] = name
    update_object_with_patch.update_object_with_patch(set_up, payload)
    update_object_with_patch.check_response_code_is_(200)
    update_object_with_patch.check_updated_name(name)
    update_object_with_patch.check_rest_fields_are_not_updated(payload)


@allure.feature("Objects")
@allure.story("Create an object")
@allure.title("Independent test for creating an object")
@pytest.mark.smoke
def test_create_object(start_end, create_object):
    create_object.create_object()
    create_object.check_response_code_is_(200)
    create_object.check_fields_of_object(test_data.DEFAULT_PAYLOAD)


@allure.feature("Objects")
@allure.story("Delete an object")
@allure.title("Independent test for deleting an object")
def test_delete_object(set_up, delete_object, get_object_by_id):
    delete_object.delete_object(set_up)
    get_object_by_id.get_object_by_id(set_up)
    get_object_by_id.check_response_code_is_(404)
