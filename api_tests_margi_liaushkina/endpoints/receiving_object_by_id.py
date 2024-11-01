import requests
import allure


from api_tests_margi_liaushkina.data import constans
from api_tests_margi_liaushkina.endpoints.base_api import BaseApi
from api_tests_margi_liaushkina.models.publication_object import PublicationObject


class GetPostsId(BaseApi):
    def get_post_by_id(self, post_id):
        self.response = requests.get(f'{constans.BASE_URL}{constans.POSTS_POSTFIX}/{post_id}')

    @property
    def data(self):
        return PublicationObject(**self.response_json)

    def check_publication_id_is_(self, pub_id):
        assert self.data.id == pub_id
