"""
Продолжим оформлять тесты из предыдущих заданий

Тест на изменение объекта с помощью метода PUT оформите так,
чтобы он тестировал 3 разных изменения с помощью parametrize

Разделите тесты на 2 файла, вынесите фикстуры в файл conftest.py.

С помощью Pydantic провалидируйте схему ответов для POST и DELETE запросов.
"""

# Я сделал для put pydantic схему и в целом полностью с ним разобрался,  у post и delete по сути тоже самое
# Не вижу смысла для них делать отдельную схему
import pytest
import requests
from helpers import FakeData
from pydentic_model import ObjectJson, ObjectDataJson


class TestHomework23:
    API_URL = "http://167.172.172.115:52353/object"

    @pytest.mark.smoke
    def test_create_object(self):
        payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        response = requests.post(self.API_URL, json=payload)
        assert response.status_code == 200, f"Ошибка при создании объекта: {response.status_code}"
        object_id = response.json()['id']
        print(response.json())
        print(f"Объект создан с id: {object_id}")
        return object_id

    @pytest.mark.critical
    @pytest.mark.parametrize(
        'name,expected', [
            (FakeData.RANDOM_WORD(), 200)
        ], ids=['update name']
    )
    @pytest.mark.parametrize(
        'year', [
            FakeData.FAKE_DATE()
        ], ids=['update year']
    )
    @pytest.mark.parametrize(
        'price', [
            FakeData.RANDOM_INT()
        ], ids=['update price']
    )
    def test_update_object_by_parametrize(self, name: str, year: int,  price: float or int, expected: int, start_end):
        payload = {
            "name": name,
            "data": {
                "year": year,
                "price": price,
                "CPU model": "Intel Core i9",
                "Hard disk size": "2 TB"
            }
        }
        object_id = start_end
        response = requests.put(f"{self.API_URL}/{object_id}", json=payload)
        print(response.json())
        assert response.status_code == expected, f"Ошибка при обновлении объекта (PUT): {response.status_code}"
        ObjectJson(**response.json())
        assert response.json()['name'] == name
        updated_object = response.json()
        assert updated_object['data']['price'] == price, "Цена объекта не обновлена корректно"
        assert updated_object['data']['year'] == year, "Цена объекта не обновлена корректно"

    def test_delete_object(self):
        object_id = self.test_create_object()
        delete_response = requests.delete(f"{self.API_URL}/{object_id}")
        assert delete_response.status_code == 200, f"Ошибка при удалении объекта: {delete_response.status_code}"
        print(f"Объект с id {object_id} успешно удален")

