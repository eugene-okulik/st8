import requests
import allure
from api_tests_dpolozkova.data import constants
from api_tests_dpolozkova.endpoints.base_api import BaseApi


class DeleteObject(BaseApi):
    @allure.step("Object is deleted")
    def test_independent_delete_an_object(self, object_id):
        self.response = requests.delete(f'{constants.BASE_URL}{constants.POSTS_POSTFIX}/{object_id}')
