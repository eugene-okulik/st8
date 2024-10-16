import pytest
import requests
from api_tests_dpolozkova.endpoints.delete_object import DeleteObject
from api_tests_dpolozkova.endpoints.get_object_by_id import GetObjectById
from api_tests_dpolozkova.endpoints.create_object import CreateObject
from api_tests_dpolozkova.endpoints.update_object_with_put import UpdateObjectPut
from api_tests_dpolozkova.endpoints.update_object_with_patch import UpdateObjectPatch
from api_tests_dpolozkova.data import test_data
from api_tests_dpolozkova.data import constants
from homework.darya_polozkova.homework_21_api_basics.api_basics import object_id


@pytest.fixture()
def set_up(create_object, delete_object):
    create_object.create_object(test_data.DEFAULT_PAYLOAD)
    object_id = create_object.response_json['id']
    yield object_id
    delete_object.delete_object(object_id)


@pytest.fixture(scope="session", autouse=True)
def start_end():
    print('Start testing')
    yield None
    print('Testing completed')


@pytest.fixture()
def get_object_by_id():
    return GetObjectById()


@pytest.fixture()
def create_object():
    # не забывать скобочки
    return CreateObject()


@pytest.fixture()
def delete_object():
    return DeleteObject()


@pytest.fixture()
def update_object_with_put():
    return UpdateObjectPut()


@pytest.fixture()
def update_object_with_patch():
    return UpdateObjectPatch()
