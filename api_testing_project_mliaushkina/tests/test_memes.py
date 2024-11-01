import requests
import pytest
import allure
import json

from api_testing_project_mliaushkina.data import constans

@allure.feature('Memes')
@allure.story('Checking token')
@allure.title('Check is token alive')
def check_if_token_alive(create_authorize):
    headers = {"Content-Type": 'application/json'}
    response = requests.get(
        f"{constans.BASE_URL}/{constans.AUTORIZ}/{create_authorize}",
        headers=headers
    )
    assert  response.status_code == 200, f"Token is not alive: {response.status_code}"


@allure.feature('Memes')
@allure.story('Get memes')
@allure.title('Получение списка всех мемов')
def get_all_mems(create_authorize):
    headers = {"Authorization": create_authorize}
    response = requests.get(
        f"{constans.BASE_URL}/{constans.MEME_POSTFIX}",
        headers=headers
    )
    assert response.status_code == 200, f"Failed to retrieve all memes: {response.status_code}"


@allure.feature('Memes')
@allure.story('Получение одного мема по id')
def get_meme_by_id(create_authorize, create_meme):
    headers = {"Authorization": create_authorize}
    response = requests.get(
        f"{constans.BASE_URL}/{constans.MEME_POSTFIX}/{create_meme}",
        headers=headers
    )
    assert response.status_code == 200, f"Failed to get meme by id: {response.status_code}"
    assert 'text' in response.json(), "Response does not contain 'text'"


@allure.feature('Memes')
@allure.story('Add meme by Id')
@allure.title('Check creating meme')
def added_meme(create_authorize, create_meme):
    assert create_meme is not None, f"failed to create meme"

    headers = {"Authorization": create_authorize}
    get_response = requests.get(
        f"{constans.BASE_URL}/{constans.MEME_POSTFIX}/{create_meme}",
        headers=headers
    )


@allure.feature('Memes')
@allure.story('Update created meme')
@allure.title('Изменение существующего мема')
@pytest.mark.parametrize(
    'text', [
        ('Good Morning'),
        ('     '),
        ('oho'),
        ('')
        ],
)
@pytest.mark.parametrize(
    'tags', [
        (["hot", "cold"]),
        (["xxx"]),
        ([]),
        ],
ids=[
        'two_tags',
        'one_tag',
        'empty_tags',
    ]
)
@pytest.mark.parametrize(
    'info', [
        ({"adress": 666, "city": 888}),
        ({"adress": 666}),
        ({}),
        ],
ids=[
        'two_fields',
        'one_field',
        'empty_object',
    ]
)
def update_meme_with_put(create_authorize, create_meme, text, tags, info):
    headers = {"Authorization": create_authorize}
    payload = {
        "id" : create_meme,
        "text": text,
        "url": "www",
        "tags": tags,
        "info": info
        }
    response = requests.put(
        f"{constans.BASE_URL}/{constans.MEME_POSTFIX}/{create_meme}",
        headers=headers,
        json=payload
    )
    result = 200
    with allure.step(f"Step 1- Check answer: expected {result}, received {response.status_code}"):
        assert response.status_code == result, f"Failed to update meme: {response.status_code}"

        if response.status_code == 200:
            response_json = response.json()

            assert (
                    response_json.get('text') == text
            ), f"Response data text mismatch: {response_json}"
            assert (
                    response_json.get('tags') == tags
            ), f"Response data tags mismatch: {response_json}"
            assert (
                    response_json.get('info') == info
            ), f"Response data info mismatch: {response_json}"

            with allure.step(f"Step 2_Verify data via GET request for ID {create_meme}"):
                get_response = requests.get(f"{constans.BASE_URL}/{constans.MEME_POSTFIX}/{create_meme}",
                                            headers=headers)
                assert get_response.status_code == 200, f"GET request failed: {get_response.status_code}"
                get_response_json = get_response.json()

                assert (
                        get_response_json.get("text") == text and
                        get_response_json.get("tags") == tags and
                        get_response_json.get('info') == info
                ), f"GET response data mismatch: {get_response_json}"
        else:
            with allure.step("Check error message for invalid requests"):
                assert response.json().get('error') is not None, "Expected an error message in the response"


@allure.feature('Memes')
@allure.story('Delete created meme')
@allure.title('Удаление мема')
def delete_meme(create_authorize, create_meme):
    headers = {"Authorization": create_authorize}
    response = requests.delete(
        f"{constans.BASE_URL}/{constans.MEME_POSTFIX}/{create_meme}",
        headers=headers
    )
    with allure.step(f" Step 1- Check delete response status: expected 200, got {response.status_code}"):
        assert response.status_code == 200, f"Failed to delete meme: {response.status_code}"
    with allure.step("Step 2- Verify meme is deleted by performing a GET request"):
        get_response = requests.get(
        f"{constans.BASE_URL}/{constans.MEME_POSTFIX}/{create_meme}",
        headers=headers
    )
    with allure.step(f"Check GET response status: expected 404, got {get_response.status_code}"):
        assert get_response.status_code == 404, f"Expected 404, got {get_response.status_code}: Meme still exists."



@allure.feature('Memes')
@allure.story('Get memes')
@allure.title('Получение списка всех мемов')
def test_get_all_memes(get_meme_list_endpoint):
    get_meme_list_endpoint.do_authorize()
    get_meme_list_endpoint.get_memes_list()
    get_meme_list_endpoint.check_response_code_is_(200)
