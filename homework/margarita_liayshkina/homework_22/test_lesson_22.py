import requests
import pytest
import allure


# fixture receiving  object ID
@allure.feature('Publications')
@allure.story('Post publications')
@pytest.fixture(scope='function')
def create_publication():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.post(
        "https://api.restful-api.dev/objects",
        json=payload,
        headers=headers
    )
    object_id = response.json().get("id")
    print(f"Object created: {object_id}")

    yield object_id

    requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    print(f"Object {object_id} deleted")


@pytest.fixture(scope='session')
def start_end():
    print("Start testing")
    yield None
    print("Testing completed")


@pytest.mark.smoke
def test_create_object(create_publication, start_end):
    print(f"created object id: {create_publication}")
    assert create_publication is not None, "Failed to create object"


@allure.feature('Publications')
@allure.story('Get publications')
def test_receiving_object_by_id(create_publication, start_end):
    response = requests.get(f"https://api.restful-api.dev/objects?id={create_publication}")
    print(response)
    assert response.status_code == 200, f"Failed to retrieve object: {response.status_code}"


# method put-change data
@pytest.mark.critical
@allure.feature('Publications')
@allure.story('Update publications')
@allure.title('Update publications using PUT method')
def test_update_subject_with_put(create_publication, start_end):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2030,
            "price": 3000,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.put(
        f"https://api.restful-api.dev/objects/{create_publication}",
        json=payload,
        headers=headers
    )
    assert response.status_code == 200, f"Failed to update object with PUT: {response.status_code}"


# method patch partial update
def test_update_subject_with_patch(create_publication, start_end):
    payload = {
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2025,
        }
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.patch(
        f"https://api.restful-api.dev/objects/{create_publication}",
        json=payload,
        headers=headers
    )
    assert response.status_code == 400, f"Failed to update object with Patch: {response.status_code}"
    response_data = response.json()
    assert response_data["data"]["year"] == payload["data"]["year"], "Year was not updated correctly"


@allure.feature('Publications')
@allure.story('Delete publication')
def test_delete_object(create_publication):
    object_id = create_publication
    response = requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    print(response)
    assert response.status_code == 200, f"Failed to delete object: {response.status_code}"
