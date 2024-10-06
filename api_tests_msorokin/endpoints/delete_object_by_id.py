import requests

from api_tests_msorokin.endpoints.base_api import BaseApi
from api_tests_msorokin.data import constants
from api_tests_msorokin.models.api_object_model import ObjectJson


class DeleteObjectById(BaseApi):
    def __init__(self):
        self.payload = None

    def delete_object(self, pub_id):
        self.response = requests.delete(
            f'{constants.BASE_URL}/{pub_id}'
        )

    @property
    def data(self):
        return ObjectJson(**self.response_json)
