import requests
import pytest


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


@pytest.mark.simple
def test_demo1(greet):
    assert 1 == 1


@pytest.mark.simple
@pytest.mark.skip('Bug #23747632')
def test_demo2(greet):
    assert 1 == 1


@pytest.mark.real
def test_get_all(start_end, greet):
    expected = 100
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()
    assert len(data) == expected, f'publications quantity is not {expected}'


@pytest.mark.real
def test_update_with_put(publication_id, start_end, greet):
    print('...testing...')
    payload = {
        'title': 'fooUPD',
        "body": "barUPD",
        "userId": 1
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{publication_id}',
        json=payload,
        headers=headers
    )
    data = response.json()
    assert data['title'] == payload['title']
    assert data['body'] == payload['body']
