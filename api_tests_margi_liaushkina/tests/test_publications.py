import requests
import pytest
import allure

from api_tests_margi_liaushkina.data import  test_data
from api_tests_margi_liaushkina.endpoints.create_object import CreatePost
from api_tests_margi_liaushkina.endpoints.receiving_object_by_id import GetPostsId
from homework.margarita_liayshkina.homework_21.lesson_21 import create_object


@allure.feature('Publications')
@allure.story('Create publication')
@pytest.mark.smoke
def test_create_object(create_publication, start_end):
    create_publication.create_obj(test_data.DEFAULT_PAYLOAD)
    create_publication.check_response_code_is_(200)
    create_publication.check_fields_of_object(test_data.DEFAULT_PAYLOAD)


@allure.feature('Publications')
@allure.story('Get publications')
def test_receiving_object_by_id(create_publication, start_end):
    get_post_by_id_endopoint = GetPostsId()
    get_post_by_id_endopoint.get_post_by_id(create_publication)
    get_post_by_id_endopoint.check_response_code_is_(200)


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
    payload = test_data.DEFAULT_PAYLOAD
    payload["year"] = year
    payload['data']['price'] = price
    payload['data']['cpu_model'] = cpu_model
  



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



@allure.feature('Publications')
@allure.story('Delete publications')
def test_delete_object(create_publication):
    object_id = create_publication
    response = requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    print("Response JSON:", response.json())
    assert response.status_code == 200, f"Failed to delete object: {response.status_code}"
