import requests
from requests.exceptions import JSONDecodeError
from api_tests_bstepchenko.data import constants
from api_tests_bstepchenko.endpoints.base_api import BaseApi


class GetObject(BaseApi):

    def get_object_by_id(self, object_id):
        self.response = requests.get(f'{constants.BASE_URL}/{object_id}')
        try:
            self.response_json = self.response.json()
        except JSONDecodeError:
            pass
