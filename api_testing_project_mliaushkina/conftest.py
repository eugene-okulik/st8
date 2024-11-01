import pytest
import requests


@pytest.fixture(scope="session")
def create_authorize():
    payload = {
        "name": "Margarita",
        }
    headers = {"Content-Type": 'application/json'}
    response = requests.post(
        "http://167.172.172.115:52355/authorize",
        json=payload,
        headers=headers
    )
    data = response.json()
    my_token = data["token"]
    print(f"Received token: {my_token}")
    return my_token


@pytest.fixture(scope="function")
def create_meme(create_authorize):
    headers = {"Authorization": create_authorize}
    payload = {
        "text": "Иван Иванов",
        "url": "ddd",
        "tags": ["blue", "red"],
        "info": {}
        }
    response = requests.post(
        f"http://167.172.172.115:52355/meme",
        headers=headers,
        json=payload
    )
    assert response.status_code == 200, f"Failed to added new meme: {response.status_code}"

    mem_id = response.json()["id"]
    yield mem_id

    requests.delete(
        f"http://167.172.172.115:52355/meme/{mem_id}",
        headers=headers
    )
