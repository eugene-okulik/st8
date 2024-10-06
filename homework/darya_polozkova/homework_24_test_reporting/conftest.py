import pytest
import requests
import allure

@allure.feature("Set-up")
@allure.story("Creating set-up object")
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


@allure.feature("Set-up")
@allure.story("Context printing...")
@pytest.fixture(scope="session", autouse=True)
def start_end():
    print('Start testing')
    yield None
    print('Testing completed')
