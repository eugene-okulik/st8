import requests
import allure
from api_tests_msorokin.data.object_api_json import ObjectApiJson
from api_tests_msorokin.data.constants import BASE_URL, HEADER
from api_tests_msorokin.endpoints.base_api import BaseApi
from api_tests_msorokin.models.api_object_model import ObjectJson


class CreateObject(BaseApi):

    def create_new_object(self, payload):
        self.response = requests.post(f'{BASE_URL}', json=payload, headers=HEADER)

    @property
    def data(self):
        return ObjectJson(**self.response_json)

    def check_all_fields(self, payload):
        assert self.response_json['name'] == payload['name']
        assert self.response_json['data']['price'] == payload['data']['price']
        assert self.response_json['data']['year'] == payload['data']['year']
        assert self.response_json['data']['cpu_model'] == payload['data']['cpu_model']
        assert self.response_json['data']['hard_disk_size'] == payload['data']['hard_disk_size']


