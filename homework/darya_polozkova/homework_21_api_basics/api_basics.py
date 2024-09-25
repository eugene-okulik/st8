import requests


# Создание объекта
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
    response = requests.post('http://167.172.172.115:52353/object', json=payload)
    if response.status_code == 200:
        object_id = response.json()['id']
        print(f"{object_id} is created")
        return object_id
    else:
        print(response.status_code)


# Получение объекта по его id
def get_object_by_id():
    response = requests.get(f'http://167.172.172.115:52353/object/{object_id}')
    data = response.json()
    print(data['name'])


# Изменение объекта с помощью метода PUT
def update_with_put():
    payload = {
            "name": "Put Apple MacBook Pro 16",
        "data": {
            "year": 2024,
            "price": 2000,
            "CPU model": "Put Intel Core i9",
            "Hard disk size": "100 TB"
        }
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=payload,
        headers=headers
    )
    print(response.json())


# Изменение объекта с помощью метода PATCH
def update_with_patch():
    payload = {
        "name": "Update Apple MacBook Pro 16",
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=payload,
        headers=headers
    )
    print(response.json())


# Удаление объекта
def delete_object():
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    print(response.status_code)


object_id = create_object()
get_object_by_id()
update_with_put()
update_with_patch()
delete_object()
