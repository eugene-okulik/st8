import requests
from api_tests_bstepchenko.data import constants
from requests.exceptions import JSONDecodeError
from api_tests_bstepchenko.endpoints.base_api import BaseApi
from api_tests_bstepchenko.models.object_data import ObjectJson


class PostObject(BaseApi):

    def post_new_object(self, payload):
        self.response = requests.post(f'{constants.BASE_URL}', json=payload, headers=constants.HEADERS)
        try:
            self.response_json = self.response.json()
        except JSONDecodeError:
            pass

    @property
    def data(self):
        return ObjectJson(**self.response_json)

    def check_updated_name(self, payload):
        assert self.data.name == payload['name']

    def check_updated_year(self, payload):
        assert self.data.data.year == payload['data']['year']

    def check_updated_price(self, payload):
        assert self.data.data.price == payload['data']['price']

    def check_updated_cpu_model(self, payload):
        assert self.data.data.CPU_model == payload['data']['CPU model']
