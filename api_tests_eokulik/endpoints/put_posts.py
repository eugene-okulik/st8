import requests
import allure
from requests.exceptions import JSONDecodeError

from api_tests_eokulik.endpoints.base_api import BaseApi
from api_tests_eokulik.data import constants


class PutPosts(BaseApi):
    @allure.step('Send PUT request with updates')
    def update_pub_with_put(self, pub_id, payload, headers=None):
        headers = headers if headers else constants.HEADERS
        self.response = requests.put(
            f'{constants.BASE_URL}{constants.POSTS_POSTFIX}/{pub_id}',
            json=payload,
            headers=headers
        )
        try:
            self.response_json = self.response.json()
        except JSONDecodeError:
            pass

    @allure.step(f'Checking title in Publication')
    def check_publication_title(self, title):
        assert self.response_json['title'] == title

    @allure.step(f'Checking body in Publication')
    def check_publication_body(self, body):
        assert self.response_json['body'] == body
