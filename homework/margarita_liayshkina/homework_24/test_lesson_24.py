import requests
import pytest
from pydantic import BaseModel
import allure


class Publication(BaseModel):
    id: int
    title: str
    body: str
    userId: int


@allure.feature('Publications')
@allure.story('Get publication')
@pytest.mark.smoke
def test_create_object(create_publication, start_end):
    print(f"created object id: {create_publication}")
    assert create_publication is not None, "Failed to create object"

    response = requests.get(f"https://api.restful-api.dev/objects/{create_publication}")
    assert response.status_code == 200, f"Failed to retrieve object: {response.status_code}"
    publication_data = response.json()
    Publication(**publication_data)


@allure.feature('Publications')
@allure.story('Get publication')
def test_receiving_object_by_id(create_publication, start_end):
    response = requests.get(f"https://api.restful-api.dev/objects?id={create_publication}")
    assert response.status_code == 200, f"Failed to retrieve object: {response.status_code}"
    publication_data = response.json()
    Publication(**publication_data)


# method put-change data
@allure.feature('Publications')
@allure.story('Update publications')
@allure.title('Update publications using PUT method')
@pytest.mark.critical
@pytest.mark.parametrize(
    'year, price, cpu_model, expected_status', [
        (2019, 1849.99, "Intel Core i9", 200),
        ({}, 1800, "*&^%&^%$&^%$", 400),
        (2050, 1700, "     ", 200),
    ],
    ids=['correct','symbols', 'spaces']
)
def test_update_object_with_put(create_publication, start_end, year, price, cpu_model, expected_status):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": year,
            "price": price,
            "CPU model": cpu_model,
            "Hard disk size": "1 TB"
        }
    }
    print(f"Sending PUT request to update object with ID {create_publication}...")
    print(f"Payload: {payload}")

    headers = {"Content-Type": 'application/json'}
    with allure.step('Send PUTrequest with updates'):
        response = requests.put(
            f"https://api.restful-api.dev/objects/{create_publication}",
            json=payload,
            headers=headers
        )
    assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"

    if expected_status == 200:
        data = response.json()
        with allure.step(f'Checking  year in Publication is {payload["data"]["price"]}'):
            assert data['data']['year'] == year
        with allure.step(f'Checking  price in Publication is {payload["data"]["price"]}'):
            assert data['data']['price'] == price
        with allure.step(f'Checking  CPU model in Publication is {payload["data"]["CPU model"]}'):
            assert data['data']['CPU model'] == cpu_model


# method patch partial update
@allure.feature('Publications')
@allure.story('Update publications')
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
    publication_data = response.json()
    Publication(**publication_data)


@allure.feature('Publications')
@allure.story('Delete publications')
def test_delete_object(create_publication):
    object_id = create_publication
    response = requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    print("Response JSON:", response.json())
    assert response.status_code == 200, f"Failed to delete object: {response.status_code}"
