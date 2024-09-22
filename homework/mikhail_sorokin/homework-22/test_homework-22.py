import pytest
import requests

API_URL = "https://restful-api.dev/objects"


# - аналогично, апишка 405 отвечает но все верно


# Фикстура для создания объекта перед каждым тестом и удаления после теста
@pytest.fixture
def setup_teardown_object():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(API_URL, json=payload)
    assert response.status_code == 201, f"Ошибка при создании объекта: {response.status_code}"
    object_id = response.json()['id']
    yield object_id  # Передаем созданный object_id в тест

    delete_response = requests.delete(f"{API_URL}/{object_id}")
    assert delete_response.status_code == 200, f"Ошибка при удалении объекта: {delete_response.status_code}"


@pytest.fixture(scope="session", autouse=True)
def start_end_tests():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.mark.smoke
def test_get_object_by_id(setup_teardown_object):
    object_id = setup_teardown_object
    response = requests.get(f"{API_URL}/{object_id}")
    assert response.status_code == 200, f"Ошибка при получении объекта: {response.status_code}"
    assert response.json()['id'] == object_id, "ID объекта не совпадает"


@pytest.mark.critical
def test_update_object_put(setup_teardown_object):
    object_id = setup_teardown_object
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1999.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }
    response = requests.put(f"{API_URL}/{object_id}", json=payload)
    assert response.status_code == 200, f"Ошибка при обновлении объекта (PUT): {response.status_code}"
    updated_object = response.json()
    assert updated_object['data']['price'] == 1999.99, "Цена объекта не обновлена корректно"


def test_update_object_patch(setup_teardown_object):
    object_id = setup_teardown_object
    payload = {"data": {"Hard disk size": "4 TB"}}
    response = requests.patch(f"{API_URL}/{object_id}", json=payload)
    assert response.status_code == 200, f"Ошибка при обновлении объекта (PATCH): {response.status_code}"
    updated_object = response.json()
    assert updated_object['data']['Hard disk size'] == "4 TB", "Размер жесткого диска не обновлен корректно"
