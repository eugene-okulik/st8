import requests
from requests.exceptions import JSONDecodeError
from api_tests_msorokin.data.constants import BASE_URL
from api_tests_msorokin.endpoints.base_api import BaseApi
from api_tests_msorokin.models.api_object_model import ObjectJson


class GetObjects(BaseApi):

    def get_objects(self):
        self.response = requests.get(f'{BASE_URL}')

    @property
    def data(self):
        return ObjectJson(**self.response_json)

    def check_that_response_is_not_empty(self):
        assert self.response_json != {}
        assert len(self.response_json) > 0


