import requests
import allure
from requests.exceptions import JSONDecodeError
from api_tests_margi_liaushkina.data import constans
from api_tests_margi_liaushkina.endpoints.base_api import BaseApi
from api_tests_margi_liaushkina.models.publication_object import PublicationObject


class GetPosts(BaseApi):
    @allure.step('Get all posts')
    def get_all_posts(self):
        self.response = requests.get(f'{constans.BASE_URL}{constans.POSTS_POSTFIX}')

    @property
    def data(self):
        return PublicationObject(**self.response_json)

    @allure.step('Check posts quantity')
    def check_posts_qty_is_(self, qty):
        assert len(self.response_json) == qty
