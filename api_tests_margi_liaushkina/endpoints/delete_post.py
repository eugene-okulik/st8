import requests

from api_tests_margi_liaushkina.endpoints.base_api import BaseApi
from api_tests_margi_liaushkina.data import constans


class DeletePost(BaseApi):
    def delete_post(self, pub_id):
        self.response = requests.delete(
            f'{constans.BASE_URL}{constans.POSTS_POSTFIX}/{pub_id}'
        )
