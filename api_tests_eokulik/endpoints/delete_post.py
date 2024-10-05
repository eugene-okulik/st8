import requests

from api_tests_eokulik.endpoints.base_api import BaseApi
from api_tests_eokulik.data import constants


class DeletePost(BaseApi):
    def delete_post(self, pub_id):
        self.response = requests.delete(
            f'{constants.BASE_URL}{constants.POSTS_POSTFIX}/{pub_id}'
        )
