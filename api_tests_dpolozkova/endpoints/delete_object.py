import requests
import allure
from api_tests_dpolozkova.data import constants
from api_tests_dpolozkova.endpoints.base_api import BaseApi
from api_tests_dpolozkova.models.object_model import ObjectWithData


class DeleteObject(BaseApi):
    @allure.step("Object is deleted")
    def delete_object(self, object_id):
        self.response = requests.delete(f'{constants.BASE_URL}{constants.OBJECT_POSTFIX}/{object_id}')

    @property
    def data(self):
        return ObjectWithData(**self.response_json)
