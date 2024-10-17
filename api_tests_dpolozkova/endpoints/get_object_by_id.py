import requests
import allure
from api_tests_dpolozkova.data import constants
from api_tests_dpolozkova.endpoints.base_api import BaseApi
from api_tests_dpolozkova.models.object_model import ObjData


class GetObjectById(BaseApi):
    @allure.step("Get object by id")
    def get_object_by_id(self, set_up):
        self.response = requests.get(f'{constants.BASE_URL}/{constants.OBJECT_POSTFIX}/{set_up}')

    @property
    def data(self):
        return ObjData(**self.response_json)

    @allure.step("Check object with right id is returned")
    def check_object_id_is_(self, set_up):
        assert self.response_json['id'] == set_up
