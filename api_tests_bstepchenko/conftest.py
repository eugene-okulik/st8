import pytest
import requests

from api_tests_bstepchenko.data import constants
from api_tests_bstepchenko.endpoints.get_object import GetObject
from api_tests_bstepchenko.endpoints.post_object import PostObject
from api_tests_bstepchenko.endpoints.put_object import PutObject
from api_tests_bstepchenko.endpoints.patch_object import PatchObject
from api_tests_bstepchenko.endpoints.del_object import DeleteObject
from api_tests_bstepchenko.data.randomizer import get_random_int, get_random_str


@pytest.fixture(scope='class')
def start_end():
    print('\nStart testing.....')
    yield
    print('\nTesting was completed!')


@pytest.fixture(scope='function')
def create_and_delete_object():
    payload = {
        "name": get_random_str(),
        "data": {
            "year": get_random_int(),
            "price": get_random_int(),
            "CPU model": get_random_str(),
        },
    }
    creation_response = requests.post(f'{constants.BASE_URL}',
                                      json=payload, headers=constants.HEADERS)
    created_object = creation_response.json()
    assert created_object is not None, "Failed to create the object"
    yield created_object['id'], payload
    requests.delete(f'{constants.BASE_URL}/{created_object["id"]}')


@pytest.fixture(scope='function')
def get_object_endpoint():
    return GetObject()


@pytest.fixture(scope='function')
def post_object_endpoint():
    return PostObject()


@pytest.fixture(scope='function')
def put_object_endpoint():
    return PutObject()


@pytest.fixture(scope='function')
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture(scope='function')
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture(scope='function')
def object_id(create_and_delete_object):
    object_id, payload = create_and_delete_object
    return object_id


@pytest.fixture(scope='function')
def payload(create_and_delete_object):
    object_id, payload = create_and_delete_object
    return payload
