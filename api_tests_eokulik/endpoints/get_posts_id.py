import requests
from requests.exceptions import JSONDecodeError

from api_tests_eokulik.data import constants
from api_tests_eokulik.endpoints.base_api import BaseApi
from api_tests_eokulik.models.publication_object import PublicationObject


class GetPostsId(BaseApi):
    def get_post_by_id(self, post_id):
        self.response = requests.get(f'{constants.BASE_URL}{constants.POSTS_POSTFIX}/{post_id}')

    @property
    def data(self):
        return PublicationObject(**self.response_json)

    def check_publication_id_is_(self, pub_id):
        assert self.data.id == pub_id
