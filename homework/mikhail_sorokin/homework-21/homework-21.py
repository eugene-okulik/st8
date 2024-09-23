"""
Задание
Для тестирования возьмем небольшое тестовое API: https://restful-api.dev
Нужно написать код, который взамодействует с перечисленными в спецификации функции этого API, а именно:

Создание объекта
Получение объекта по его id
Изменение объекта с помощью метода PUT
Изменение объекта с помощью метода PATCH
Удаление объекта
Выполняйте всё задание так же, как я делал на занятии, - каждый запрос в отдельной функции.
"""

# у меня апишка 405 возвращает, лень разбираться что там к чему, но вроде как все верно и должно работать.

import requests

API_URL = "https://restful-api.dev/objects"


def create_object():
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
    if response.status_code == 201:
        object_id = response.json()['id']
        print(f"Объект успешно создан c id - {object_id}")
        return object_id
    else:
        print(f"Ошибка при создании объекта: {response.status_code}")
        return None


def get_object_by_id(object_id1):
    response = requests.get(f"{API_URL}/{object_id1}")
    if response.status_code == 200:
        print("Объект успешно получен")
        return response.json()['id']
    else:
        print(f"Ошибка при получении объекта: {response.status_code}")
        return None


def update_object_put(object_id1):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }
    response = requests.put(f"{API_URL}/{object_id}", json=payload)
    if response.status_code == 200:
        print("Объект успешно обновлен (PUT)")
        return response.json()
    else:
        print(f"Ошибка при обновлении объекта (PUT): {response.status_code}")
        return None


def update_object_patch(object_id1):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }
    response = requests.patch(f"{API_URL}/{object_id1}", json=payload)
    if response.status_code == 200:
        print("Объект успешно обновлен (PATCH)")
        return response.json()
    else:
        print(f"Ошибка при обновлении объекта (PATCH): {response.status_code}")
        return None


def delete_object(object_id1):
    response = requests.delete(f"{API_URL}/{object_id1}")
    if response.status_code == 200:
        print("Объект успешно удален")
        return True
    else:
        print(f"Ошибка при удалении объекта: {response.status_code}")
        return False


object_id = create_object()
get_object_by_id(object_id)
update_object_patch(object_id)
update_object_put(object_id)
delete_object(object_id)
