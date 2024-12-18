import pytest
import allure
from api_tests_msorokin.data.helpers import FakeData
from api_tests_msorokin.data.object_api_json import ObjectApiJson


@allure.feature("tests for homework 25-26")
class TestHomeworkProject:

    @pytest.mark.smoke
    @allure.severity("Smoke")
    @allure.title("test for create object api")
    def test_create_object(self, create_api_object, delete_api_object_by_id):
        payload = ObjectApiJson.create_object_request_body_generated_json()
        create_api_object.create_new_object(payload)
        create_api_object.check_response_code_is_(200)
        create_api_object.check_all_fields(payload)
        delete_api_object_by_id.delete_object(create_api_object.response_json['id'])

    @pytest.mark.smoke
    @allure.severity("Smoke")
    @allure.title("test for get object api")
    def test_get_objects(self, get_api_objects):
        get_api_objects.get_objects()
        get_api_objects.check_response_code_is_(200)
        get_api_objects.check_that_response_is_not_empty()

    @pytest.mark.smoke
    @allure.severity("Smoke")
    @allure.title("test for get object by id api")
    def test_get_object_by_id(self, get_api_object_by_id, create_delete_object):
        object_id, payload = create_delete_object()
        get_api_object_by_id.get_object_by_id(object_id)
        get_api_object_by_id.check_all_fields(payload)

    @pytest.mark.smoke
    @allure.severity("Smoke")
    @allure.title("test for update object api")
    def test_update_object(self, update_api_object_by_id, create_delete_object):
        object_id = create_delete_object()
        payload = ObjectApiJson.create_object_request_body_generated_json()
        update_api_object_by_id.update_object_by_id(object_id, payload)
        update_api_object_by_id.check_response_code_is_(200)
        update_api_object_by_id.check_that_all_fields_are_updated(payload)

    @pytest.mark.smoke
    @allure.severity("Smoke")
    @allure.title("test for partial object update api")
    def test_partial_update(self, partial_update_api_by_id, create_delete_object, get_api_object_by_id):
        payload = ObjectApiJson.partial_update_name_json(FakeData.RANDOM_WORD())
        object_id = create_delete_object()
        partial_update_api_by_id.partial_update_object_by_id(object_id, payload)
        get_api_object_by_id.get_object_by_id(object_id)
        get_api_object_by_id.check_name(payload['name'])

    @pytest.mark.smoke
    @allure.severity("Smoke")
    @allure.title("test for delete object api")
    def test_delete_object(self, create_api_object, delete_api_object_by_id, get_api_object_by_id):
        payload = ObjectApiJson.create_object_request_body_generated_json()
        create_api_object.create_new_object(payload)
        object_id = create_api_object.response_json['id']
        get_api_object_by_id.get_object_by_id(object_id)
        get_api_object_by_id.check_all_fields(payload)
        delete_api_object_by_id.delete_object(object_id)
        get_api_object_by_id.get_object_by_id(object_id)
        get_api_object_by_id.check_response_code_is_(404)
