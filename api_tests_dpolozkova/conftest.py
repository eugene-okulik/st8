import pytest
import requests
from api_tests_dpolozkova.endpoints.delete_an_object import DeleteObject
from api_tests_dpolozkova.endpoints.get_object_by_id import GetObjectById
from api_tests_dpolozkova.endpoints.create_an_object import CreateObject
from api_tests_dpolozkova.endpoints.update_object_with_put import UpdateObjectPut
from api_tests_dpolozkova.endpoints.update_object_with_patch import UpdateObjectPatch
from api_tests_dpolozkova.data import test_data
from api_tests_dpolozkova.data import constants


@pytest.fixture()
def set_up():
    payload = test_data.DEFAULT_PAYLOAD
    creation_response = requests.post(f'{constants.BASE_URL}{constants.POSTS_POSTFIX}',
                                      json=payload, headers=constants.HEADERS)
    created_object = creation_response.json()
    yield created_object['id']
    requests.delete(f'{constants.BASE_URL}/{created_object["id"]}')

@pytest.fixture(scope="session", autouse=True)
def start_end():
    print('Start testing')
    yield None
    print('Testing completed')

@pytest.fixture()
def get_object_by_id():
    return GetObjectById()

@pytest.fixture()
def independent_test_create_an_object():
    # не забывать скобочки
    return CreateObject()

@pytest.fixture()
def independent_test_delete_an_object():
    return DeleteObject()

@pytest.fixture()
def update_object_with_put():
    return UpdateObjectPut()

@pytest.fixture()
def update_object_with_patch():
    return UpdateObjectPatch()