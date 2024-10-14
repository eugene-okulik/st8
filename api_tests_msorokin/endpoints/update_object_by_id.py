import requests
import allure
from requests.exceptions import JSONDecodeError

from api_tests_msorokin.endpoints.base_api import BaseApi
from api_tests_msorokin.data.constants import HEADER, BASE_URL
from api_tests_msorokin.models.api_object_model import ObjectJson


class UpdateObjectById(BaseApi):

    @allure.step('Send PUT request with updates')
    def update_object_by_id(self, object_id, payload, headers=None):
        headers = headers if headers else HEADER
        self.response = requests.put(
            f'{BASE_URL}/{object_id}',
            json=payload,
            headers=headers
        )

    @property
    def data(self):
        return ObjectJson(**self.response_json)

    def check_that_all_fields_are_updated(self, payload):
        assert self.response_json != payload
