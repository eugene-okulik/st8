import requests
import pytest
from pydantic import BaseModel, Field
from typing import Any


@pytest.mark.real
def test_get_all(start_end, greet):
    expected = 100
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()
    assert len(data) == expected, f'publications quantity is not {expected}'


class Publication(BaseModel):
    id: int
    title: str
    body: str
    userId: int


def test_by_id():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts/42')
    assert response.status_code == 200
    data = response.json()
    Publication(**data)


class NewObj(BaseModel):
    id: str
    name: str
    data: dict[str, Any]


class ObjData(BaseModel):
    color: str
    capacity_GB: int = Field(alias='capacity GB')


class NewObjWithData(BaseModel):
    id: str
    name: str
    data: ObjData


def test_hw():
    response = {
        "id": "1",
        "name": "Google Pixel 6 Pro",
        "data": {
            "color": "Cloudy White",
            "capacity GB": 128
        }
    }
    NewObj(**response)
    NewObjWithData(**response)

@pytest.mark.real
@pytest.mark.parametrize(
    'data,result', [
        ('titleUPD', 200),
        ('     ', 200),
        ('*&^%&^%$&^%$', 200),
        ({}, 400)
    ], ids=['letters', 'spaces', 'symbols', 'object']
)
@pytest.mark.parametrize(
    'body', [
        'bodyUPD', '     ', '*&^%&^%$&^%$', {}
    ], ids=['B_letters', 'B_spaces', 'B_symbols', 'B_object']
)
def test_update_with_put(publication_id, start_end, greet, data, result, body):
    # data, result = title
    print('...testing...')
    payload = {
        'title': data,
        "body": body,
        "userId": 1
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{publication_id}',
        json=payload,
        headers=headers
    )
    data = response.json()
    assert response.status_code == result
    assert data['title'] == payload['title']
    assert data['body'] == payload['body']
