import pytest
import allure

from api_tests_eokulik.data import test_data


@allure.feature('Publications')
@allure.story('Get publications')
@allure.title('Получение всех публикаций')
@pytest.mark.real
def test_get_all(get_posts_endpoint):
    get_posts_endpoint.get_all_posts()
    get_posts_endpoint.check_response_code_is_(200)
    get_posts_endpoint.check_posts_qty_is_(test_data.POSTS_QTY)


@allure.feature('Publications')
@allure.story('Get publications')
def test_by_id(publication_id, get_post_by_id_endpoint):
    get_post_by_id_endpoint.get_post_by_id(publication_id)
    get_post_by_id_endpoint.check_response_code_is_(200)
    get_post_by_id_endpoint.check_publication_id_is_(publication_id)


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
def test_update_with_put(publication_id, put_pub_endpoint, data, result, body):
    '''
    This test is for testing publication update
    '''
    payload = test_data.DEFAULT_PAYLOAD
    payload['body'] = body
    payload['title'] = data
    put_pub_endpoint.update_pub_with_put(publication_id, payload)
    put_pub_endpoint.check_response_code_is_(result)
    put_pub_endpoint.check_publication_title(data)
    put_pub_endpoint.check_publication_body(body)
