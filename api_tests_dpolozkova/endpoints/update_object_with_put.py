import requests
import allure
from api_tests_dpolozkova.data import constants
from api_tests_dpolozkova.endpoints.base_api import BaseApi
from homework.darya_polozkova.homework_23_test_configuration.test_configuration import ObjectWithData


class UpdateObjectPut(BaseApi):
    @allure.step("Update object with method: PUT")
    def update_object_with_put(self, set_up, payload, headers=None):
        headers = headers if headers else constants.HEADERS
        self.response = requests.put(
            f'{constants.BASE_URL}{constants.OBJECT_POSTFIX}/{set_up}',
            json=payload,
            headers=headers
        )

    @property
    def data(self):
        return ObjectWithData(**self.response_json)

    @allure.step("Check name is updated")
    def check_name_is_updated(self, payload):
        assert self.response_json['name'] == payload

    @allure.step("Check year is updated")
    def check_year_is_updated(self, payload):
        assert self.response_json['data']['year'] == payload

    @allure.step("Check price is updated")
    def check_price_is_updated(self, payload):
        assert self.response_json['data']['price'] == payload
