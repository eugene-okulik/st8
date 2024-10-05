import requests

from api_tests_eokulik.endpoints.base_api import BaseApi
from api_tests_eokulik.data import constants
from api_tests_eokulik.models.publication_object import PublicationObject


class PostPost(BaseApi):
    def create_publication(self, payload, headers=None):
        headers = headers if headers else constants.HEADERS
        self.response = requests.post(
            f'{constants.BASE_URL}{constants.POSTS_POSTFIX}',
            json=payload,
            headers=headers
        )

    @property
    def data(self):
        return PublicationObject(**self.response_json)
