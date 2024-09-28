import pytest
import requests
from helpers import FakeData


@pytest.mark.smoke
def create_object():
    API_URL = "http://167.172.172.115:52353/object"
    payload = {
        "name": f"{FakeData.RANDOM_WORD()}",
        "data": {
            "year": f"{FakeData.FAKE_DATE()}",
            "price": f"{FakeData.RANDOM_INT()}",
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(API_URL, json=payload)
    assert response.status_code == 200, f"Ошибка при создании объекта: {response.status_code}"
    object_id = response.json()['id']
    print(response.json())
    print(f"Объект создан с id: {object_id}")
    return object_id


def delete_object(object_id):
    API_URL = "http://167.172.172.115:52353/object"
    delete_response = requests.delete(f"{API_URL}/{object_id}")
    assert delete_response.status_code == 200, f"Ошибка при удалении объекта: {delete_response.status_code}"
    print(f"Объект с id {object_id} успешно удален")


@pytest.fixture
def start_end():
    print('start test')
    object_id = create_object()
    yield object_id
    delete_object(object_id)
    print('end test')