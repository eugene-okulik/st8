import requests
import allure
from api_tests_dpolozkova.data import constants
from api_tests_dpolozkova.endpoints.base_api import BaseApi
from api_tests_dpolozkova.models.object_model import ObjectWithData


class GetObjectById(BaseApi):
    @allure.step("Get object by id")
    def get_object_by_id(self, set_up):
        self.response = requests.get(f'{constants.BASE_URL}/{constants.POSTS_POSTFIX}/{set_up}')

    @property
    def data(self):
        return ObjectWithData(**self.response_json)
