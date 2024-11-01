from abc import abstractmethod

import allure
from requests import Response


class BaseApi:
    response: Response

    @allure.step('Check response status code')
    def check_response_code_is_(self, code):
        assert self.response.status_code == code

    @property
    def response_json(self):
        return self.response.json()

    @abstractmethod
    @property
    def data(self):
        pass
