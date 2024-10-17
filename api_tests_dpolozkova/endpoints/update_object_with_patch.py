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

    @allure.step("Check name is updated")
    def check_updated_name(self, name):
        assert self.response_json['name'] == name

    @allure.step("Check rest of fields are not deleted and not updated")
    def check_rest_fields_are_not_updated(self, payload):
        assert self.response_json['data']['year'] == payload['data']['year']
        assert self.response_json['data']['price'] == payload['data']['price']
        assert self.response_json['data']['CPU model'] == payload['data']['CPU model']
        assert self.response_json['data']['Hard disk size'] == payload['data']['Hard disk size']
