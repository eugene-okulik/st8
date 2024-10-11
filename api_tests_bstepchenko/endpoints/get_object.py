from json import JSONDecodeError

import requests
from api_tests_bstepchenko.data import constants
from api_tests_bstepchenko.endpoints.base_api import BaseApi
from api_tests_bstepchenko.models.object_data import ObjectJson


class GetObject(BaseApi):

    def get_object_by_id(self, object_id):
        self.response = requests.get(f'{constants.BASE_URL}/{object_id}')
        try:
            self.response_json = self.response.json()
        except JSONDecodeError:
            assert False, "Failed to decode JSON response"

    @property
    def data(self):
        return ObjectJson(**self.response_json)

    def check_name(self, payload):
        assert self.data.name == payload['name']

    def check_year(self, payload):
        assert self.data.data.year == payload['data']['year']

    def check_price(self, payload):
        assert self.data.data.price == payload['data']['price']

    def check_cpu_model(self, payload):
        assert self.data.data.CPU_model == payload['data']['CPU model']
