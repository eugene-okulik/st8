import requests
import allure
from api_tests_dpolozkova.data import constants
from api_tests_dpolozkova.data import test_data
from api_tests_dpolozkova.endpoints.base_api import BaseApi
from api_tests_dpolozkova.models import object_model
from api_tests_dpolozkova.models.object_model import ObjectWithData


class UpdateObjectPut(BaseApi):
    @allure.step("Update object with method: PUT")
    def update_object_with_put(self, set_up, payload, headers=None):
        headers = headers if headers else constants.HEADERS
        self.response = requests.put(
            f'{constants.BASE_URL}{constants.POSTS_POSTFIX}/{set_up}',
            json=payload,
            headers=headers
        )

    @property
    def data(self):
        return ObjectWithData(**self.response_json)

    @allure.step("Check updated object name with PUT")
    def check_updated_name(self, name):
        assert self.data.name == name

    @allure.step("Check updated object year with PUT")
    def check_updated_object_year(self, year):
        assert self.data.data['year'] == year

    @allure.step("Check updated object price with PUT")
    def check_updated_object_price(self, price):
        assert self.data.data['price'] == price
