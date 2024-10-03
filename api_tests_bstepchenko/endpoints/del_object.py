import requests
from api_tests_bstepchenko.data import constants
from requests.exceptions import JSONDecodeError
from api_tests_bstepchenko.endpoints.base_api import BaseApi


class DeleteObject(BaseApi):

    def create_new_object(self):
        payload = constants.PAYLOAD_FOR_OBJECT
        self.response = requests.post(f'{constants.BASE_URL}', json=payload, headers=constants.HEADERS)
        try:
            created_object = self.response.json()
        except JSONDecodeError:
            created_object = None
        assert created_object is not None, "Failed to create the object"
        return created_object['id']

    def delete_created_object(self, obj_id):
        self.response = requests.delete(f'{constants.BASE_URL}/{obj_id}')
        try:
            self.response_json = self.response.json()
        except JSONDecodeError:
            pass

    def check_obj_absense(self, obj_id):
        self.response = requests.get(f'{constants.BASE_URL}/{obj_id}')
        assert self.response is not None, "No response received when checking object absence"
        try:
            self.response_json = self.response.json()
        except JSONDecodeError:
            self.response_json = None

        assert self.response_json is None or self.response_json == {}, "Object still exists"
