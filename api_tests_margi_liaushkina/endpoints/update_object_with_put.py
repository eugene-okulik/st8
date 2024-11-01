import requests
import allure


from api_tests_margi_liaushkina.endpoints.base_api import BaseApi
from api_tests_margi_liaushkina.data import constans
from api_tests_margi_liaushkina.models.publication_object import PublicationObject


class PutPosts(BaseApi):
    @allure.step('Send PUT request with updates')
    def update_pub_with_put(self, create_id, payload, headers=None):
        headers = headers if headers else constans.HEADERS
        self.response = requests.put(
            f'{constans.BASE_URL}{constans.POSTS_POSTFIX}/{create_id}',
            json=payload,
            headers=headers
        )

    @property
    def data(self):
        return PublicationObject(**self.response_json)


    @allure.step("Check name is updated")
    def check_name_is_updated(self, payload):
        assert self.response_json['name'] == payload


    @allure.step("Check year is updated")
    def check_year_is_updated(self, payload):
        assert self.response_json['data']['year'] == payload


    @allure.step("Check price is updated")
    def check_price_is_updated(self, payload):
        assert self.response_json['data']['price'] == payload