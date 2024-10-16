import requests
import allure
from api_tests_dpolozkova.data import constants
from api_tests_dpolozkova.data import test_data
from api_tests_dpolozkova.endpoints.base_api import BaseApi
from api_tests_dpolozkova.models.object_model import ObjectWithData
from homework.darya_polozkova.homework_23_test_configuration.test_configuration import ObjData


class CreateObject(BaseApi):
    @allure.step("Object is created")
    def create_object(self, payload=None):
        payload = payload if payload else test_data.DEFAULT_PAYLOAD
        self.response = requests.post(
            f'{constants.BASE_URL}{constants.OBJECT_POSTFIX}', json=payload
        )

    @property
    def data(self):
        return ObjectWithData(**self.response_json)

