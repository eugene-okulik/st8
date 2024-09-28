import requests
import pytest
from pydantic import BaseModel
import allure


@allure.feature('Publications')
@allure.story('Get publications')
@allure.title('Получение всех публикаций')
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


@allure.feature('Publications')
@allure.story('Get publications')
def test_by_id():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts/42')
    assert response.status_code == 200
    data = response.json()
    Publication(**data)


@allure.feature('Publications')
@allure.story('Update publications')
# @allure.description('what this test is about')
@allure.title('Update publications using PUT method')
@pytest.mark.real
@pytest.mark.parametrize(
    'data,result', [
        ('titleUPD', 200),
        ('     ', 200),
        ('*&^%&^%$&^%$', 200),
        ({}, 200)
    ], ids=['letters', 'spaces', 'symbols', 'object']
)
@pytest.mark.parametrize(
    'body', [
        'bodyUPD', '     ', '*&^%&^%$&^%$', {}
    ], ids=['B_letters', 'B_spaces', 'B_symbols', 'B_object']
)
def test_update_with_put(publication_id, start_end, greet, data, result, body):
    '''
    This test is for testing publication update
    '''
    # data, result = title
    print('...testing...')
    payload = {
        'title': data,
        "body": body,
        "userId": 1
    }
    headers = {"Content-Type": 'application/json'}
    with allure.step('Send PUT request with updates'):
        response = requests.put(
            f'https://jsonplaceholder.typicode.com/posts/{publication_id}',
            json=payload,
            headers=headers
        )
        data = response.json()
    with allure.step(f'Check that status code is {result}'):
        assert response.status_code == result
    with allure.step(f'Checking title in Publication is {payload["title"]}'):
        assert data['title'] == payload['title']
    with allure.step(f'Checking body in Publication is {payload["body"]}'):
        assert data['body'] == payload['body']
