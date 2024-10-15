import requests
import pytest
from pydantic import BaseModel
from typing import Any, Dict


class PostResponse(BaseModel):
    id: str
    name: str
    data: Dict[str, Any]


class DeleteResponse(BaseModel):
    message: str


@pytest.mark.smoke
def test_create_object(create_publication, start_end):
    print(f"created object id: {create_publication}")
    assert create_publication is not None, "Failed to create object"

    response = requests.get(f"https://api.restful-api.dev/objects/{create_publication}")
    assert response.status_code == 200, f"Failed to retrieve object: {response.status_code}"
    response_data = PostResponse(**response.json())
    print(response.json())
    assert response_data.id == create_publication, "ID does not match"
    assert response_data.name == "Apple MacBook Pro 16", "Name does not match"


def test_receiving_object_by_id(create_publication, start_end):
    response = requests.get(f"https://api.restful-api.dev/objects?id={create_publication}")
    print(response)
    assert response.status_code == 200, f"Failed to retrieve object: {response.status_code}"


# method put-change data
@pytest.mark.critical
@pytest.mark.parametrize(
    'year, price, cpu_model, expected_status', [
        (2019, 1849.99, "Intel Core i9", 200),
        ({}, 1800, "*&^%&^%$&^%$", 200),
        (2050, 1700, "     ", 200),
    ],
    ids=['correct', 'symbols', 'spaces']
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
    response = requests.put(
        f"https://api.restful-api.dev/objects/{create_publication}",
        json=payload,
        headers=headers
    )
    assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"

    if expected_status == 200:
        data = response.json()
        assert data['data']['year'] == year
        assert data['data']['price'] == price
        assert data['data']['CPU model'] == cpu_model


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


def test_delete_object(create_publication):
    object_id = create_publication
    response = requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    print("Response JSON:", response.json())
    assert response.status_code == 200, f"Failed to delete object: {response.status_code}"
    response_data = DeleteResponse(**response.json())
    assert response_data.message == f"Object with id = {object_id} has been deleted."
