import requests
from api_tests_bstepchenko.data import constants
from requests.exceptions import JSONDecodeError
from api_tests_bstepchenko.endpoints.base_api import BaseApi


class PutObject(BaseApi):

    def update_obj_with_put(self, obj_id, payload):
        self.payload = payload
        self.response = requests.put(f'{constants.BASE_URL}/{obj_id}',
                                     json=self.payload, headers=constants.HEADERS)
        try:
            self.response_json = self.response.json()
        except JSONDecodeError:
            pass
