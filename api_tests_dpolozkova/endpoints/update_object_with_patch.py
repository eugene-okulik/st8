import requests
import allure
from api_tests_dpolozkova.data import constants
from api_tests_dpolozkova.endpoints.base_api import BaseApi


class UpdateObjectPatch(BaseApi):
    @allure.step("Update object with method: PATCH")
    def update_object_with_patch(self, set_up, payload, headers=None):
        headers = headers if headers else constants.HEADERS
        self.response = requests.patch(
            f'{constants.BASE_URL}{constants.OBJECT_POSTFIX}/{set_up}',
            json=payload,
            headers=headers
        )

    def check_updated_name(self, name):
        assert self.response_json['name'] == name
