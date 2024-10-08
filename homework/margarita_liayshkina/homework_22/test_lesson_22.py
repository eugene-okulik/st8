import requests
import pytest


# fixture receiving  object ID
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
    if response.status_code == 200:
        print(f"Failed to create object: {response.status_code} - {response.text}")
        return None
    object_id = response.json().get("id")
    if object_id is None:
        print("Response does not contain object ID")
        return None
    print(f"Object created: {object_id}")

    yield object_id

    delete_response = requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    if delete_response.status_code == 200:
        print(f"Failed to delete object: {delete_response.status_code} - {delete_response.text}")
    else:
        print(f"Object {object_id} deleted")


@pytest.fixture(scope='session')
def start_end():
    print("Start testing")
    yield None
    print("Testing completed")


@pytest.mark.smoke
def test_create_object(create_publication):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post("https://api.restful-api.dev/objects", json=payload)
    assert response.status_code == 200, f"Failed to create object: {response.status_code}"
    object_id = create_publication
    assert object_id is not None, "Object ID should not be None after creation"
    print(f"Object created {object_id}!")


def test_receiving_object_by_id(create_publication, start_end):
    request_value = "https://api.restful-api.dev/objects?id={}".format(create_publication)
    response = requests.get(request_value)
    assert response.status_code == 200, f"Failed to retrieve object: {response.status_code}"
    response_data = response.json()
    print(response_data)


# method put-change data
@pytest.mark.critical
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
    response_data = response.json()
    assert response_data["name"] == payload["name"], "Name was not updated correctly"
    assert response_data["data"]["year"] == payload["data"]["year"], "Year was not updated correctly"
    assert response_data["data"]["price"] == payload["data"]["price"], "Price was not updated correctly"
    print(response.json())


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
    assert response.status_code == 200, f"Failed to update object with Patch: {response.status_code}"
    response_data = response.json()
    assert response_data["data"]["year"] == payload["data"]["year"], "Year was not updated correctly"
    print(response.json())


def test_delete_object(create_publication):
    object_id = create_publication
    response = requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    assert response.status_code == 200, f"Failed to delete object: {response.status_code}"