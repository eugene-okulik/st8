import requests
import allure
from api_tests_dpolozkova.data import constants
from api_tests_dpolozkova.data import test_data
from api_tests_dpolozkova.endpoints.base_api import BaseApi
from api_tests_dpolozkova.models.object_model import ObjectWithData


class CreateObject(BaseApi):
    @allure.step("Object is created")
    def independent_test_create_an_object(self, payload=None):
        payload = payload if payload else test_data.DEFAULT_PAYLOAD
        self.response = requests.post(
            f'{constants.BASE_URL}{constants.POSTS_POSTFIX}', json=payload
        )
        object_id = self.response.json()['id']
        return object_id

    @property
    def data(self):
        return ObjectWithData(**self.response_json)
