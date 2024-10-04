import requests
from api_tests_bstepchenko.data import constants
from requests.exceptions import JSONDecodeError
from api_tests_bstepchenko.endpoints.base_api import BaseApi


class PatchObject(BaseApi):

    def update_obj_with_patch(self, obj_id):
        self.payload = constants.PAYLOAD_FOR_OBJECT
        self.response = requests.patch(f'{constants.BASE_URL}/{obj_id}',
                                       json=self.payload, headers=constants.HEADERS)
        try:
            self.response_json = self.response.json()
        except JSONDecodeError:
            pass
