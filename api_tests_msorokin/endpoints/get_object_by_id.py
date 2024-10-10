import requests
from requests.exceptions import JSONDecodeError
from api_tests_msorokin.data.constants import BASE_URL
from api_tests_msorokin.endpoints.base_api import BaseApi
from api_tests_msorokin.models.api_object_model import ObjectJson


class GetObjectById(BaseApi):

    def get_object_by_id(self, object_id):
        self.response = requests.get(f'{BASE_URL}/{object_id}')

    @property
    def data(self):
        return ObjectJson(**self.response_json)

    def check_name(self, name):
        assert self.response_json['name'] == name

    def check_all_fields(self, payload):
        assert self.response_json['name'] == payload['name']
        assert self.response_json['data']['price'] == payload['data']['price']
        assert self.response_json['data']['year'] == payload['data']['year']
        assert self.response_json['data']['cpu_model'] == payload['data']['cpu_model']
        assert self.response_json['data']['hard_disk_size'] == payload['data']['hard_disk_size']

    def check_that_object_is_deleted(self):
        assert self.response_json == {}
