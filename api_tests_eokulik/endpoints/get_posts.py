import requests
import allure
from requests.exceptions import JSONDecodeError
from api_tests_eokulik.data import constants
from api_tests_eokulik.endpoints.base_api import BaseApi


class GetPosts(BaseApi):
    @allure.step('Get all posts')
    def get_all_posts(self):
        self.response = requests.get(f'{constants.BASE_URL}{constants.POSTS_POSTFIX}')
        try:
            self.response_json = self.response.json()
        except JSONDecodeError:
            pass

    @allure.step('Check posts quantity')
    def check_posts_qty_is_(self, qty):
        assert len(self.response_json) == qty
