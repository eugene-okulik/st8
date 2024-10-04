import pytest
import requests
from api_tests_bstepchenko.data import constants


@pytest.fixture(scope='class')
def start_end():
    print('\nStart testing.....')
    yield
    print('\nTesting was completed!')


@pytest.fixture(scope='function')
def create_and_delete_object():
    payload = constants.PAYLOAD_FOR_OBJECT
    creation_response = requests.post(f'{constants.BASE_URL}',
                                      json=payload, headers=constants.HEADERS)
    created_object = creation_response.json()
    assert created_object is not None, "Failed to create the object"
    yield created_object['id']
    requests.delete(f'{constants.BASE_URL}/{created_object["id"]}')
