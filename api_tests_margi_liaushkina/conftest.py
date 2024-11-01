import pytest
import requests


@pytest.fixture()
def publication_id():
    payload = {
        'title': 'foo',
        "body": "bar",
        "userId": 1
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=payload,
        headers=headers
    )
    data = response.json()
    data['id'] = 42
    print(f'Created publication with ID {data["id"]}')
    yield data['id']
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{data["id"]}')
    print(f'Post {data["id"]} deleted')


@pytest.fixture()
def start_end():
    print('start test')
    yield None
    print('end test')


@pytest.fixture(scope='session')
def greet():
    print('Hello')
    yield None
    print('Bye')
