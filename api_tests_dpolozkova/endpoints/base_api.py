from abc import abstractmethod

import allure
from requests import Response


class BaseApi:
    response: Response

    @allure.step("Check response status code")
    def check_response_code_is_(self, code):
        assert self.response.status_code == code

    @allure.step("Validate created object")
    def check_fields_of_object(self, payload):
        assert self.response_json['name'] == payload['name']
        assert self.response_json['data']['price'] == payload['data']['price']
        assert self.response_json['data']['year'] == payload['data']['year']
        assert self.response_json['data']['CPU model'] == payload['data']['CPU model']
        assert self.response_json['data']['Hard disk size'] == payload['data']['Hard disk size']

    # property привращает результат функции в переменную
    # проверят вычитку респонса
    @property
    def response_json(self):
        return self.response.json()

    @property
    @abstractmethod
    # означает что во всех подклассах должна быть реализванно
    def data(self):
        pass
