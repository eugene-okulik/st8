import requests

from api_tests_margi_liaushkina.endpoints.base_api import BaseApi
from api_tests_margi_liaushkina.data import constans
from api_tests_margi_liaushkina.data import  test_data
from api_tests_margi_liaushkina.models.publication_object import PublicationObject


class CreatePost(BaseApi):
    def create_obj(self, payload, headers=None):
        payload = payload if payload else test_data.DEFAULT_PAYLOAD
        self.response = requests.post(
            f'{constans.BASE_URL}{constans.POSTS_POSTFIX}',
            json=payload,
        )

    @property
    def data(self):
        return PublicationObject(**self.response_json)

