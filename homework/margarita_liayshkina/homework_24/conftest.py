import pytest
import requests
from pydantic import BaseModel
from typing import Any, Dict


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
    object_id = response.json().get("id")
    print(f"Object created: {object_id}")

    yield object_id

    requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    print(f"Object {object_id} deleted")


@pytest.fixture()
def start_end():
    print('Start testind')
    yield None
    print('Testing completed')
