import pytest

from api_tests_msorokin.endpoints.get_objects import GetObjects
from api_tests_msorokin.endpoints.get_object_by_id import GetObjectById
from api_tests_msorokin.endpoints.update_object_by_id import UpdateObjectById
from api_tests_msorokin.endpoints.create_object import CreateObject
from api_tests_msorokin.endpoints.delete_object_by_id import DeleteObjectById
from api_tests_msorokin.endpoints.partial_object_update_by_id import PartialUpdateObjectById
from api_tests_msorokin.data.object_api_json import ObjectApiJson


@pytest.fixture()
def create_delete_object(create_api_object, delete_api_object_by_id):
    payload = ObjectApiJson.create_object_request_body_generated_json()
    create_api_object.create_new_object(payload)
    object_id = create_api_object.response_json['id']
    yield object_id, payload
    delete_api_object_by_id.delete_object(object_id)


@pytest.fixture(scope="session")
def get_api_objects():
    return GetObjects()


@pytest.fixture(scope="session")
def get_api_object_by_id():
    return GetObjectById()


@pytest.fixture(scope="session")
def update_api_object_by_id():
    return UpdateObjectById()


@pytest.fixture(scope="session")
def create_api_object():
    return CreateObject()


@pytest.fixture(scope="session")
def delete_api_object_by_id():
    return DeleteObjectById()


@pytest.fixture(scope="session")
def partial_update_api_by_id():
    return PartialUpdateObjectById()
