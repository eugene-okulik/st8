import pytest
import requests

API_URL = "https://restful-api.dev/objects"


# Фикстура для вывода сообщений перед и после тестов
@pytest.fixture(scope="session", autouse=True)
def start_end_tests():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.mark.smoke
def test_create_object():
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
    print(f"Объект создан с id: {object_id}")
    return object_id


@pytest.mark.smoke
def test_get_object_by_id():
    object_id = test_create_object()
    response = requests.get(f"{API_URL}/{object_id}")
    assert response.status_code == 200, f"Ошибка при получении объекта: {response.status_code}"
    assert response.json()['id'] == object_id, "ID объекта не совпадает"


@pytest.mark.critical
def test_update_object_put():
    object_id = test_create_object()
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


def test_update_object_patch():
    object_id = test_create_object()
    payload = {"data": {"Hard disk size": "4 TB"}}
    response = requests.patch(f"{API_URL}/{object_id}", json=payload)
    assert response.status_code == 200, f"Ошибка при обновлении объекта (PATCH): {response.status_code}"
    updated_object = response.json()
    assert updated_object['data']['Hard disk size'] == "4 TB", "Размер жесткого диска не обновлен корректно"


def test_delete_object():
    object_id = test_create_object()
    delete_response = requests.delete(f"{API_URL}/{object_id}")
    assert delete_response.status_code == 200, f"Ошибка при удалении объекта: {delete_response.status_code}"
    print(f"Объект с id {object_id} успешно удален")
