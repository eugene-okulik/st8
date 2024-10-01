import pytest
import requests


@pytest.fixture()
def set_up():
    payload = {
        "name": "Unittest MacBook Pro 16",
        "data": {
            "year": 2024,
            "price": 2000,
            "CPU model": "M1",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(
        'http://167.172.172.115:52353/object', json=payload
    )
    object_id = response.json()['id']
    print(f'Object for set-up is created with ID {object_id}')
    yield object_id
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    print(f'Object for set-up is deleted with ID {object_id}')


@pytest.fixture(scope="session", autouse=True)
def start_end():
    print('Start testing')
    yield None
    print('Testing completed')


@pytest.mark.smoke
def test_get_object_by_id(set_up, start_end):
    response = requests.get(f'http://167.172.172.115:52353/object/{set_up}')
    data = response.json()
    name = data['name']
    print(f'Your newly created object is {name}')


@pytest.mark.critical
def test_update_object_with_put(set_up, start_end):
    payload = {
        "name": "Put Unittest MacBook Pro 16",
        "data": {
            "year": 2024,
            "price": 2000,
            "CPU model": "Put Intel Core i9",
            "Hard disk size": "100 TB"
        }
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{set_up}',
        json=payload,
        headers=headers
    )
    print(response.json())


def test_update_object_with_patch(set_up, start_end):
    payload = {
        "name": "Update Unittest MacBook Pro 16",
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{set_up}',
        json=payload,
        headers=headers
    )
    print(f'Your updated object data: {response.json()}')


@pytest.mark.smoke
def test_independent_create_an_object():
    payload = {
        "name": " Real Unittest MacBook Pro 16",
        "data": {
            "year": 2050,
            "price": 3000,
            "CPU model": "M1",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(
        'http://167.172.172.115:52353/object', json=payload
    )
    object_id = response.json()['id']
    print(f"{object_id} is created")
    return object_id


def test_independent_delete_an_object():
    object_id = test_independent_create_an_object()
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    print(f'Object is deleted with ID {object_id}')
