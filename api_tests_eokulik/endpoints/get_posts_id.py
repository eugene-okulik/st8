import requests
from requests.exceptions import JSONDecodeError

from api_tests_eokulik.data import constants
from api_tests_eokulik.endpoints.base_api import BaseApi


class GetPostsId(BaseApi):
    def get_post_by_id(self, post_id):
        self.response = requests.get(f'{constants.BASE_URL}{constants.POSTS_POSTFIX}/{post_id}')
        try:
            self.response_json = self.response.json()
        except JSONDecodeError:
            pass
