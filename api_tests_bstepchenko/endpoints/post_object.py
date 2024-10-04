import requests
from api_tests_bstepchenko.data import constants
from requests.exceptions import JSONDecodeError
from api_tests_bstepchenko.endpoints.base_api import BaseApi


class PostObject(BaseApi):

    def post_new_object(self):
        self.payload = constants.PAYLOAD_FOR_OBJECT
        self.response = requests.post(f'{constants.BASE_URL}', json=self.payload, headers=constants.HEADERS)
        try:
            self.response_json = self.response.json()
        except JSONDecodeError:
            pass
