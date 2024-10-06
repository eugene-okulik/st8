import pytest

from api_tests_msorokin.endpoints.get_objects import GetObjects
from api_tests_msorokin.endpoints.get_object_by_id import GetObjectById
from api_tests_msorokin.endpoints.update_object_by_id import UpdateObjectById
from api_tests_msorokin.endpoints.create_object import CreateObject
from api_tests_msorokin.endpoints.delete_object_by_id import DeleteObjectById
from api_tests_msorokin.endpoints.partial_object_update_by_id import PartialUpdateObjectById


@pytest.fixture()
def get_api_objects():
    return GetObjects()


@pytest.fixture()
def get_api_object_by_id():
    return GetObjectById()


@pytest.fixture()
def update_api_object_by_id():
    return UpdateObjectById()


@pytest.fixture()
def create_api_object():
    return CreateObject()


@pytest.fixture()
def delete_api_object_by_id():
    return DeleteObjectById()


@pytest.fixture()
def partial_update_api_by_id():
    return PartialUpdateObjectById()
